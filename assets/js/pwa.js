(() => {
  const currentScript = document.currentScript;
  if (!currentScript?.src) return;

  const siteRoot = new URL('../../', currentScript.src);

  if (!document.querySelector('link[rel="manifest"]')) {
    const manifest = document.createElement('link');
    manifest.rel = 'manifest';
    manifest.href = new URL('manifest.webmanifest', siteRoot).href;
    document.head.append(manifest);
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

  if ('serviceWorker' in navigator) {
    window.addEventListener('load', () => {
      navigator.serviceWorker.register(new URL('service-worker.js', siteRoot), { scope: siteRoot.pathname })
        .catch(error => console.warn('EpochLex service worker registration failed.', error));
    }, { once: true });
  }
})();
