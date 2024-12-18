import threading
import speech_recognition
import pyttsx3 as tts
from neuralintents import BasicAssistant

class Assistant:
    def __init__(self):
        self.recognizer = speech_recognition.Recognizer()
        self.speaker = tts.init()
        self.speaker.setProperty("rate", 150)
        self.assistant = BasicAssistant("intents.json")
        threading.Thread(target=self.run_assistant).start()

    def run_assistant(self):
        while True:
            try:
                with speech_recognition.Microphone() as mic:
                    print("Listening...")
                    self.recognizer.adjust_for_ambient_noise(mic, duration=0.2)
                    audio = self.recognizer.listen(mic)
                    text = self.recognizer.recognize_google(audio).lower()
                    print("User:", text)
                    if "stop" in text:
                        self.speaker.say("Goodbye!")
                        self.speaker.runAndWait()
                        return
                    else:
                        response = self.assistant.request(text)
                        if response:
                            print("Assistant:", response)
                            self.speaker.say(response)
                            self.speaker.runAndWait()
            except speech_recognition.UnknownValueError:
                print("Could not understand audio.")
            except speech_recognition.RequestError:
                print("Recognition request failed.")
            except KeyboardInterrupt:
                print("Assistant stopped by user.")
                return
            except Exception as e:
                print("An error occurred:", e)

Assistant()
