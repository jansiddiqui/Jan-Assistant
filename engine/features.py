from playsound import playsound
import eel

# Play assistant sound function
@eel.expose
def playassistantsound():
    music_dir = "front\\assets\\audio\\start_sound.mp3"
    playsound(music_dir)