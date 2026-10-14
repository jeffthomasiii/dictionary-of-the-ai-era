(() => {
  const currentScript = document.currentScript;
  const assetVersion = new URL(currentScript?.src || window.location.href).searchParams.get('v');
  const siteRoot = currentScript?.src ? new URL('../../', currentScript.src) : new URL('./', window.location.href);
  const termPage = document.getElementById('term-page');

  function ensureTermPageShell() {
    if (!termPage) return false;

    let shellInjected = false;
    let header = document.querySelector('.site-header');
    if (!header) {
      header = document.createElement('header');
      header.className = 'site-header';
      header.dataset.shellInjected = 'true';
      header.innerHTML = `
        <div class="shell header-inner">
          <a class="brand" href="${siteRoot.href}" aria-label="EpochLex home">
            <span class="brand-lockup" aria-hidden="true"><img class="brand-lockup-image brand-lockup-light" src="${new URL('assets/brand/epochlex/epochlex-logo-horizontal-light.png', siteRoot).href}" alt=""><img class="brand-lockup-image brand-lockup-dark" src="${new URL('assets/brand/epochlex/epochlex-logo-horizontal-dark.png', siteRoot).href}" alt=""></span><span class="sr-only">EpochLex</span>
          </a>
          <nav class="primary-nav" aria-label="Primary navigation">
            <a class="active" href="${siteRoot.href}">Browse</a>
            <a href="${new URL('categories.html', siteRoot).href}">Categories</a>
            <a href="${new URL('about.html', siteRoot).href}">About</a>
            <a href="${new URL('contribute.html', siteRoot).href}">Contribute</a>
            <a href="${new URL('methodology.html', siteRoot).href}">Methodology</a>
          </nav>
          <button id="theme-toggle" class="theme-toggle" type="button" aria-label="Switch color theme" title="Switch color theme">
            <span class="sun" aria-hidden="true">☼</span><span class="toggle-track"><span class="toggle-knob"></span></span><span class="moon" aria-hidden="true">☾</span>
          </button>
        </div>`;
      document.body.insertBefore(header, document.body.firstChild);
      shellInjected = true;
    }

    if (!document.querySelector('.site-footer')) {
      const footer = document.createElement('footer');
      footer.className = 'site-footer';
      footer.innerHTML = '<div class="shell footer-inner"><span class="footer-mark" aria-hidden="true">◎</span><p><strong>EpochLex · Dictionary of the AI Era</strong><br>Vibe coded · Human-directed · AI-assisted · Human-reviewed</p><p class="footer-license">Code: MIT · Content: CC BY 4.0</p></div>';
      document.body.append(footer);
    }

    return shellInjected;
  }

  const shellInjected = ensureTermPageShell();

  if (currentScript?.src && !document.querySelector('script[data-pwa-loader]')) {
    const pwaScript = document.createElement('script');
    const pwaUrl = new URL('pwa.js', currentScript.src);
    pwaUrl.searchParams.set('v', 'epochlex-pwa-20260915-2');
    pwaScript.src = pwaUrl.href;
    pwaScript.dataset.pwaLoader = 'true';
    document.head.append(pwaScript);
  }

  const header = document.querySelector('.site-header');
  const headerInner = header?.querySelector('.header-inner');
  const desktopNav = header?.querySelector('.primary-nav');
  const themeToggle = header?.querySelector('.theme-toggle');

  if (shellInjected && themeToggle) {
    const readTheme = () => {
      try {
        return localStorage.getItem('ai-era-theme') || (window.matchMedia('(prefers-color-scheme: dark)').matches ? 'dark' : 'light');
      } catch (_) {
        return window.matchMedia('(prefers-color-scheme: dark)').matches ? 'dark' : 'light';
      }
    };
    const setTheme = theme => {
      document.documentElement.dataset.theme = theme;
      try { localStorage.setItem('ai-era-theme', theme); } catch (_) {}
      const next = theme === 'dark' ? 'light' : 'dark';
      themeToggle.setAttribute('aria-label', `Switch to ${next} mode`);
      themeToggle.setAttribute('title', `Switch to ${next} mode`);
    };
    setTheme(readTheme());
    themeToggle.addEventListener('click', () => setTheme(document.documentElement.dataset.theme === 'dark' ? 'light' : 'dark'));
  }

  if (document.getElementById('dictionary') && currentScript?.src && !document.querySelector('script[data-browse-collapse-loader]')) {
    const collapseScript = document.createElement('script');
    const collapseUrl = new URL('browse-collapse.js', currentScript.src);
    if (assetVersion) collapseUrl.searchParams.set('v', assetVersion);
    collapseScript.src = collapseUrl.href;
    collapseScript.dataset.browseCollapseLoader = 'true';
    document.head.append(collapseScript);
  }

  if (!header || !headerInner || !desktopNav || header.querySelector('.mobile-nav-details')) return;

  if (currentScript?.src && !document.querySelector('link[data-mobile-nav-styles]')) {
    const styles = document.createElement('link');
    styles.rel = 'stylesheet';
    const stylesUrl = new URL('../css/mobile-nav.css', currentScript.src);
    if (assetVersion) stylesUrl.searchParams.set('v', assetVersion);
    styles.href = stylesUrl.href;
    styles.dataset.mobileNavStyles = 'true';
    document.head.append(styles);
  }

  const details = document.createElement('details');
  details.className = 'mobile-nav-details';

  const summary = document.createElement('summary');
  summary.className = 'mobile-nav-toggle';
  summary.setAttribute('aria-label', 'Navigation menu');
  summary.innerHTML = '<span class="mobile-nav-icon mobile-nav-icon-menu" aria-hidden="true"><svg viewBox="0 0 24 24"><path d="M4 7h16M4 12h16M4 17h16"/></svg></span><span class="mobile-nav-icon mobile-nav-icon-close" aria-hidden="true"><svg viewBox="0 0 24 24"><path d="m6 6 12 12M18 6 6 18"/></svg></span>';

  const panel = document.createElement('div');
  panel.className = 'mobile-nav-panel';

  const mobileNav = document.createElement('nav');
  mobileNav.className = 'mobile-primary-nav';
  mobileNav.setAttribute('aria-label', 'Mobile primary navigation');
  mobileNav.innerHTML = desktopNav.innerHTML;

  const searchLink = document.createElement('a');
  searchLink.className = 'mobile-nav-search';
  searchLink.href = new URL('#search', siteRoot).href;
  searchLink.textContent = 'Search';
  mobileNav.prepend(searchLink);

  panel.append(mobileNav);
  details.append(summary, panel);

  if (themeToggle) headerInner.insertBefore(details, themeToggle);
  else headerInner.append(details);

  mobileNav.addEventListener('click', event => {
    if (event.target.closest('a')) details.removeAttribute('open');
  });

  document.addEventListener('keydown', event => {
    if (event.key === 'Escape' && details.open) {
      details.removeAttribute('open');
      summary.focus();
    }
  });

  document.addEventListener('click', event => {
    if (details.open && !header.contains(event.target)) details.removeAttribute('open');
  });

  const desktopQuery = window.matchMedia('(min-width: 981px)');
  desktopQuery.addEventListener?.('change', event => {
    if (event.matches) details.removeAttribute('open');
  });

  if (document.getElementById('dictionary') && currentScript?.src && !document.querySelector('script[data-mobile-browse-loader]')) {
    const browseScript = document.createElement('script');
    const browseUrl = new URL('mobile-browse.js', currentScript.src);
    if (assetVersion) browseUrl.searchParams.set('v', assetVersion);
    browseScript.src = browseUrl.href;
    browseScript.dataset.mobileBrowseLoader = 'true';
    document.head.append(browseScript);
  }
})();
