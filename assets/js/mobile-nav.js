(() => {
  const header = document.querySelector('.site-header');
  const headerInner = header?.querySelector('.header-inner');
  const desktopNav = header?.querySelector('.primary-nav');
  const themeToggle = header?.querySelector('.theme-toggle');

  if (!header || !headerInner || !desktopNav || header.querySelector('.mobile-nav-toggle')) return;

  const currentScript = document.currentScript;
  if (currentScript?.src && !document.querySelector('link[data-mobile-nav-styles]')) {
    const styles = document.createElement('link');
    styles.rel = 'stylesheet';
    styles.href = new URL('../css/mobile-nav.css', currentScript.src).href;
    styles.dataset.mobileNavStyles = 'true';
    document.head.append(styles);
  }

  const toggle = document.createElement('button');
  toggle.type = 'button';
  toggle.className = 'mobile-nav-toggle';
  toggle.setAttribute('aria-expanded', 'false');
  toggle.setAttribute('aria-controls', 'mobile-primary-nav');
  toggle.setAttribute('aria-label', 'Open navigation menu');
  toggle.innerHTML = '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M4 7h16M4 12h16M4 17h16"/></svg>';

  const panel = document.createElement('div');
  panel.className = 'mobile-nav-panel';
  panel.id = 'mobile-primary-nav';
  panel.hidden = true;

  const mobileNav = document.createElement('nav');
  mobileNav.className = 'mobile-primary-nav';
  mobileNav.setAttribute('aria-label', 'Mobile primary navigation');
  mobileNav.innerHTML = desktopNav.innerHTML;
  panel.append(mobileNav);

  if (themeToggle) headerInner.insertBefore(toggle, themeToggle);
  else headerInner.append(toggle);
  header.append(panel);

  const setOpen = (open, { focus = false } = {}) => {
    panel.hidden = !open;
    header.classList.toggle('mobile-nav-open', open);
    toggle.setAttribute('aria-expanded', String(open));
    toggle.setAttribute('aria-label', open ? 'Close navigation menu' : 'Open navigation menu');
    toggle.innerHTML = open
      ? '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="m6 6 12 12M18 6 6 18"/></svg>'
      : '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M4 7h16M4 12h16M4 17h16"/></svg>';
    if (open && focus) mobileNav.querySelector('a')?.focus();
  };

  toggle.addEventListener('click', () => setOpen(toggle.getAttribute('aria-expanded') !== 'true'));
  mobileNav.addEventListener('click', event => {
    if (event.target.closest('a')) setOpen(false);
  });

  document.addEventListener('keydown', event => {
    if (event.key === 'Escape' && toggle.getAttribute('aria-expanded') === 'true') {
      setOpen(false);
      toggle.focus();
    }
  });

  document.addEventListener('click', event => {
    if (toggle.getAttribute('aria-expanded') === 'true' && !header.contains(event.target)) setOpen(false);
  });

  const desktopQuery = window.matchMedia('(min-width: 981px)');
  const closeOnDesktop = event => { if (event.matches) setOpen(false); };
  desktopQuery.addEventListener?.('change', closeOnDesktop);
})();
