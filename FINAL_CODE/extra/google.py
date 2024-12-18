import os
import speech_recognition as sr
import pyttsx3

# Initialize the recognizer
recognizer = sr.Recognizer()

# Initialize the text-to-speech engine
engine = pyttsx3.init()

def listen():
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

    try:
        print("Recognizing...")
        # Use Google Speech Recognition to convert speech to text
        command = recognizer.recognize_google(audio)
        print("You said:", command)
        return command.lower()
    except sr.UnknownValueError:
        print("Sorry, I didn't get that.")
        return ""
    except sr.RequestError:
        print("Sorry, speech recognition service is unavailable.")
        return ""

def search_on_google(query):
    # You can perform the search operation here
    # For simplicity, let's just return the search query
    return f"Here are the search results for {query}"

def speak(text):
    engine.say(text)
    engine.runAndWait()

if __name__ == "__main__":
    speak("Hello! I am your voice assistant.")
    while True:
        command = listen()
        if command:
            search_results = search_on_google(command)
            speak("Let me search that for you on Google.")
            speak(search_results)
