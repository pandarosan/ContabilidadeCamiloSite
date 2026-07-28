# 📖 Manual Pedagógico de Operação, Publicação e SEO Orgânico
**Projeto:** Portal Corporativo Contabilidade Camilo  
**Versão:** 1.0 (Módulo Institucional & Central de Notícias e Artigos)  
**Objetivo:** Orientar sócios, equipe de atendimento, marketing e suporte técnico sobre o funcionamento autônomo do site, rotinas de publicação de artigos, boas práticas visuais e estratégias avançadas de posicionamento orgânico (SEO e Inteligência Artificial).

---

## 1. 🏗️ Visão Geral da Arquitetura (Jamstack Moderno)
O portal da **Contabilidade Camilo** foi projetado sob a moderna arquitetura **Jamstack** (Javascript, APIs e Markup estático). 
* **Velocidade Extrema:** Ao contrário de sites tradicionais (como WordPress mal configurado) que dependem de bancos de dados lentos e pesados, nossas páginas carregam em milissegundos.
* **Segurança Blindada:** Sem banco de dados exposto na web, o risco de invasões de servidores, injeção de SQL ou perda de dados contábeis é praticamente reduzido a zero.
* **Custo Zero de Licenças:** Toda a inteligência de filtragem, paginação e varredura de categorias é executada em tempo real no próprio navegador do cliente, sem necessidade de servidores pagos de banco de dados.

---

## 2. 📰 Módulo de Notícias & Artigos (O Motor Jamstack)

O módulo de blog e artigos foi concebido para ser uma **máquina contínua de atração e captação de leads**, combinando leitura ergonômica com conversão consultiva.

### 2.1. Varredura Automática de Categorias e Contagem
* **Como funciona:** O menu de filtros de categorias no topo da página `noticias-e-artigos.html` **não possui botões fixos ou programados manualmente no código**.
* **Inteligência em Tempo Real:** No instante em que a página carrega, nosso algoritmo faz uma varredura em todas as publicações na tela, lê o atributo de categoria de cada artigo, cataloga os temas exclusivos e calcula a quantidade exata de artigos para cada um.
* **Auto-Limpeza:** Se um novo artigo com a categoria `"Holding Familiar"` for publicado amanhã, o botão aparecerá no topo do site sozinho com a contagem `(1)`. Se todos os artigos de um tema forem excluídos, o botão desaparecerá automaticamente, impedindo categorias vazias ou links quebrados.

### 2.2. A Mágica do WhatsApp Dinâmico (CTA de Conversão)
Ao final de todo artigo individual (como no modelo `artigo-modelo.html`), há um box premium de atendimento consultivo com um botão de WhatsApp.
* **O Diferencial:** O botão não envia uma mensagem genérica! Nosso script lê em tempo real o título oficial do artigo (`<h1>`) na tela do visitante e monta um convite personalizado:
  > *"Olá! Li o artigo **'[Título Exato do Artigo Lido]'** no site de vocês e gostaria de conversar com um especialista para receber orientação técnica sobre este assunto."*
* **Benefício Comercial:** O contador ou atendente que receber a mensagem no WhatsApp saberá exatamente qual foi a dor fiscal ou tributária que motivou o contato do lead!

---

## 3. ✍️ Guia Prático de Publicação para o Cliente e Marketing

Para o cliente e sua agência de marketing, manter o site atualizado é simples, intuitivo e não requer conhecimentos de programação.

### 3.1. Como Publicar um Novo Artigo (Duas Abordagens)
1. **Abordagem A (Painel Administrativo Visual - CMS Gratuito):**
   * Através da integração com ferramentas modernas sem banco de dados (como *Decap CMS* ou *Netlify CMS*), o usuário acessa um link seguro na web (ex: `/admin`), digita seu login e senha e entra em um editor visual similar ao Word.
   * Basta clicar em *"Novo Artigo"*, digitar o título, escolher ou criar uma tag de categoria, fazer o upload da foto de capa e clicar em **"Publicar"**.
   * O próprio gerenciador gera o arquivo em plano de fundo e atualiza a central automaticamente.
2. **Abordagem B (Publicação Concierge / Equipe Técnica):**
   * O texto e a imagem são enviados para o suporte técnico ou agência, que duplica o modelo estático (`artigo-modelo.html`), insere as informações em 2 minutos e publica diretamente nos arquivos do servidor com máximo controle de qualidade e formatação.

### 3.2. 🎨 Diretrizes Oficiais para Imagens de Capa (Padrão Canva)
Para garantir que o site se mantenha sempre rápido, elegante e perfeito para compartilhamento em redes sociais, todas as imagens criadas (no Canva ou no Photoshop) devem seguir estas regras de ouro:

| Critério | Recomendação Oficial | Motivo Técnico / Benefício |
| :--- | :--- | :--- |
| **Formato do Arquivo** | `.jpg` ou `.webp` | Evitar `.png` em fotos complexas para não gerar arquivos pesados que deixam o site lento. |
| **Resolução Opção A** *(Recomendado)* | **1200 x 630 pixels** *(Proporção 1.91:1)* | **Padrão Universal Open Graph.** É a proporção exata exigida pelo WhatsApp, LinkedIn e Facebook para gerar miniaturas de link perfeitas. |
| **Resolução Opção B** | **851 x 315 pixels** *(Proporção ~2.7:1)* | Padrão Panorâmico (Capa de Facebook). Fica lindo na moldura de topo por ser horizontal e compacto na altura. |
| **Peso Máximo** | Até **150 KB** *(Ideal: abaixo de 100 KB)* | Garante nota 100 no Google PageSpeed e carregamento instantâneo em redes móveis 4G/5G. |
| **Comportamento Visual** | `object-fit: cover; border-radius: 20px;` | O site possui proteção CSS nativa: ele enquadra e corta suavemente as bordas da imagem para preencher a moldura sem **nunca achatar ou distorcer** a foto. |

