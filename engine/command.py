#command.py
import pyttsx3
import speech_recognition as sr
import eel

def speak(text):
    engine = pyttsx3.init('sapi5')
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[1].id)
    engine.setProperty('rate', 174)
    print(voices)
    engine.say(text)
    engine.runAndWait()
@eel.expose
def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print('Listening...')
        eel.DisplayMessage('Listening...')
        r.pause_threshold = 1
        r.adjust_for_ambient_noise(source)
        try:
            audio = r.listen(source, timeout=10, phrase_time_limit=6)
        except Exception as e:
            print(f"Error in listening: {e}")
            eel.DisplayMessage(f"Error in listening: {e}")
            return ""
    
    try:
        print('Recognizing...')
        eel.DisplayMessage('Recognizing...')
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}")
        eel.DisplayMessage(query)
        speak(query)
        eel.DisplayHood()
        return query.lower()
    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand audio")
        eel.DisplayMessage("Could not understand audio")
    except sr.RequestError as e:
        print(f"Could not request results from Google Speech Recognition service; {e}")
        eel.DisplayMessage(f"Could not request results; {e}")
    except Exception as e:
        print(f"Error during recognition: {e}")
        eel.DisplayMessage(f"Error during recognition: {e}")
    return ""
