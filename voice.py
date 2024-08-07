import speech_recognition as sr
import pyttsx3
import webbrowser
from datetime import datetime

engine = pyttsx3.init()
engine.setProperty('rate', 150)
engine.setProperty('volume', 0.9)

def speak(text):
    engine.say(text)
    engine.runAndWait()

def listen():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio = recognizer.listen(source)
        try:
            command = recognizer.recognize_google(audio)
            print(f"You said: {command}")
            return command.lower()
        except sr.UnknownValueError:
            print("Sorry, I did not understand that.")
            return ""
        except sr.RequestError:
            print("Sorry, my speech service is down.")
            return ""

def tell_time():
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    speak(f"The current time is {current_time}")

def tell_date():
    today = datetime.today().strftime("%B %d, %Y")
    speak(f"Today's date is {today}")

def search_web(query):
    webbrowser.open(f"https://www.google.com/search?q={query}")
    speak("Here are the results I found on the web.")

def main():
    speak("Hello, how can I help you today?")
    while True:
        command = listen()

        if "hello" in command:
            speak("Hello! How can I assist you?")
        elif "time" in command:
            tell_time()
        elif "date" in command:
            tell_date()
        elif "search for" in command:
            query = command.replace("search for", "").strip()
            search_web(query)
        elif "exit" in command or "quit" in command:
            speak("Goodbye!")
            break
        else:
            speak("I'm sorry, I don't know how to help with that.")

if __name__ == "__main__":
    main()