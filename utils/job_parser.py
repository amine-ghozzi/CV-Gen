import requests
from bs4 import BeautifulSoup
import openai

def extract_job_description(url):
    """
    Extrait le contenu d'une offre d'emploi depuis une URL
    """
    try:
        response = requests.get(url)
        response.raise_for_status()
        
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Suppression des éléments non pertinents
        for element in soup(['script', 'style', 'nav', 'footer', 'header']):
            element.decompose()
        
        # Extraction du texte principal
        text = soup.get_text(separator='\n', strip=True)
        
        # Utilisation de l'API OpenAI pour extraire les informations pertinentes
        return analyze_job_description(text)
    
    except Exception as e:
        raise Exception(f"Erreur lors de l'extraction de l'offre d'emploi: {str(e)}")

def analyze_job_description(text):
    """
    Analyse le texte de l'offre d'emploi avec l'API OpenAI
    """
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "Vous êtes un expert en analyse d'offres d'emploi. Extrayez les informations clés de l'offre."},
                {"role": "user", "content": f"Analysez cette offre d'emploi et extrayez les informations importantes :\n\n{text}"}
            ]
        )
        
        return response.choices[0].message.content
    
    except Exception as e:
        raise Exception(f"Erreur lors de l'analyse de l'offre d'emploi: {str(e)}") 