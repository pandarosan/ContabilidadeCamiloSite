import urllib.request
from bs4 import BeautifulSoup
import sys

def parse_url(url):
    req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    try:
        html = urllib.request.urlopen(req).read()
        soup = BeautifulSoup(html, 'html.parser')
        print(f"--- {url} ---")
        
        # Extract form inputs if any
        inputs = soup.find_all(['input', 'select', 'button'])
        if inputs:
            print("Inputs found:")
            for inp in inputs:
                label = ""
                if inp.has_attr('id'):
                    label_tag = soup.find('label', {'for': inp['id']})
                    if label_tag:
                        label = label_tag.text.strip()
                name = inp.get('name', '')
                type_ = inp.get('type', inp.name)
                placeholder = inp.get('placeholder', '')
                print(f" - {label} | {name} | {type_} | {placeholder}")
                
        # Extract headers to get an idea of the content
        headers = soup.find_all(['h1', 'h2', 'h3'])
        print("Headers:")
        for h in headers:
            print(" - " + h.text.strip())
            
    except Exception as e:
        print(f"Error parsing {url}: {e}")

parse_url("https://investnews.com.br/ferramentas/calculadoras/calculadora-inss/")
parse_url("https://www.contabilizei.com.br/calculadora-salario-liquido/")
