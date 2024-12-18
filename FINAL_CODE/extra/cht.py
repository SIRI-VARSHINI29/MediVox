import speech_recognition as sr
import pyttsx3
import json

# Initialize the recognizer
recognizer = sr.Recognizer()

# Initialize the text-to-speech engine
engine = pyttsx3.init()

# Load commands from JSON file
with open("command.json") as f:
    commands_data = json.load(f)

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
        print("Sorry, could not request results. Check your internet connection.")
        return ""

def speak(text):
    engine.say(text)
    engine.runAndWait()

def process_command(command):
    response = commands_data.get(command)
    if response:
        speak(response)
    else:
        speak("Sorry, I didn't understand that command.")

if __name__ == "__main__":
    speak("Hello! I am your voice assistant.")
    while True:
        command = listen()
        if command:
            process_command(command)
