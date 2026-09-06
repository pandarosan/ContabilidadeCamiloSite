import datetime

html_content = """<!DOCTYPE html>
<html lang="pt-BR">
<head>
    <meta charset="UTF-8">
    <title>Manual Definitivo - Contabilidade Camilo</title>
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;600;700&display=swap');
        
        :root {
            --primary: #1E3A8A;
            --secondary: #3B82F6;
            --accent: #F59E0B;
            --title-gold: #A4862D; /* Cor dourada do logo Camilo */
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
            font-size: 3.5rem;
            color: var(--primary);
            margin-bottom: 10px;
            line-height: 1.2;
            font-weight: 700;
            letter-spacing: -1px;
        }

        .cover-page h2 {
            font-size: 1.5rem;
            color: var(--text-light);
            font-weight: 300;
            margin-bottom: 40px;
            padding-bottom: 40px;
            border-bottom: 1px solid var(--border);
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
            text-align: justify;
        }

        ul, ol {
            margin-bottom: 1.5rem;
            padding-left: 20px;
            text-align: justify;
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
            text-align: justify;
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

        .footer-assinatura {
            text-align: center;
            margin-top: 60px;
            padding-top: 30px;
            border-top: 2px solid var(--border);
            color: var(--text-light);
            font-size: 0.9rem;
        }

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
        <h1>Contabilidade <span style="color: var(--title-gold);">Camilo</span></h1>
        <h2>Manual Definitivo de Operação, Governança e Estratégia Digital</h2>

        <div style="margin: 50px 0;">
            <p style="font-size: 1.2rem; color: #4B5563; text-align: center;">Projeto: <strong>Ecossistema Corporativo Contabilidade Camilo</strong></p>
        </div>

        <div class="cover-details">
            <p>Engenharia e Arquitetura: <strong>PandaRoSan IT Solutions</strong></p>
            <p>Responsável Técnica: <strong>Rosangela Corrêa — Arquiteta de Software</strong></p>
            <p>Versão: <strong>1.0 (Edição Definitiva de Entrega)</strong></p>
            <p>Data: <strong>Setembro / 2026</strong></p>
        </div>
    </div>

    <div class="page-break"></div>

    <!-- APRESENTAÇÃO EXECUTIVA -->
    <h2>Apresentação Executiva</h2>
    <p>Este documento consolida a entrega da reengenharia digital da <strong>Contabilidade Camilo</strong>. O projeto substitui modelos tradicionais obsoletos por uma infraestrutura <strong>Jamstack de alto padrão</strong>, orientada à soberania do cliente, conversão comercial, blindagem cibernética e custo operacional de hospedagem zero.</p>
    <p>Além do escopo contratado, a <strong>PandaRoSan IT Solutions</strong> implementou funcionalidades de ponta (como o Dark Mode e calculadoras extras) como bônus de engenharia.</p>

    <!-- ÍNDICE -->
    <div class="toc">
        <h3>Índice</h3>
        <ul>
            <li><a href="#pilar1">Pilar 1: A Revolução Arquitetural (Engenharia, Valor e Segurança)</a></li>
            <li><a href="#pilar2">Pilar 2: Navegação Comercial e Engenharia de Conversão</a></li>
            <li><a href="#pilar3">Pilar 3: Arsenal de Autoridade Interativa (Calculadoras Inteligentes e Impressão)</a></li>
            <li><a href="#pilar4">Pilar 4: Máquina de Conteúdo, Autonomia e Decap CMS</a></li>
            <li><a href="#pilar5">Pilar 5: Soberania de Infraestrutura, Governança, Eficiência Operacional & SEO Estratégico</a></li>
            <li><a href="#anexo">Anexo: Relação das Páginas do Portal</a></li>
        </ul>
    </div>

    <div class="page-break"></div>

    <!-- PILAR 1 -->
    <h2 id="pilar1">Pilar 1: A Revolução Arquitetural (Engenharia, Valor e Segurança)</h2>
    
    <h3>1. O Modelo Jamstack vs. Plataformas Legadas</h3>
    <ul>
        <li><strong>O modelo tradicional (WordPress/PHP):</strong> É marcado pelo uso de <em>templates genéricos de prateleira muito comuns no mercado</em>. Tais soluções dependem de requisições a bancos de dados MySQL e processamento dinâmico em servidor a cada acesso. Isso gera dependência técnica constante, lentidão crônica no carregamento e vulnerabilidades a invasões (como <em>SQL Injection</em> e ataques de força bruta), além de necessidade constante de atualizações corretivas.</li>
        <li><strong>A arquitetura Jamstack adotada:</strong> As páginas nascem pré-compiladas em arquivos estáticos ultraleves (HTML5 semântico, CSS3 e JavaScript otimizado). Ao contrário dos templates genéricos, nossas páginas carregam instantaneamente. O navegador do visitante consome o conteúdo de forma instantânea, garantindo nota máxima em métricas de <em>Core Web Vitals</em> e Google PageSpeed.</li>
    </ul>

    <h3>2. A Tríade Tecnológica Serverless (Custo Zero de Hospedagem)</h3>
    <p>Utilizamos a infraestrutura mais robusta e moderna do mundo para eliminar custos recorrentes com hospedagem web:</p>
    <ul>
        <li><strong>GitHub (Versionamento e Custódia):</strong> Todo o histórico de código-fonte, artigos e alterações é arquivado em uma nuvem criptografada. Funciona como uma "caixa preta" inviolável com controle de versão imutável. Se algo der errado, garantimos o <em>Rollback</em> (restauração) instantâneo.</li>
        <li><strong>Cloudflare Pages (Borda Global e CDN):</strong> O site não fica em um único servidor. Ele é replicado em mais de 300 data centers globais da Cloudflare, entregando conteúdo com latência zero e certificados SSL corporativos automáticos.</li>
        <li><strong>Decap CMS (Gerenciador Desacoplado):</strong> Painel visual amigável que atua como interface para a equipe publicar conteúdos, eliminando totalmente a dependência de servidores web PHP/MySQL pagos dedicados 24/7.</li>
    </ul>

    <h3>Blindagem Ativa contra Ameaças Digitais</h3>
    <p>A segurança deste portal é absoluta por design. Como não há banco de dados aberto na web, mitigamos qualquer invasão estrutural. O projeto conta com imunidade a plugins desatualizados e proteção perimetral contra ataques DDoS.</p>

    <div class="page-break"></div>

    <!-- PILAR 2 -->
    <h2 id="pilar2">Pilar 2: Navegação Comercial e Engenharia de Conversão</h2>

    <h3>1. Mapa Estrutural do Portal e Integração de Portais</h3>
    <ul>
        <li><strong>Home (/):</strong> Vitrine comercial de impacto. Realiza o cálculo automático de experiência do escritório, apresenta as soluções primárias de forma arrojada e possui captura estratégica.</li>
        <li><strong>Soluções Verticais:</strong> Páginas dedicadas e focadas nas especialidades do escritório (Área Fiscal, Departamento Pessoal, BPO Financeiro, etc.).</li>
        <li><strong>Acesso aos Portais Corporativos:</strong> Atendendo a uma solicitação explícita e vital do cliente, o menu principal abriga o acesso direto ao <strong>[Portal do Cliente]</strong> e <strong>[Portal do Empregado]</strong>. Essa integração facilita enormemente a rotina diária de quem já é cliente da contabilidade, tudo isso sem poluir a navegação voltada à prospecção comercial.</li>
    </ul>

    <h3>2. Mecânica do WhatsApp Dinâmico Geral</h3>
    <p>O fluxo de conversão deste portal não se baseia em links genéricos. Desenvolvemos uma inteligência que opera mensagens contextualizadas em <strong>toda a malha de contato do site</strong>, enviando mensagens pré-qualificadas e assertivas direto para o WhatsApp do escritório:</p>
    <ul>
        <li><strong>Modais Flutuantes Contextuais (Topo da Home):</strong> Implementamos os modais interativos <strong>[PARA VOCÊ]</strong>, <strong>[ABRA SUA EMPRESA]</strong> e <strong>[TROQUE DE CONTADOR]</strong>. O cliente seleciona sua intenção primária ali mesmo e a ferramenta formata o pedido, direcionando com uma mensagem altamente qualificada.</li>
        <li><strong>Seletor de Assuntos (Contato e Rodapé):</strong> O formulário da página <code>contato.html</code> e o envio direto pelo rodapé adaptam dinamicamente a mensagem baseada no assunto escolhido.</li>
        <li><strong>Leitura Contextual Dinâmica (Artigos):</strong> Ao final de cada leitura no blog (<code>artigo.html</code>), o script mapeia silenciosamente a tag <code>&lt;h1&gt;</code> lida pelo usuário e constrói o gatilho de atendimento com URL codificada: <em>"Olá! Li o artigo <strong>'[Título Exato do Artigo]'</strong> no site de vocês e gostaria de orientação técnica especializada sobre este tema."</em></li>
    </ul>

    <h3>3. Automação de Tempo de Fundação (Inteligência de Código)</h3>
    <p>No arquivo <code>main.js</code>, projetamos um script dinâmico ancorado na classe <code>.anos-experiencia</code>, baseado no ano base de fundação (2009). Com isso, a cada novo ano, o portal atualiza automaticamente toda a comunicação da idade institucional (ex: os "17 anos" de experiência). Evidenciamos que o escritório nunca precisará atualizar estes textos manualmente.</p>

    <h3>4. Funcionalidades Bônus de Engenharia (PandaRoSan)</h3>
    <div class="highlight-box">
        <p>Visando entregar um portal com excelência sem precedentes, e embora não estivesse previsto no escopo e orçamento iniciais, a PandaRoSan entregou como diferencial adiciona um sofisticado sistema de <strong>Modo Escuro (Dark Mode)</strong> e <strong>Botão Flutuante de Retorno ao Topo:</strong></p>
        <ul>
            <li><strong>Dark Mode Dinâmico:</strong> Alternância (botão Sol/Lua) que adapta a identidade do site para fundos escuros, reduzindo cansaço visual e transmitindo vanguarda.</li>
            <li><strong>Botão de Retorno ao Topo (Back to Top):</strong> Inclusão de navegação inteligente com rolagem ergonômica suave na lateral.</li>
        </ul>
    </div>

    <div class="page-break"></div>

    <!-- PILAR 3 -->
    <h2 id="pilar3">Pilar 3: Arsenal de Autoridade Interativa (Calculadoras Inteligentes e Impressão)</h2>

    <h3>1. Processamento Client-Side de Alta Performance</h3>
    <p><strong>Quatro ferramentas ativas:</strong> Simples Nacional, IRPF, INSS e a <strong>Calculadora de Salário Líquido</strong> (ferramenta complexa entregue como <strong>Bônus de Engenharia</strong> da PandaRoSan IT Solutions, maximizando o arsenal de atração do escritório).</p>
    <p><strong>Segurança e Privacidade:</strong> O motor de cálculo opera inteiramente no navegador do usuário via biblioteca corporativa (SheetJS). O usuário digita os valores e a resposta é calculada em milissegundos sem que nenhum dado salarial trafegue pela internet.</p>

    <h3>2. O Laudo Timbrado em A4 (A Mágica da Impressão CSS)</h3>
    <p><strong>Gatilho Visual:</strong> Ao clicar em "Imprimir / Salvar em PDF", folhas de estilo de mídia (<code>@media print</code>) reformatam a página.</p>
    <p><strong>Composição do Documento:</strong> Elementos de navegação e botões são ocultados. O relatório exibe o logotipo oficial da Contabilidade Camilo, cabeçalhos sóbrios, tabelas com o detalhamento de alíquotas e o rodapé de responsabilidade técnica. Mais do que isso, o rodapé do documento gerado estampa os contatos oficiais, endereço e credenciamento do escritório, transformando a impressão em um autêntico laudo técnico de autoridade que atua como poderoso material institucional de divulgação perante o cliente final.</p>
    <p><strong>Orientação de Uso:</strong> A impressão deve ser configurada de forma exclusiva no modo <strong>Retrato (Portrait)</strong>. Destacamos que a simulação do <strong>IRPF</strong> foi compactada para caber perfeitamente em <strong>1 única folha A4</strong>, enquanto a simulação do <strong>Simples Nacional</strong> é estruturada como um parecer executivo de <strong>2 páginas</strong>.</p>

    <h3>3. Manual de Manutenção das Planilhas de Cálculo</h3>
    <p>As calculadoras operam consultando bases matemáticas estruturadas em arquivos Excel disponíveis no repositório. Alterações nas faixas tributárias são atualizadas exclusivamente através deles.</p>
    
    <div class="highlight-box" style="border-left-color: #EF4444; background-color: #FEF2F2;">
        <strong>REGRA CRÍTICA DE MANUTENÇÃO:</strong> É terminantemente proibido renomear o título das planilhas, os nomes das abas internas ou o cabeçalho de qualquer coluna/campo. Alterar essa nomenclatura quebrará o mapeamento lógico das calculadoras instantaneamente! As consequências de alterações indevidas afetam o motor de processamento direto no navegador.
    </div>

    <table>
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
                <td>Faixa, Limite_Ate, Aliquota, Parcela_Deduzir.<br>Categoria, Base_Calculo.</td>
            </tr>
            <tr>
                <td><strong>Qualquer Arquivo</strong></td>
                <td>(Abas de <strong>Parâmetros</strong>)</td>
                <td><strong>Todas</strong></td>
                <td>O campo <code>Ano_Base</code> dita o ano vigente nas regras de exibição do site (Ex: 2026).</td>
            </tr>
        </tbody>
    </table>

    <div class="page-break"></div>

    <!-- PILAR 4 -->
    <h2 id="pilar4">Pilar 4: Máquina de Conteúdo, Autonomia e Decap CMS</h2>

    <h3>1. Roteiro Operacional do Painel</h3>
    <ul>
        <li><strong>Endereço de Acesso:</strong> <code>https://[seu-site]/admin</code></li>
        <li><strong>Credenciais:</strong> Login via e-mail corporativo autenticado. É impossível que um cliente, ao usar o painel, quebre o site. Ele tem acesso restrito e blindado apenas aos artigos e planilhas de base.</li>
    </ul>

    <h3>2. Publicação de Artigos e Regras Editoriais (Passo a Passo Prático)</h3>
    <ul>
        <li><strong>Criação de Artigos:</strong> Em "Notícias & Artigos", preencha o Título comercial. <strong>Recomendação: deixe o campo Slug em branco!</strong> O sistema gerará a URL automaticamente.</li>
        <li><strong>Data e Hora:</strong> Sempre selecione a data no seletor nativo. <strong>Uso obrigatório do botão "Agora"</strong> para postagens imediatas. A trava lógica de compilação do script <code>build.js</code> garante que publicações datadas para o futuro permaneçam como rascunhos invisíveis até a data estipulada.</li>
        <li><strong>Resumo:</strong> Redija um resumo atrativo para os cards (até 150 caracteres).</li>
        <li><strong>Hierarquia Semântica:</strong> Regra vital: nunca use H1 no corpo do texto (ele já é gerado pelo Título principal). Use <strong>H2 para tópicos principais</strong> e <strong>H3 para subtópicos internos</strong>.</li>
        <li><strong>Indexação Otimizada:</strong> O preenchimento correto é obrigatório para atingir a meta de ranqueamento, focando tanto no Google quanto em motores de busca baseados em Inteligência Artificial (ChatGPT, Google Gemini, Perplexity).</li>
    </ul>
    
    <h3>3. Utilizando Widgets Ricos (O Botão '+ Add Widget')</h3>
    <p>Ampliamos as funcionalidades nativas do editor de texto para que os artigos se tornem multimídia. Enriqueça brutalmente o tempo de leitura do seu cliente aplicando os seguintes widgets interativos na formatação:</p>
    <ul>
        <li><strong>Imagem no corpo do texto:</strong> Para ilustrar parágrafos.</li>
        <li><strong>Imagem Clicável:</strong> Banners ou botões gráficos com links.</li>
        <li><strong>Links nativos:</strong> Para ancoragem interna de palavras-chave.</li>
        <li><strong>Blockquotes:</strong> Citações de destaque.</li>
        <li><strong>Vídeos do YouTube:</strong> Permite embed nativo, inserindo vídeos para aumentar massivamente o tempo de retenção do usuário na página (fator chave para o Google).</li>
    </ul>

    <h3>4. Diretrizes Oficiais de Imagens (Capa)</h3>
    <ul>
        <li><strong>Formato Preferencial:</strong> <code>.jpg</code> (padrão de exportação do Canva) ou <code>.webp</code>.</li>
        <li><strong>Teto de Peso:</strong> Máximo de 150 KB (sendo o ideal abaixo de 100 KB). Recomendamos fortemente o uso de compressores gratuitos como <em>TinyPNG</em> ou <em>Squoosh</em>.</li>
        <li><strong>Dimensões Recomendadas:</strong> 1200 x 630 px ou 851 x 315 px.</li>
        <li><strong>SEO Obrigatório:</strong> O preenchimento dos campos <strong>Alt Text e Title</strong> é rigorosamente obrigatório para garantir a indexação nos mecanismos do Google Imagens.</li>
    </ul>

    <h3>5. Atualização das Planilhas via CMS</h3>
    <p>Roteiro prático: Acesse <em>Configurações do Sistema > Base de Dados da Calculadora</em> no painel `/admin`. Faça o upload das novas planilhas <code>.xlsx</code> e salve. Ocorrerá a recompilação automática na Cloudflare.</p>

    <div class="page-break"></div>

    <!-- PILAR 5 -->
    <h2 id="pilar5">Pilar 5: Soberania de Infraestrutura, Governança, Eficiência Operacional & SEO Estratégico</h2>

    <h3>1. Custódia do Patrimônio Digital (Engenharia Externa)</h3>
    <p>Auditoria Whois: Recuperação do domínio e configuração cadastral definitiva no <strong>Registro.br</strong>.</p>
    <p>Cloudflare: Migração da zona DNS, garantindo blindagem de rede, controle sobre zonas de e-mail e registros (DKIM, SPF e DMARC). As contas foram criadas com a titularidade do cliente, garantindo independência contratual absoluta.</p>

    <h3>2. Automação de SEO e Google Search Console</h3>
    <p>Esteira build.js: A cada publicação, o script constrói o <code>sitemap.xml</code> descartando rascunhos futuros e aplicando as datas reais (<code>&lt;lastmod&gt;</code>).</p>
    <p>Diretivas robots.txt: Libera e direciona o rastreamento do motor de busca para o mapa XML.</p>
    <p>Google Search Console: Propriedade validada ativamente via DNS. Sitemap ativamente submetido e processado pelo Google para as 21 páginas estratégicas.</p>

    <h3>3. Diagnóstico e Eficiência Operacional (Roadmap Google Workspace)</h3>
    <p>A PandaRoSan IT analisou a estrutura corporativa do Google Workspace distribuída entre os domínios <code>@contabilidadecamilo.com.br</code> e <code>@bluebpofinanceiro.com.br</code>. Identificamos 11 licenças pagas ativas.</p>
    
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
                <td><strong>Duplicidade.</strong> Pode operar como Alias gratuito.</td>
            </tr>
            <tr>
                <td><code>contato@contabilidadecamilo.com.br</code></td>
                <td>Atendimento Geral</td>
                <td>Caixa departamental com histórico (11,5 GB).</td>
            </tr>
            <tr>
                <td><code>contato@bluebpofinanceiro.com.br</code></td>
                <td>Atendimento BPO</td>
                <td>Caixa departamental.</td>
            </tr>
            <tr>
                <td><code>arquivos@contabilidadecamilo.com.br</code></td>
                <td>Armazenamento</td>
                <td>Uso ínfimo (0,001 GB). <strong>Converter em Alias/Grupo.</strong></td>
            </tr>
            <tr>
                <td><code>financeiro@contabilidadecamilo.com.br</code></td>
                <td>Administrativo</td>
                <td>Uso baixo (0,39 GB). <strong>Converter em Alias/Grupo.</strong></td>
            </tr>
            <tr>
                <td><code>fiscal2@contabilidadecamilo.com.br</code></td>
                <td>Setor Fiscal</td>
                <td>Uso baixo (0,08 GB). <strong>Converter em Alias compartilhado.</strong></td>
            </tr>
            <tr>
                <td><code>legal@</code>, <code>fiscal@</code>, <code>dp@</code>, <code>contabil@</code></td>
                <td>Operacionais</td>
                <td>Avaliar agrupamento colaborativo ou unificação.</td>
            </tr>
        </tbody>
    </table>

    <div class="highlight-box">
        <strong>Plano Tático de Redução de Custos:</strong>
        <p><strong>Segurança e Sigilo:</strong> Fica claro que os departamentos críticos (Diretoria/Thaís, Departamento Pessoal e Financeiro) mantêm suas contas e acessos restritos individualmente via autenticação e pastas privadas no Google Drive.</p>
        <p><strong>Comunicação Interna:</strong> Nestas contas individuais, preservam-se as ferramentas do Google Workspace (Chat e Meet) para a rotina de colaboração plena.</p>
        <p><strong>Plano de Eficiência:</strong> A conversão cirúrgica de caixas departamentais de baixo tráfego (como <code>arquivos@</code>, <code>financeiro@</code> e <code>fiscal2@</code>) em Aliases (apelidos) ou Grupos Colaborativos gratuitos. Somada ao roteamento inteligente via <strong>Cloudflare Email Routing</strong> para o domínio secundário, esta medida <strong>reduzirá de 3 a 5 licenças mensais (cobradas em dólar)</strong> com total zero atrito operacional, preservando a identidade institucional e mantendo a operação da equipe inalterada.</p>
    </div>

    <div class="page-break"></div>

    <!-- ANEXO -->
    <h2 id="anexo">Anexo: Relação das Páginas do Portal</h2>
    <p>Para fins de governança de SEO e acompanhamento do crescimento do domínio, estruturamos a relação completa de páginas criadas (sem contar os artigos dinâmicos do CMS). Todas estas páginas estão validadas e contidas no mapa do Google (Sitemap).</p>

    <h3>Páginas Institucionais e Comerciais</h3>
    <ul>
        <li><code>index.html</code> (Home)</li>
        <li><code>sobre-nos.html</code> (Sobre a empresa)</li>
        <li><code>planos.html</code> (Ancoragem de preços)</li>
        <li><code>contato.html</code> (Canais de atendimento)</li>
        <li><code>noticias-e-artigos.html</code> (Central de navegação do Blog com filtro dinâmico de tags)</li>
    </ul>

    <h3>Páginas de Soluções e Especialidades</h3>
    <ul>
        <li><code>fiscal-e-contabilidade.html</code></li>
        <li><code>abertura-de-empresas-e-societario.html</code></li>
        <li><code>departamento-de-pessoal.html</code></li>
        <li><code>bpo-financeiro.html</code></li>
        <li><code>certificado-digital.html</code></li>
        <li><code>demais-solucoes.html</code></li>
    </ul>

    <h3>Calculadoras de Autoridade</h3>
    <ul>
        <li><code>calculadora-simples-nacional.html</code></li>
        <li><code>calculadora-inss.html</code></li>
        <li><code>calculadora-irpf.html</code></li>
        <li><code>calculadora-salario-liquido.html</code> (Bônus Integrado)</li>
    </ul>

    <h3>Estrutura Dinâmica de Postagens (O Motor de SEO)</h3>
    <ul>
        <li><code>artigo.html?id=[slug]</code><br>
        <strong>Nota Técnica:</strong> Esta é a "página casca" (template) desacoplada. O script dinâmico lê o parâmetro de URL (<code>artigo.html?id=slug-do-post</code>) e consome os dados do arquivo <code>artigos.json</code>, montando a matéria em milissegundos na tela do usuário. Esse consumo injeta, em tempo real, as Tags Canônicas exclusivas, evitam a punição por conteúdo duplicado no Google e protegem integralmente o SEO do projeto.</li>
    </ul>

    <h3>Documentação Legal (LGPD)</h3>
    <ul>
        <li><code>politica-de-privacidade.html</code></li>
        <li><code>termos-de-uso.html</code></li>
    </ul>

    <div class="footer-assinatura">
        <p><strong>PandaRoSan IT Solutions © 2026</strong><br>
        Engenharia de Software de Elite, Automações e Presença Digital de Alta Performance.</p>
    </div>

</div>

</body>
</html>
"""

with open("manual-pandarosan.html", "w", encoding="utf-8") as f:
    f.write(html_content)
