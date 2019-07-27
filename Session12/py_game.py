import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
from pygame import mixer
mixer.init()
mixer.music.load('Spirited Away (2001) - The Name of Life (Instrumental piano) Inochi No Namae いのちの名前-ImPM5IDIYPs.mp3')
mixer.music.play()
while True:
    input("Press any key to stop")
    break