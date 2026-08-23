const fs = require('fs');

let html = fs.readFileSync('index.html', 'utf8');

// 4.1 Remover item [13. Guia DAS (Documento de Arrecadação do Simples)]
// We need to find the accordion item for 13. Guia DAS and remove it.
const regexGuia = /<div class="accordion-item">[\s\S]*?<span class="accordion-title">13\. Guia DAS \(Documento de Arrecadação do Simples\)<\/span>[\s\S]*?<\/div>\s*<\/div>/g;
html = html.replace(regexGuia, '');

// 4.2 Retirar a numeração dos títulos
// Example: <span class="accordion-title">1. Microempreendedor Individual (MEI)</span>
// Regex to match <span class="accordion-title"> followed by digits and dot and space
const regexNum = /(<span class="accordion-title">)\d+\.\s+/g;
html = html.replace(regexNum, '$1');

fs.writeFileSync('index.html', html);
console.log('Fixed index.html');
