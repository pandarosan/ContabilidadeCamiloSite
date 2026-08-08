# Módulo 3: Protocolo OAuth Nativo (O Fim do Netlify)

## 📌 Finalidade
A autenticação padrão do Decap CMS é baseada no Netlify Identity ou Netlify Gateway, ambos provedores com forte *vendor lock-in* e dependentes de serviços fora do nosso controle.
Quando abdicamos do Netlify e construímos nossa arquitetura 100% no GitHub + Cloudflare Pages, precisamos de um Auth Server próprio para fazer a ponte de login OAuth (Cliente -> Servidor -> GitHub).
Este módulo explica como contornar os pesados bloqueios de segurança do navegador (Chrome COOP/COEP) usando a solução definitiva em duas etapas.

---

## 🛠️ Roteiro de Utilização (Para o Usuário Humano)
1. **Configuração Cloudflare:** Criamos um Cloudflare Worker genérico (ex: `cms-auth`).
2. **Configuração GitHub:** O usuário vai no GitHub Developer Settings, cria um OAuth App, cola a Client ID e a Secret no Cloudflare Worker, e coloca a URL do Worker como *Callback URL*.
3. **Configuração Decap:** No arquivo `admin/config.yml` do projeto, adicionamos:
```yaml
  name: github
  base_url: https://url-do-worker.workers.dev
  auth_endpoint: /auth
```
O login passa a ser invisível, soberano e 100% gratuito.

---

## ⚙️ A Mágica (Código e Engenharia para a IA)

O erro fatal de implementações antigas (ou gambiarras via `localStorage`) é que o Google Chrome destrói a variável `window.opener` se a janela popup do GitHub sofrer um redirecionamento de domínio (`Response.redirect()`) na volta para o site. Sem `window.opener`, a popup fica cega e não consegue entregar a chave OAuth para o painel principal do CMS.

### O Handshake em Duas Etapas (Solução Definitiva)
Para resolver isso, o Worker **não faz redirecionamento na rota de callback**. Ele renderiza o HTML final na própria URL do Worker. O Decap CMS escuta e faz o aperto de mãos.

### O Código do Worker (`worker.js`)
Copie e cole isso no seu Worker da Cloudflare:
```javascript
export default {
  async fetch(request, env) {
    const url = new URL(request.url);
    const client_id = env.GITHUB_CLIENT_ID;
    const client_secret = env.GITHUB_CLIENT_SECRET;

    // Rota 1: O CMS pede para iniciar o login
    if (url.pathname === "/auth") {
      const params = new URLSearchParams({
        client_id,
        scope: "repo,user",
      });
      return Response.redirect(
        "https://github.com/login/oauth/authorize?" + params.toString(),
        302
      );
    }

    // Rota 2: O GitHub devolve o código para trocarmos por Token
    if (url.pathname === "/callback") {
      const code = url.searchParams.get("code");
      if (!code) return new Response("Missing code", { status: 400 });

      const tokenResponse = await fetch("https://github.com/login/oauth/access_token", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
          Accept: "application/json",
          "User-Agent": "Cloudflare-Worker",
        },
        body: JSON.stringify({ client_id, client_secret, code }),
      });

      const tokenData = await tokenResponse.json();

      if (!tokenData.access_token) {
        const errorHtml = "<html><body><h2>Erro de Autenticacao</h2><p>GitHub recusou.</p></body></html>";
        return new Response(errorHtml, { status: 400, headers: { "Content-Type": "text/html" } });
      }

      const token = tokenData.access_token;
      
      // O Pulo do Gato: Não redirecione! Injete o código do protocolo Decap CMS Proxy:
      const html = `<!DOCTYPE html>
<html>
<head><title>Autorizando...</title></head>
<body>
<p>Autorizando Decap CMS...</p>
<script>
  const receiveMessage = (message) => {
    window.opener.postMessage(
      'authorization:github:success:' + JSON.stringify({ token: "${token}" }),
      message.origin
    );
    window.removeEventListener("message", receiveMessage, false);
  };
  window.addEventListener("message", receiveMessage, false);
  
  // O Handshake: Avisamos o CMS que estamos prontos para receber ordens
  window.opener.postMessage("authorizing:github", "*");
</script>
</body>
</html>`;

      return new Response(html, {
        headers: { "Content-Type": "text/html; charset=UTF-8" },
      });
    }

    return new Response("Decap CMS Auth Worker is running!", { status: 200 });
  }
};
```
