import re

with open("manual-pandarosan.html", "r", encoding="utf-8") as f:
    content = f.read()

# Point 3: Alignment of Header and separate blue line
# Let's fix the CSS
content = re.sub(
    r'\.cover-details\s*\{[^}]*\}',
    ".cover-details {\n            margin-top: auto;\n            width: 100%;\n            padding-bottom: 30px;\n        }",
    content
)
content = re.sub(
    r'\.cover-details\s*p\s*\{[^}]*\}',
    ".cover-details p {\n            font-size: 1.1rem;\n            color: var(--text-light);\n            text-align: left;\n            margin: 5px 0;\n        }",
    content
)

# Replace the text of the header to include the arrows? 
# "→ Engenharia e Arquitetura..." The user put arrows in the prompt. I will not put arrows unless they are in the HTML, they probably just used arrows to point to the lines. Wait, no, they said "→ Engenharia e Arquitetura...". I'll stick to the original `<p>` tags without arrows but left-aligned.

# Point 4: Names of Pilares
content = content.replace("Pilar 1: A Revolução Arquitetural (Engenharia, Valor e Segurança)", "Pilar 1: A Revolução Arquitetural (Engenharia, Valor e Segurança)")
# Actually, let's use regex to replace the exact strings in TOC and H2
titles = {
    r'Pilar 1: .*': "Pilar 1: A Revolução Arquitetural (Engenharia, Valor e Segurança)",
    r'Pilar 2: .*': "Pilar 2: Navegação Comercial e Engenharia de Conversão",
    r'Pilar 3: .*': "Pilar 3: Arsenal de Autoridade Interativa (Calculadoras Inteligentes e Impressão)",
    r'Pilar 4: .*': "Pilar 4: Máquina de Conteúdo, Autonomia e Decap CMS",
    r'Pilar 5: .*': "Pilar 5: Soberania de Infraestrutura, Governança, Eficiência Operacional &amp; SEO Estratégico",
    r'Anexo: .*': "Anexo: Relação das Páginas do Portal"
}

# The easiest way to fix Pilar 1 text (Point 5):
pilar1_2_html = """<h3>2. A Tríade Tecnológica Serverless (Custo Zero de Hospedagem)</h3>
    <p>Utilizamos a infraestrutura mais robusta e moderna do mundo para eliminar custos recorrentes com hospedagem web:</p>
    <ul>
        <li><strong>GitHub (Versionamento e Custódia):</strong> Todo o histórico de código-fonte, artigos e alterações é arquivado em uma nuvem criptografada. Funciona como uma "caixa preta" inviolável com controle de versão imutável. Se algo der errado, garantimos o <em>Rollback</em> (restauração) instantâneo.</li>
        <li><strong>Cloudflare Pages (Borda Global e CDN):</strong> O site não fica em um único servidor. Ele é replicado em mais de 300 data centers globais da Cloudflare, entregando conteúdo com latência zero e certificados SSL corporativos automáticos.</li>
        <li><strong>Decap CMS (Gerenciador Desacoplado):</strong> Painel visual amigável que atua como interface para a equipe publicar conteúdos, eliminando totalmente a dependência de servidores web PHP/MySQL pagos dedicados 24/7.</li>
    </ul>

    <h3>Blindagem Ativa contra Ameaças Digitais</h3>
    <p>A segurança deste portal é absoluta por design. Como não há banco de dados aberto na web, mitigamos qualquer invasão estrutural. O projeto conta com imunidade a plugins desatualizados e proteção perimetral contra ataques DDoS.</p>"""

# Find where "2. A Tríade" starts and "<!-- PILAR 2 -->" starts, and replace it
content = re.sub(r'<h3>2\. A Tríade Tecnológica Serverless.*?<div class="page-break"></div>\s*<!-- PILAR 2 -->',
                 pilar1_2_html + '\n\n    <div class="page-break"></div>\n\n    <!-- PILAR 2 -->',
                 content, flags=re.DOTALL)


