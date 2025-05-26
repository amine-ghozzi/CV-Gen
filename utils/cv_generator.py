import openai

def generate_adapted_cv(cv_data, job_description):
    """
    Génère un CV adapté à l'offre d'emploi en utilisant l'API OpenAI
    """
    try:
        # Préparation du prompt pour l'API OpenAI
        prompt = f"""
        CV original:
        Nom: {cv_data['full_name']}
        Email: {cv_data['email']}
        Téléphone: {cv_data['phone']}
        
        Expérience:
        {cv_data['experience']}
        
        Formation:
        {cv_data['education']}
        
        Compétences:
        {cv_data['skills']}
        
        Offre d'emploi:
        {job_description}
        
        Veuillez adapter ce CV pour qu'il corresponde parfaitement à l'offre d'emploi.
        Mettez en avant les compétences et expériences pertinentes.
        Réorganisez le contenu si nécessaire.
        """
        
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "Vous êtes un expert en recrutement et en rédaction de CV. Adaptez le CV pour qu'il corresponde parfaitement à l'offre d'emploi."},
                {"role": "user", "content": prompt}
            ]
        )
        
        return response.choices[0].message.content
    
    except Exception as e:
        raise Exception(f"Erreur lors de la génération du CV adapté: {str(e)}") 