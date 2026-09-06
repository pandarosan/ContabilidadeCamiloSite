import datetime

html_content = """<!DOCTYPE html>
<html lang="pt-BR">
<head>
    <meta charset="UTF-8">
    <title>Manual Definitivo - Contabilidade Camilo</title>
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;600;700&display=swap');
        
        :root {
            --primary: #1E3A8A; /* Azul escuro corporativo */
            --secondary: #3B82F6; /* Azul claro */
            --accent: #F59E0B; /* Destaque laranja/amarelo */
            --text-main: #1F2937;
            --text-light: #4B5563;
            --bg-body: #F9FAFB;
            --bg-card: #FFFFFF;
            --border: #E5E7EB;
        }

        body {
            font-family: 'Inter', sans-serif;
            background-color: var(--bg-body);
            color: var(--text-main);
            margin: 0;
            padding: 0;
            line-height: 1.7;
        }

        .container {
            max-width: 900px;
            margin: 0 auto;
            background-color: var(--bg-card);
            box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1);
            padding: 60px 80px;
        }

        /* CAPA */
        .cover-page {
            display: flex;
            flex-direction: column;
            justify-content: center;
            align-items: center;
            height: 80vh;
            text-align: center;
            border-bottom: 5px solid var(--primary);
            margin-bottom: 50px;
        }

        .cover-page h1 {
            font-size: 3rem;
            color: var(--primary);
            margin-bottom: 10px;
            line-height: 1.2;
        }

        .cover-page h2 {
            font-size: 1.5rem;
            color: var(--text-light);
            font-weight: 300;
            margin-bottom: 40px;
        }

        .cover-details {
            margin-top: auto;
            font-size: 1.1rem;
            color: var(--text-light);
            text-align: right;
            width: 100%;
        }
        
        .cover-details strong {
            color: var(--primary);
        }

        /* ÍNDICE */
        .toc {
            background-color: #F3F4F6;
            padding: 30px;
            border-radius: 8px;
            margin-bottom: 50px;
        }

        .toc h3 {
            margin-top: 0;
            color: var(--primary);
            border-bottom: 2px solid var(--secondary);
            padding-bottom: 10px;
        }

        .toc ul {
            list-style: none;
            padding: 0;
        }

        .toc ul li {
            margin-bottom: 10px;
        }

        .toc ul li a {
            text-decoration: none;
            color: var(--text-main);
            font-weight: 600;
        }
        
        .toc ul li a:hover {
            color: var(--secondary);
        }

        /* CONTEÚDO */
        h1, h2, h3, h4 {
            color: var(--primary);
            margin-top: 2rem;
        }

        h2 {
            border-bottom: 2px solid var(--border);
            padding-bottom: 10px;
            font-size: 1.8rem;
        }

        h3 {
            font-size: 1.4rem;
            color: var(--secondary);
        }

        p {
            margin-bottom: 1.2rem;
            color: var(--text-main);
        }

        ul, ol {
            margin-bottom: 1.5rem;
            padding-left: 20px;
        }

        li {
            margin-bottom: 0.5rem;
        }

        .highlight-box {
            background-color: #EFF6FF;
            border-left: 4px solid var(--secondary);
            padding: 15px 20px;
            margin: 20px 0;
            border-radius: 0 8px 8px 0;
        }

        table {
            width: 100%;
            border-collapse: collapse;
            margin: 30px 0;
            font-size: 0.95rem;
        }

        th, td {
            border: 1px solid var(--border);
            padding: 12px 15px;
            text-align: left;
        }

        th {
            background-color: var(--primary);
            color: white;
            font-weight: 600;
        }

        tr:nth-child(even) {
            background-color: #F9FAFB;
        }

        /* IMPRESSÃO (A4) */
        @media print {
            body {
                background-color: white;
            }
            .container {
                box-shadow: none;
                padding: 0;
                max-width: 100%;
            }
            .page-break {
                page-break-before: always;
            }
            .toc {
                background-color: transparent;
                border: 1px solid var(--border);
            }
        }
    </style>
</head>
<body>

<div class="container">

    <!-- CAPA -->
    <div class="cover-page">
        <h1>LIVRO DE OURO</h1>
        <h2>Manual Definitivo de Operação, Governança e Estratégia Digital</h2>
        
        <div style="margin: 50px 0;">
            <p style="font-size: 1.2rem; color: #4B5563;">Projeto: <strong>Ecossistema Corporativo Contabilidade Camilo</strong></p>
        </div>

        <div class="cover-details">
            <p>Engenharia e Arquitetura: <strong>PandaRoSan IT Solutions</strong></p>
            <p>Responsável Técnica: <strong>Rosangela Corrêa — Arquiteta de Software</strong></p>
            <p>Versão: <strong>1.0 (Edição Definitiva de Entrega)</strong></p>
            <p>Data: <strong>""" + datetime.datetime.now().strftime("%B / %Y") + """</strong></p>
        </div>
    </div>

    <div class="page-break"></div>

    <!-- APRESENTAÇÃO EXECUTIVA -->
    <h2>Apresentação Executiva</h2>
    <p>Este documento consolida a entrega da reengenharia digital da <strong>Contabilidade Camilo</strong>. O projeto substitui modelos tradicionais obsoletos por uma infraestrutura <strong>Jamstack de alto padrão</strong>, orientada à soberania do cliente, conversão comercial, blindagem cibernética e custo operacional de hospedagem zero.</p>
    <p>Além do escopo contratado, a <strong>PandaRoSan IT Solutions</strong> fez questão de entregar excelência através de funcionalidades de ponta implementadas como <strong>Bônus de Engenharia</strong>, agregando um valor inestimável à plataforma final.</p>

    <!-- ÍNDICE -->
    <div class="toc">
        <h3>Índice</h3>
        <ul>
            <li><a href="#pilar1">Pilar 1: A Revolução Arquitetural (Engenharia, Valor e Segurança)</a></li>
            <li><a href="#pilar2">Pilar 2: Navegação Comercial e Engenharia de Conversão</a></li>
            <li><a href="#pilar3">Pilar 3: Arsenal de Autoridade Interativa (Calculadoras em A4)</a></li>
            <li><a href="#pilar4">Pilar 4: Máquina de Conteúdo, Autonomia e Decap CMS</a></li>
            <li><a href="#pilar5">Pilar 5: Soberania Digital, Governança e Eficiência Operacional</a></li>
            <li><a href="#anexo">Anexo: Relação das Páginas do Portal</a></li>
        </ul>
    </div>

    <div class="page-break"></div>

    <!-- PILAR 1 -->
    <h2 id="pilar1">Pilar 1: A Revolução Arquitetural (Engenharia, Valor e Segurança)</h2>
    
    <h3>1. O Modelo Jamstack vs. Plataformas Legadas</h3>
    <ul>
        <li><strong>O modelo tradicional (WordPress/PHP):</strong> Depende de requisições a bancos de dados MySQL e processamento dinâmico em servidor a cada acesso. Isso gera lentidão crônica, vulnerabilidades a invasões (como <em>SQL Injection</em> e ataques de força bruta) e a necessidade constante de manutenções e atualizações corretivas pagas.</li>
        <li><strong>A arquitetura Jamstack adotada:</strong> As páginas nascem pré-compiladas em arquivos estáticos ultraleves (HTML5 semântico, CSS3 e JavaScript otimizado). Ao contrário de sites tradicionais, nossas páginas carregam em milissegundos. O navegador do visitante consome o conteúdo de forma instantânea, garantindo nota máxima em métricas de <em>Core Web Vitals</em> e Google PageSpeed.</li>
    </ul>

    <h3>2. A Tríade Tecnológica Serverless (Custo Zero de Hospedagem)</h3>
    <p>Utilizamos a infraestrutura mais robusta e moderna do mundo para eliminar custos recorrentes com hospedagem web:</p>
    <ul>
        <li><strong>GitHub (Versionamento e Custódia):</strong> Todo o histórico de código-fonte, artigos e alterações é arquivado em uma nuvem criptografada. Funciona como uma "caixa preta" inviolável com controle de versão imutável. Se algo der errado, garantimos o <em>Rollback</em> (restauração) instantâneo.</li>
        <li><strong>Cloudflare Pages (Borda Global e CDN):</strong> O site não fica em um único servidor. Ele é replicado em mais de 300 data centers globais da Cloudflare, entregando conteúdo com latência zero e certificados SSL corporativos automáticos.</li>
        <li><strong>Decap CMS (Gerenciador Desacoplado):</strong> Painel visual amigável que atua como interface para a equipe publicar conteúdos, eliminando totalmente a dependência de servidores web PHP/MySQL pagos dedicados 24/7.</li>
    </ul>

    <h3>3. Blindagem Ativa contra Ameaças Digitais</h3>
    <div class="highlight-box">
        <p>A segurança deste portal é absoluta por design. Como o projeto <strong>não possui banco de dados aberto na web</strong>, não há porta de entrada para que hackers roubem ou sequestrem informações da Contabilidade Camilo.</p>
    </div>
    <ul>
        <li>Ausência total de portas de banco de dados expostas na web.</li>
        <li>Imunidade arquitetural a invasões via plugins desatualizados (o "calcanhar de Aquiles" do WordPress).</li>
        <li>Mitigação perimetral contra ataques distribuídos de negação de serviço (DDoS) provida pela rede global da Cloudflare.</li>
    </ul>

    <div class="page-break"></div>

    <!-- PILAR 2 -->
    <h2 id="pilar2">Pilar 2: Navegação Comercial e Engenharia de Conversão</h2>

    <h3>1. Mapa Estrutural do Portal e Integração de Portais</h3>
    <ul>
        <li><strong>Home (/):</strong> Vitrine comercial de impacto. Realiza o cálculo automático de experiência do escritório, apresenta as soluções primárias de forma arrojada e possui captura estratégica.</li>
        <li><strong>Soluções Verticais:</strong> Páginas dedicadas e focadas nas especialidades do escritório (Área Fiscal, Departamento Pessoal, BPO Financeiro, etc.).</li>
        <li><strong>Acesso aos Portais Corporativos:</strong> Atendendo a uma solicitação explícita e vital do cliente, o menu principal abriga o acesso direto ao <strong>[Portal do Cliente]</strong> e <strong>[Portal do Empregado]</strong>. Essa integração facilita enormemente a rotina diária de quem já é cliente da contabilidade, tudo isso sem poluir a navegação voltada à prospecção comercial.</li>
    </ul>

    <h3>2. Mecânica do WhatsApp Dinâmico (Captura Inteligente)</h3>
    <p>A captação de leads neste projeto não utiliza botões genéricos. Criamos uma engenharia de conversão que qualifica o lead no momento do clique:</p>
    <ul>
        <li><strong>Nos Artigos (URL dinâmica):</strong> O script lê em tempo real a tag <code>&lt;h1&gt;</code> (Título da publicação) lida pelo usuário e constrói um gatilho de atendimento com URL codificada. O escritório recebe a mensagem: <em>"Olá! Li o artigo <strong>'[Título Exato do Artigo]'</strong> no site de vocês e gostaria de orientação técnica especializada sobre este tema."</em></li>
        <li><strong>Modais Flutuantes Inteligentes:</strong> No topo da tela principal, destacam-se os botões de ação primária <strong>[PARA VOCÊ]</strong>, <strong>[ABRA SUA EMPRESA]</strong> e <strong>[TROQUE DE CONTADOR]</strong>. Eles abrem modais interativos elegantes onde o usuário seleciona exatamente sua "dor" ou interesse, disparando mensagens pré-configuradas cirúrgicas pelo WhatsApp, acelerando o fechamento comercial.</li>
    </ul>

    <h3>3. Funcionalidade Bônus: Dark Mode Dinâmico</h3>
    <div class="highlight-box">
        <p><strong>Inovação de UX (Bônus PandaRoSan):</strong> Embora não estivesse previsto no escopo e orçamento iniciais, a PandaRoSan entregou como diferencial um sofisticado sistema de <strong>Modo Escuro (Dark Mode)</strong>. Controlado pelo elegante botão Sol/Lua no menu, ele reduz o cansaço visual da leitura noturna, economiza bateria em celulares e consolida a percepção de uma marca vanguardista e tecnológica.</p>
    </div>

    <h3>4. Integração de Redes Sociais e Compartilhamento</h3>
    <p>Botões dinâmicos e elegantes com codificação de URI automática para LinkedIn, WhatsApp e Facebook, preservando a legibilidade e identidade da marca em qualquer tema (claro ou escuro).</p>

    <div class="page-break"></div>

    <!-- PILAR 3 -->
    <h2 id="pilar3">Pilar 3: Arsenal de Autoridade Interativa (Calculadoras em A4)</h2>

    <h3>1. Processamento Client-Side de Alta Performance</h3>
    <p>O portal entrega quatro ferramentas de cálculo poderosas que atuam como "ímãs" para atrair empreendedores que pesquisam soluções no Google:</p>
    <ul>
        <li><strong>Calculadora Simples Nacional</strong></li>
        <li><strong>Calculadora IRPF</strong></li>
        <li><strong>Calculadora INSS</strong></li>
        <li><strong>Calculadora Salário Líquido</strong> <span style="color:var(--accent); font-weight:bold;">[Bônus PandaRoSan]</span> — Ferramenta complexa entregue integralmente como bônus não-orçado para maximizar exponencialmente a tração do escritório.</li>
    </ul>
    <p><strong>Segurança e Privacidade:</strong> O motor de cálculo opera 100% no navegador do visitante usando a biblioteca SheetJS. A resposta é calculada em milissegundos sem que nenhum dado salarial seja enviado pela internet, preservando total sigilo.</p>

    <h3>2. O Laudo Timbrado em A4 (A Mágica da Impressão CSS)</h3>
    <p>Esta é uma sacada de engenharia de valor inestimável. Quando o usuário clica no botão <strong>"Imprimir / Salvar em PDF"</strong>, nosso CSS de Impressão entra em ação:</p>
    <ul>
        <li><strong>Re-formatação:</strong> Elementos de navegação (menus) e botões do site são sumariamente ocultados.</li>
        <li><strong>Composição do Documento:</strong> O resultado se transforma na tela em um <strong>laudo oficial timbrado A4</strong>. O relatório exibe o logotipo oficial da Contabilidade Camilo no topo, cabeçalhos sóbrios, a tabela exata de alíquotas gerada e um rodapé com a responsabilidade técnica do escritório.</li>
        <li><strong>Uso Prático:</strong> Configurando a impressora para o formato Retrato (Portrait), o cliente imprime um material impecável que funciona como um "panfleto" ou laudo de autoridade.</li>
    </ul>

    <div class="page-break"></div>

    <!-- PILAR 4 -->
    <h2 id="pilar4">Pilar 4: Máquina de Conteúdo, Autonomia e Decap CMS</h2>

    <h3>1. Roteiro Operacional do Painel</h3>
    <ul>
        <li><strong>Endereço de Acesso:</strong> <code>https://[seu-site]/admin</code></li>
        <li><strong>Credenciais:</strong> Login via e-mail corporativo autenticado. É impossível que um cliente, ao usar o painel, quebre o site. Ele tem acesso restrito e blindado apenas aos artigos e planilhas de base.</li>
    </ul>

    <h3>2. Recursos Completos de Publicação e Regras Editoriais</h3>
    <div class="highlight-box">
        <p>Desenvolvemos este painel para ser uma usina de atração de leads via SEO orgânico. O preenchimento correto é vital para posicionar os artigos na primeira página do Google.</p>
    </div>
    <ul>
        <li><strong>Campos Estruturados:</strong> O sistema separa perfeitamente o "Título" principal e o "Resumo" da notícia, formando a isca inicial de leitura.</li>
        <li><strong>Data e Hora (Trava de Agendamento):</strong> Ao usar o seletor nativo, você controla a hora. Se programar 10 publicações para o futuro, o nosso script de compilação <code>build.js</code> impõe uma <strong>trava lógica rigorosa</strong>: os textos agendados ficarão invisíveis e seguros, não vazando nem no site nem no mapa do Google, até atingirem a data e minuto exatos estipulados!</li>
        <li><strong>Hierarquia Semântica (SEO):</strong> O <strong>H1</strong> é injetado pelo sistema (o Título). No corpo, utilize <strong>H2</strong> para Tópicos Principais e <strong>H3</strong> para Subtópicos internos. Essa "escada" é vital para os robôs de busca.</li>
        <li><strong>Taxonomia Dinâmica (Autolimpeza de Tags):</strong> Ao inserir Tags (como "Tributário"), o site varre o banco e adiciona um botão no menu do blog com a contagem de posts daquele tema. Se todos os artigos daquela Tag forem removidos, o botão desaparecerá sozinho para evitar cliques falsos.</li>
        <li><strong>Imagens de Capa e Metadados (Alt Text):</strong> É <strong>obrigatório</strong> o uso da resolução universal de compartilhamento (1200 x 630 px) padrão Canva. Além disso, incluímos os campos críticos de <strong>Alt Text e Title</strong>. Como o Google é "cego", essas descrições ditam como a imagem rankeará nas pesquisas de imagens.</li>
    </ul>

    <h3>3. Widgets Ricos Disponíveis no Editor</h3>
    <p>Ampliamos as funcionalidades nativas do editor de texto para que os artigos se tornem multimídia. No botão "+" (Add Widget), você conta com arsenal total:</p>
    <ul>
        <li><strong>Imagem no corpo do texto:</strong> Permite inserção de imagens soltas entre parágrafos.</li>
        <li><strong>Imagem Clicável:</strong> Permite injetar banners no texto que operam como botões direcionadores (links).</li>
        <li><strong>Links nativos:</strong> Para ancoragem interna de palavras-chave.</li>
        <li><strong>Citações (Blockquotes):</strong> Blocos de texto destacados visualmente.</li>
        <li><strong>Vídeos do YouTube:</strong> Permite embed nativo, inserindo vídeos para aumentar massivamente o tempo de retenção do usuário na página (fator chave para o Google).</li>
    </ul>

    <h3>4. Autonomia na Atualização das Calculadoras (via Excel)</h3>
    <p>Você tem controle soberano sobre a tributação! Para atualizar as tabelas do IRPF e do INSS sem depender de programação:</p>
    <ol>
        <li>No painel <code>/admin</code>, clique na guia de configurações de arquivos.</li>
        <li>Baixe e edite a planilha <code>.xlsx</code> para atualizar os dados, e altere o campo mágico <strong>Ano_Base</strong> (ex: de 2026 para 2027).</li>
        <li>Faça o upload do novo arquivo Excel. O servidor recompilará o site em segundos, injetando o novo Ano Base e a nova matemática nos formulários do site.</li>
    </ol>

    <div class="page-break"></div>

    <!-- PILAR 5 -->
    <h2 id="pilar5">Pilar 5: Soberania Digital, Governança e Eficiência Operacional</h2>

    <h3>1. Custódia do Patrimônio Digital (Engenharia Externa)</h3>
    <p>A PandaRoSan IT Solutions realizou uma minuciosa auditoria na infraestrutura da Contabilidade Camilo:</p>
    <ul>
        <li><strong>Whois e Registro.br:</strong> Localizamos a custódia original do domínio, recuperamos credenciais e o estabelecemos em bases seguras no Registro oficial brasileiro.</li>
        <li><strong>Cloudflare e Blindagem DNS:</strong> A zona de DNS foi migrada sob nossa arquitetura para a Cloudflare, providenciando blindagem de rede e total soberania de apontamentos de segurança de E-mails (DKIM, SPF, DMARC). Todas as contas (GitHub, Cloudflare, CMS) foram estabelecidas sob a titularidade primária da Contabilidade Camilo, sem amarração com agências ou terceiros.</li>
    </ul>

    <h3>2. Automação de SEO e Google Search Console</h3>
    <ul>
        <li><strong>Esteira de Build e Sitemap:</strong> Desenvolvemos um script nativo (<code>build.js</code>) que roda silenciosamente a cada publicação. Ele identifica e descarta conteúdos de rascunho/futuros e emite um <code>sitemap.xml</code> impecável formatado com tags <code>&lt;lastmod&gt;</code> precisas e URLs convertidas com escape seguro.</li>
        <li><strong>Robots.txt e GSC:</strong> Apontamos o mapa para os robôs com diretrizes claras e ativamos, com maestria, a validação de Propriedade de Domínio (via DNS) diretamente no <strong>Google Search Console</strong>. As páginas vitais encontram-se mapeadas e em processo de submissão prioritária.</li>
    </ul>

    <h3>3. Diagnóstico e Eficiência Operacional (Roadmap Google Workspace)</h3>
    <p>O grande diferencial da engenharia PandaRoSan é focar na eficiência global da empresa (redução de <em>OpEx</em>).</p>
    <p>Realizamos a auditoria das licenças corporativas distribuídas entre <code>@contabilidadecamilo.com.br</code> e <code>@bluebpofinanceiro.com.br</code>. <strong>Foram identificadas 11 licenças pagas ativas mensais.</strong></p>

    <table>
        <thead>
            <tr>
                <th>Conta Mapeada</th>
                <th>Tipo de Uso</th>
                <th>Diagnóstico Estratégico</th>
            </tr>
        </thead>
        <tbody>
            <tr>
                <td><code>thais@contabilidadecamilo.com.br</code></td>
                <td>Titular / Operação</td>
                <td>Manter licença individual ativa.</td>
            </tr>
            <tr>
                <td><code>thais@bluebpofinanceiro.com.br</code></td>
                <td>Titular / BPO</td>
                <td><strong>Duplicidade identificada.</strong> Pode operar gratuitamente como Alias.</td>
            </tr>
            <tr>
                <td><code>contato@contabilidadecamilo.com.br</code></td>
                <td>Atendimento Geral</td>
                <td>Caixa departamental com histórico crítico (11,5 GB). Manter.</td>
            </tr>
            <tr>
                <td><code>contato@bluebpofinanceiro.com.br</code></td>
                <td>Atendimento BPO</td>
                <td>Caixa departamental que deve ser otimizada.</td>
            </tr>
            <tr>
                <td><code>arquivos@contabilidadecamilo.com.br</code></td>
                <td>Armazenamento</td>
                <td>Uso ínfimo (0,001 GB). <strong>Converter em Alias ou Grupo.</strong></td>
            </tr>
            <tr>
                <td><code>financeiro@contabilidadecamilo.com.br</code></td>
                <td>Administrativo</td>
                <td>Uso baixo (0,39 GB). <strong>Converter em Alias ou Grupo.</strong></td>
            </tr>
            <tr>
                <td><code>fiscal2@contabilidadecamilo.com.br</code></td>
                <td>Setor Fiscal</td>
                <td>Uso baixo (0,08 GB). <strong>Converter em Alias Compartilhado.</strong></td>
            </tr>
            <tr>
                <td><code>legal@</code>, <code>fiscal@</code>, <code>dp@</code>, <code>contabil@</code></td>
                <td>Setores Operacionais</td>
                <td>Avaliar fluxo para agrupamento colaborativo ou unificação.</td>
            </tr>
        </tbody>
    </table>

    <div class="highlight-box">
        <strong>Plano Tático de Redução de Custos:</strong>
        <p>A diretriz para os próximos meses visa a <strong>conversão das caixas departamentais</strong> (como <code>arquivos@</code>, <code>financeiro@</code>) em Aliases (apelidos) ou Grupos Colaborativos sem custo de licença no Workspace.</p>
        <p>Em paralelo, faremos a orquestração do <strong>Cloudflare Email Routing</strong>, permitindo redirecionar e-mails nativamente recebidos pelo domínio secundário diretamente para as caixas-mãe sem demandar licenças atreladas. O impacto estimado atinge a mitigação e o <strong>corte direto no desperdício de 3 a 5 licenças em moeda forte (Dólar) mensalmente</strong>, mantendo 100% da identidade institucional para o público e sem ferir a rotina da equipe de colaboradores.</p>
    </div>

    <div class="page-break"></div>

    <!-- ANEXO -->
    <h2 id="anexo">Anexo: Relação das Páginas do Portal</h2>
    <p>Para fins de auditoria, manutenção futura de conteúdo e mapeamento completo no Sitemap.xml, segue a relação definitiva das rotas arquitetadas dentro do escopo físico e dinâmico deste projeto.</p>

    <h3>Páginas Institucionais e Comerciais Base</h3>
    <ul>
        <li><code>index.html</code> — Home, landing page principal, resumo de experiência.</li>
        <li><code>sobre-nos.html</code> — Histórico de empresa, missão, valores institucionais.</li>
        <li><code>planos.html</code> — Estratégia de ancoragem de preços e pacotes de soluções.</li>
        <li><code>contato.html</code> — Formulários primários e mapa corporativo.</li>
        <li><code>noticias-e-artigos.html</code> — Central indexadora do CMS, que varre e aplica filtros interativos baseados na taxonomia inteligente de tags dos artigos cadastrados.</li>
    </ul>

    <h3>Páginas de Especialidades Técnicas</h3>
    <ul>
        <li><code>fiscal-e-contabilidade.html</code></li>
        <li><code>abertura-de-empresas-e-societario.html</code></li>
        <li><code>departamento-de-pessoal.html</code></li>
        <li><code>bpo-financeiro.html</code></li>
        <li><code>certificado-digital.html</code></li>
        <li><code>demais-solucoes.html</code></li>
    </ul>

    <h3>Calculadoras de Autoridade e Retenção (Bônus & Escopo)</h3>
    <ul>
        <li><code>calculadora-simples-nacional.html</code></li>
        <li><code>calculadora-inss.html</code></li>
        <li><code>calculadora-irpf.html</code></li>
        <li><code>calculadora-salario-liquido.html</code> (Ferramenta de alto nível adicionada extra escopo/bônus).</li>
    </ul>

    <h3>A Engrenagem Dinâmica (O Motor do Conteúdo e SEO)</h3>
    <ul>
        <li><code>artigo.html?id=[slug-do-post]</code><br>
        <strong>Nota de Engenharia (Template Cego):</strong> O arquivo <code>artigo.html</code> é a carcaça inteligente de SEO. O texto de fato do artigo nunca está dentro desta página. Quando clicada, a URL intercepta o "ID" via JavaScript puro e consome a imensa matriz de dados do banco gerado em <code>artigos.json</code>, montando a imagem de capa, os widgets ricos e o texto na tela do cliente. Ela também injeta as regras de Canonical Links de proteção ao SEO na aba invisível para blindar a Contabilidade contra penas por conteúdo duplicado no Google.</li>
    </ul>

    <h3>Legal e Compliance (LGPD)</h3>
    <ul>
        <li><code>politica-de-privacidade.html</code></li>
        <li><code>termos-de-uso.html</code></li>
    </ul>

    <div style="text-align: center; margin-top: 60px; padding-top: 30px; border-top: 2px solid var(--border); color: var(--text-light);">
        <p><strong>PandaRoSan IT Solutions © 2026</strong></p>
        <p><em>Inovação, Segurança e Engenharia de Vendas para o Setor Contábil.</em></p>
    </div>

</div>

</body>
</html>
"""

with open("manual-pandarosan.html", "w", encoding="utf-8") as f:
    f.write(html_content)
