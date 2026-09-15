import fs from 'fs';
import path from 'path';
import { fileURLToPath } from 'url';
import XLSX from 'xlsx';

const __filename = fileURLToPath(import.meta.url);
const __dirname = path.dirname(__filename);

const artigosDir = path.join(__dirname, 'artigos');
const outputFile = path.join(__dirname, 'artigos.json');

// Criar pasta se não existir
if (!fs.existsSync(artigosDir)) {
  fs.mkdirSync(artigosDir);
}

const files = fs.readdirSync(artigosDir).filter(f => f.endsWith('.md'));

const artigosLista = files.map(file => {
  const content = fs.readFileSync(path.join(artigosDir, file), 'utf8');
  
  // Parse simples de Markdown + Frontmatter (suporta Windows CRLF e Linux LF)
  const match = content.match(/^---\r?\n([\s\S]*?)\r?\n---\r?\n([\s\S]*)/);
  if (!match) return null;
  
  const frontmatter = match[1] + '\n__END__:';
  const body = match[2].trim();
  
  const getValue = (key) => {
    // Regex que pega o valor da chave atual até encontrar a próxima chave ou o final do arquivo
    const regex = new RegExp(`^${key}:\\s*([\\s\\S]*?)(?=\\n\\w+:)`, 'm');
    const m = frontmatter.match(regex);
    if (m) {
      let val = m[1].trim();
      // Se for uma string multi-linha (folded YAML), remove as quebras de linha e espaços extras
      val = val.replace(/\r?\n\s*/g, ' ');
      // Remove aspas se existirem
      if (val.startsWith('"') && val.endsWith('"')) val = val.slice(1, -1);
      else if (val.startsWith("'") && val.endsWith("'")) val = val.slice(1, -1);
      return val.trim();
    }
    return '';
  };

  const articleData = {
    title: getValue('title'),
    category: getValue('category'),
    date: getValue('date'),
    image: getValue('image'),
    image_alt: getValue('image_alt'),
    image_title: getValue('image_title'),
    summary: getValue('summary'),
    slug: getValue('slug'),
    body: body
  };
  
  // A mágica: Injeta o slug automaticamente baseado no nome do arquivo (se o usuário não preencheu)
  if (!articleData.slug || articleData.slug.trim() === '') {
    articleData.slug = file.replace('.md', '');
  }
  
  return articleData;
}).filter(a => {
  if (a === null) return false;
  // Oculta artigos com data de publicação no futuro (Agendados)
  try {
    if (a.date && new Date(a.date).getTime() > new Date().getTime()) {
      return false;
    }
  } catch (e) {}
  return true;
});

// Ordenar do mais novo pro mais velho
artigosLista.sort((a, b) => new Date(b.date) - new Date(a.date));

const finalOutput = {
  artigos_lista: artigosLista
};

fs.writeFileSync(outputFile, JSON.stringify(finalOutput, null, 2));
console.log('Build de artigos completo usando Markdown!');

// ==========================================
// SEO: Geração de sitemap.xml e robots.txt
// ==========================================

const escapeXml = (unsafe) => {
    if (!unsafe) return '';
    return unsafe.replace(/[<>&'"]/g, (c) => {
        switch (c) {
            case '<': return '&lt;';
            case '>': return '&gt;';
            case '&': return '&amp;';
            case '\'': return '&apos;';
            case '"': return '&quot;';
        }
    });
};

