import speech_recognition as sr
import pyttsx3
import json
import random
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Initialize the recognizer
recognizer = sr.Recognizer()

# Initialize the text-to-speech engine
engine = pyttsx3.init()

# # Download NLTK resources -----Main Download----
# nltk.download('punkt')
# nltk.download('wordnet')
# nltk.download('stopwords')

# Initialize NLTK components
stop_words = set(stopwords.words('english'))
lemmatizer = WordNetLemmatizer()

def preprocess_text(text):
    tokens = word_tokenize(text.lower())  
    tokens = [lemmatizer.lemmatize(token) for token in tokens if token.isalnum()]  
    tokens = [token for token in tokens if token not in stop_words]  
    return ' '.join(tokens)

def listen():
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

    try:
        print("Recognizing...")
        command = recognizer.recognize_google(audio)
        print("You said:", command)
        return command.lower()
    except sr.UnknownValueError:
        print("Sorry, I didn't get that.")
        return ""
    except sr.RequestError:
        print("Sorry, could not request results. Check your internet connection.")
        return ""

def speak(text):
    engine.say(text)
    engine.runAndWait()

def process_command(command, intents):
    command = preprocess_text(command)
    max_similarity = 0
    best_response = None
    for intent in intents["intents"]:
        for pattern in intent["patterns"]:
            pattern = preprocess_text(pattern)
            tfidf_vectorizer = TfidfVectorizer()
            tfidf_matrix = tfidf_vectorizer.fit_transform([command, pattern])
            similarity = cosine_similarity(tfidf_matrix)[0][1]
            if similarity > max_similarity:
                max_similarity = similarity
                best_response = random.choice(intent["responses"])
    if max_similarity > 0.5:  # Threshold for similarity
        speak(best_response)
    else:
        speak("Sorry, I didn't understand that command.")

if __name__ == "__main__":
    speak("Hello! I am your voice assistant.")
    
    # Load intents from JSON file
    with open("intents.json") as f:
        intents = json.load(f)
        
    while True:
        command = listen()
        if command:
            process_command(command, intents)
