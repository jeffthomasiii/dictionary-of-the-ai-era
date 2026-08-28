const state = { terms: [], query: "", category: "all", view: localStorage.getItem("ai-era-view") || "list" };
const dictionary = document.getElementById("dictionary");
const search = document.getElementById("search");
const count = document.getElementById("result-count");
const heroTermCount = document.getElementById("hero-term-count");
const empty = document.getElementById("empty-state");
const alpha = document.getElementById("alpha-nav");
const filters = [...document.querySelectorAll(".filter")];
const themeToggle = document.getElementById("theme-toggle");
const listViewButton = document.getElementById("list-view");
const gridViewButton = document.getElementById("grid-view");

const esc = (value = "") => String(value).replace(/[&<>"']/g, ch => ({"&":"&amp;","<":"&lt;",">":"&gt;",'"':"&quot;","'":"&#39;"}[ch]));

function categoryKey(term) {
  const categories = term.categories || [];
  if (categories.includes("AI Culture & Slang")) return "culture";
  if (categories.includes("AI Ways of Working")) return "work";
  if (categories.includes("AI Risks, Safety & Governance")) return "risks";
  return "systems";
}

function searchableText(term) {
  return [term.term, term.pronunciation, term.definition, term.example, ...(term.aliases || []), ...(term.categories || []), term.status].join(" ").toLowerCase();
}

function filteredTerms() {
  return state.terms.filter(term => {
    const queryMatch = !state.query || searchableText(term).includes(state.query);
    const categoryMatch = state.category === "all" || term.categories.includes(state.category);
    return queryMatch && categoryMatch;
  }).sort((a,b) => a.term.localeCompare(b.term));
}

function renderAlpha(terms) {
  if (!alpha) return;
  const letters = [...new Set(terms.map(t => t.term[0].toUpperCase()))];
  alpha.innerHTML = letters.map(letter => `<button type="button" data-letter="${esc(letter)}" aria-label="Jump to ${esc(letter)}">${esc(letter)}</button>`).join("");
  alpha.querySelectorAll("button").forEach(button => button.addEventListener("click", () => document.getElementById(`letter-${button.dataset.letter}`)?.scrollIntoView({behavior:"smooth"})));
}

function termCard(term) {
  return `<article class="entry" data-category="${categoryKey(term)}" id="${esc(term.slug)}">
    <div class="term-block"><h3 class="term-name"><a href="terms/${encodeURIComponent(term.slug)}/">${esc(term.term)}</a></h3><div class="pronunciation">${esc(term.pronunciation)}</div><div class="part-of-speech">${esc(term.partOfSpeech || "")}</div></div>
    <div class="definition-block"><span class="entry-label">Definition</span><p class="definition">${esc(term.definition)}</p></div>
    <div class="example-block"><span class="entry-label">Used in a sentence</span><p class="example"><em>${esc(term.example)}</em></p></div>
    <div class="entry-meta">${(term.categories || []).map(c => `<span class="pill">${esc(c)}</span>`).join("")}<span class="pill status-pill">${esc(term.status)}</span>${(term.aliases || []).length ? `<span class="aliases"><strong>Also known as:</strong> ${term.aliases.map(esc).join(", ")}</span>` : ""}</div>
  </article>`;
}

function render() {
  if (!dictionary) return;
  const terms = filteredTerms();
  if (count) count.textContent = `${terms.length} ${terms.length === 1 ? "term" : "terms"}`;
  if (heroTermCount) heroTermCount.textContent = state.terms.length || "—";
  if (empty) empty.hidden = terms.length !== 0;
  renderAlpha(terms);

  dictionary.classList.toggle("grid-view", state.view === "grid");
  dictionary.classList.toggle("list-view", state.view === "list");
  listViewButton?.classList.toggle("active", state.view === "list");
  gridViewButton?.classList.toggle("active", state.view === "grid");

  const grouped = terms.reduce((acc, term) => { const letter = term.term[0].toUpperCase(); (acc[letter] ||= []).push(term); return acc; }, {});
  dictionary.innerHTML = Object.entries(grouped).map(([letter, group]) => `<section class="letter-group" id="letter-${esc(letter)}"><h2 class="letter-heading">${esc(letter)}</h2><div class="letter-entries">${group.map(termCard).join("")}</div></section>`).join("");
}

function setTheme(theme) {
  document.documentElement.dataset.theme = theme;
  localStorage.setItem("ai-era-theme", theme);
  if (themeToggle) {
    const next = theme === "dark" ? "light" : "dark";
    themeToggle.setAttribute("aria-label", `Switch to ${next} mode`);
    themeToggle.setAttribute("title", `Switch to ${next} mode`);
  }
}

if (themeToggle) {
  setTheme(document.documentElement.dataset.theme || "light");
  themeToggle.addEventListener("click", () => setTheme(document.documentElement.dataset.theme === "dark" ? "light" : "dark"));
}

search?.addEventListener("input", event => { state.query = event.target.value.trim().toLowerCase(); render(); });
document.addEventListener("keydown", event => {
  if ((event.metaKey || event.ctrlKey) && event.key.toLowerCase() === "k" && search) { event.preventDefault(); search.focus(); }
  if (event.key === "Escape" && document.activeElement === search) { search.value = ""; state.query = ""; search.blur(); render(); }
});

filters.forEach(button => button.addEventListener("click", () => { state.category = button.dataset.category; filters.forEach(b => b.classList.toggle("active", b === button)); render(); }));
listViewButton?.addEventListener("click", () => { state.view = "list"; localStorage.setItem("ai-era-view", state.view); render(); });
gridViewButton?.addEventListener("click", () => { state.view = "grid"; localStorage.setItem("ai-era-view", state.view); render(); });

if (dictionary) {
  fetch("data/terms.json").then(response => { if (!response.ok) throw new Error("Could not load dictionary data."); return response.json(); }).then(terms => { state.terms = terms; render(); }).catch(error => { dictionary.innerHTML = `<p>Unable to load the dictionary. ${esc(error.message)}</p>`; });
}
