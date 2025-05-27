@echo off
echo Deploying Python application...

:: Créer l'environnement virtuel s'il n'existe pas
IF NOT EXIST "%DEPLOYMENT_TARGET%\env" (
    echo Creating virtual environment...
    python -m venv "%DEPLOYMENT_TARGET%\env"
)

:: Activer l'environnement virtuel
call "%DEPLOYMENT_TARGET%\env\Scripts\activate.bat"

:: Installer les dépendances
echo Installing dependencies...
pip install -r requirements.txt

:: Copier les fichiers
echo Copying files...
xcopy /Y /E /I /Q "%DEPLOYMENT_SOURCE%" "%DEPLOYMENT_TARGET%"

:: Démarrer l'application
echo Starting application...
cd "%DEPLOYMENT_TARGET%"
python app.py 