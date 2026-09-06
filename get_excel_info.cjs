const xlsx = require('xlsx');
const fs = require('fs');

const files = fs.readdirSync('out').filter(f => f.endsWith('.xlsx'));
for (const file of files) {
    const wb = xlsx.readFile(`out/${file}`);
    console.log(`File: ${file}`);
    console.log(`Tabs: ${wb.SheetNames.join(', ')}`);
    for (const sheetName of wb.SheetNames) {
        const sheet = wb.Sheets[sheetName];
        const range = xlsx.utils.decode_range(sheet['!ref']);
        const headers = [];
        for (let C = range.s.c; C <= range.e.c; ++C) {
            const cell = sheet[xlsx.utils.encode_cell({c: C, r: range.s.r})];
            if (cell && cell.v) headers.push(cell.v);
        }
        console.log(`  Tab '${sheetName}' Headers: ${headers.join(', ')}`);
    }
    console.log('-'.repeat(40));
}
