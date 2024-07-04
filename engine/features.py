#features.py
from playsound import playsound
import eel
import os
import re
from engine.command import speak
from engine.config import ASSISTANT_NAME
import pywhatkit as kit
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

def PlayYoutube(query):
    search_term = extract_yt_term(query)
    speak("Playing "+search_term+" on YouTube")
    kit.playonyt(search_term)

def extract_yt_term(command):
    # Define a regular expression pattern to capture the song name
    pattern = r'play\s+(.*?)\s+on\s+youtube'
    # Use reseach to find the match in the command
    match = re.search(pattern, command, re.IGNORECASE)
    # If a match is found, return the extracted song name; otherwise, return none
    return match.group(1) if match else None