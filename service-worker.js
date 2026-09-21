const CACHE_VERSION = 'epochlex-pwa-20260921-report-figures-4';
const CORE_CACHE = `${CACHE_VERSION}-core`;
const RUNTIME_CACHE = `${CACHE_VERSION}-runtime`;

const CORE_ASSETS = [
  './',
  './index.html',
  './offline.html',
  './manifest.webmanifest',
  './favicon.png',
  './categories.html',
  './about.html',
  './contribute.html',
  './methodology.html',
  './word-of-the-day/',
  './experiment/',
  './experiment/report/',
  './assets/brand/epochlex/epochlex-logo-stacked-pronunciation-light.png',
  './assets/css/styles.css',
  './assets/css/term-pages.css',
  './assets/css/brand-theme.css',
  './assets/css/accessibility.css',
  './assets/css/taxonomy.css',
  './assets/css/mobile-nav.css',
  './assets/css/mobile-browse.css',
  './assets/css/pwa.css',
  './assets/css/pwa-compact.css',
  './assets/css/pwa-polish.css',
  './assets/css/word-of-the-day.css',
  './assets/css/experiment.css',
  './assets/js/app.js',
  './assets/js/mobile-nav.js',
  './assets/js/mobile-browse.js',
  './assets/js/pwa.js',
  './assets/js/pwa-compact.js',
  './assets/js/word-of-the-day.js',
  './assets/js/experiment.js',
  './data/terms.json'
];

self.addEventListener('install', event => {
  event.waitUntil(
    caches.open(CORE_CACHE)
      .then(cache => cache.addAll(CORE_ASSETS))
      .then(() => self.skipWaiting())
  );
});

self.addEventListener('activate', event => {
  event.waitUntil(
    caches.keys()
      .then(keys => Promise.all(keys
        .filter(key => key.startsWith('epochlex-pwa-') && ![CORE_CACHE, RUNTIME_CACHE].includes(key))
        .map(key => caches.delete(key))))
      .then(() => self.clients.claim())
  );
});

async function networkFirst(request) {
  const runtimeCache = await caches.open(RUNTIME_CACHE);
  try {
    const response = await fetch(request);
    if (response && response.ok) runtimeCache.put(request, response.clone());
    return response;
  } catch (error) {
    const runtimeCached = await runtimeCache.match(request);
    if (runtimeCached) return runtimeCached;
    const coreCache = await caches.open(CORE_CACHE);
    const coreCached = await coreCache.match(request);
    if (coreCached) return coreCached;
    if (request.mode === 'navigate') return coreCache.match('./offline.html');
    throw error;
  }
}

async function staleWhileRevalidate(request) {
  const runtimeCache = await caches.open(RUNTIME_CACHE);
  const coreCache = await caches.open(CORE_CACHE);
  const cached = await runtimeCache.match(request) || await coreCache.match(request);
  const network = fetch(request).then(response => {
    if (response && response.ok) runtimeCache.put(request, response.clone());
    return response;
  }).catch(() => null);
  return cached || network;
}

self.addEventListener('fetch', event => {
  const { request } = event;
  if (request.method !== 'GET') return;

  const url = new URL(request.url);
  if (url.origin !== self.location.origin) return;

  if (request.mode === 'navigate' || url.pathname.endsWith('/data/terms.json') || url.pathname.endsWith('/data/provenance.json')) {
    event.respondWith(networkFirst(request));
    return;
  }

  if (request.destination === 'script') {
    event.respondWith(networkFirst(request));
    return;
  }

  if (['style', 'image', 'font'].includes(request.destination)) {
    event.respondWith(staleWhileRevalidate(request));
  }
});
