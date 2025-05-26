import docx
from PyPDF2 import PdfReader
import io

def parse_cv(file):
    """
    Parse un fichier CV (Word ou PDF) et extrait les informations pertinentes
    """
    filename = file.filename.lower()
    
    if filename.endswith('.docx'):
        return parse_docx(file)
    elif filename.endswith('.pdf'):
        return parse_pdf(file)
    else:
        raise ValueError("Format de fichier non supporté. Utilisez .docx ou .pdf")

def parse_docx(file):
    """
    Parse un fichier Word (.docx)
    """
    doc = docx.Document(io.BytesIO(file.read()))
    text = '\n'.join([paragraph.text for paragraph in doc.paragraphs])
    return extract_cv_sections(text)

def parse_pdf(file):
    """
    Parse un fichier PDF
    """
    pdf = PdfReader(io.BytesIO(file.read()))
    text = ''
    for page in pdf.pages:
        text += page.extract_text() + '\n'
    return extract_cv_sections(text)

def extract_cv_sections(text):
    """
    Extrait les différentes sections d'un CV à partir du texte
    """
    # Utilisation de l'API OpenAI pour extraire les sections
    # Cette fonction sera implémentée avec l'API OpenAI
    # Pour l'instant, retournons un dictionnaire vide
    return {
        'full_name': '',
        'email': '',
        'phone': '',
        'experience': '',
        'education': '',
        'skills': ''
    } 