### 3.3. ❓ Por que o link não mostra pré-visualização no LinkedIn durante o desenvolvimento?
* Quando clicamos no botão **"in LinkedIn"** em ambiente local (`localhost:3000`), a caixa de postagem do LinkedIn pode abrir em branco.
* **Explicação:** Os robôs de varredura do LinkedIn e do WhatsApp ficam em servidores externos (nos EUA) e precisam acessar o link pela internet pública para ler as *Meta Tags* da foto e do título. Como o endereço local (`localhost`) só existe dentro do computador de teste, o robô não consegue acessar a página (erro 404), descartando o link como proteção anti-spam.
* **Garantia:** Nosso código já possui o pacote completo de meta tags **Open Graph (`og:title`, `og:image`, `og:url`)**. Assim que o site for publicado ao vivo no domínio oficial do escritório, os cards aparecerão instantaneamente em todas as redes sociais!

### 3.4. 🔐 Governança, LOGs e Rastreabilidade de Usuários
A arquitetura Jamstack com Decap CMS oferece um nível de governança e segurança infinitamente superior aos painéis tradicionais (como WordPress), graças à sua integração nativa com o **GitHub** (o maior sistema de versionamento de código do mundo).
* **LOG Indestrutível:** O "Administrador Master" (Agência/TI) possui acesso ao painel do GitHub, onde **absolutamente toda ação é registrada permanentemente**.
* **Rastreabilidade Exata:** Cada vez que qualquer usuário clica em "Publicar", "Editar" ou "Excluir" no painel do Decap CMS, um *Commit* (Registro Oficial) é criado. Esse registro mostra exatamente **QUEM** foi o usuário (e-mail), **A HORA E O SEGUNDO** exatos da ação, e **QUAL ARQUIVO/TEXTO** foi alterado.
* **Proteção Anti-Deleção (Rollback):** Como o histórico é gravado no GitHub, se um usuário deletar um artigo acidentalmente (ou maliciosamente), nada é perdido. O Administrador Master consegue acessar o histórico e restaurar a versão do site de 5 minutos atrás com apenas 1 clique, garantindo proteção total contra perda de dados.

---

## 4. ⚙️ Automações Inteligentes do Site

### 4.1. Contagem de Anos de Experiência Automática
* O escritório **nunca precisará alterar manualmente** o texto "há mais de 17 anos oferecendo soluções..." na Home, Rodapé, Sobre Nós ou nos Artigos!
* **A Tecnologia:** Injetamos a classe CSS `.anos-experiencia` em todos os locais onde o tempo de fundação é mencionado. O nosso arquivo Javascript central (`main.js`) calcula automaticamente o ano atual do sistema menos o ano de fundação (2009).
* Em 2026, o site exibirá **17 anos**. Em 1º de janeiro de 2027, o site mudará sozinho para **18 anos**, em 2028 para **19 anos**, e assim sucessivamente!

---

## 5. 🚀 Estratégia de SEO Orgânico e Ranqueamento no Google & IAs

A estrutura técnica do site foi desenhada não apenas para impressionar humanos, mas para ser tratada como autoridade máxima pelos algoritmos de busca e pelas Inteligências Artificiais generativas (Google Gemini, ChatGPT, Claude, Perplexity).

### 5.1. Autoridade Temática (Topical Authority)
O Google não ranqueia apenas "palavras isoladas"; ele busca **autoridade em ecossistemas de assunto**. 
* Ao publicar artigos segmentados nas categorias do nosso motor (`Simples Nacional`, `Tributário & Impostos`, `Trabalhista & eSocial`), o escritório demonstra aos robôs de busca um domínio completo sobre a legislação contábil.
* Quanto mais artigos publicamos dentro de uma mesma categoria, mais alta é a nota de confiança do site para aquele termo em Jundiaí e região.

### 5.2. Teia de Link Building Interno
* Em todas as publicações, orientamos que termos contábeis sejam hiperlinkados para as nossas páginas de especialidades.
* *Exemplo:* Se o artigo falar sobre redução de impostos, a expressão "planejamento tributário" deve ser um link apontando para `servicos-contabeis.html`.
* Isso distribui o "suco de autoridade" (Link Juice) do artigo para as páginas comerciais de fechamento de contrato!

### 5.3. Microdados Estruturados (Schema.org) e Visibilidade em IAs
* Em todo artigo, injetamos um bloco invisível para humanos chamado **JSON-LD Schema.org (`@type: Article` & `@type: Organization`)**.
* Ele entrega uma "identidade digital mastigada" para os motores de busca, informando quem escreveu (Contabilidade Camilo), o CRC oficial, a data de publicação e a imagem de capa.
* **Vantagem Competitiva em IA:** Quando um empresário pergunta ao ChatGPT ou ao Google Gemini *"Como funciona o sublimite do Simples Nacional em 2026?"*, as IAs dão prioridade absoluta na citação e recomendação de fontes que possuem dados estruturados limpos e código sem erros, como o nosso portal!

---

## 6. 🔜 Módulos Futuros (Em Construção)

### 6.1. Fase 3: Calculadoras Fisco-Tributárias Interativas
*(Esta seção será detalhada assim que implementarmos as calculadoras interativas para captação direta de empreendedores na próxima fase!)*

---
*Documentação elaborada pela equipe de engenharia e arquitetura de software contábil.*  
**Contabilidade Camilo — Inovação, Tradição e Excelência.**
