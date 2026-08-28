(() => {
  const root = document.getElementById('category-directory');
  if (!root) return;

  const categories = [
    { key: 'culture', name: 'AI Culture & Slang', label: 'Culture & Slang' },
    { key: 'work', name: 'AI Ways of Working', label: 'Ways of Working' },
    { key: 'systems', name: 'AI Systems & Technical Concepts', label: 'Systems & Technical' },
    { key: 'risks', name: 'AI Risks, Safety & Governance', label: 'Risks & Governance' }
  ];

  const esc = (value = '') => String(value).replace(/[&<>"']/g, ch => ({
    '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;', "'": '&#39;'
  }[ch]));

  function render(terms) {
    const jumpNav = categories.map(category => {
      const count = terms.filter(term => (term.categories || []).includes(category.name)).length;
      return `<a href="#category-${category.key}" data-category-key="${category.key}"><span class="category-jump-dot" aria-hidden="true"></span>${esc(category.label)} <span aria-label="${count} terms">${count}</span></a>`;
    }).join('');

    const sections = categories.map(category => {
      const matches = terms
        .filter(term => (term.categories || []).includes(category.name))
        .sort((a, b) => a.term.localeCompare(b.term));

      const cards = matches.map(term => `<a class="category-term-card" href="terms/${encodeURIComponent(term.slug)}/"><h4>${esc(term.term)}</h4><p>${esc(term.definition)}</p></a>`).join('');

      return `<section class="category-collection" id="category-${category.key}" data-category-key="${category.key}"><div class="category-collection-heading"><h3>${esc(category.label)}</h3><span class="category-count">${matches.length} ${matches.length === 1 ? 'term' : 'terms'}</span></div><div class="category-term-grid">${cards}</div></section>`;
    }).join('');

    root.innerHTML = `<nav class="category-jump-nav" aria-label="Jump to category">${jumpNav}</nav>${sections}`;
  }

  fetch('data/terms.json')
    .then(response => {
      if (!response.ok) throw new Error('Could not load dictionary data.');
      return response.json();
    })
    .then(render)
    .catch(error => {
      root.innerHTML = `<p class="category-load-error">Unable to load category collections. ${esc(error.message)}</p>`;
    });
})();
