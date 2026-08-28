const state = { terms: [], query: "", category: "all" };
const dictionary = document.getElementById("dictionary");
const search = document.getElementById("search");
const count = document.getElementById("result-count");
const empty = document.getElementById("empty-state");
const alpha = document.getElementById("alpha-nav");
const filters = [...document.querySelectorAll(".filter")];

const esc = (value = "") => value.replace(/[&<>"']/g, ch => ({
  "&":"&amp;","<":"&lt;",">":"&gt;",'"':"&quot;","'":"&#39;"
}[ch]));

function searchableText(term) {
  return [
    term.term, term.pronunciation, term.definition, term.example,
    ...(term.aliases || []), ...(term.categories || []), term.status
  ].join(" ").toLowerCase();
}

function filteredTerms() {
  return state.terms.filter(term => {
    const queryMatch = !state.query || searchableText(term).includes(state.query);
    const categoryMatch = state.category === "all" || term.categories.includes(state.category);
    return queryMatch && categoryMatch;
  }).sort((a,b) => a.term.localeCompare(b.term));
}

function renderAlpha(terms) {
  const letters = [...new Set(terms.map(t => t.term[0].toUpperCase()))];
  alpha.innerHTML = letters.map(letter =>
    `<button type="button" data-letter="${esc(letter)}" aria-label="Jump to ${esc(letter)}">${esc(letter)}</button>`
  ).join("");
  alpha.querySelectorAll("button").forEach(button => {
    button.addEventListener("click", () => {
      document.getElementById(`letter-${button.dataset.letter}`)?.scrollIntoView({behavior:"smooth"});
    });
  });
}

function render() {
  const terms = filteredTerms();
  count.textContent = `${terms.length} ${terms.length === 1 ? "term" : "terms"}`;
  empty.hidden = terms.length !== 0;
  renderAlpha(terms);

  const grouped = terms.reduce((acc, term) => {
    const letter = term.term[0].toUpperCase();
    (acc[letter] ||= []).push(term);
    return acc;
  }, {});

  dictionary.innerHTML = Object.entries(grouped).map(([letter, group]) => `
    <section class="letter-group" id="letter-${esc(letter)}">
      <h2 class="letter-heading">${esc(letter)}</h2>
      ${group.map(term => `
        <article class="entry" id="${esc(term.slug)}">
          <div>
            <h3 class="term-name">${esc(term.term)}</h3>
            <div class="pronunciation">${esc(term.pronunciation)}</div>
            <div class="part-of-speech">${esc(term.partOfSpeech || "")}</div>
          </div>
          <div>
            <p class="definition"><strong>Definition:</strong> ${esc(term.definition)}</p>
            <p class="example"><strong>In a sentence:</strong> <em>${esc(term.example)}</em></p>
            <div class="meta-row">
              ${(term.categories || []).map(c => `<span class="pill">${esc(c)}</span>`).join("")}
              <span class="pill">${esc(term.status)}</span>
            </div>
            ${(term.aliases || []).length ? `<p class="aliases"><strong>Also known as:</strong> ${term.aliases.map(esc).join(", ")}</p>` : ""}
          </div>
        </article>
      `).join("")}
    </section>
  `).join("");

  if (location.hash) {
    const target = document.querySelector(location.hash);
    if (target) setTimeout(() => target.scrollIntoView(), 0);
  }
}

search.addEventListener("input", event => {
  state.query = event.target.value.trim().toLowerCase();
  render();
});

filters.forEach(button => {
  button.addEventListener("click", () => {
    state.category = button.dataset.category;
    filters.forEach(b => b.classList.toggle("active", b === button));
    render();
  });
});

fetch("data/terms.json")
  .then(response => {
    if (!response.ok) throw new Error("Could not load dictionary data.");
    return response.json();
  })
  .then(terms => {
    state.terms = terms;
    render();
  })
  .catch(error => {
    dictionary.innerHTML = `<p>Unable to load the dictionary. ${esc(error.message)}</p>`;
  });
