import pyttsx3


def speak(text):
    engine = pyttsx3.init('sapi5')
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[1].id)
    engine.setProperty('rate', 174)
    print(voices)
    engine.say(text)
    engine.runAndWait()

speak("Good Morning, Jan, How are you? I hope you are doing well.")