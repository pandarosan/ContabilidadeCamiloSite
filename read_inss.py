import zipfile, xml.etree.ElementTree as ET, sys
path = sys.argv[1]
with zipfile.ZipFile(path, 'r') as z:
    strings = [c.text for c in ET.fromstring(z.read('xl/sharedStrings.xml')).findall('.//{http://schemas.openxmlformats.org/spreadsheetml/2006/main}t')] if 'xl/sharedStrings.xml' in z.namelist() else []
    for s in z.namelist():
        if s.startswith('xl/worksheets/sheet'):
            print(f"--- {s} ---")
            for r in ET.fromstring(z.read(s)).findall('.//{http://schemas.openxmlformats.org/spreadsheetml/2006/main}row'):
                row = []
                for c in r.findall('.//{http://schemas.openxmlformats.org/spreadsheetml/2006/main}c'):
                    v = c.find('{http://schemas.openxmlformats.org/spreadsheetml/2006/main}v')
                    val = v.text if v is not None else ''
                    if c.get('t') == 's' and val.isdigit(): val = strings[int(val)]
                    row.append(val)
                print('\t'.join(row))