# Point 6: Pilar 2: 1. Mapa Estrutural
pilar2_1_html = """<h3>1. Mapa Estrutural do Portal e Integração de Portais</h3>
    <ul>
        <li><strong>Home (/):</strong> Vitrine comercial de impacto. Realiza o cálculo automático de experiência do escritório, apresenta as soluções primárias de forma arrojada e possui captura estratégica.</li>
        <li><strong>Soluções Verticais:</strong> Páginas dedicadas e focadas nas especialidades do escritório (Área Fiscal, Departamento Pessoal, BPO Financeiro, etc.).</li>
        <li><strong>Acesso aos Portais Corporativos:</strong> Atendendo a uma solicitação explícita e vital do cliente, o menu principal abriga o acesso direto ao <strong>[Portal do Cliente]</strong> e <strong>[Portal do Empregado]</strong>. Essa integração facilita enormemente a rotina diária de quem já é cliente da contabilidade, tudo isso sem poluir a navegação voltada à prospecção comercial.</li>
    </ul>"""
content = re.sub(r'<h3>1\. Mapa Estrutural do Portal.*?</ul>', pilar2_1_html, content, flags=re.DOTALL, count=1)


# Point 7: Pilar 2 - 4. Bônus
bonus_html = """<h3>4. Funcionalidades Bônus de Engenharia (PandaRoSan)</h3>
    <div class="highlight-box">
        <p>Visando entregar um portal com excelência sem precedentes, e embora não estivesse previsto no escopo e orçamento iniciais, a PandaRoSan entregou como diferencial adiciona um sofisticado sistema de <strong>Modo Escuro (Dark Mode)</strong> e <strong>Botão Flutuante de Retorno ao Topo:</strong></p>"""
content = re.sub(r'<h3>4\. Funcionalidades Bônus de Engenharia \(PandaRoSan\)</h3>\s*<div class="highlight-box">\s*<p>.*?</p>',
                 bonus_html, content, flags=re.DOTALL)


# Point 9: Table
correct_table_html = """<table>
        <thead>
            <tr>
                <th>Arquivo Físico (Excel)</th>
                <th>Abas Internas Utilizadas</th>
                <th>Calculadora Afetada</th>
                <th>Campos / Parâmetros Atualizáveis</th>
            </tr>
        </thead>
        <tbody>
            <tr>
                <td><code>calculadora-ir-configuracoes.xlsx</code></td>
                <td><code>tabelas_referencia</code><br><code>parametros_gerais</code></td>
                <td>Calculadora de IRPF</td>
                <td>Faixa, Limite, Aliquota, Deducao.<br>Parametro, Valor.</td>
            </tr>
            <tr>
                <td><code>calculadora-simples-nacional-configuracoes.xlsx</code></td>
                <td><code>Tabelas_Referencia</code><br><code>Configuracoes</code></td>
                <td>Simples Nacional</td>
                <td>Anexo, Faixa, Limite, AliqNom, Ded.<br>Parametro, Valor.</td>
            </tr>
            <tr>
                <td><code>calculadora-inss-configuracoes.xlsx</code></td>
                <td><code>Tabelas_Referencia</code><br><code>Outras_Categorias</code><br><code>Parametros_Gerais</code></td>
                <td>INSS &amp; Salário Líquido</td>
                <td>Faixa, Limite_Ate, Aliquota, Parcela_Deduzir.<br>Categoria, Aliquota, Base_Calculo.<br>Parametro, Valor.</td>
            </tr>
            <tr>
                <td><strong>Qualquer Arquivo</strong></td>
                <td>(Abas de <strong>Parâmetros</strong>)</td>
                <td><strong>Todas</strong></td>
                <td>O campo <code>Ano_Base</code> dita o ano vigente nas regras de exibição do site (Ex: 2026).</td>
            </tr>
        </tbody>
    </table>"""
content = re.sub(r'<table>.*?</table>', correct_table_html, content, flags=re.DOTALL, count=1)


# Point 12: Footer alignment
footer_html = """<div class="footer-assinatura">
        <p><strong>PandaRoSan IT Solutions © 2026</strong><br>
        Engenharia de Software de Elite, Automações e Presença Digital de Alta Performance.</p>
    </div>"""
content = re.sub(r'<div class="footer-assinatura">.*?</div>', footer_html, content, flags=re.DOTALL)

with open("manual-pandarosan.html", "w", encoding="utf-8") as f:
    f.write(content)

