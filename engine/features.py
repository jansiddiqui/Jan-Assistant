#features.py
from playsound import playsound
import eel
import os
import re
import sqlite3
import webbrowser
from engine.command import speak
from engine.config import ASSISTANT_NAME
import pywhatkit as kit

conn = sqlite3.connect("jan.db")
cursor = conn.cursor()
# Play assistant sound function
@eel.expose
def playassistantsound():
    music_dir = "front\\assets\\audio\\start_sound.mp3"
    playsound(music_dir)

def openCommand(query):
    query = query.replace(ASSISTANT_NAME, "")
    query = query.replace("open", "")
    query.lower()

    app_name = query.strip()

    if app_name != "":
        try:
            cursor.execute(
                "SELECT path FROM sys_command WHERE name IN (?)", (app_name,))
            results = cursor.fetchall()

            if len(results) != 0:
                speak("Opening "+query)
                os.startfile(results[0][0])
            elif len(results) == 0:
                cursor.execute(
                    "SELECT url FROM web_command WHERE name IN (?)", (app_name,))
                results = cursor.fetchall()

                if len(results) != 0:
                    speak("Opening "+query)
                    webbrowser.open(results[0][0])
                else:
                    speak("Opening "+query)
                    try:
                        os.system('start '+query)
                    except:
                        speak("Sorry, not found")
        except:
            speak("something went wrong")


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