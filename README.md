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
- Un compte Azure (pour le déploiement)

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
SECRET_KEY=votre_clé_secrète_ici
```

## Déploiement sur Azure

1. Installez l'Azure CLI et connectez-vous :
```bash
az login
```

2. Créez un groupe de ressources :
```bash
az group create --name cv-generator-rg --location westeurope
```

3. Créez un plan App Service :
```bash
az appservice plan create --name cv-generator-plan --resource-group cv-generator-rg --sku B1 --is-linux
```

4. Créez l'application web :
```bash
az webapp create --name cv-generator-app --resource-group cv-generator-rg --plan cv-generator-plan --runtime "PYTHON|3.9"
```

5. Configurez les variables d'environnement :
```bash
az webapp config appsettings set --name cv-generator-app --resource-group cv-generator-rg --settings OPENAI_API_KEY="votre_clé_api_ici" SECRET_KEY="votre_clé_secrète_ici"
```

6. Déployez l'application :
```bash
az webapp deployment source config-local-git --name cv-generator-app --resource-group cv-generator-rg
git remote add azure <URL_GIT_AZURE>
git push azure master
```

## Utilisation

1. Démarrez l'application localement :
```bash
python app.py
```

2. Accédez à l'application :
   - En local : `http://localhost:5000`
   - Sur Azure : `https://cv-generator-app.azurewebsites.net`

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
├── runtime.txt        # Version de Python
├── web.config         # Configuration IIS
├── .env              # Variables d'environnement
├── templates/        # Templates HTML
│   └── index.html
└── utils/           # Utilitaires
    ├── cv_parser.py
    ├── job_parser.py
    └── cv_generator.py
```

## Contribution

Les contributions sont les bienvenues ! N'hésitez pas à ouvrir une issue ou à soumettre une pull request.

## Licence

Ce projet est sous licence MIT. Voir le fichier `LICENSE` pour plus de détails. 