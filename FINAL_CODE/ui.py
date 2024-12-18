import tkinter as tk
from tkinter import ttk
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

class VoiceAssistantApp:
    def __init__(self, root):
        self.root = root
        self.root.title("MediVox")

        # Set background color
        self.root.configure(bg="#FEECE2")

        # Set frame size
        self.root.geometry("600x400")

        # Create main frame
        self.main_frame = tk.Frame(self.root, bg="#FEECE2")
        self.main_frame.grid(row=0, column=0, padx=100, pady=50, sticky="nsew")

        # Heading label
        self.heading_label = ttk.Label(self.main_frame, text="MediVox", font=('Helvetica', 50), background="#FEECE2")
        self.heading_label.grid(row=0, column=0, columnspan=3, pady=(30, 20))

        # Command label
        self.command_label = ttk.Label(self.main_frame, text="Command:", background="#FEECE2",font=('Helvetica', 20))
        self.command_label.grid(row=1, column=0, padx=(10, 5), pady=(10, 5), sticky="w")

        # Command entry
        self.command_entry = ttk.Entry(self.main_frame, width=50,font=('Helvetica', 15))
        self.command_entry.grid(row=1, column=1, padx=(0, 10), pady=(10, 5), sticky="w")

        # Listen button
        self.listen_button = ttk.Button(self.main_frame, text="Listen", command=self.listen)
        self.listen_button.grid(row=1, column=2, pady=(10, 5), sticky="w")

        # Response label
        self.response_label = ttk.Label(self.main_frame, text="Response:", background="#FEECE2",font=('Helvetica', 20))
        self.response_label.grid(row=2, column=0, padx=(10, 5), pady=(10, 5), sticky="w")

        # Response text area
        self.response_text = tk.Text(self.main_frame, width=50, height=7 ,font=('Helvetica', 15))
        self.response_text.grid(row=2, column=1, padx=(0, 10), pady=(10, 5), sticky="w")

        # Initialize the recognizer
        self.recognizer = sr.Recognizer()

        # Initialize the text-to-speech engine
        self.engine = pyttsx3.init()

        # Initialize NLTK components
        self.stop_words = set(stopwords.words('english'))
        self.lemmatizer = WordNetLemmatizer()

        # Load intents from JSON file
        with open("intents.json") as f:
            self.intents = json.load(f)

    def preprocess_text(self, text):
        tokens = word_tokenize(text.lower())  
        tokens = [self.lemmatizer.lemmatize(token) for token in tokens if token.isalnum()]  
        tokens = [token for token in tokens if token not in self.stop_words]  
        return ' '.join(tokens)

    def listen(self):
        with sr.Microphone() as source:
            self.command_entry.delete(0, tk.END)
            self.command_entry.insert(0, "Listening...")
            self.command_entry.update_idletasks()
            self.recognizer.adjust_for_ambient_noise(source)
            audio = self.recognizer.listen(source)

        try:
            self.command_entry.delete(0, tk.END)
            self.command_entry.insert(0, "Recognizing...")
            self.command_entry.update_idletasks()
            command = self.recognizer.recognize_google(audio)
            self.command_entry.delete(0, tk.END)
            self.command_entry.insert(0, command)
            self.command_entry.update_idletasks()
            self.process_command(command)
        except sr.UnknownValueError:
            self.command_entry.delete(0, tk.END)
            self.command_entry.insert(0, "Sorry, I didn't get that.")
        except sr.RequestError:
            self.command_entry.delete(0, tk.END)
            self.command_entry.insert(0, "Sorry, could not request results. Check your internet connection.")

    def speak(self, text):
        self.engine.say(text)
        self.engine.runAndWait()

    def process_command(self, command):
        command = self.preprocess_text(command)
        max_similarity = 0
        best_response = None
        for intent in self.intents["intents"]:
            for pattern in intent["patterns"]:
                pattern = self.preprocess_text(pattern)
                tfidf_vectorizer = TfidfVectorizer()
                tfidf_matrix = tfidf_vectorizer.fit_transform([command, pattern])
                similarity = cosine_similarity(tfidf_matrix)[0][1]
                if similarity > max_similarity:
                    max_similarity = similarity
                    best_response = random.choice(intent["responses"])
        if max_similarity > 0.5:  # Threshold for similarity
            self.response_text.delete(1.0, tk.END)
            self.response_text.insert(tk.END, best_response)
            self.response_text.update_idletasks()
            self.speak(best_response)
        else:
            self.response_text.delete(1.0, tk.END)
            self.response_text.insert(tk.END, "Sorry, I didn't understand that command.")
            self.response_text.update_idletasks()
            self.speak("Sorry, I didn't understand that command.")

if __name__ == "__main__":
    root = tk.Tk()
    app = VoiceAssistantApp(root)
    root.mainloop()
