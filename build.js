const fs = require('fs');
const path = require('path');

const artigosDir = path.join(__dirname, 'artigos');
const outputFile = path.join(__dirname, 'artigos.json');

// Criar pasta se não existir
if (!fs.existsSync(artigosDir)) {
  fs.mkdirSync(artigosDir);
}

const files = fs.readdirSync(artigosDir).filter(f => f.endsWith('.json'));

const artigosLista = files.map(file => {
  const content = fs.readFileSync(path.join(artigosDir, file), 'utf8');
  return JSON.parse(content);
});

// Ordenar do mais novo pro mais velho
artigosLista.sort((a, b) => new Date(b.date) - new Date(a.date));

const finalOutput = {
  artigos_lista: artigosLista
};

fs.writeFileSync(outputFile, JSON.stringify(finalOutput, null, 2));
console.log('Build de artigos completo!');
