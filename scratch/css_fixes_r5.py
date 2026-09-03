import re

with open('style.css', 'r') as f:
    content = f.read()

# Make article-summary white in dark mode
content = re.sub(
    r'(html\[data-theme="dark"\] \.article-summary \{\s*color:\s*)#CBD5E1(;)',
    r'\g<1>#ffffff\2',
    content
)

# Make article-title white in dark mode
content = re.sub(
    r'(html\[data-theme="dark"\] \.article-title \{\s*color:\s*)#E2E8F0(;)',
    r'\g<1>#ffffff\2',
    content
)

# Add rule for recommended articles grid h4
new_rules = """
html[data-theme="dark"] #recommended-articles-grid .article-content h4 {
  color: #ffffff !important;
}
"""
content += new_rules

with open('style.css', 'w') as f:
    f.write(content)
