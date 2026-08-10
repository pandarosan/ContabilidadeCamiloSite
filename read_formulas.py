import zipfile, xml.etree.ElementTree as ET

def read_xlsx_formulas(path):
    with zipfile.ZipFile(path, 'r') as z:
        strings = [c.text for c in ET.fromstring(z.read('xl/sharedStrings.xml')).findall('.//{http://schemas.openxmlformats.org/spreadsheetml/2006/main}t')] if 'xl/sharedStrings.xml' in z.namelist() else []
        for s in z.namelist():
            if s.startswith('xl/worksheets/sheet'):
                for r in ET.fromstring(z.read(s)).findall('.//{http://schemas.openxmlformats.org/spreadsheetml/2006/main}row'):
                    row = []
                    for c in r.findall('.//{http://schemas.openxmlformats.org/spreadsheetml/2006/main}c'):
                        v = c.find('{http://schemas.openxmlformats.org/spreadsheetml/2006/main}v')
                        f = c.find('{http://schemas.openxmlformats.org/spreadsheetml/2006/main}f')
                        val = v.text if v is not None else ''
                        form = f.text if f is not None else ''
                        if c.get('t') == 's' and val.isdigit(): val = strings[int(val)]
                        
                        cell_repr = f"[{val}]"
                        if form: cell_repr += f" (Formula: {form})"
                        row.append(cell_repr)
                    print('\t'.join(row))

read_xlsx_formulas('Planilha/Calculadora IR.xlsx')
