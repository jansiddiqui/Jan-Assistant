#features.py
import struct
import time
from playsound import playsound
import eel
import os
import re
import sqlite3
import webbrowser
import pvporcupine
import pyaudio
from engine.command import speak
from engine.config import ASSISTANT_NAME
import pywhatkit as kit
from engine.helper import extract_yt_term

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

def hotword():
    porcupine=None
    paud=None
    audio_stream=None
    try:
        # pre trained keywords
        porcupine = pvporcupine.create(keywords=["Jan", "jarvis","alexa"])
        paud=pyaudio.PyAudio()
        audio_stream = paud.open(rate=porcupine.sample_rate, channels=1, format=pyaudio.paInt16, input=True, frames_per_buffer=porcupine.frame_length)
        # loop for streaming
        while True:
            keyword=audio_stream.read(porcupine.frames_length)
            keyword=struct.unpack_from("h"*porcupine.frame_length,keyword)
            #processing keyword comes from mic
            keyword_index=porcupine.process(keyword)
            #checking first keyword detected for not
            if keyword_index>=0:
                print("hotword detected")
                #pressing shortcut key win+j
                import pyautogui as autogui
                autogui.keyDown("win")
                autogui.press("j")
                time.sleep(2)
                autogui.keyUp("win")
    except:
        if porcupine is not None:
            porcupine.delete()
        if audio_stream is not None:
            audio_stream.close()
        if paud is not None:
            paud.terminate()