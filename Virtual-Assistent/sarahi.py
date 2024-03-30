import speech_recognition as sr 
import pywhatkit
import pyautogui
import wikipedia
import datetime
from pygame import mixer
import threading as tr
from gtts import gTTS
from playsound import playsound
import cam
import subprocess as sub
import os

name = "sarahí"
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

sites={
    'google': 'google.com',
    'youtube': 'youtube.com',
    'facebook': 'facebook.com'
}

programs={
    'brave': "brave-browser",
    'firefox': "firefox",
    'spotify': "spotify",
    'visual studio': "code",
    'consola': 'konsole'
}

def clock(rec):
    num = rec.replace('alarma a las', '')
    num = num.strip()
    if num[0] != '0' and len(num) < 5:
        num = '0' + num
    alarma = 'Alarma activada a las ' + num
    print(alarma)
    alarmatts = gTTS(alarma, lang='es')
    alarmatts.save("alarma.mp3")
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

def run_sarahi():
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
            reproducirtts = gTTS(reproduciendo, lang='es')
            reproducirtts.save("reproduce.mp3")
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
            buscartts = gTTS(busqueda, lang='es')
            buscartts.save("busqueda.mp3")
            playsound('busqueda.mp3')

        elif 'alarma' in rec:
            t = tr.Thread(target=clock, args=(rec,))
            t.start()
        
        elif 'detente' in rec:
            mixer.music.stop()
            print('Alarma detenida')

        elif 'enciende camara' in rec:
            encender = 'enseguida'
            print("Camara encendida")
            camaratts = gTTS(encender, lang='es')
            camaratts.save("camara.mp3")
            playsound('camara.mp3')
            cam.capture()

        elif 'abre' in rec:
            for site in sites:
                if site in rec:
                    abrir = f'Abriendo {site}'
                    print(abrir)
                    abrirtts = gTTS(abrir, lang='es')
                    abrirtts.save('abriendo.mp3')
                    playsound('abriendo.mp3')
                    sub.call(f'brave-browser {sites[site]}', shell=True)
            for app in programs:
                if app in rec:
                    abrirapp = f'Abriendo {app}'
                    print(abrirapp)
                    abrirapptts = gTTS(abrirapp, lang='es')
                    abrirapptts.save('abriendo-app.mp3')
                    playsound('abriendo-app.mp3')
                    sub.call(f'{programs[app]}', shell=True)

        elif 'escribe' in rec:
            try:
                with open('nota.txt', 'a') as f:
                    write(f)
            
            except FileNotFoundError as e:
                file = open('nota.txt', 'w')
                write(file)

        elif 'termina' in rec:
            print('Cerrando...')
            closetts = gTTS('Adíos', lang='es')
            closetts.save('close.mp3')
            playsound('close.mp3')
            break

def write(f):
    writetts = gTTS('¿Que quieres que escriba?', lang='es')
    print('Escribiendo')
    writetts.save('WantForWrite.mp3')
    playsound('WantForWrite.mp3')
    rec_write = listen()
    f.write(rec_write + os.linesep)
    f.close()
    readytts = gTTS('Listo, puedes revisarlo', lang='es')
    readytts.save('ready.mp3')
    playsound('ready.mp3')
    sub.Popen('xdg-open nota.txt', shell=True)

if __name__ == '__main__':
    run_sarahi()