const generateSitemap = () => {
    const baseUrl = 'https://contabilidadecamilo.com.br';
    const now = new Date().toISOString().split('T')[0];
    
    // Ler todos os arquivos HTML na raiz
    const ignoreFiles = ['demo.html', 'artigo-modelo.html'];
    const staticPages = fs.readdirSync(__dirname)
        .filter(f => f.endsWith('.html') && !ignoreFiles.includes(f))
        .map(f => f === 'index.html' ? '' : f); 

    let xml = `<?xml version="1.0" encoding="UTF-8"?>\n`;
    xml += `<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n`;

    // 1. Páginas estáticas
    staticPages.forEach(page => {
        const url = page === '' ? baseUrl + '/' : `${baseUrl}/${page}`;
        xml += `  <url>\n`;
        xml += `    <loc>${url}</loc>\n`;
        xml += `    <lastmod>${now}</lastmod>\n`;
        xml += `  </url>\n`;
    });

    // 2. Páginas dinâmicas (Artigos)
    artigosLista.forEach(article => {
        const url = `${baseUrl}/artigo.html?id=${article.slug}`;
        
        let articleDate = now;
        try {
            if (article.date) {
                articleDate = new Date(article.date).toISOString().split('T')[0];
            }
        } catch (e) {
            console.warn(`Data inválida para o artigo ${article.slug}`);
        }

        xml += `  <url>\n`;
        xml += `    <loc>${escapeXml(url)}</loc>\n`;
        xml += `    <lastmod>${articleDate}</lastmod>\n`;
        xml += `  </url>\n`;
    });

    xml += `</urlset>`;

    fs.writeFileSync(path.join(__dirname, 'sitemap.xml'), xml);
    console.log('sitemap.xml gerado com sucesso!');
};

const generateRobots = () => {
    const robotsContent = `User-agent: *\nAllow: /\n\nSitemap: https://contabilidadecamilo.com.br/sitemap.xml\n`;
    fs.writeFileSync(path.join(__dirname, 'robots.txt'), robotsContent);
    console.log('robots.txt gerado com sucesso!');
};

generateSitemap();
generateRobots();

// ==========================================
// ETAPA 3: Gera data/simples-anexo-iii.json
// Autonomia do cliente: o administrador atualiza
// calculadora-simples-nacional-configuracoes.xlsx no CMS
// e este build extrai apenas o Anexo III para um JSON
// leve (~250 bytes), sem custo de SheetJS no navegador.
// ==========================================

const gerarAnexoIII = () => {
  const planilhaPath = path.join(__dirname, 'public', 'calculadora-simples-nacional-configuracoes.xlsx');

  if (!fs.existsSync(planilhaPath)) {
    console.warn('AVISO: calculadora-simples-nacional-configuracoes.xlsx não encontrado. simples-anexo-iii.json não gerado.');
    return;
  }

  try {
    const workbook = XLSX.readFile(planilhaPath);
    const nomeAba = workbook.SheetNames.find(n => n.trim().toLowerCase() === 'tabelas_referencia');

    if (!nomeAba) {
      console.warn('AVISO: Aba "Tabelas_Referencia" não encontrada na planilha. simples-anexo-iii.json não gerado.');
      return;
    }

    const rows = XLSX.utils.sheet_to_json(workbook.Sheets[nomeAba], { defval: null });

    const anexoIII = rows
      .filter(r => String(r.Anexo || '').trim() === 'III')
      .map(r => ({
        rbt12_ate:       parseFloat(r.Limite),
        aliquota:        parseFloat(r.AliqNom),
        parcela_deduzir: parseFloat(r.Ded) || 0
      }))
      .filter(r => !isNaN(r.rbt12_ate) && !isNaN(r.aliquota));

    if (anexoIII.length === 0) {
      console.warn('AVISO: Nenhuma linha do Anexo III encontrada na planilha.');
      return;
    }

    const dataDir = path.join(__dirname, 'data');
    if (!fs.existsSync(dataDir)) fs.mkdirSync(dataDir);

    fs.writeFileSync(
      path.join(dataDir, 'simples-anexo-iii.json'),
      JSON.stringify(anexoIII, null, 2)
    );
    console.log(`simples-anexo-iii.json gerado com sucesso! (${anexoIII.length} faixas do Anexo III)`);
  } catch (err) {
    console.error('ERRO ao gerar simples-anexo-iii.json:', err.message);
  }
};

gerarAnexoIII();
