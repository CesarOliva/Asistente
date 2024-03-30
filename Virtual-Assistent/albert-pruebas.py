import speech_recognition as sr 
import pywhatkit
import pyautogui
import wikipedia
import datetime, keyboard
from pygame import mixer
import threading as tr
from gtts import gTTS
from playsound import playsound

name = "eva"
listener = sr.Recognizer()
def listen():
    try:
        with sr.Microphone() as source:
            print('Escuchando ....')
            pc = listener.listen(source)
            rec = listener.recognize_google(pc, language="es")
            rec = rec.lower()
            if name in rec:
                rec = rec.replace(name, '')

    except:
        pass

    return rec


def clock(rec):
    num = rec.replace('alarma a las', '')
    num = num.strip()
    alarma = 'Alarma activada a las ' + num
    print(alarma)
    tts = gTTS(alarma, lang='es')
    tts.save("alarma.mp3")
    playsound('alarma.mp3')
    while True:
        if datetime.datetime.now().strftime('%H:%M') == num:
            print('Estableciste una alarma')
            mixer.init()
            mixer.music.load("ringtone.mp3")
            mixer.music.play()
        else:
            continue 

        break

def run_albert():
    while True:
        try:
            rec = listen()

        except UnboundLocalError:
            print("Perdon, no entendí. ¿Podrias repetirlo?")
            continue

        if 'reproduce' in rec:
            music = rec.replace('reproduce', '')
            reproduciendo = "Reproduciendo " + music
            print(reproduciendo)
            tts = gTTS(reproduciendo, lang='es')
            tts.save("reproduce.mp3")
            playsound('reproduce.mp3')

            pywhatkit.playonyt(music)

        elif 'pausa' in rec:
            music = rec.replace('pausando', '')
            print('Pausando')
            pyautogui.press('space')

        elif 'busca' in rec:
            search = rec.replace('busca', '')
            wikipedia.set_lang("es")
            wiki = wikipedia.summary(search, 1)
            print(search + ": " + wiki)
            busqueda = wiki
            tts = gTTS(busqueda, lang='es')
            tts.save("busqueda.mp3")
            playsound('busqueda.mp3')

        elif 'alarma' in rec:
            t = tr.Thread(target=clock, args=(rec,))
            t.start()
        
        elif 'detente' in rec:
            mixer.music.stop()
            print('Alarma detenida')

if __name__ == '__main__':
    run_albert()