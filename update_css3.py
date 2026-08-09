import re

with open('style.css', 'r', encoding='utf-8') as f:
    css = f.read()

# 1. Print page break
print_css = """
    .info-importantes { page-break-before: always; margin-top: 0 !important; }
"""
css = css.replace('@media print {\n', '@media print {\n' + print_css)

# 2. Mobile positioning for Toast
mobile_css = """
  .toast-container {
      position: static !important;
      margin-top: 1.5rem;
  }
"""
css = css.replace('@media (max-width: 768px) {\n', '@media (max-width: 768px) {\n' + mobile_css)

with open('style.css', 'w', encoding='utf-8') as f:
    f.write(css)

print("CSS updated.")
