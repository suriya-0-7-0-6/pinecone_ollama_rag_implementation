
from pathlib import Path
import pdfplumber
from bs4 import BeautifulSoup

def load_txt(path: Path) -> str:
    with path.open('r', encoding='utf-8', errors='ignore') as f:
        return f.read()
    
def load_pdf(path: Path) -> str:
    text_parts = []
    with pdfplumber.open(path) as pdf:
        i = 0
        for page in pdf.pages:
            text = page.extract_text()
            if text:
                text_parts.append(text)
    return '\n'.join(text_parts)

def load_html(path: Path) -> str:
    with path.open('r', encoding='utf-8', errors='ignore') as f:
        html = f.read()
    soup = BeautifulSoup(html, 'html.parser')

    for s in soup(['script', 'style']):
        s.decompose()

    return soup.get_text(separator='\n')


def load_file(path: Path) -> str:
    suffix = path.suffix.lower()
    if suffix == '.txt':
        return load_txt(path)
    elif suffix == '.pdf':
        return load_pdf(path)
    elif suffix in ['.html', '.htm']:
        return load_html(path)
    else:
        raise ValueError(f"Unsupported file type: {suffix}")
    
