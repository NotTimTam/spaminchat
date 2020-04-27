# Pastes and sends data in chats from data.txt
# Imports
import time
from pynput.keyboard import Key, Controller
import keyboard
from gtts import gTTS
import os

print("Please put the text you want printed in the 'data.txt' file.")
print("Press 'P' at any time to abort.")

# Set to true for an audio ONLY experience
use_tts = False

with open("data.txt") as f:
    file_contents = f.read()
    word_list = file_contents.split()
    e = 0
    e_end = len(word_list)
    paster = Controller()
    language = 'en'
    print("\nStarting in 5 seconds... Please select the text input field of the message program you are using.\n")
    time.sleep(5)
    for i in word_list:
        if keyboard.is_pressed('p'):
            print("Aborting!")
            break
        else:
            e += 1
            print(str(round((e / e_end) * 100)) + "% complete... | Current Word:", i)
            if use_tts:
                tts = gTTS(text=i, lang="en")
                tts.save("tempaudio.mp3")
                os.system("start tempaudio.mp3")
            else:
                paster.type(i)
                time.sleep(0.01)
                paster.press(Key.enter)
                time.sleep(0.01)
                paster.release(Key.enter)
                time.sleep(0.01)
