from flask import Flask, render_template, request, jsonify
from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField
from wtforms.validators import DataRequired
import os
from dotenv import load_dotenv
import openai
from utils.cv_parser import parse_cv
from utils.job_parser import extract_job_description
from utils.cv_generator import generate_adapted_cv

load_dotenv()

app = Flask(__name__)
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY', os.urandom(24))
openai.api_key = os.getenv('OPENAI_API_KEY')

class CVForm(FlaskForm):
    full_name = StringField('Nom complet', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired()])
    phone = StringField('Téléphone')
    experience = TextAreaField('Expérience professionnelle', validators=[DataRequired()])
    education = TextAreaField('Formation', validators=[DataRequired()])
    skills = TextAreaField('Compétences', validators=[DataRequired()])
    submit = SubmitField('Générer CV')

@app.route('/')
def index():
    form = CVForm()
    return render_template('index.html', form=form)

@app.route('/upload', methods=['POST'])
def upload_cv():
    if 'cv_file' not in request.files:
        return jsonify({'error': 'Aucun fichier n\'a été envoyé'}), 400
    
    file = request.files['cv_file']
    if file.filename == '':
        return jsonify({'error': 'Aucun fichier sélectionné'}), 400

    cv_data = parse_cv(file)
    return jsonify(cv_data)

@app.route('/extract-job', methods=['POST'])
def extract_job():
    url = request.json.get('url')
    if not url:
        return jsonify({'error': 'URL non fournie'}), 400

    job_description = extract_job_description(url)
    return jsonify({'job_description': job_description})

@app.route('/generate-cv', methods=['POST'])
def generate_cv():
    cv_data = request.json.get('cv_data')
    job_description = request.json.get('job_description')
    
    if not cv_data or not job_description:
        return jsonify({'error': 'Données manquantes'}), 400

    adapted_cv = generate_adapted_cv(cv_data, job_description)
    return jsonify({'adapted_cv': adapted_cv})

if __name__ == '__main__':
    port = int(os.getenv('PORT', 5000))
    app.run(host='0.0.0.0', port=port) 