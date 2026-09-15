(() => {
  const currentScript = document.currentScript;
  if (!currentScript?.src) return;

  const siteRoot = new URL('../../', currentScript.src);
  const assetVersion = new URL(currentScript.src).searchParams.get('v') || 'epochlex-pwa-20260915-2';

  if (!document.querySelector('link[rel="manifest"]')) {
    const manifest = document.createElement('link');
    manifest.rel = 'manifest';
    manifest.href = new URL('manifest.webmanifest', siteRoot).href;
    document.head.append(manifest);
  }

  if (!document.querySelector('link[data-pwa-styles]')) {
    const styles = document.createElement('link');
    styles.rel = 'stylesheet';
    const stylesUrl = new URL('assets/css/pwa.css', siteRoot);
    stylesUrl.searchParams.set('v', assetVersion);
    styles.href = stylesUrl.href;
    styles.dataset.pwaStyles = 'true';
    document.head.append(styles);
  }

  if (!document.querySelector('link[rel="apple-touch-icon"]')) {
    const touchIcon = document.createElement('link');
    touchIcon.rel = 'apple-touch-icon';
    touchIcon.href = new URL('favicon.png', siteRoot).href;
    document.head.append(touchIcon);
  }

  const ensureMeta = (name, content) => {
    if (document.querySelector(`meta[name="${name}"]`)) return;
    const meta = document.createElement('meta');
    meta.name = name;
    meta.content = content;
    document.head.append(meta);
  };

  ensureMeta('theme-color', '#0F1D2D');
  ensureMeta('mobile-web-app-capable', 'yes');
  ensureMeta('apple-mobile-web-app-capable', 'yes');
  ensureMeta('apple-mobile-web-app-status-bar-style', 'black-translucent');
  ensureMeta('apple-mobile-web-app-title', 'EpochLex');

  const standaloneQuery = window.matchMedia?.('(display-mode: standalone)');
  const isStandalone = () => Boolean(standaloneQuery?.matches || window.navigator.standalone === true);

  const icons = {
    browse: '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M3.5 11.2 12 4l8.5 7.2"/><path d="M5.5 10.2V20h13v-9.8M9.2 20v-6h5.6v6"/></svg>',
    categories: '<svg viewBox="0 0 24 24" aria-hidden="true"><rect x="4" y="4" width="6" height="6" rx="1"/><rect x="14" y="4" width="6" height="6" rx="1"/><rect x="4" y="14" width="6" height="6" rx="1"/><rect x="14" y="14" width="6" height="6" rx="1"/></svg>',
    word: '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M3.5 5.5c3-.8 5.8-.3 8.5 1.4v12c-2.7-1.7-5.5-2.2-8.5-1.4v-12Z"/><path d="M20.5 5.5c-3-.8-5.8-.3-8.5 1.4v12c2.7-1.7 5.5-2.2 8.5-1.4v-12Z"/></svg>',
    about: '<svg viewBox="0 0 24 24" aria-hidden="true"><circle cx="12" cy="12" r="9"/><path d="M12 10.8v5.5M12 7.7h.01"/></svg>',
    more: '<svg viewBox="0 0 24 24" aria-hidden="true"><circle cx="5" cy="12" r="1.4"/><circle cx="12" cy="12" r="1.4"/><circle cx="19" cy="12" r="1.4"/></svg>',
    contribute: '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M12 3v12M7.5 7.5 12 3l4.5 4.5"/><path d="M5 13v6h14v-6"/></svg>',
    methodology: '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M4 5.5h6.5c1.3 0 1.5.7 1.5 1.5v12c0-.8-.2-1.5-1.5-1.5H4v-12Z"/><path d="M20 5.5h-6.5c-1.3 0-1.5.7-1.5 1.5v12c0-.8.2-1.5 1.5-1.5H20v-12Z"/></svg>',
    close: '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="m6 6 12 12M18 6 6 18"/></svg>'
  };

  const relativePath = () => {
    const rootPath = siteRoot.pathname.endsWith('/') ? siteRoot.pathname : `${siteRoot.pathname}/`;
    const current = window.location.pathname;
    const withinRoot = current.startsWith(rootPath) ? current.slice(rootPath.length) : current.replace(/^\//, '');
    return withinRoot.replace(/^\/+|\/+$/g, '');
  };

  function activeSection() {
    const path = relativePath();
    if (path === 'categories.html') return 'categories';
    if (path === 'word-of-the-day') return 'word';
    if (path === 'about.html') return 'about';
    if (path === 'contribute.html' || path === 'methodology.html') return 'more';
    return 'browse';
  }

  function navLink(key, label, href) {
    const active = activeSection() === key;
    return `<a class="pwa-app-tab${active ? ' is-active' : ''}" href="${new URL(href, siteRoot).href}"${active ? ' aria-current="page"' : ''}>${icons[key]}<span>${label}</span></a>`;
  }

  function wireStandaloneThemeToggle(button) {
    if (!button || button.dataset.pwaThemeWired) return;
    button.dataset.pwaThemeWired = 'true';

    const stored = (() => {
      try { return localStorage.getItem('ai-era-theme'); } catch (_) { return null; }
    })();
    if (!document.documentElement.dataset.theme) {
      document.documentElement.dataset.theme = stored || (window.matchMedia?.('(prefers-color-scheme: dark)').matches ? 'dark' : 'light');
    }

    const syncLabel = () => {
      const next = document.documentElement.dataset.theme === 'dark' ? 'light' : 'dark';
      button.setAttribute('aria-label', `Switch to ${next} mode`);
      button.setAttribute('title', `Switch to ${next} mode`);
    };

    syncLabel();
    button.addEventListener('click', () => {
      const next = document.documentElement.dataset.theme === 'dark' ? 'light' : 'dark';
      document.documentElement.dataset.theme = next;
      try { localStorage.setItem('ai-era-theme', next); } catch (_) {}
      syncLabel();
    });
  }

  function ensureStandaloneHeader() {
    let header = document.querySelector('.site-header');
    if (header) return header;

    header = document.createElement('header');
    header.className = 'site-header pwa-generated-header';
    header.innerHTML = `
      <div class="shell header-inner">
        <a class="brand" href="${siteRoot.href}" aria-label="EpochLex home">
          <span class="brand-lockup" aria-hidden="true">
            <img class="brand-lockup-image brand-lockup-light" src="${new URL('assets/brand/epochlex/epochlex-logo-horizontal-light.png', siteRoot).href}" alt="">
            <img class="brand-lockup-image brand-lockup-dark" src="${new URL('assets/brand/epochlex/epochlex-logo-horizontal-dark.png', siteRoot).href}" alt="">
          </span>
          <span class="sr-only">EpochLex</span>
        </a>
        <button class="theme-toggle pwa-generated-theme-toggle" type="button" aria-label="Switch color theme" title="Switch color theme">
          <span class="sun" aria-hidden="true">☼</span><span class="toggle-track"><span class="toggle-knob"></span></span><span class="moon" aria-hidden="true">☾</span>
        </button>
      </div>`;
    document.body.prepend(header);
    wireStandaloneThemeToggle(header.querySelector('.theme-toggle'));
    return header;
  }

  function closeMoreSheet() {
    const backdrop = document.querySelector('.pwa-more-backdrop');
    const sheet = document.querySelector('.pwa-more-sheet');
    if (!backdrop || !sheet || sheet.hidden) return;
    backdrop.hidden = true;
    sheet.hidden = true;
    document.documentElement.classList.remove('pwa-more-open');
    const moreButton = document.querySelector('.pwa-app-more');
    moreButton?.setAttribute('aria-expanded', 'false');
    moreButton?.focus();
  }

  function openMoreSheet() {
    const backdrop = document.querySelector('.pwa-more-backdrop');
    const sheet = document.querySelector('.pwa-more-sheet');
    if (!backdrop || !sheet) return;
    backdrop.hidden = false;
    sheet.hidden = false;
    document.documentElement.classList.add('pwa-more-open');
    document.querySelector('.pwa-app-more')?.setAttribute('aria-expanded', 'true');
    sheet.querySelector('a,button')?.focus();
  }

  function ensureAppShell() {
    if (!isStandalone() || document.querySelector('.pwa-app-nav')) return;

    document.documentElement.dataset.pwaStandalone = 'true';
    document.body.classList.add('pwa-standalone');
    ensureStandaloneHeader();

    const nav = document.createElement('nav');
    nav.className = 'pwa-app-nav';
    nav.setAttribute('aria-label', 'App navigation');
    nav.innerHTML = `
      ${navLink('browse', 'Browse', './')}
      ${navLink('categories', 'Categories', 'categories.html')}
      ${navLink('word', 'Word', 'word-of-the-day/')}
      ${navLink('about', 'About', 'about.html')}
      <button class="pwa-app-tab pwa-app-more${activeSection() === 'more' ? ' is-active' : ''}" type="button" aria-haspopup="dialog" aria-expanded="false">${icons.more}<span>More</span></button>`;

    const backdrop = document.createElement('button');
    backdrop.type = 'button';
    backdrop.className = 'pwa-more-backdrop';
    backdrop.hidden = true;
    backdrop.setAttribute('aria-label', 'Close more menu');

    const sheet = document.createElement('section');
    sheet.className = 'pwa-more-sheet';
    sheet.hidden = true;
    sheet.setAttribute('role', 'dialog');
    sheet.setAttribute('aria-modal', 'true');
    sheet.setAttribute('aria-labelledby', 'pwa-more-title');
    sheet.innerHTML = `
      <div class="pwa-more-handle" aria-hidden="true"></div>
      <div class="pwa-more-heading">
        <div><p class="pwa-more-kicker">EpochLex</p><h2 id="pwa-more-title">More</h2></div>
        <button class="pwa-more-close" type="button" aria-label="Close more menu">${icons.close}</button>
      </div>
      <div class="pwa-more-links">
        <a href="${new URL('contribute.html', siteRoot).href}">${icons.contribute}<span><strong>Contribute</strong><small>Suggest terms, corrections, research, design, or code.</small></span></a>
        <a href="${new URL('methodology.html', siteRoot).href}">${icons.methodology}<span><strong>Methodology</strong><small>See how EpochLex selects, researches, and reviews entries.</small></span></a>
      </div>`;

    document.body.append(backdrop, sheet, nav);

    const moreButton = nav.querySelector('.pwa-app-more');
    moreButton?.addEventListener('click', () => {
      if (sheet.hidden) openMoreSheet();
      else closeMoreSheet();
    });

    backdrop.addEventListener('click', closeMoreSheet);
    sheet.querySelector('.pwa-more-close')?.addEventListener('click', closeMoreSheet);
    sheet.querySelectorAll('a').forEach(link => link.addEventListener('click', closeMoreSheet));

    document.addEventListener('keydown', event => {
      if (event.key === 'Escape') closeMoreSheet();
    });
  }

  function syncStandaloneState() {
    if (isStandalone()) ensureAppShell();
    else {
      delete document.documentElement.dataset.pwaStandalone;
      document.body?.classList.remove('pwa-standalone');
    }
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', syncStandaloneState, { once: true });
  } else {
    syncStandaloneState();
  }
  standaloneQuery?.addEventListener?.('change', syncStandaloneState);

  if ('serviceWorker' in navigator) {
    window.addEventListener('load', () => {
      navigator.serviceWorker.register(new URL('service-worker.js', siteRoot), { scope: siteRoot.pathname })
        .catch(error => console.warn('EpochLex service worker registration failed.', error));
    }, { once: true });
  }
})();
