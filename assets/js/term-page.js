const termPage = document.getElementById("term-page");

const termEsc = (value = "") => String(value).replace(/[&<>"']/g, ch => ({"&":"&amp;","<":"&lt;",">":"&gt;",'"':"&quot;","'":"&#39;"}[ch]));
const safeUrl = value => /^https?:\/\//i.test(String(value || "")) ? String(value) : "#";

function formatDate(value) {
  if (!value) return "Unknown";
  if (/^\d{4}$/.test(value)) return value;
  if (/^\d{4}-\d{2}$/.test(value)) {
    const [year, month] = value.split("-").map(Number);
    return new Intl.DateTimeFormat("en-US", { month: "long", year: "numeric", timeZone: "UTC" }).format(new Date(Date.UTC(year, month - 1, 1)));
  }
  const date = new Date(`${value}T00:00:00Z`);
  if (Number.isNaN(date.getTime())) return value;
  return new Intl.DateTimeFormat("en-US", { month: "long", day: "numeric", year: "numeric", timeZone: "UTC" }).format(date);
}

function categoryKey(term) {
  const categories = term.categories || [];
  if (categories.includes("AI Culture & Slang")) return "culture";
  if (categories.includes("AI Ways of Working")) return "work";
  if (categories.includes("AI Risks, Safety & Governance")) return "risks";
  return "systems";
}

function renderFirstKnownUse(record) {
  if (!record.firstKnownUse) return `<p class="muted-note">A defensible first-known-use date has not been established in AILex's current research.</p>`;
  const precision = record.firstKnownUse.precision ? `<span class="provenance-precision">${termEsc(record.firstKnownUse.precision)} precision</span>` : "";
  return `<p class="first-use-date">${termEsc(formatDate(record.firstKnownUse.date))} ${precision}</p>${record.firstKnownUse.note ? `<p>${termEsc(record.firstKnownUse.note)}</p>` : ""}`;
}

function renderSources(sources = []) {
  return sources.map(source => `<li class="source-item">
    <a href="${termEsc(safeUrl(source.url))}" target="_blank" rel="noopener noreferrer">${termEsc(source.title)}</a>
    <div class="source-meta">${termEsc(source.publisher || "Source")}${source.published ? ` · ${termEsc(formatDate(source.published))}` : ""} · ${termEsc(source.type || "source")}</div>
    <div class="source-supports">Supports: ${(source.supports || []).map(item => `<span>${termEsc(item)}</span>`).join("")}</div>
  </li>`).join("");
}

function renderTermPage(term, provenance, termsBySlug) {
  const category = categoryKey(term);
  termPage.dataset.category = category;
  document.title = `${term.term} | AILex`;

  const related = (provenance.relatedTerms || []).map(slug => {
    const relatedTerm = termsBySlug.get(slug);
    return relatedTerm ? `<a class="related-term" href="../${encodeURIComponent(slug)}/">${termEsc(relatedTerm.term)}</a>` : "";
  }).filter(Boolean).join("");

  const history = (provenance.history || []).length
    ? `<ol class="history-list">${provenance.history.map(item => `<li><time>${termEsc(formatDate(item.date))}</time><p>${termEsc(item.event)}</p></li>`).join("")}</ol>`
    : `<p class="muted-note">No separate history milestones are currently recorded.</p>`;

  termPage.innerHTML = `
    <nav class="term-breadcrumb" aria-label="Breadcrumb"><a href="../../">Browse</a><span aria-hidden="true">/</span><span>${termEsc(term.term)}</span></nav>
    <header class="term-page-header">
      <p class="eyebrow">AILex entry</p>
      <h1>${termEsc(term.term)}</h1>
      <div class="term-pronunciation-row"><span class="term-page-pronunciation">${termEsc(term.pronunciation)}</span><span class="part-of-speech">${termEsc(term.partOfSpeech || "")}</span></div>
      <div class="term-page-pills">${(term.categories || []).map(c => `<span class="pill">${termEsc(c)}</span>`).join("")}<span class="pill status-pill">${termEsc(term.status)}</span></div>
    </header>

    <div class="term-page-layout">
      <div class="term-main-column">
        <section class="term-section definition-section"><span class="entry-label">Definition</span><p class="term-page-definition">${termEsc(term.definition)}</p></section>
        <section class="term-section"><span class="entry-label">Used in a sentence</span><p class="term-page-example"><em>${termEsc(term.example)}</em></p></section>
        ${term.aliases?.length ? `<section class="term-section"><span class="entry-label">Also known as</span><p>${term.aliases.map(termEsc).join(", ")}</p></section>` : ""}
        <section class="term-section"><span class="entry-label">Origin & context</span><p>${termEsc(provenance.origin || "Origin research is not yet available.")}</p></section>
        <section class="term-section"><span class="entry-label">History</span>${history}</section>
        <section class="term-section"><span class="entry-label">Sources</span><ol class="source-list">${renderSources(provenance.sources || [])}</ol></section>
      </div>
      <aside class="term-side-column">
        <section class="term-fact-card"><span class="entry-label">First known use</span>${renderFirstKnownUse(provenance)}</section>
        <section class="term-fact-card"><span class="entry-label">Research status</span><p class="research-status">${termEsc(provenance.researchStatus || "unknown")}</p></section>
        <section class="term-fact-card"><span class="entry-label">Related terms</span><div class="related-terms">${related || `<span class="muted-note">None listed yet.</span>`}</div></section>
        <section class="term-fact-card term-record-meta"><span class="entry-label">Entry record</span><p>Added ${termEsc(formatDate(term.added))}</p><p>Last reviewed ${termEsc(formatDate(term.lastReviewed))}</p></section>
      </aside>
    </div>`;
}

if (termPage) {
  const slug = termPage.dataset.termSlug;
  Promise.all([
    fetch("../../data/terms.json").then(response => { if (!response.ok) throw new Error("Could not load dictionary data."); return response.json(); }),
    fetch("../../data/provenance.json").then(response => { if (!response.ok) throw new Error("Could not load provenance data."); return response.json(); })
  ]).then(([terms, provenance]) => {
    const termsBySlug = new Map(terms.map(term => [term.slug, term]));
    const term = termsBySlug.get(slug);
    const record = provenance[slug];
    if (!term || !record) throw new Error("This AILex entry could not be found.");
    renderTermPage(term, record, termsBySlug);
  }).catch(error => {
    const fallback = document.getElementById("term-fallback");
    if (fallback) fallback.insertAdjacentHTML("beforeend", `<p class="term-load-error">${termEsc(error.message)}</p>`);
  });
}
