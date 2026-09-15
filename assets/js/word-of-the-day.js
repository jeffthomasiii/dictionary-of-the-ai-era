(() => {
  const currentScript = document.currentScript;
  if (!currentScript?.src) return;

  const siteRoot = new URL('../../', currentScript.src);
  const TERMS_URL = new URL('data/terms.json', siteRoot).href;
  const TIME_ZONE = 'America/Los_Angeles';
  const START_DATE = '2026-09-15';
  const ALGORITHM_VERSION = 'epochlex-wotd-v1';
  const NO_REPEAT_DAYS = 90;

  const esc = (value = '') => String(value).replace(/[&<>"']/g, ch => ({
    '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;', "'": '&#39;'
  }[ch]));

  const isYmd = value => /^\d{4}-\d{2}-\d{2}$/.test(value || '');

  function getEpochLexDate(now = new Date()) {
    const parts = new Intl.DateTimeFormat('en-US', {
      timeZone: TIME_ZONE,
      year: 'numeric', month: '2-digit', day: '2-digit'
    }).formatToParts(now).reduce((acc, part) => {
      if (part.type !== 'literal') acc[part.type] = part.value;
      return acc;
    }, {});
    return `${parts.year}-${parts.month}-${parts.day}`;
  }

  function addDays(ymd, amount) {
    const [year, month, day] = ymd.split('-').map(Number);
    const date = new Date(Date.UTC(year, month - 1, day + amount));
    return date.toISOString().slice(0, 10);
  }

  function compareDates(a, b) {
    return a.localeCompare(b);
  }

  function formatDate(ymd, options = {}) {
    const [year, month, day] = ymd.split('-').map(Number);
    const date = new Date(Date.UTC(year, month - 1, day, 12));
    return new Intl.DateTimeFormat('en-US', {
      timeZone: 'UTC',
      year: 'numeric', month: 'long', day: 'numeric',
      ...options
    }).format(date);
  }

  function hash32(input) {
    let hash = 0x811c9dc5;
    for (let i = 0; i < input.length; i += 1) {
      hash ^= input.charCodeAt(i);
      hash = Math.imul(hash, 0x01000193);
    }
    return hash >>> 0;
  }

  function eligibleTerms(terms, date) {
    return terms
      .filter(term => term && term.slug && term.term && isYmd(term.added) && compareDates(term.added, date) < 0)
      .sort((a, b) => a.slug.localeCompare(b.slug));
  }

  function pickForDate(terms, date, recentSlugs) {
    const eligible = eligibleTerms(terms, date);
    if (!eligible.length) return null;

    let protectedRecent = [...recentSlugs];
    let candidates = eligible.filter(term => !protectedRecent.includes(term.slug));

    while (!candidates.length && protectedRecent.length) {
      protectedRecent = protectedRecent.slice(1);
      candidates = eligible.filter(term => !protectedRecent.includes(term.slug));
    }

    if (!candidates.length) return null;
    const seed = hash32(`${ALGORITHM_VERSION}|${date}`);
    return candidates[seed % candidates.length];
  }

  function buildSchedule(terms, throughDate) {
    const schedule = new Map();
    if (compareDates(throughDate, START_DATE) < 0) return schedule;

    const recent = [];
    for (let date = START_DATE; compareDates(date, throughDate) <= 0; date = addDays(date, 1)) {
      const term = pickForDate(terms, date, recent);
      if (!term) continue;
      schedule.set(date, term);
      recent.push(term.slug);
      if (recent.length > NO_REPEAT_DAYS) recent.shift();
    }
    return schedule;
  }

  function categoryClass(category = '') {
    if (category === 'AI Culture & Slang') return 'culture';
    if (category === 'AI Ways of Working') return 'work';
    if (category === 'AI Risks, Safety & Governance') return 'risks';
    if (category === 'AI Organizations, Products & Models') return 'entities';
    return 'systems';
  }

  function categoryMarkup(term) {
    return (term.categories || []).map(category =>
      `<span class="wotd-category ${categoryClass(category)}">${esc(category)}</span>`
    ).join('');
  }

  function pronunciationMarkup(term, className = 'pronunciation-button') {
    const audio = window.EpochLexPronunciation?.button?.(term, className) || '';
    return `<span class="wotd-pronunciation">${esc(term.pronunciation || '')}</span>${audio}`;
  }

  function wirePronunciation(container, term) {
    if (!container || !window.EpochLexPronunciation?.wire) return;
    const button = container.querySelector('[data-pronunciation-slug]');
    if (button) window.EpochLexPronunciation.wire(button, term);
  }

  function renderHome(term, date) {
    const container = document.getElementById('word-of-day-home');
    if (!container || !term) return;
    const entryUrl = new URL(`terms/${encodeURIComponent(term.slug)}/`, siteRoot).href;
    const pageUrl = new URL('word-of-the-day/', siteRoot).href;

    container.innerHTML = `
      <div class="wotd-home-card">
        <div class="wotd-home-main">
          <div class="wotd-kicker-row"><span class="wotd-kicker">Word of the Day</span><time datetime="${date}">${esc(formatDate(date))}</time></div>
          <h2 class="wotd-term">${esc(term.term)}</h2>
          <div class="wotd-pronunciation-row">${pronunciationMarkup(term, 'pronunciation-button')}</div>
          <p class="wotd-definition">${esc(term.definition)}</p>
          <div class="wotd-categories">${categoryMarkup(term)}</div>
        </div>
        <div class="wotd-home-actions">
          <a class="wotd-primary-link" href="${pageUrl}">Explore today's word <span aria-hidden="true">→</span></a>
          <a class="wotd-secondary-link" href="${pageUrl}#previous-words">View previous words <span aria-hidden="true">→</span></a>
          <a class="wotd-text-link" href="${entryUrl}">Open complete entry</a>
        </div>
      </div>`;
    wirePronunciation(container, term);
  }

  function renderPage(term, date, schedule) {
    const container = document.getElementById('word-of-day-page');
    if (!container || !term) return;
    const entryUrl = new URL(`terms/${encodeURIComponent(term.slug)}/`, siteRoot).href;

    container.innerHTML = `
      <article class="wotd-feature-card">
        <p class="wotd-kicker">Word of the Day</p>
        <time class="wotd-date" datetime="${date}">${esc(formatDate(date))}</time>
        <h1 class="wotd-page-term">${esc(term.term)}</h1>
        <div class="wotd-pronunciation-row">${pronunciationMarkup(term, 'pronunciation-button')}</div>
        ${term.partOfSpeech ? `<p class="wotd-pos">${esc(term.partOfSpeech)}</p>` : ''}
        <div class="wotd-categories">${categoryMarkup(term)}</div>
        <p class="wotd-page-definition">${esc(term.definition)}</p>
        ${term.example ? `<section class="wotd-example"><span>In use</span><p><em>${esc(term.example)}</em></p></section>` : ''}
        <div class="wotd-page-actions">
          <a class="wotd-primary-link" href="${entryUrl}">Explore the complete ${esc(term.term)} entry <span aria-hidden="true">→</span></a>
          <button id="wotd-share" class="wotd-share-button" type="button">Share today's word</button>
        </div>
        <p class="wotd-time-note">Word of the Day changes daily at midnight Pacific Time.</p>
      </article>`;

    wirePronunciation(container, term);

    const shareButton = document.getElementById('wotd-share');
    shareButton?.addEventListener('click', async () => {
      const url = new URL('word-of-the-day/', siteRoot).href;
      const shareData = { title: `EpochLex Word of the Day: ${term.term}`, text: `EpochLex Word of the Day: ${term.term}`, url };
      try {
        if (navigator.share) {
          await navigator.share(shareData);
        } else if (navigator.clipboard) {
          await navigator.clipboard.writeText(url);
          shareButton.textContent = 'Link copied';
          setTimeout(() => { shareButton.textContent = "Share today's word"; }, 1800);
        }
      } catch (_) {}
    });

    renderHistory(schedule, date);
  }

  function renderHistory(schedule, today) {
    const container = document.getElementById('word-of-day-history');
    if (!container) return;

    const entries = [...schedule.entries()]
      .filter(([date]) => compareDates(date, today) <= 0)
      .reverse()
      .slice(0, 30);

    if (!entries.length) {
      container.innerHTML = '<p class="wotd-history-empty">Previous words will appear here as the daily history grows.</p>';
      return;
    }

    const rows = entries.map(([date, term]) => {
      const entryUrl = new URL(`terms/${encodeURIComponent(term.slug)}/`, siteRoot).href;
      const category = (term.categories || [])[0] || '';
      return `<li class="wotd-history-row${date === today ? ' is-today' : ''}">
        <time datetime="${date}" class="wotd-history-date">${esc(formatDate(date, { month: 'short', day: 'numeric', year: undefined }))}</time>
        <div class="wotd-history-term"><a href="${entryUrl}">${esc(term.term)}</a>${category ? `<span>${esc(category)}</span>` : ''}</div>
        ${date === today ? '<span class="wotd-today-badge">Today</span>' : ''}
      </li>`;
    }).join('');

    container.innerHTML = `<ol class="wotd-history-list">${rows}</ol>`;
  }

  async function init() {
    const today = getEpochLexDate();
    if (compareDates(today, START_DATE) < 0) return;

    try {
      const response = await fetch(TERMS_URL);
      if (!response.ok) throw new Error('Could not load dictionary data.');
      const terms = await response.json();
      const schedule = buildSchedule(terms, today);
      const term = schedule.get(today);
      if (!term) return;
      renderHome(term, today);
      renderPage(term, today, schedule);
    } catch (error) {
      document.querySelectorAll('[data-wotd-loading]').forEach(node => {
        node.textContent = 'Word of the Day is temporarily unavailable.';
      });
      console.warn('EpochLex Word of the Day failed to load.', error);
    }
  }

  window.EpochLexWordOfTheDay = {
    timeZone: TIME_ZONE,
    startDate: START_DATE,
    version: ALGORITHM_VERSION,
    noRepeatDays: NO_REPEAT_DAYS,
    getEpochLexDate,
    buildSchedule,
    getWordForDate(terms, date) {
      return buildSchedule(terms, date).get(date) || null;
    }
  };

  init();
})();
