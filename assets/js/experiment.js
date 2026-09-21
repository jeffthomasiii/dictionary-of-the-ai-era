(() => {
  const nav = document.querySelector('.experiment-mobile-nav');
  if (!nav) return;

  const links = [...nav.querySelectorAll('a[data-experiment-section]')];
  const sections = links
    .map(link => document.getElementById(link.dataset.experimentSection))
    .filter(Boolean);

  const setActive = id => {
    links.forEach(link => {
      if (link.dataset.experimentSection === id) link.setAttribute('aria-current', 'page');
      else link.removeAttribute('aria-current');
    });
  };

  links.forEach(link => {
    link.addEventListener('click', () => setActive(link.dataset.experimentSection));
  });

  if (!('IntersectionObserver' in window)) return;

  const observer = new IntersectionObserver(entries => {
    const visible = entries
      .filter(entry => entry.isIntersecting)
      .sort((a,b) => b.intersectionRatio - a.intersectionRatio)[0];
    if (visible?.target?.id) setActive(visible.target.id);
  }, {
    rootMargin: '-20% 0px -55% 0px',
    threshold: [0.08, 0.25, 0.5]
  });

  sections.forEach(section => observer.observe(section));
})();
