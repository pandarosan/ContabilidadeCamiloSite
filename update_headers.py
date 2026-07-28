import os
import re

header_html = """    <header class="header">
      <div class="container header-content">
        <a href="index.html" class="logo">
          <span class="logo-text">Contabilidade <strong>Camilo</strong></span>
        </a>
        <nav class="nav">
          <ul class="nav-list">
            <li><a href="index.html" class="nav-link">Home</a></li>
            <li class="dropdown">
              <a href="index.html#solucoes" class="nav-link">Soluções <span class="caret">▾</span></a>
              <ul class="dropdown-menu">
                <li><a href="abertura-de-empresas.html">Abertura e Legalização</a></li>
                <li><a href="servicos-contabeis.html">Serviços Contábeis</a></li>
                <li><a href="departamento-pessoal.html">Departamento Pessoal</a></li>
                <li><a href="planejamento-estrategico.html">Planejamento Estratégico</a></li>
              </ul>
            </li>
            <li><a href="sobre-nos.html" class="nav-link">Sobre Nós</a></li>
            <li><a href="contato.html" class="nav-link">Contato</a></li>
          </ul>
        </nav>
        <a href="#whatsapp" class="btn-primary">Fale com um Especialista</a>
      </div>
    </header>"""

for root, _, files in os.walk('.'):
    for file in files:
        if file.endswith('.html'):
            filepath = os.path.join(root, file)
            with open(filepath, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # Replace Header
            content = re.sub(
                r'<header class="header">.*?</header>',
                header_html,
                content,
                flags=re.DOTALL
            )
            
            # Replace Year
            content = re.sub(
                r'&copy; \d{4} Contabilidade Camilo\. Todos os direitos reservados\.',
                '&copy; <span id="current-year"></span> Contabilidade Camilo. Todos os direitos reservados.',
                content
            )
            
            # Replace href="/" with href="index.html" just in case there are other links
            # content = content.replace('href="/"', 'href="index.html"')
            
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(content)

print("Updated headers and footer year in all HTML files.")
