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
            text-align: justify; /* Alinhamento justificado adicionado */
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
        <h1>Contabilidade Camilo</h1>
        <h2>Manual Definitivo de Operação, Governança e Estratégia Digital</h2>

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
    <p>Além do escopo contratado, a <strong>PandaRoSan IT Solutions</strong> fez questão de entregar excelência através de funcionalidades de ponta implementadas como <strong>Bônus de Engenharia</strong>, agregando um valor inestimável à plataforma final.</p>

    <!-- ÍNDICE -->
    <div class="toc">
        <h3>Índice</h3>
        <ul>
            <li><a href="#pilar1">Pilar 1: Engenharia e Arquitetura</a></li>
            <li><a href="#pilar2">Pilar 2: Navegação e Engenharia de Vendas</a></li>
            <li><a href="#pilar3">Pilar 3: Calculadoras Inteligentes e Impressão</a></li>
            <li><a href="#pilar4">Pilar 4: Operando o Decap CMS (Pedagógico e Mastigado)</a></li>
            <li><a href="#pilar5">Pilar 5: Governança, SEO e Eficiência Workspace</a></li>
            <li><a href="#anexo">Anexo Oficial: Relação das Páginas do Portal</a></li>
        </ul>
    </div>

    <div class="page-break"></div>

    <!-- PILAR 1 -->
    <h2 id="pilar1">Pilar 1: Engenharia e Arquitetura</h2>
    
    <h3>O Modelo Jamstack vs. Plataformas Legadas</h3>
    <ul>
        <li><strong>O modelo tradicional (WordPress/PHP):</strong> É marcado pelo uso de <em>templates genéricos de prateleira muito comuns no mercado</em>. Tais soluções dependem de requisições lentas a bancos de dados MySQL a cada acesso do usuário. Isso gera dependência técnica constante, lentidão crônica no carregamento e escancara portas para graves vulnerabilidades a invasões (como ataques de força bruta e injeções de SQL).</li>
        <li><strong>A arquitetura Jamstack adotada:</strong> As páginas nascem pré-compiladas em arquivos estáticos ultraleves (HTML5 semântico, CSS3 e JavaScript otimizado). Ao contrário dos templates genéricos, nossas páginas carregam em milissegundos. O navegador do visitante consome o conteúdo de forma instantânea, garantindo nota máxima em métricas de <em>Core Web Vitals</em> e Google PageSpeed.</li>
    </ul>

    <h3>A Tríade Tecnológica Serverless (Custo Zero de Hospedagem)</h3>
    <p>Utilizamos a infraestrutura mais robusta e moderna do mundo para eliminar custos recorrentes com hospedagem web:</p>
    <ul>
        <li><strong>GitHub (Versionamento e Custódia):</strong> Funciona como um cofre inviolável. Todo o histórico de alterações é arquivado com controle de versão imutável. Se algo der errado, o <em>Rollback</em> (restauração) é imediato.</li>
        <li><strong>Cloudflare Pages (Borda Global e CDN):</strong> O site é replicado em centenas de data centers globais, entregando latência zero e certificados SSL automáticos.</li>
        <li><strong>Decap CMS:</strong> Interface visual amigável e segura, eliminando a dependência de servidores web pagos dedicados 24/7.</li>
    </ul>

    <h3>Blindagem Ativa contra Ameaças Digitais</h3>
    <div class="highlight-box">
        <p>A segurança deste portal é absoluta por design. Como <strong>não há banco de dados aberto na web</strong>, mitigamos qualquer invasão estrutural. O projeto conta com imunidade a plugins desatualizados e proteção perimetral contra ataques DDoS.</p>
    </div>

    <div class="page-break"></div>

    <!-- PILAR 2 -->
    <h2 id="pilar2">Pilar 2: Navegação e Engenharia de Vendas</h2>

    <h3>1. Mapa Estrutural do Portal e Portais Externos</h3>
    <ul>
        <li><strong>Home (/):</strong> Vitrine comercial com âncora visual arrojada, destacando de cara a expertise e as soluções do escritório.</li>
        <li><strong>Integração de Portais do Cliente:</strong> Atendendo a uma solicitação explícita do escritório, o menu principal agora abriga de forma elegante os links de acesso direto ao <strong>[Portal do Cliente]</strong> e <strong>[Portal do Empregado]</strong>, facilitando enormemente a rotina diária da sua base de clientes sem ferir o apelo visual da prospecção.</li>
    </ul>

    <h3>2. Mecânica do WhatsApp Dinâmico Geral</h3>
    <p>O fluxo de conversão deste portal não se baseia em links genéricos. Desenvolvemos uma inteligência que opera mensagens contextualizadas em <strong>toda a malha de contato do site</strong>, enviando mensagens pré-qualificadas e assertivas direto para o WhatsApp do escritório:</p>
    <ul>
        <li><strong>Modais Flutuantes Contextuais (Topo da Home):</strong> Implementamos os modais interativos <strong>[PARA VOCÊ]</strong>, <strong>[ABRA SUA EMPRESA]</strong> e <strong>[TROQUE DE CONTADOR]</strong>. O cliente seleciona sua intenção primária ali mesmo e a ferramenta formata o pedido.</li>
        <li><strong>Seletor de Assuntos (Contato e Rodapé):</strong> O formulário da página <code>contato.html</code> e o envio direto pelo rodapé adaptam dinamicamente a mensagem baseada no assunto escolhido.</li>
        <li><strong>Leitura Contextual Dinâmica (Artigos):</strong> Ao final de cada leitura no blog (<code>artigo.html</code>), o sistema captura silenciosamente a tag <code>&lt;h1&gt;</code> e formula o gatilho de contato com o nome exato do artigo lido.</li>
    </ul>

    <h3>3. Automação de Tempo de Fundação (Inteligência de Código)</h3>
    <p>Adeus às atualizações manuais de textos do tipo "Temos 17 anos de experiência". No arquivo <code>main.js</code>, projetamos um script dinâmico ancorado na classe <code>.anos-experiencia</code> e baseado no ano base de fundação (2009). Com isso, a cada novo ano, o portal atualiza toda a comunicação da sua idade institucional de forma orgânica e infalível, sem intervenção humana.</p>

    <h3>4. Funcionalidades Bônus de Engenharia (PandaRoSan)</h3>
    <div class="highlight-box">
        <p>Visando entregar um portal com excelência sem precedentes, adicionamos os seguintes recursos não orçados:</p>
        <ol>
            <li><strong>Dark Mode Dinâmico:</strong> Um sistema elegante de alternância (botão Sol/Lua) que adapta 100% da identidade do site para fundos escuros, reduzindo cansaço visual e transmitindo vanguarda.</li>
            <li><strong>Botão de Retorno ao Topo (Back to Top):</strong> Inclusão de navegação inteligente com rolagem ergonômica suave na lateral direita da tela.</li>
        </ol>
    </div>

    <div class="page-break"></div>

    <!-- PILAR 3 -->
    <h2 id="pilar3">Pilar 3: Calculadoras Inteligentes e Impressão</h2>

    <h3>1. Processamento de Alta Performance (SheetJS)</h3>
    <p>Nosso motor de cálculo client-side assegura cálculos imediatos e sigilo inquebrável dos dados imputados pelo visitante. Compõem este arsenal:</p>
    <ul>
        <li>Simples Nacional</li>
        <li>IRPF</li>
        <li>INSS</li>
        <li><strong>Calculadora de Salário Líquido:</strong> Ferramenta avançada para o público em geral e RH, formalmente entregue como um <strong>Bônus de Engenharia</strong> da PandaRoSan IT Solutions. Permite calcular exibições de proventos e descontos mensais.</li>
    </ul>

    <h3>2. Laudo Timbrado A4 e Divulgação Indireta</h3>
    <p>O clique em "Imprimir / Salvar em PDF" ativa um refinado CSS de impressão. Essa formatação oculta botões da interface e exibe o logotipo da empresa no topo. Mais do que isso, <strong>o rodapé do documento gerado estampa os contatos oficiais, endereço e credenciamento do escritório</strong>, transformando a impressão em um autêntico laudo técnico de autoridade que atua como poderoso material institucional de divulgação perante o cliente final.</p>
    <p><strong>Diretriz de Impressão:</strong> Instrua a equipe e usuários a sempre utilizarem o formato <strong>Retrato (Portrait)</strong> nas configurações da impressora. Garantimos que a simulação do <strong>IRPF foi estrategicamente compactada para caber em 1 única folha A4</strong>, enquanto a simulação do <strong>Simples Nacional está estruturada como um parecer executivo encorpado de 2 páginas</strong>.</p>

    <h3>3. Manual de Manutenção das Planilhas de Cálculo</h3>
    <p>As calculadoras operam consultando bases matemáticas estruturadas em arquivos Excel disponíveis no repositório. Alterações nas faixas tributárias são atualizadas exclusivamente através deles.</p>
    
    <div class="highlight-box" style="border-left-color: #EF4444; background-color: #FEF2F2;">
        <strong>REGRA CRÍTICA DE MANUTENÇÃO:</strong> É terminantemente proibido renomear o título das planilhas, os nomes das abas internas ou o cabeçalho de qualquer coluna (ex: <code>Ano_Base</code>, <code>Faixa</code>, <code>Aliquota</code>). Alterar essa nomenclatura quebrará o mapeamento lógico das calculadoras instantaneamente! Apenas valores numéricos (taxas e tetos) devem ser alterados.
    </div>

    <table>
        <thead>
            <tr>
                <th>Arquivo Físico (Excel)</th>
                <th>Aba Interna</th>
                <th>Calculadora Afetada</th>
                <th>Parâmetros / Campos Atualizáveis</th>
            </tr>
        </thead>
        <tbody>
            <tr>
                <td><code>calculadora-ir-configuracoes.xlsx</code></td>
                <td>IRPF</td>
                <td>Calculadora de IRPF</td>
                <td>Faixa de Renda (Min/Max), Alíquotas e Parcela a Deduzir.</td>
            </tr>
            <tr>
                <td><code>calculadora-ir-configuracoes.xlsx</code></td>
                <td>Simples Nacional</td>
                <td>Simples Nacional</td>
                <td>Faturamento, Anexos I a V, Alíquota Nominal e Valor a Deduzir.</td>
            </tr>
            <tr>
                <td><code>calculadora-inss-configuracoes.xlsx</code></td>
                <td>INSS</td>
                <td>INSS &amp; Salário Líquido</td>
                <td>Salário de Contribuição, Alíquota Progressiva e Dedutível.</td>
            </tr>
            <tr>
                <td><strong>Qualquer Arquivo</strong></td>
                <td><strong>Parametros_Gerais</strong></td>
                <td><strong>Todas</strong></td>
                <td>O campo especial <code>Ano_Base</code> dita o ano vigente das regras no site (Ex: 2026).</td>
            </tr>
        </tbody>
    </table>

    <div class="page-break"></div>

    <!-- PILAR 4 -->
    <h2 id="pilar4">Pilar 4: Operando o Decap CMS (Pedagógico e Mastigado)</h2>

    <h3>1. Instruções Detalhadas de Uso do Painel</h3>
    <p>O Decap CMS é a sua usina de geração de tráfego. Siga este roteiro rigoroso para indexar perfeitamente os conteúdos no Google e nos robôs de Inteligência Artificial (ChatGPT, Gemini e Perplexity).</p>
    
    <ul>
        <li><strong>Acesso Autenticado:</strong> Acesse via <code>/admin</code> logando com sua credencial corporativa integrada à Cloudflare/GitHub.</li>
        <li><strong>Criação de Artigos e Slug:</strong> Vá em "Notícias & Artigos" e crie um novo registro. Preencha o "Título" com foco comercial. <strong>Deixe o campo Slug em branco!</strong> O sistema gera a URL amigável automaticamente para você.</li>
        <li><strong>Data e Trava de Segurança:</strong> Ao selecionar a data/hora, utilize preferencialmente o botão <strong>"Agora"</strong> (Now) para postagens imediatas. Graças ao <code>build.js</code>, agendamentos com data e hora futuras são travados pela segurança do sistema e só aparecerão no site no exato momento programado.</li>
        <li><strong>O Resumo:</strong> Redija um pequeno texto atrativo (máximo 150 caracteres) para os cards de exibição na grade do blog.</li>
        <li><strong>Hierarquia de Títulos (O Segredo do SEO):</strong> Nunca utilize a formatação H1 dentro da caixa de texto do artigo (o H1 já é injetado pelo seu Título principal). Dentro do corpo do texto, use <strong>H2 para os Tópicos principais</strong> e <strong>H3 para subtópicos</strong>. Os robôs rastreadores cobram essa hierarquia em cascata.</li>
    </ul>

    <h3>2. Utilizando Widgets Ricos (O Botão '+ Add Widget')</h3>
    <p>Enriqueça brutalmente o tempo de leitura do seu cliente aplicando os seguintes widgets interativos na formatação:</p>
    <ul>
        <li><strong>Imagem no corpo do texto:</strong> Fotografias complementares ilustrando os parágrafos.</li>
        <li><strong>Imagem Clicável:</strong> Permite injetar banners de marketing que operam como botões direcionadores (links para consultorias).</li>
        <li><strong>Citações (Blockquotes):</strong> Destaque visual (em borda e itálico) para frases de efeito ou leis aplicadas.</li>
        <li><strong>Vídeos do YouTube:</strong> Permite realizar embed nativo, essencial para reter o leitor assistindo a materiais educativos da contabilidade.</li>
    </ul>

    <h3>3. Diretrizes Oficiais de Imagens (Capa)</h3>
    <p>O rigor com o tratamento das imagens assegura a velocidade de carregamento (Nota "A" no Google PageSpeed) e a inclusão no Google Imagens.</p>
    <ul>
        <li><strong>Dimensões Recomendadas:</strong> Formato padrão paisagem, preferencialmente 1200 x 630 px ou 851 x 315 px.</li>
        <li><strong>Extensão e Peso (Leveza):</strong> Utilize <code>.jpg</code> (padrão Canva) ou <code>.webp</code>. O teto absoluto de peso é 150 KB, sendo o <strong>ideal mantê-lo abaixo de 100 KB</strong>. Utilize compressores gratuitos como <em>TinyPNG</em> ou <em>Squoosh</em>.</li>
        <li><strong>SEO Obrigatório:</strong> O preenchimento do <strong>Alt Text</strong> (Texto Alternativo descrevendo a foto para robôs e deficientes visuais) e do <strong>Title</strong> é obrigatório para não sofrer punições nas métricas de varredura.</li>
    </ul>

    <h3>4. Atualização das Planilhas via CMS</h3>
    <p>O cliente detém autonomia fiscal plena. Para alterar as bases anuais das calculadoras, acesse o painel lateral em <em>Configurações do Sistema > Base de Dados da Calculadora</em>. Faça o upload da sua nova planilha <code>.xlsx</code> (editada conforme as regras do Pilar 3) e salve. A infraestrutura da Cloudflare realizará a recompilação automática do código instantaneamente.</p>

    <div class="page-break"></div>

    <!-- PILAR 5 -->
    <h2 id="pilar5">Pilar 5: Governança, SEO e Eficiência Workspace</h2>

    <h3>1. Engenharia Externa e Resgate</h3>
    <p>Promovemos a assepsia completa do patrimônio digital da Contabilidade Camilo. Executamos pesquisa Whois e garantimos o resgate definitivo da titularidade no <strong>Registro.br</strong>. Na sequência, delegamos os apontamentos de DNS para a <strong>Cloudflare</strong>. Essa migração garantiu blindagem cibernética avançada, permitiu a estruturação profissional dos registros de e-mail (SPF, DKIM, DMARC) e certificou que todas as contas nasceram exclusivamente sob a titularidade primária da Contabilidade, extinguindo vínculos de dependência com agências e servidores de terceiros.</p>

    <h3>2. Esteira de SEO (Automatizada)</h3>
    <p>O rastreamento do portal é orquestrado por scripts inteligentes:</p>
    <ul>
        <li><strong>O motor build.js:</strong> A cada artigo, o script intercepta a pasta do repositório, valida se as datas já passaram, filtra os arquivos válidos e cospe um mapa atualizado <code>sitemap.xml</code> com tags <code>&lt;lastmod&gt;</code> irretocáveis.</li>
        <li>O arquivo estrutural <code>robots.txt</code> orienta o crawler (aranha do motor de busca) para o índice XML.</li>
        <li>Realizamos a submissão ativa e validamos a Propriedade do Domínio no <strong>Google Search Console</strong>. As 21 páginas estratégicas do site encontram-se com o status "Processado".</li>
    </ul>

    <h3>3. Roadmap Operacional e Google Workspace</h3>
    <p>Realizamos a auditoria estratégica de licenciamento da Contabilidade Camilo mapeando a distribuição entre <code>@contabilidadecamilo.com.br</code> e <code>@bluebpofinanceiro.com.br</code>.</p>
    
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
                <td>Manter licença individual.</td>
            </tr>
            <tr>
                <td><code>thais@bluebpofinanceiro.com.br</code></td>
                <td>Titular / BPO</td>
                <td><strong>Duplicidade identificada.</strong> Operar como Alias.</td>
            </tr>
            <tr>
                <td><code>contato@contabilidadecamilo.com.br</code></td>
                <td>Atendimento Geral</td>
                <td>Caixa departamental (Histórico 11,5 GB). Manter.</td>
            </tr>
            <tr>
                <td><code>contato@bluebpofinanceiro.com.br</code></td>
                <td>Atendimento BPO</td>
                <td>Caixa departamental.</td>
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
                <td>Operacionais</td>
                <td>Avaliar agrupamento colaborativo ou unificação.</td>
            </tr>
        </tbody>
    </table>

    <div class="highlight-box">
        <strong>Plano de Eficiência e Comunicação (O Roadmap):</strong>
        <p><strong>Segurança e Sigilo:</strong> É inegociável que departamentos críticos (Diretoria/Thaís, Departamento Pessoal e Financeiro) mantenham suas contas individuais ativas, assegurando acesso individual via autenticação forte e isolamento de informações confidenciais em pastas privadas no Google Drive.</p>
        <p><strong>Comunicação Interna:</strong> Nestas contas individuais primárias, mantêm-se a estrutura corporativa de colaboração plena (ferramentas como Chat e Meet).</p>
        <p><strong>Eficiência Tática (O Corte):</strong> Visando a eliminação de redundâncias, recomendaremos a conversão sumária de caixas departamentais ociosas ou de baixo tráfego (como <code>arquivos@</code>, <code>financeiro@</code> e <code>fiscal2@</code>) em Aliases (apelidos) ou Grupos Colaborativos Gratuitos. Essa medida atua em convergência com o direcionamento do <strong>Cloudflare Email Routing</strong>, que fará a ponte sem custo dos e-mails do domínio secundário. Em resumo, esta reengenharia proporcionará a <strong>redução imediata de 3 a 5 licenças mensais (cobradas em dólar)</strong>, gerando altíssimo impacto financeiro na planilha da empresa, com absoluto zero atrito operacional.</p>
    </div>

    <div class="page-break"></div>

    <!-- ANEXO -->
    <h2 id="anexo">Anexo Oficial: Relação das Páginas do Portal</h2>
    <p>Para atestar a densidade orgânica de URLs cadastradas e auxiliar na governança de SEO a longo prazo, segue o sumário estrutural das páginas entregues, todas amparadas em sintaxe legível ao mapa do Google (Sitemap).</p>

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
        <strong>Engenharia de Template:</strong> A URL em questão opera como uma página-casca (template desacoplado). A inteligência desenvolvida lê o sufixo passado na URL (o ID), consome as entidades geradas de forma leve através da matriz <code>artigos.json</code> e realiza a construção reativa do conteúdo textual e imagético no navegador. Crucialmente, esse sistema injeta em tempo real as <strong>Tags Canônicas</strong> (Canonical Links) e meta descrições para resguardar as métricas de SEO, evitando terminantemente qualquer penalização punitiva por conteúdo duplicado por parte do algoritmo do Google.</li>
    </ul>

    <h3>Documentação Legal (LGPD)</h3>
    <ul>
        <li><code>politica-de-privacidade.html</code></li>
        <li><code>termos-de-uso.html</code></li>
    </ul>

    <div class="footer-assinatura">
        <p><strong>PandaRoSan IT Solutions © 2026 — Engenharia de Software de Elite, Automações e Presença Digital de Alta Performance.</strong></p>
    </div>

</div>

</body>
</html>
"""

with open("manual-pandarosan.html", "w", encoding="utf-8") as f:
    f.write(html_content)
