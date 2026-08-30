(() => {
  const header = document.querySelector('.site-header');
  const headerInner = header?.querySelector('.header-inner');
  const desktopNav = header?.querySelector('.primary-nav');
  const themeToggle = header?.querySelector('.theme-toggle');

  if (!header || !headerInner || !desktopNav || header.querySelector('.mobile-nav-details')) return;

  const currentScript = document.currentScript;
  const assetVersion = new URL(currentScript?.src || window.location.href).searchParams.get('v');
  const siteRoot = currentScript?.src ? new URL('../../', currentScript.src) : new URL('./', window.location.href);
  if (currentScript?.src && !document.querySelector('link[data-mobile-nav-styles]')) {
    const styles = document.createElement('link');
    styles.rel = 'stylesheet';
    const stylesUrl = new URL('../css/mobile-nav.css', currentScript.src);
    if (assetVersion) stylesUrl.searchParams.set('v', assetVersion);
    styles.href = stylesUrl.href;
    styles.dataset.mobileNavStyles = 'true';
    document.head.append(styles);
  }

  if (currentScript?.src && !document.querySelector('script[data-pwa-loader]')) {
    const pwaScript = document.createElement('script');
    const pwaUrl = new URL('pwa.js', currentScript.src);
    if (assetVersion) pwaUrl.searchParams.set('v', assetVersion);
    pwaScript.src = pwaUrl.href;
    pwaScript.dataset.pwaLoader = 'true';
    document.head.append(pwaScript);
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
