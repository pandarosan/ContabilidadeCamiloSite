import os
import glob
import re

replacements = {
    r"abertura-de-empresas\.html": "abertura-de-empresas-e-societario.html",
    r"servicos-contabeis\.html": "fiscal-e-contabilidade.html",
    r"departamento-pessoal\.html": "departamento-de-pessoal.html",
    r"planejamento-estrategico\.html": "bpo-financeiro.html",
    r"troca-de-contador\.html": "demais-solucoes.html"
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
        print(f"Links atualizados em {filepath}")

