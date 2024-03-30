import speech_recognition as sr 
import pywhatkit
import pyautogui
import wikipedia
import datetime
from pygame import mixer
import threading as tr
from gtts import gTTS
from playsound import playsound
# import cam
import subprocess as sub
import os
from tkinter import *
from PIL import Image
from PIL import ImageTk

main_window = Tk()
main_window.title("Sarahí Assistent")

main_window.geometry("800x400")
main_window.resizable(0,0)
main_window.configure(bg='#00B4DB')

comandos = """
            Comandos que puedes usar:
            - Reproduce (cancion)
            - Busca (algo)
            - Abre (pagina web o app)
            - Alarma a las (hora en 24H)
            - Colores (rojo, azul, amarillo)
            - Termina
"""

label_title = Label(main_window, text="Sarahí", fg="#2E3534", bg="#00B4DB",
                        font=('Arial', '28', 'bold'))
label_title.pack(pady=10)

canvas_comandos = Canvas(bg="#6dd5ed", height="170", width="198")
canvas_comandos.place(y=0, x=0)
canvas_comandos.create_text(75, 80, text=comandos, fill="#434343", font="Arial 10")

text_info = Text(main_window, bg="#00B4DB", fg="#434343")
text_info.place(x=0, y=170, height=230, width=200)

sarahi_photo = ImageTk.PhotoImage(Image.open("media/Sarahi.jpg"))
window_photo = Label(main_window, image=sarahi_photo)
window_photo.pack(pady=5)

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

name = "sarahí"
listener = sr.Recognizer()

def read_and_talk():
    text = text_info.get("1.0", "end")
    talk = gTTS(text, lang="es")
    talk.save('talk.mp3')
    playsound('talk.mp3')

def write_text(text_wiki):
    text_info.insert(INSERT, text_wiki)

def listen():
    try:
        with sr.Microphone() as source:
            print('Escuchando ....')
            listeningtts = gTTS('Te escucho', lang='es')
            listeningtts.save('listening.mp3')
            playsound('listening.mp3')
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
            busqueda = wiki
            buscartts = gTTS(busqueda, lang='es')
            buscartts.save("busqueda.mp3")
            playsound('busqueda.mp3')
            write_text(search + ": " + wiki)
            break

        elif 'alarma' in rec:
            t = tr.Thread(target=clock, args=(rec,))
            t.start()
        
        elif 'detente' in rec:
            mixer.music.stop()
            print('Alarma detenida')

        # elif 'enciende camara' in rec:
        #     encender = 'enseguida'
        #     print("Camara encendida")
        #     camaratts = gTTS(encender, lang='es')
        #     camaratts.save("camara.mp3")
        #     playsound('camara.mp3')
        #     cam.capture()

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
            closetts = gTTS('Adios', lang='es')
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

button_listen = Button(main_window, text="Escuchar", fg="white", bg="#1565C0",
                        font=('Arial', '15', 'bold'), command=run_sarahi)
button_listen.pack(pady=10)

button_speak = Button(main_window, text="Hablar", fg="white", bg="#149FE0",
                        font=('Arial', '10', 'bold'), command=read_and_talk)
button_speak.place(x=625, y=70, width=100, height=30)

main_window.mainloop()