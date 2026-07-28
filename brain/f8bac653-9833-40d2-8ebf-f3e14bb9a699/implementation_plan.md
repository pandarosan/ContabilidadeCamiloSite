# Arquitetura Premium: Painel de Blog Profissional (Decap CMS)

Para resolvermos a interface pouco amigável e garantirmos uma experiência de ponta para o cliente, vamos reestruturar a conexão do CMS. O painel passará a exibir os artigos como "Cards" individuais em uma lista elegante, abandonando o formato de "formulário infinito".

## ⚠️ User Review Required
> [!IMPORTANT]
> **Ajustes de Infraestrutura na Netlify:** Para que essa interface elegante funcione, precisaremos adicionar um comando de Build na Netlify (`node build.js`). Isso garante que os artigos criados individualmente no painel sejam empacotados e entregues na velocidade da luz para a vitrine do site.

## Respostas aos seus pedidos:
1. **Calendário para Data:** O campo de data voltará com um calendário interativo (Datepicker). Ele virá preenchido com a data atual por padrão, mas o cliente poderá clicar e escolher datas futuras ou passadas sem precisar digitar nada!
2. **Slug (URL) Editável:** O campo "URL Amigável" será gerado automaticamente, mas continuará visível na tela para que o cliente possa encurtar ou alterar a URL do artigo se desejar.
3. **Tempo de Leitura:** Será 100% invisível no painel. O robô calculará sozinho no momento em que o visitante abrir a página.

---

## 🛠️ Proposed Changes

### 1. Painel de Administração (`admin/config.yml`)
#### [MODIFY] admin/config.yml
- Reverter a estrutura de `files` para `folder: "artigos"`.
- O CMS passará a salvar cada artigo como um arquivo `.json` individual (ex: `artigo-sobre-impostos.json`), gerando uma lista limpa no painel.
- Adição dos widgets corretos: `datetime` (com calendário) e `slug` (editável).

### 2. O Motor de Compilação (`build.js`)
#### [NEW] build.js
- Um script Node.js ultra-rápido que varrerá a pasta `artigos/`, pegará todos os arquivos `.json` individuais que o painel criou, e os unificará no arquivo `artigos.json` que a vitrine precisa ler. 
- *Ação necessária na Netlify:* Após eu enviar isso, você precisará ir na Netlify e colocar `node build.js` no campo "Build command".

### 3. Adaptação dos Artigos Originais
#### [MODIFY] artigos.json -> Pasta `artigos/`
- Os 6 artigos que criamos não serão perdidos! Eu vou dividi-los em 6 arquivos separados dentro da nova pasta `artigos/` para que eles apareçam perfeitamente no novo visual do painel.

### 4. Remoção do Tempo de Leitura Fixo (`noticias-e-artigos.html` e `artigo-modelo.html`)
#### [MODIFY] noticias-e-artigos.html
#### [MODIFY] artigo-modelo.html
- O script passará a calcular o tempo de leitura dinamicamente: `Math.ceil(quantidade_de_palavras / 200) + ' min de leitura'`.

## ✅ Verification Plan
1. Eu codificarei o `build.js` e separarei os 6 arquivos originais na pasta correta.
2. Atualizarei o `config.yml` para a interface "Folder" Premium.
3. Enviarei para o GitHub.
4. Você irá na Netlify, ajustará o comando de Build, e testaremos a nova interface perfeita no seu painel!
