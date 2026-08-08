# Módulo 1: O Blog Sem Banco de Dados (Arquitetura Serverless com Markdown)

## 📌 Finalidade
Em um ambiente onde a premissa máxima é **soberania, custo zero de hospedagem e ausência de banco de dados tradicional** (MySQL, Postgres), precisamos de uma forma de gerenciar e renderizar postagens de blog em tempo real sem servidor (Serverless).

Para isso, usamos o **Decap CMS** para que o usuário redija artigos visualmente, e os salvamos como arquivos de texto (Markdown - `.md`). Em seguida, um script intercepta esses arquivos e os compila para que o site os leia com velocidade extrema.

---

## 🛠️ Roteiro de Utilização (Para o Usuário Humano)
1. **Redação:** O usuário entra no painel do Decap CMS (`/admin`), clica em "Novo Artigo" e preenche Título, Resumo e Corpo do texto.
2. **Salvamento (Commit Automático):** Ao clicar em *Publicar*, o CMS não salva em um banco de dados, mas sim cria um arquivo físico (ex: `artigos/meu-post.md`) direto no repositório GitHub.
3. **Mágica da Cloudflare:** O GitHub avisa a Cloudflare Pages. A Cloudflare roda o comando de Build.
4. **O Site no Ar:** Em menos de 2 minutos, o script converte aquele texto em dados consumíveis e o site exibe o post novo.

---

## ⚙️ A Mágica (Código e Engenharia para a IA)

A genialidade desta solução reside no arquivo `build.js` que roda exclusivamente durante o deploy na Cloudflare.

Ele lê todos os arquivos `.md` da pasta `/artigos`, extrai o cabeçalho (Frontmatter) e o conteúdo, e constrói um grande arquivo `artigos.json`. O front-end do site faz um `fetch('/artigos.json')` no carregamento e monta a tela de notícias instantaneamente.

### O Código de Build (O Coração da Rotina)
```javascript
import fs from 'fs';
import path from 'path';
import { fileURLToPath } from 'url';

const __filename = fileURLToPath(import.meta.url);
const __dirname = path.dirname(__filename);
const artigosDir = path.join(__dirname, 'artigos');
const outputFile = path.join(__dirname, 'artigos.json');

if (!fs.existsSync(artigosDir)) {
  fs.mkdirSync(artigosDir);
}

const files = fs.readdirSync(artigosDir).filter(f => f.endsWith('.md'));

const artigosLista = files.map(file => {
  const content = fs.readFileSync(path.join(artigosDir, file), 'utf8');
  
  // Regex para separar o Frontmatter (YAML) do Corpo (Markdown)
  const match = content.match(/^---\r?\n([\s\S]*?)\r?\n---\r?\n([\s\S]*)/);
  if (!match) return null;
  
  const frontmatter = match[1];
  const body = match[2].trim();
  
  // Função helper para extrair valores YAML manualmente sem dependências externas
  const getValue = (key) => {
    const regex = new RegExp(`^${key}:\\s*([\\s\\S]*?)(?=\\n\\w+:)`, 'm');
    const m = (frontmatter + '\n__END__:').match(regex);
    if (m) {
      let val = m[1].trim().replace(/\r?\n\s*/g, ' ');
      if ((val.startsWith('"') && val.endsWith('"')) || (val.startsWith("'") && val.endsWith("'"))) {
        val = val.slice(1, -1);
      }
      return val.trim();
    }
    return '';
  };

  const articleData = {
    title: getValue('title'),
    category: getValue('category'),
    date: getValue('date'),
    image: getValue('image'),
    summary: getValue('summary'),
    slug: getValue('slug') || file.replace('.md', ''),
    body: body
  };
  
  return articleData;
}).filter(a => a !== null);

// Ordena os artigos do mais recente para o mais antigo
artigosLista.sort((a, b) => new Date(b.date) - new Date(a.date));

// Salva o JSON final para consumo do Frontend
fs.writeFileSync(outputFile, JSON.stringify({ artigos_lista: artigosLista }, null, 2));
```

### Por que isso é incrível?
1. **Velocidade (CDN):** O JSON vira um arquivo estático distribuído em todos os servidores da Cloudflare no mundo (cache infinito).
2. **Independência:** Não há custo com AWS RDS, Vercel ou Supabase. A hospedagem e o "banco de dados" custam R$ 0,00.
