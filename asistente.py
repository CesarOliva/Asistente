import speech_recognition as sr
from gtts import gTTS
from playsound import playsound
import pywhatkit
import wikipedia
import datetime
import keyboard
from pygame import mixer
import threading as tr
import subprocess as sub
import os

name = "alexa"
listener = sr.Recognizer()

def talk(text, name):
    playAudio = gTTS(text, lang='es')
    name = f"media/{name}"
    playAudio.save(name)
    playsound(name)

def listen():
    listener = sr.Recognizer()
    with sr.Microphone() as source:
        print("Escuchando")
        pc = listener.listen(source)
    try:
        rec = listener.recognize_google(pc, language="es")
        rec = rec.lower()
    except sr.UnknownValueError:
        print("Lo siento, no te entendí. Intenta de nuevo")    
    if name in rec:
        rec = rec.replace(name, '')
    return rec

def alarm(rec):
    time = rec.replace('alarma a las', '')
    time = time.strip()
    if time[0]!='0' and len(time) <5:
        time= '0'+time
    text = 'Alarma activada a las '+time
    print(text)
    name = "alarm.mp3"
    talk(text, name)
    while True:
        if datetime.datetime.now().strftime('%H:%M') == time:
            print('Estableciste una alarma')
            mixer.init()
            mixer.music.load("media/ringtone.mp3")
            mixer.music.play()
            if keyboard.read_key() == "s":
                mixer.music.stop()
                break
        else:
            continue
        break

def write(f):
    text = "¿Qué quieres que escriba?"
    name = "WantForWrite.mp3"
    print(text)
    talk(text, name)
    rec_write = listen()
    f.write(rec_write + os.linesep)
    f.close()
    text = "Listo, puedes revisarlo"
    print(text)
    name = "textReady.mp3"
    talk(text, name)
    sub.Popen("media\pendientes.txt", shell=True)

sites={
    'google': 'google.com',
    'youtube': 'youtube.com',
    'github': 'github.com/CesarOliva',
    'whatsapp': 'web.whatsapp.com',
    'campus': 'campus.itnuevoleon.com'
}

programs={
    'visual studio': 'code',
    'spotify': 'spotify',
    'chrome': 'start chrome',
    'cámara': 'start microsoft.windows.camera:',
    'archivos': 'explorer'
}

def run_assistent():
    while True:
        try:
            rec = listen()
        except UnboundLocalError:
            print("Lo siento, no te entendí. Intenta de nuevo")
            continue

        if 'reproduce' in rec:
            music = rec.replace("reproduce", '')
            text = "Reproduciendo"+music
            name = "play.mp3"
            print(text)
            talk(text, name)
            pywhatkit.playonyt(music)
        
        elif 'busca' in rec:
            search = rec.replace("busca", '')
            wikipedia.set_lang("es")
            text = wikipedia.summary(search, 1)
            print(search+":\n"+text)
            name = "search.mp3"
            talk(text, name)
        
        elif 'alarma' in rec:
            thread = tr.Thread(target=alarm, args=(rec,))
            thread.start()
        elif 'detente' in rec:
            mixer.music.stop()
            print('Alarma detenida')

        elif 'abre' in rec:
            for site in sites:
                if site in rec:
                    text = f"Abriendo {site}"
                    name = "opening.mp3"
                    print(text)
                    talk(text, name)
                    sub.call(f'start chrome {sites[site]}', shell=True)
            for app in programs:
                if app in rec:
                    text = f"Abriendo {app}"
                    name = "opening.mp3"
                    print(text)
                    talk(text, name)
                    sub.call(f'{programs[app]}', shell=True)

        elif 'escribe' in rec:
            try:
                with open('media/pendientes.txt', 'a') as f:
                    write(f)
            except FileNotFoundError as e:
                file = open('media/pendientes.txt', 'w')
                write(file)

        elif 'termina' in rec:
            print("Cerrando...")
            playsound("media/bye.mp3")
            break

if __name__ == '__main__':
    playsound("media/initiating.mp3")
    run_assistent()
