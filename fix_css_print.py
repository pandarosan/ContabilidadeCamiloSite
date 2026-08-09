import re
with open('style.css', 'r', encoding='utf-8') as f:
    css = f.read()

print_adjustments = """
  /* Ajustes extras para caber tudo em 2 folhas de PDF */
  .calc-container-wrapper {
      padding: 0.5rem !important;
      margin: 0 !important;
  }
  .info-importantes-section {
      padding: 0 !important;
  }
  .info-importantes-section .container {
      padding: 1rem !important;
      box-shadow: none !important;
  }
  ul {
      line-height: 1.4 !important;
      font-size: 0.95rem !important;
  }
  li {
      margin-bottom: 0.5rem !important;
  }
"""

if 'Ajustes extras para caber tudo' not in css:
    css = css.replace('@media print {\n', '@media print {\n' + print_adjustments)

with open('style.css', 'w', encoding='utf-8') as f:
    f.write(css)
