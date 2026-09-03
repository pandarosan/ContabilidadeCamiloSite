import re

with open('style.css', 'r') as f:
    content = f.read()

# Fix 1: Change .article-body color to #ffffff in dark mode
content = re.sub(
    r'(html\[data-theme="dark"\] \.article-body \{\s*color:\s*)#CBD5E1(;)',
    r'\g<1>#ffffff\2',
    content
)

# Fix 2: Append new rules at the very end of the file for the other fixes
new_rules = """
html[data-theme="dark"] .related-articles-section h3 {
  color: #ffffff !important;
}
html[data-theme="dark"] .share-bar > span {
  color: #ffffff !important;
}
html[data-theme="dark"] .article-header-meta,
html[data-theme="dark"] .article-header-meta span,
html[data-theme="dark"] .article-header-meta strong {
  color: #ffffff !important;
}
"""

content += new_rules

with open('style.css', 'w') as f:
    f.write(content)
