import fs from 'fs';
import path from 'path';
import { fileURLToPath } from 'url';

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
    summary: getValue('summary'),
    slug: getValue('slug'),
    body: body
  };
  
  // A mágica: Injeta o slug automaticamente baseado no nome do arquivo (se o usuário não preencheu)
  if (!articleData.slug || articleData.slug.trim() === '') {
    articleData.slug = file.replace('.md', '');
  }
  
  return articleData;
}).filter(a => a !== null);

// Helper para converter string de data (ISO ou BR) em objeto Date
function parseDateBR(dateStr) {
  if (!dateStr) return new Date(0);
  // Tenta parse nativo primeiro (para ISO 8601 como YYYY-MM-DD)
  let d = new Date(dateStr);
  if (!isNaN(d.getTime())) return d;
  
  // Tenta parse no formato DD/MM/YYYY HH:mm
  const m = dateStr.match(/^(\d{2})\/(\d{2})\/(\d{4})(?:\s+(\d{2}):(\d{2}))?/);
  if (m) {
    const day = parseInt(m[1], 10);
    const month = parseInt(m[2], 10) - 1;
    const year = parseInt(m[3], 10);
    const hour = m[4] ? parseInt(m[4], 10) : 0;
    const min = m[5] ? parseInt(m[5], 10) : 0;
    return new Date(year, month, day, hour, min);
  }
  return new Date(0);
}

// Ordenar do mais novo pro mais velho
artigosLista.sort((a, b) => parseDateBR(b.date) - parseDateBR(a.date));

const finalOutput = {
  artigos_lista: artigosLista
};

fs.writeFileSync(outputFile, JSON.stringify(finalOutput, null, 2));
console.log('Build de artigos completo usando Markdown!');


