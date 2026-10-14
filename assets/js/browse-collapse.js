(() => {
  const dictionary = document.getElementById('dictionary');
  if (!dictionary) return;

  const LIST_PREVIEW_COUNT = 4;
  const GRID_PREVIEW_COUNT = 6;
  const expandedLetters = new Set();
  let applying = false;
  let applyQueued = false;

  if (!document.querySelector('style[data-browse-collapse-styles]')) {
    const styles = document.createElement('style');
    styles.dataset.browseCollapseStyles = 'true';
    styles.textContent = `
      .letter-group .entry[hidden]{display:none!important}
      .letter-expand-control{display:flex;justify-content:flex-start;margin:16px 0 4px}
      .letter-expand-button{appearance:none;border:0;background:transparent;color:var(--accent,var(--teal,#477f7a));font:600 .82rem/1.3 var(--font-sans,system-ui,sans-serif);letter-spacing:.01em;padding:7px 0;cursor:pointer;text-decoration:none}
      .letter-expand-button:hover{text-decoration:underline;text-underline-offset:3px}
      .letter-expand-button:focus-visible{outline:2px solid currentColor;outline-offset:4px;border-radius:2px}
      .letter-expand-button .expand-arrow{display:inline-block;margin-left:5px;transition:transform .18s ease}
      .letter-expand-button[aria-expanded="true"] .expand-arrow{transform:rotate(180deg)}
      @media(max-width:640px){.letter-expand-control{margin-top:12px}.letter-expand-button{font-size:.8rem}}
      @media(prefers-reduced-motion:reduce){.letter-expand-button .expand-arrow{transition:none}}
    `;
    document.head.append(styles);
  }

  const isRefined = () => {
    const query = document.getElementById('search')?.value.trim();
    const activeFilter = document.querySelector('.filter.active');
    const category = activeFilter?.dataset.category || 'all';
    return Boolean(query) || category !== 'all';
  };

  const previewCount = () => dictionary.classList.contains('grid-view') ? GRID_PREVIEW_COUNT : LIST_PREVIEW_COUNT;

  function applyCollapseState() {
    if (applying) return;
    applying = true;

    const refined = isRefined();
    const limit = previewCount();

    dictionary.querySelectorAll('.letter-group').forEach(group => {
      const entriesWrap = group.querySelector('.letter-entries');
      const entries = [...group.querySelectorAll('.entry')];
      const heading = group.querySelector('.letter-heading');
      const letter = (heading?.textContent || '').trim();
      group.querySelector('.letter-expand-control')?.remove();

      if (!entriesWrap || !letter) return;

      if (refined || entries.length <= limit) {
        entries.forEach(entry => { entry.hidden = false; });
        return;
      }

      const expanded = expandedLetters.has(letter);
      entries.forEach((entry, index) => { entry.hidden = !expanded && index >= limit; });

      const control = document.createElement('div');
      control.className = 'letter-expand-control';
      const button = document.createElement('button');
      button.type = 'button';
      button.className = 'letter-expand-button';
      button.dataset.letter = letter;
      button.setAttribute('aria-expanded', String(expanded));
      button.setAttribute('aria-controls', `${group.id}-entries`);
      entriesWrap.id = `${group.id}-entries`;
      button.innerHTML = expanded
        ? `Show fewer <span class="expand-arrow" aria-hidden="true">⌄</span>`
        : `Show all ${entries.length} ${letter} terms <span class="expand-arrow" aria-hidden="true">⌄</span>`;
      control.append(button);
      group.append(control);
    });

    applying = false;
  }

  function queueApply() {
    if (applyQueued) return;
    applyQueued = true;
    requestAnimationFrame(() => {
      applyQueued = false;
      applyCollapseState();
    });
  }

  dictionary.addEventListener('click', event => {
    const button = event.target.closest('.letter-expand-button');
    if (!button) return;
    const letter = button.dataset.letter;
    if (!letter) return;
    if (expandedLetters.has(letter)) expandedLetters.delete(letter);
    else expandedLetters.add(letter);
    applyCollapseState();
  });

  ['list-view', 'grid-view'].forEach(id => {
    document.getElementById(id)?.addEventListener('click', () => {
      expandedLetters.clear();
      queueApply();
    });
  });

  document.getElementById('search')?.addEventListener('input', queueApply);
  document.querySelector('.toolbar')?.addEventListener('click', event => {
    if (event.target.closest('.filter')) queueApply();
  });

  const observer = new MutationObserver(mutations => {
    if (applying) return;
    if (mutations.some(mutation => mutation.type === 'childList' || mutation.attributeName === 'class')) queueApply();
  });
  observer.observe(dictionary, { childList: true, subtree: false, attributes: true, attributeFilter: ['class'] });

  queueApply();
})();
