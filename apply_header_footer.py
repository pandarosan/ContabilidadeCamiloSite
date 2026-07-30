import os
import re
import glob

# 1. Obter os blocos de header e footer corretos a partir do noticias-e-artigos.html
with open('noticias-e-artigos.html', 'r', encoding='utf-8') as f:
    ref_html = f.read()

# Extrair a dropdown-menu
match_nav = re.search(r'(<ul class="dropdown-menu">.*?</ul>)', ref_html, re.DOTALL)
if not match_nav:
    print("Erro ao achar nav")
    exit(1)
new_nav = match_nav.group(1)

# Extrair o footer + footer-bottom
# Em noticias-e-artigos.html o footer termina e depois vem footer-bottom
match_footer = re.search(r'(<footer class="footer">.*?</nav>\s*</div>\s*</div>\s*</div><!-- /\.footer-content -->\s*</footer>\s*<div class=\"footer-bottom\">.*?</div>)', ref_html, re.DOTALL)
if not match_footer:
    match_footer = re.search(r'(<footer class="footer">.*?</svg>\n          </a>\n        </div><!-- /\.social-links -->\n      </div><!-- /\.footer-col -->\n    </div><!-- /\.footer-content -->\n  </footer>\n  <div class="footer-bottom\">\n.*?</div>)', ref_html, re.DOTALL)

if not match_footer:
    print("Erro ao achar footer")
    exit(1)
new_footer = match_footer.group(1)

# Loop por todos os HTMLs
for filepath in glob.glob('*.html'):
    with open(filepath, 'r', encoding='utf-8') as f:
        html = f.read()

    # Substituir nav
    html = re.sub(r'<ul class="dropdown-menu">.*?</ul>', new_nav, html, flags=re.DOTALL)
    
    # Substituir footer
    # O footer nos outros arquivos pode estar estruturado de formas diferentes, mas todos começam com <footer class="footer"> e terminam com a div footer-bottom </div>
    html = re.sub(r'<footer class="footer">.*?</nav>\s*</div>\s*</div>\s*</div><!-- /\.footer-content -->\s*</footer>\s*<div class=\"footer-bottom\">.*?</div>', new_footer, html, flags=re.DOTALL)
    html = re.sub(r'<footer class="footer">.*?</svg>\n          </a>\n        .*?</div><!-- /\.social-links -->\n      </div><!-- /\.footer-contact -->\n    </div><!-- /\.footer-content -->\n  </footer>\n  <div class="footer-bottom\">\n.*?</div>', new_footer, html, flags=re.DOTALL)
    html = re.sub(r'<footer class="footer">.*?</footer>\n  <div class="footer-bottom">.*?</div>', new_footer, html, flags=re.DOTALL)
    
    # Exceção para o artigo-modelo.html que pode ter footer-bottom dentro do footer
    html = re.sub(r'<footer class="footer">.*?<div class="footer-bottom">.*?</div>\n  </footer>', new_footer, html, flags=re.DOTALL)

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(html)
    print(f"Atualizado {filepath}")

