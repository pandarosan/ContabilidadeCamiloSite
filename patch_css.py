import re
with open('style.css', 'r', encoding='utf-8') as f:
    css = f.read()

print_rules = """
  /* Regras para não quebrar layout de tela, mas formatar tabela na impressao */
  .hide-print { display: none !important; }
  .show-print { display: inline !important; }
  
  .rbt12-group {
      display: flex !important;
      flex-direction: row !important;
      justify-content: center !important;
      align-items: center !important;
      max-width: 100% !important;
      gap: 15px;
  }
  .rbt12-group label, .rbt12-group input {
      width: auto !important;
      margin: 0 !important;
      text-align: left !important;
  }
"""

if '.hide-print' not in css:
    css = css.replace('@media print {\n', '@media print {\n' + print_rules)

if '@media screen' not in css:
    css += '\n@media screen {\n  .show-print { display: none !important; }\n}\n'

with open('style.css', 'w', encoding='utf-8') as f:
    f.write(css)
