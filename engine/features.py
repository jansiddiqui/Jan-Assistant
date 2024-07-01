#features.py
from playsound import playsound
import eel
import os
from engine.command import speak
from engine.config import ASSISTANT_NAME

# Play assistant sound function
@eel.expose
def playassistantsound():
    music_dir = "front\\assets\\audio\\start_sound.mp3"
    playsound(music_dir)

def openCommand(query):
    query = query.replace(ASSISTANT_NAME, "")
    query = query.replace("open", "")

    if query!="":
        speak("Opening "+query)
        os.system('start '+query)
    else:
        speak("Not found")