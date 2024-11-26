import os
import base64
from flask import Flask, request, render_template, session
from werkzeug.utils import secure_filename
from openai import OpenAI
from flask import jsonify
import io
import pyttsx3


# Initialize OpenAI client
client = OpenAI(api_key='XXX')

# Configuration des dossiers et types de fichiers autorisés pour l'upload
UPLOAD_FOLDER = 'uploads'
AUDIO_FOLDER = 'audio'  # Dossier pour les fichiers audio
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}

app = Flask(__name__)
app.secret_key = os.urandom(24)  # Utilisé pour la gestion des sessions

# Assurez-vous que le dossier de téléchargement existe
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

# Créez le dossier pour les fichiers audio si nécessaire
if not os.path.exists(AUDIO_FOLDER):
    os.makedirs(AUDIO_FOLDER)

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['AUDIO_FOLDER'] = AUDIO_FOLDER

# Fonction pour vérifier si le fichier a une extension autorisée
def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

# Fonction pour encoder une image en base64
def encode_image_to_base64(image_path):
    try:
        with open(image_path, "rb") as image_file:
            return base64.b64encode(image_file.read()).decode('utf-8')
    except Exception as e:
        print(f"Erreur lors de l'encodage de l'image : {e}")
        return None

# Fonction pour envoyer l'image encodée en base64 à l'API OpenAI et récupérer une description
def image_to_description_with_openai(image_path):
    try:
        print("Encodage de l'image en base64...")
        base64_image = encode_image_to_base64(image_path)

        if not base64_image:
            return "Erreur lors de l'encodage de l'image."

        print("Envoi de l'image encodée à OpenAI pour analyse...")
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {
                    "role": "user",
                    "content": [
                        {"type": "text", "text": "What's in this image? If there is some text, write the full transcript, keeping the same language."},
                        {
                            "type": "image_url",
                            "image_url": {
                                "url": f"data:image/jpeg;base64,{base64_image}"
                            },
                        },
                    ],
                }
            ],
            max_tokens=300,
        )

        # Récupération de la description générée
        description = response.choices[0].message.content
        print(f"Description extraite par OpenAI : {description}")
        return description
    except Exception as e:
        print(f"Erreur avec l'API OpenAI : {e}")
        return "Une erreur est survenue lors de l'analyse de l'image."

# Fonction pour analyser et traduire la description de l'image
def analyze_and_translate_image(image_path, target_language="en"):
    # Étape 1 : Envoyer l'image locale encodée à OpenAI pour une description
    description = image_to_description_with_openai(image_path)
    if not description or "Erreur" in description:
        return description

    # Étape 2 : Préparer une requête pour le LLM (traduction)
    prompt = (
        f"La description suivante a été générée à partir d'une image :\n\n"
        f"\"{description}\"\n\n"
        f"Veuillez résumer les informations clefs de cette description en {target_language}. Utilise un language simple et naturel, avec les infos clefs."
    )

    # Étape 3 : Envoyer la requête au LLM pour traduction
    try:
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": "You are a helpful translator and text clarification assistant."},
                {"role": "user", "content": prompt}
            ],
            max_tokens=300,
            temperature=0.7,
        )
        translation_result = response.choices[0].message.content
        return translation_result
    except Exception as e:
        print(f"Erreur lors de l'appel à l'API OpenAI : {e}")
        return "Erreur lors de la traduction de la description."

# Fonction TTS (Text-to-Speech)
def text_to_speech(text, filename):
    engine = pyttsx3.init()
    # Configurer la voix française si disponible
    voices = engine.getProperty('voices')
    french_voice = None
    for voice in voices:
        if 'french' in voice.name.lower():
            french_voice = voice.id
            break
    
    if french_voice:
        engine.setProperty('voice', french_voice)
    
    # Chemin complet pour sauvegarder le fichier audio
    full_path = os.path.join(AUDIO_FOLDER, filename)
    
    # Générer le fichier audio
    engine.save_to_file(text, full_path)
    engine.runAndWait()
    
    return f'/static/audio/{filename}'  # URL pour accéder au fichier audio

# Route pour afficher le formulaire HTML
@app.route('/')
def index():
    # Si la session n'a pas de message thread, on l'initialise
    if 'messages' not in session:
        session['messages'] = []

    return render_template('final-improved.html', messages=session['messages'])

# Route pour générer et retourner le fichier audio TTS
@app.route('/generate_audio', methods=['POST'])
def generate_audio():
    text = request.form.get('text')
    if not text:
        return jsonify({"error": "No text provided"}), 400

    # Générer un nom de fichier audio unique
    filename = "tts_output.mp3"  # Vous pouvez personnaliser ce nom si nécessaire

    # Appeler la fonction text-to-speech
    audio_url = text_to_speech(text, filename)

    # Répondre avec l'URL du fichier audio généré
    return jsonify({"audio_url": audio_url})

# Route pour traiter l'upload d'image
@app.route('/upload', methods=['POST'])
def upload_file():
    if 'image' not in request.files:
        return "Aucun fichier sélectionné", 400

    file = request.files['image']

    if file.filename == '':
        return "Aucun fichier sélectionné", 400

    if file and allowed_file(file.filename):
        # Sécurisation du nom de fichier et sauvegarde
        filename = secure_filename(file.filename)
        file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(file_path)

        # Traitement de l'image et récupération de la description
        print(f"Traitement de l'image : {file_path}")
        description = analyze_and_translate_image(file_path)  # Analyse de l'image

        # Ajouter le message de l'utilisateur et la réponse du bot dans le thread
        session['messages'].append({'role': 'user', 'text': 'Image téléchargée.', 'filename': filename})
        session['messages'].append({'role': 'bot', 'text': description, 'filename': filename})
        session.modified = True

        return render_template('final-improved.html', messages=session['messages'])
    else:
        return "Fichier invalide. Veuillez télécharger une image.", 400

# Route for voice transcription
@app.route('/transcribe', methods=['POST'])
def transcribe_audio():
    if 'audio' not in request.files:
        return jsonify({"error": "No audio file"}), 400
    audio_file = request.files['audio']
    
    # Save the uploaded file
    audio_path = os.path.join(app.config['UPLOAD_FOLDER'], 'recording.webm')
    audio_file.save(audio_path)
    try:
        # Transcribe using OpenAI
        with open(audio_path, "rb") as audio_file:
            transcription = client.audio.transcriptions.create(
                model="whisper-1", 
                file=audio_file
            )
        
        # Remove temporary file
        os.remove(audio_path)
        return jsonify({"transcription": transcription.text})
    except Exception as e:
        print(f"Transcription error: {e}")
        return jsonify({"error": "Transcription failed"}), 500

# Route to handle text questions
@app.route('/ask', methods=['POST'])
def ask_question():
    question = request.form.get('question')
    
    try:
        # Use OpenAI to answer the question
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": question}
            ],
            max_tokens=300,
            temperature=0.7,
        )
        
        answer = response.choices[0].message.content
        
        # Update session messages
        session['messages'].append({
            'role': 'user', 
            'text': question
        })
        session['messages'].append({
            'role': 'bot', 
            'text': answer
        })
        session.modified = True
        return render_template('final-improved.html', messages=session['messages'])
    
    except Exception as e:
        print(f"Error processing question: {e}")
        return "An error occurred", 500


if __name__ == "__main__":
    app.run(debug=True)