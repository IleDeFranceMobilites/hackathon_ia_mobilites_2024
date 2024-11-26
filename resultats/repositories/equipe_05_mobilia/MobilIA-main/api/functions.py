import os
import base64
from openai import OpenAI
import pyttsx3
from dotenv import load_dotenv
from .directions import DirectionsAPI
# Load environment variables
load_dotenv()

# Initialize OpenAI client
openAIClient = OpenAI(api_key=os.getenv('OPENAI_API_KEY'))



# Function to encode an image to base64
def encode_image_to_base64(image_path):
    """
    Encode an image file to a base64 string.
    """
    try:
        with open(image_path, "rb") as image_file:
            return base64.b64encode(image_file.read()).decode('utf-8')
    except Exception as e:
        print(f"Error encoding image: {e}")
        return None

# Function to analyze an image using OpenAI API
def analyze_image_with_openai(image_path):
    """
    Analyze an image using OpenAI's API and return a description.
    """
    base64_image = encode_image_to_base64(image_path)
    if not base64_image:
        return "Error encoding image."

    try:
        response = client.chat.completions.create(
            model="gpt-4o",
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
        description = response.choices[0].message.content
        return description
    except Exception as e:
        print(f"OpenAI API error: {e}")
        return "An error occurred while analyzing the image."

# Function to analyze and translate image description
def analyze_and_translate_image(image_path, target_language="en"):
    """
    Analyze an image using OpenAI and translate the description.
    """
    description = analyze_image_with_openai(image_path)
    if not description or "Error" in description:
        return description

    prompt = (
        f"The following description was generated from an image:\n\n"
        f"\"{description}\"\n\n"
        f"Please summarize the key information from this description in {target_language} using simple and natural language."
    )

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
        print(f"Error during translation: {e}")
        return "Error translating the description."

# Function for text-to-speech
def text_to_speech(text, filename, audio_folder='audio'):
    """
    Convert text to speech and save as an audio file.
    """
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    french_voice = None
    for voice in voices:
        if 'french' in voice.name.lower():
            french_voice = voice.id
            break
    if french_voice:
        engine.setProperty('voice', french_voice)
    else:
        engine.setProperty('voice', voices[0].id)
    
    if not os.path.exists(audio_folder):
        os.makedirs(audio_folder)

    full_path = os.path.join(audio_folder, filename)
    engine.save_to_file(text, full_path)
    engine.runAndWait()
    return full_path

# Function to transcribe audio using OpenAI API
def transcribe_audio_with_openai(audio_path):
    """
    Transcribe audio using OpenAI's Whisper model.
    """
    try:
        with open(audio_path, "rb") as audio_file:
            transcription = client.audio.transcriptions.create(
                model="whisper-1",
                file=audio_file
            )
        return transcription.text
    except Exception as e:
        print(f"Transcription error: {e}")
        return "Transcription failed."


