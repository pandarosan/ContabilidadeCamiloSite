import os
import glob
import re

replacements = {
    r"Abertura\s+de\s+empresas\s+e\s+societário": "Abertura de Empresas e Societário",
    r"Departamento\s+de\s+pessoal": "Departamento de Pessoal",
    r"Certificado\s+digital": "Certificado Digital",
    r"Demais\s+soluções": "Demais Soluções",
    r"Fiscal\s+e\s+contabilidade": "Fiscal e Contabilidade"
}

for filepath in glob.glob('*.html'):
    with open(filepath, 'r', encoding='utf-8') as f:
        html = f.read()

    changed = False
    for old, new in replacements.items():
        new_html = re.sub(old, new, html)
        if new_html != html:
            html = new_html
            changed = True

    if changed:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(html)
        print(f"Atualizado com REGEX {filepath}")

