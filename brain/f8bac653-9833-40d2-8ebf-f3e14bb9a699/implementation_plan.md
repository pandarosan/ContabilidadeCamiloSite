# Conexão do Motor Jamstack com o Banco de Dados JSON do Decap CMS

Para que o site consiga exibir magicamente o artigo 15 segundos após você clicar em "Publicar" no painel do Decap CMS, precisamos criar a "ponte" entre o painel e o site.

Atualmente, os cards do site são estáticos no HTML. O plano é transformarmos o site para ler um arquivo inteligente (`artigos.json`) gerenciado pelo painel.

## ⚠️ User Review Required
> [!IMPORTANT]
> **Mudança na Arquitetura do CMS:** Em vez de gerar vários arquivos soltos, o Decap CMS será configurado para salvar todos os artigos em um único "banco de dados estático" (`artigos.json`). O site lerá esse arquivo e gerará os cards e as páginas de leitura dinamicamente no navegador! Isso é o ápice do Jamstack moderno.

## 🛠️ Proposed Changes

### 1. Painel de Administração (`admin/config.yml`)
#### [MODIFY] admin/config.yml
- Mudar a `collection` de "folder" para "files".
- Configurar para salvar os dados em um arquivo único `artigos.json`.

### 2. A Vitrine de Artigos (`noticias-e-artigos.html`)
#### [MODIFY] noticias-e-artigos.html
- Remover os cards de artigos hardcoded no HTML.
- Adicionar um script `fetch('/artigos.json')` que lê os artigos publicados no CMS e gera o código HTML dos cards dinamicamente na tela.
- O link "Ler Artigo Completo" apontará para `artigo-modelo.html?id=[slug-do-artigo]`.

### 3. A Página de Leitura Dinâmica (`artigo-modelo.html`)
#### [MODIFY] artigo-modelo.html
- Remover os textos fixos.
- Adicionar um script que captura o ID do artigo na URL, faz o `fetch('/artigos.json')` e injeta o Título, a Foto de Capa, e converte o Corpo do Texto (Markdown) para HTML perfeitamente usando a biblioteca super leve `marked.js`.

## ✅ Verification Plan
1. Eu farei as modificações no código e farei um novo envio (Push) para o seu GitHub.
2. A Netlify publicará a nova versão automaticamente.
3. Você acessará o seu painel ao vivo, criará um artigo real chamado "Artigo Teste", clicará em Publicar, e ele aparecerá na vitrine principal instantaneamente!
