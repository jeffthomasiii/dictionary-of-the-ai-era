(() => {
  const search = document.getElementById('search');
  const toolbar = document.querySelector('.toolbar');
  const filters = [...document.querySelectorAll('.filter')];
  const dictionary = document.getElementById('dictionary');
  if (!search || !toolbar || !filters.length || !dictionary) return;

  if (!document.querySelector('link[data-mobile-browse-styles]')) {
    const style = document.createElement('link');
    style.rel = 'stylesheet';
    style.href = new URL('../css/mobile-browse.css', document.currentScript.src).href;
    style.dataset.mobileBrowseStyles = 'true';
    document.head.append(style);
  }

  const mobileQuery = window.matchMedia('(max-width: 680px)');
  const originalPlaceholder = search.getAttribute('placeholder') || '';
  const syncPlaceholder = () => {
    search.setAttribute('placeholder', mobileQuery.matches ? 'Search AILex…' : originalPlaceholder);
  };
  syncPlaceholder();
  mobileQuery.addEventListener?.('change', syncPlaceholder);

  const searchWrap = search.closest('.search-wrap');
  if (!searchWrap || searchWrap.closest('.mobile-browse-controls')) return;

  const controls = document.createElement('div');
  controls.className = 'mobile-browse-controls';
  searchWrap.parentNode.insertBefore(controls, searchWrap);
  controls.appendChild(searchWrap);

  const toggle = document.createElement('button');
  toggle.className = 'mobile-filter-toggle';
  toggle.type = 'button';
  toggle.setAttribute('aria-expanded', 'false');
  toggle.setAttribute('aria-controls', 'mobile-filter-menu');
  toggle.setAttribute('aria-label', 'Filter dictionary terms');
  toggle.innerHTML = '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M4 7h16M7 12h10M10 17h4"/></svg><span class="mobile-filter-label">All terms</span><svg class="mobile-filter-chevron" viewBox="0 0 24 24" aria-hidden="true"><path d="m7 9 5 5 5-5"/></svg>';
  controls.appendChild(toggle);

  const menu = document.createElement('div');
  menu.id = 'mobile-filter-menu';
  menu.className = 'mobile-filter-menu';
  menu.hidden = true;
  menu.setAttribute('role', 'menu');
  document.body.appendChild(menu);

  const keyFor = filter => {
    if (filter.classList.contains('culture')) return 'culture';
    if (filter.classList.contains('work')) return 'work';
    if (filter.classList.contains('systems')) return 'systems';
    if (filter.classList.contains('risks')) return 'risks';
    return 'all';
  };

  const labelFor = filter => filter.querySelector('span:last-child')?.textContent?.trim() || 'All terms';

  filters.forEach(filter => {
    const option = document.createElement('button');
    option.type = 'button';
    option.className = 'mobile-filter-option';
    option.dataset.category = filter.dataset.category;
    option.dataset.key = keyFor(filter);
    option.setAttribute('role', 'menuitem');
    option.innerHTML = `<span class="mobile-filter-dot" aria-hidden="true"></span><span>${labelFor(filter)}</span>`;
    menu.appendChild(option);
  });

  const options = [...menu.querySelectorAll('.mobile-filter-option')];
  const label = toggle.querySelector('.mobile-filter-label');

  function positionMenu() {
    if (menu.hidden) return;
    const rect = toggle.getBoundingClientRect();
    const gutter = 14;
    const width = Math.min(220, window.innerWidth - gutter * 2);
    const left = Math.min(window.innerWidth - width - gutter, Math.max(gutter, rect.right - width));
    menu.style.width = `${width}px`;
    menu.style.left = `${left}px`;
    menu.style.top = `${rect.bottom + 8}px`;
  }

  function closeMenu({restoreFocus = false} = {}) {
    menu.hidden = true;
    toggle.setAttribute('aria-expanded', 'false');
    if (restoreFocus) toggle.focus();
  }

  function openMenu() {
    menu.hidden = false;
    toggle.setAttribute('aria-expanded', 'true');
    positionMenu();
    const selected = menu.querySelector('[aria-current="true"]') || options[0];
    requestAnimationFrame(() => selected?.focus());
  }

  function syncFromFilter(filter) {
    if (!filter) return;
    label.textContent = labelFor(filter);
    options.forEach(option => option.setAttribute('aria-current', String(option.dataset.category === filter.dataset.category)));
  }

  syncFromFilter(filters.find(filter => filter.classList.contains('active')) || filters[0]);

  toggle.addEventListener('click', () => {
    if (menu.hidden) openMenu();
    else closeMenu();
  });

  options.forEach(option => {
    option.addEventListener('click', () => {
      const source = filters.find(filter => filter.dataset.category === option.dataset.category);
      source?.click();
      syncFromFilter(source);
      closeMenu({restoreFocus: true});
    });
  });

  filters.forEach(filter => filter.addEventListener('click', () => syncFromFilter(filter)));

  document.addEventListener('keydown', event => {
    if (event.key === 'Escape' && !menu.hidden) {
      event.preventDefault();
      closeMenu({restoreFocus: true});
    }
  });

  document.addEventListener('click', event => {
    if (!menu.hidden && !controls.contains(event.target) && !menu.contains(event.target)) closeMenu();
  });

  window.addEventListener('resize', () => {
    if (!mobileQuery.matches) closeMenu();
    else positionMenu();
  });
  window.addEventListener('scroll', positionMenu, {passive: true});
})();
