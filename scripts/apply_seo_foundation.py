import json
import html
import pathlib
import re
from datetime import date

ROOT = pathlib.Path('.')
BASE = 'https://jeffthomasiii.github.io/dictionary-of-the-ai-era/'
TODAY = '2026-08-28'

terms = json.loads((ROOT / 'data/terms.json').read_text())
assert len(terms) == 100


def meta_block(title, description, url, og_type='website', structured=None):
    parts = [
        f'<link rel="canonical" href="{html.escape(url, quote=True)}">',
        '<meta property="og:site_name" content="AILex">',
        f'<meta property="og:title" content="{html.escape(title, quote=True)}">',
        f'<meta property="og:description" content="{html.escape(description, quote=True)}">',
        f'<meta property="og:type" content="{og_type}">',
        f'<meta property="og:url" content="{html.escape(url, quote=True)}">',
        '<meta name="twitter:card" content="summary">',
        f'<meta name="twitter:title" content="{html.escape(title, quote=True)}">',
        f'<meta name="twitter:description" content="{html.escape(description, quote=True)}">',
    ]
    if structured is not None:
        parts.append('<script type="application/ld+json">' + json.dumps(structured, ensure_ascii=False, separators=(',', ':')).replace('</', '<\\/') + '</script>')
    return '\n  '.join(parts)


def inject_after_description(path, block):
    text = path.read_text()
    assert 'rel="canonical"' not in text, path
    match = re.search(r'(<meta\s+name="description"\s+content="[^"]*"\s*/?>)', text, re.I)
    assert match, path
    text = text[:match.end()] + '\n  ' + block + text[match.end():]
    path.write_text(text)

# Home
home_title = 'AILex · Dictionary of the AI Era'
home_desc = 'AILex is a living Dictionary of the AI Era, cataloging the terms, concepts, slang, and language emerging around artificial intelligence.'
home_structured = {
    '@context': 'https://schema.org',
    '@type': 'DefinedTermSet',
    'name': 'AILex',
    'alternateName': 'Dictionary of the AI Era',
    'description': home_desc,
    'url': BASE,
    'inLanguage': 'en'
}
inject_after_description(ROOT/'index.html', meta_block(home_title, home_desc, BASE, 'website', home_structured))

# Top-level informational pages
pages = {
    'categories.html': ('Categories · AILex', 'Explore the four editorial categories used by AILex, the Dictionary of the AI Era.'),
    'about.html': ('About · AILex', 'Learn what AILex is, why the Dictionary of the AI Era exists, and how this living reference approaches fast-changing AI language.'),
    'contribute.html': ('Contribute · AILex', 'Learn how to suggest terms, corrections, sources, and editorial improvements for AILex, the Dictionary of the AI Era.'),
    'methodology.html': ('Methodology · AILex', 'See how AILex researches, classifies, sources, reviews, and maintains terminology for the Dictionary of the AI Era.'),
}
for filename, (title, description) in pages.items():
    path = ROOT/filename
    text = path.read_text()
    # Preserve existing description if one exists; otherwise use readiness copy.
    desc_match = re.search(r'<meta\s+name="description"\s+content="([^"]*)"', text, re.I)
    if desc_match:
        description = html.unescape(desc_match.group(1))
    url = BASE + filename
    inject_after_description(path, meta_block(title, description, url, 'website'))

# Term pages
for term in terms:
    slug = term['slug']
    path = ROOT/'terms'/slug/'index.html'
    assert path.exists(), slug
    title = f"{term['term']} | AILex"
    description = term['definition']
    url = BASE + f'terms/{slug}/'
    structured = {
        '@context': 'https://schema.org',
        '@type': 'DefinedTerm',
        'name': term['term'],
        'description': description,
        'url': url,
        'inDefinedTermSet': BASE,
        'inLanguage': 'en'
    }
    aliases = term.get('aliases') or []
    if aliases:
        structured['alternateName'] = aliases
    inject_after_description(path, meta_block(title, description, url, 'article', structured))

# 404 should never be indexed.
not_found = ROOT/'404.html'
text = not_found.read_text()
if 'name="robots"' not in text:
    head_match = re.search(r'(<meta\s+name="viewport"[^>]*>)', text, re.I)
    assert head_match
    text = text[:head_match.end()] + '\n  <meta name="robots" content="noindex, nofollow">' + text[head_match.end():]
    not_found.write_text(text)

# robots.txt
(ROOT/'robots.txt').write_text(
    'User-agent: *\n'
    'Allow: /\n\n'
    f'Sitemap: {BASE}sitemap.xml\n'
)

# sitemap.xml
urls = [
    (BASE, TODAY),
    (BASE+'categories.html', TODAY),
    (BASE+'about.html', TODAY),
    (BASE+'contribute.html', TODAY),
    (BASE+'methodology.html', TODAY),
]
for term in terms:
    lastmod = term.get('lastReviewed') or term.get('added') or TODAY
    urls.append((BASE + f"terms/{term['slug']}/", lastmod))
assert len(urls) == 105
xml = ['<?xml version="1.0" encoding="UTF-8"?>', '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">']
for loc, lastmod in urls:
    xml.extend(['  <url>', f'    <loc>{html.escape(loc)}</loc>', f'    <lastmod>{lastmod}</lastmod>', '  </url>'])
xml.append('</urlset>')
(ROOT/'sitemap.xml').write_text('\n'.join(xml) + '\n')

# Validation after mutation
indexable = [ROOT/'index.html', ROOT/'categories.html', ROOT/'about.html', ROOT/'contribute.html', ROOT/'methodology.html'] + [ROOT/'terms'/t['slug']/'index.html' for t in terms]
assert len(indexable) == 105
for path in indexable:
    text = path.read_text()
    for required in ('rel="canonical"', 'property="og:title"', 'property="og:description"', 'property="og:url"', 'name="twitter:card"'):
        assert required in text, (path, required)
for term in terms:
    text = (ROOT/'terms'/term['slug']/'index.html').read_text()
    assert '"@type":"DefinedTerm"' in text, term['slug']
assert '"@type":"DefinedTermSet"' in (ROOT/'index.html').read_text()
assert '<meta name="robots" content="noindex, nofollow">' in (ROOT/'404.html').read_text()
assert (ROOT/'robots.txt').exists() and (ROOT/'sitemap.xml').exists()
assert (ROOT/'sitemap.xml').read_text().count('<url>') == 105
print('SEO foundation validated: 105 canonical indexable pages, 100 DefinedTerm pages, sitemap and robots ready.')
