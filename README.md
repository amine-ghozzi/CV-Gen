# Générateur de CV Adapté

Une application web qui utilise l'IA pour adapter votre CV à une offre d'emploi spécifique.

## Fonctionnalités

- Extraction d'offres d'emploi depuis une URL
- Analyse et adaptation automatique du CV selon l'offre
- Support pour les fichiers Word et PDF
- Formulaire de saisie manuelle des informations
- Interface utilisateur moderne et intuitive

## Prérequis

- Python 3.7 ou supérieur
- pip (gestionnaire de paquets Python)
- Une clé API OpenAI

## Installation

1. Clonez ce dépôt :
```bash
git clone [URL_DU_REPO]
cd cv-generator
```

2. Créez un environnement virtuel et activez-le :
```bash
python -m venv venv
source venv/bin/activate  # Sur Windows : venv\Scripts\activate
```

3. Installez les dépendances :
```bash
pip install -r requirements.txt
```

4. Créez un fichier `.env` à la racine du projet et ajoutez votre clé API OpenAI :
```
OPENAI_API_KEY=votre_clé_api_ici
```

## Utilisation

1. Démarrez l'application :
```bash
python app.py
```

2. Ouvrez votre navigateur et accédez à `http://localhost:5000`

3. Vous pouvez :
   - Entrer l'URL d'une offre d'emploi
   - Télécharger votre CV existant (PDF ou Word)
   - Remplir le formulaire manuellement
   - Générer un CV adapté à l'offre

## Structure du projet

```
cv-generator/
├── app.py              # Application principale
├── requirements.txt    # Dépendances
├── .env               # Variables d'environnement
├── templates/         # Templates HTML
│   └── index.html
└── utils/            # Utilitaires
    ├── cv_parser.py
    ├── job_parser.py
    └── cv_generator.py
```

## Contribution

Les contributions sont les bienvenues ! N'hésitez pas à ouvrir une issue ou à soumettre une pull request.

## Licence

Ce projet est sous licence MIT. Voir le fichier `LICENSE` pour plus de détails. 