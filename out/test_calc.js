const rbt12 = 5000;
const anexo = "I";
const aliquotasData = [
  { anexo: "I", rbt12_de: 0, rbt12_ate: 180000, aliquota: 0.04, parcela_deduzir: 0 },
  { anexo: "II", rbt12_de: 0, rbt12_ate: 180000, aliquota: 0.045, parcela_deduzir: 0 }
];
const faixaEncontrada = aliquotasData.find(row => row.anexo === anexo && rbt12 >= row.rbt12_de && rbt12 <= row.rbt12_ate);
let aliquotaEfetiva = ((rbt12 * faixaEncontrada.aliquota) - faixaEncontrada.parcela_deduzir) / rbt12;
console.log((aliquotaEfetiva * 100).toFixed(2).replace(".", ",") + "%");
