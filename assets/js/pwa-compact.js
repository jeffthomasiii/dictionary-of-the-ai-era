(() => {
  if (document.documentElement.dataset.pwaStandalone !== 'true') return;

  const script = document.currentScript;
  const siteRoot = script?.src ? new URL('../../', script.src) : new URL('./', window.location.href);
  const path = (() => {
    const rootPath = siteRoot.pathname.endsWith('/') ? siteRoot.pathname : `${siteRoot.pathname}/`;
    const current = window.location.pathname;
    return (current.startsWith(rootPath) ? current.slice(rootPath.length) : current.replace(/^\//, '')).replace(/^\/+|\/+$/g, '');
  })();

  const categoryDefinitions = [
    {
      name: 'AI Culture & Slang',
      label: 'Culture & Slang',
      key: 'culture',
      description: 'Language, memes, and evolving expressions.',
      icon: '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M5 6h14v9H9l-4 3V6Z"/><circle cx="9" cy="10.5" r=".7"/><circle cx="12" cy="10.5" r=".7"/><circle cx="15" cy="10.5" r=".7"/></svg>'
    },
    {
      name: 'AI Ways of Working',
      label: 'Ways of Working',
      key: 'work',
      description: 'People, processes, and new collaborations.',
      icon: '<svg viewBox="0 0 24 24" aria-hidden="true"><circle cx="8" cy="8" r="3"/><circle cx="16" cy="8" r="3"/><path d="M3.5 19c.3-4 2-6 4.5-6s4.2 2 4.5 6M11.5 19c.3-4 2-6 4.5-6s4.2 2 4.5 6"/></svg>'
    },
    {
      name: 'AI Systems & Technical Concepts',
      label: 'Systems & Technical',
      key: 'systems',
      description: 'Models, training, infrastructure, and more.',
      icon: '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="m12 3 7 4v10l-7 4-7-4V7l7-4Z"/><path d="m5 7 7 4 7-4M12 11v10"/></svg>'
    },
    {
      name: 'AI Risks, Safety & Governance',
      label: 'Risks & Governance',
      key: 'risks',
      description: 'Safety, policy, ethics, and accountability.',
      icon: '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M12 3 19 6v5c0 4.6-2.7 8-7 10-4.3-2-7-5.4-7-10V6l7-3Z"/></svg>'
    },
    {
      name: 'AI Organizations, Products & Models',
      label: 'Organizations, Products & Models',
      key: 'entities',
      description: 'Companies, tools, models, and named AI entities.',
      icon: '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M4 20h16M6 20V8l6-4 6 4v12M9 10h2v2H9zM13 10h2v2h-2zM9 14h2v2H9zM13 14h2v2h-2z"/></svg>'
    }
  ];

  function waitFor(selector, callback) {
    const found = document.querySelector(selector);
    if (found) {
      callback(found);
      return;
    }
    const observer = new MutationObserver(() => {
      const node = document.querySelector(selector);
      if (!node) return;
      observer.disconnect();
      callback(node);
    });
    observer.observe(document.documentElement, { childList: true, subtree: true });
  }

  function markView(name) {
    document.body.classList.add(`pwa-view-${name}`);
  }

  function afterPageLoad(callback) {
    if (document.readyState === 'complete') callback();
    else window.addEventListener('load', callback, { once: true });
  }

  function restorePendingCategory() {
    let category = null;
    try {
      category = sessionStorage.getItem('epochlex-pwa-category');
      sessionStorage.removeItem('epochlex-pwa-category');
    } catch (_) {}
    if (!category) return;

    afterPageLoad(() => {
      const button = [...document.querySelectorAll('.filter')].find(item => item.dataset.category === category);
      if (!button) return;
      button.click();
      requestAnimationFrame(() => document.getElementById('browse')?.scrollIntoView({ block: 'start' }));
    });
  }

  function refineBrowse() {
    markView('browse');
    afterPageLoad(() => document.getElementById('list-view')?.click());
    restorePendingCategory();
  }

  async function refineCategories() {
    markView('categories');
    const main = document.querySelector('main');
    if (!main || main.querySelector('.pwa-category-app')) return;

    const section = document.createElement('section');
    section.className = 'pwa-category-app shell';
    section.innerHTML = `
      <header class="pwa-app-page-heading">
        <p class="eyebrow">Explore by Category</p>
        <h1>Find Your Starting Point</h1>
        <p>Browse terms and concepts across key areas of the AI era.</p>
      </header>
      <div class="pwa-category-card-list" aria-live="polite"><p class="pwa-app-loading">Loading categories…</p></div>`;
    main.prepend(section);

    try {
      const response = await fetch(new URL('data/terms.json', siteRoot));
      if (!response.ok) throw new Error('Could not load terms.');
      const terms = await response.json();
      const list = section.querySelector('.pwa-category-card-list');
      list.innerHTML = categoryDefinitions.map(category => {
        const count = terms.filter(term => (term.categories || []).includes(category.name)).length;
        return `
          <a class="pwa-category-card pwa-category-card--${category.key}" href="${siteRoot.href}" data-pwa-category="${category.name}">
            <span class="pwa-category-icon">${category.icon}</span>
            <span class="pwa-category-copy"><strong>${category.label}</strong><small>${category.description}</small></span>
            <span class="pwa-category-count">${count} terms</span>
            <span class="pwa-category-chevron" aria-hidden="true">›</span>
          </a>`;
      }).join('');

      list.querySelectorAll('[data-pwa-category]').forEach(link => {
        link.addEventListener('click', () => {
          try { sessionStorage.setItem('epochlex-pwa-category', link.dataset.pwaCategory); } catch (_) {}
        });
      });
    } catch (_) {
      section.querySelector('.pwa-category-card-list').innerHTML = '<p class="pwa-app-loading">Categories are temporarily unavailable.</p>';
    }
  }

  function aboutDetailsCard(title, description, node, secondary = false) {
    const details = document.createElement('details');
    details.className = `pwa-about-card${secondary ? ' pwa-about-card--secondary' : ''}`;
    const summary = document.createElement('summary');
    summary.innerHTML = `<span><strong>${title}</strong><small>${description}</small></span><span class="pwa-about-chevron" aria-hidden="true">›</span>`;
    const content = document.createElement('div');
    content.className = 'pwa-about-card-content';
    content.append(node);
    details.append(summary, content);
    return details;
  }

  function refineAbout() {
    markView('about');
    const main = document.querySelector('main');
    const page = document.querySelector('.content-page--editorial');
    if (!main || !page || main.querySelector('.pwa-about-app')) return;

    const introCards = [...page.querySelectorAll('.doc-intro-grid > .doc-card')];
    const sections = [...page.querySelectorAll(':scope > .doc-section')];
    const researchCards = [...page.querySelectorAll('.doc-card-grid > .doc-card')];
    const callout = page.querySelector(':scope > .doc-callout');

    const primary = [
      ['What EpochLex means', 'The name, pronunciation, and the idea behind it.', introCards[0]],
      ['Why a dictionary for the AI era?', 'Why AI-era language deserves a living reference.', introCards[1]],
      ['What you can do', 'Search, browse, listen, explore, and discover.', sections[0]],
      ['Our origin story', 'How Meat Proxy became the beginning of EpochLex.', sections[1]],
      ['More than a definition', 'How provenance, evidence, and research fit together.', researchCards[0]],
      ['Designed to change with the language', 'How the Living Dictionary evolves over time.', researchCards[1]]
    ].filter(item => item[2]);

    const app = document.createElement('section');
    app.className = 'pwa-about-app shell';
    app.innerHTML = `
      <header class="pwa-app-page-heading">
        <p class="eyebrow">About EpochLex</p>
        <h1>Dictionary of the AI Era</h1>
        <p>A living, open-source reference for the language developing around artificial intelligence.</p>
      </header>
      <div class="pwa-about-card-list"></div>
      <div class="pwa-about-secondary-list"></div>`;

    const cardList = app.querySelector('.pwa-about-card-list');
    primary.forEach(([title, description, node]) => cardList.append(aboutDetailsCard(title, description, node)));

    const secondary = app.querySelector('.pwa-about-secondary-list');
    if (callout) secondary.append(aboutDetailsCard('How EpochLex is built', 'The human-directed, AI-assisted development experiment.', callout, true));
    const licensing = sections.find(section => section.querySelector('h2')?.textContent.trim() === 'Licensing');
    if (licensing) secondary.append(aboutDetailsCard('Open source & licensing', 'Code, content, and how EpochLex can be reused.', licensing, true));

    main.prepend(app);
  }

  function refineWord() {
    markView('word');

    waitFor('.wotd-feature-card', () => {
      document.body.classList.add('pwa-word-ready');
    });

    waitFor('.wotd-history-list', list => {
      if (list.children.length <= 5) return;
      const section = list.closest('.wotd-history-section');
      const heading = section?.querySelector('.wotd-history-heading');
      if (!section || !heading || heading.querySelector('.pwa-history-toggle')) return;
      const button = document.createElement('button');
      button.className = 'pwa-history-toggle';
      button.type = 'button';
      button.textContent = 'See all';
      button.addEventListener('click', () => {
        const expanded = section.classList.toggle('pwa-history-expanded');
        button.textContent = expanded ? 'Show less' : 'See all';
      });
      heading.append(button);
    });
  }

  if (!path || path === 'index.html') refineBrowse();
  else if (path === 'categories.html') refineCategories();
  else if (path === 'word-of-the-day') refineWord();
  else if (path === 'about.html') refineAbout();
})();
