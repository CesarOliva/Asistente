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
from tkinter import *
from PIL import Image, ImageTk

comandos = """
            Comandos que puedes usar:
            - Reproduce (cancion)
            - Busca (algo)
            - Abre (pagina web o app)
            - Alarma a las (hora en 24H)
            - Escribe (nota)
            - Termina
"""

name = "sarahí"
listener = sr.Recognizer()

main_window = Tk()
main_window.title("Sarahí Assistent")
main_window.geometry("900x450")
main_window.resizable(0,0)
main_window.configure(bg="#00B4DB")

label_title = Label(main_window, text="Sarahí", fg="#2E3534", bg="#00B4DB",
                    font=("Poppins", "28", "bold"))
label_title.pack(pady=10)

canvas = Canvas(bg="#6DD5ED", height="230", width="200")
canvas.place(y=0, x=0)
canvas.create_text(75, 80, text=comandos, fill="#434343", font="Arial 10")

text_info = Text(main_window, bg="#00B4DB", fg="#434343")
text_info.place(x=0, y=230, height=230, width=204)

photo = ImageTk.PhotoImage(Image.open("media/Sarahi.jpg"))
window_photo = Label(main_window, image=photo)
window_photo.pack(pady=5)

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

def talk(text, filename):
    playAudio = gTTS(text, lang='es')
    filename = f"media/{filename}"
    playAudio.save(filename)
    playsound(filename)
    os.remove(filename)

def read_and_talk():
    text = text_info.get("1.0", "end")
    filename = "talk.mp3"
    talk(text, filename)

def write_text(text):
    text_info.insert(INSERT, text)

def alarm(rec):
    time = rec.replace('alarma a las', '')
    time = time.strip()
    if time[0]!='0' and len(time) <5:
        time= '0'+time
    text = 'Alarma activada a las '+time
    print(text)
    filename = "alarm.mp3"
    talk(text, filename)
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
    filename = "WantForWrite.mp3"
    print(text)
    talk(text, filename)
    rec_write = listen()
    f.write(rec_write + os.linesep)
    f.close()
    text = "Listo, puedes revisarlo"
    print(text)
    filename = "textReady.mp3"
    talk(text, filename)
    sub.Popen('media\pendientes.txt', shell=True)

def open_w_pages():
    global namepage_entry, pathpage_entry
    window_pages = Toplevel()
    window_pages.title("Agrega Paginas")
    window_pages.configure(bg="#434343")
    window_pages.geometry("300x200")
    window_pages.resizable(0, 0)
    main_window.eval(f'tk::PlaceWindow {str(window_pages)} center')

    title_label = Label(window_pages, text="Agrega una pagina", fg="white", bg="#434343",
                        font=("Arial", "15", "bold"))
    title_label.pack(pady=3)

    name_label = Label(window_pages, text="Nombre de la pagina", fg="white", bg="#434343",
                        font=("Arial", "10"))
    name_label.pack(pady=2)
    namepage_entry = Entry(window_pages, width=20)
    namepage_entry.pack(pady=1)

    path_label = Label(window_pages, text="Liga de la pagina", fg="white", bg="#434343",
                        font=("Arial", "10"))
    path_label.pack(pady=2)
    pathpage_entry = Entry(window_pages, width=25)
    pathpage_entry.pack(pady=1)

    save_button = Button(window_pages, text="Guardar", bg="#16222A", fg="white", width=8, height=1, command=add_pages)
    save_button.pack(pady=4)

def add_pages():
    name_page = namepage_entry.get().strip()
    path_page = pathpage_entry.get().strip()
    sites[name_page] = path_page
    save_data(name_page, path_page, "pages.txt")
    namepage_entry.delete(0, "end")
    pathpage_entry.delete(0, "end")

def open_w_apps():
    global nameapp_entry, pathapp_entry
    window_apps = Toplevel()
    window_apps.title("Agrega Paginas")
    window_apps.configure(bg="#434343")
    window_apps.geometry("300x200")
    window_apps.resizable(0, 0)
    main_window.eval(f'tk::PlaceWindow {str(window_apps)} center')

    title_label = Label(window_apps, text="Agrega un programa", fg="white", bg="#434343",
                        font=("Arial", "15", "bold"))
    title_label.pack(pady=3)

    name_label = Label(window_apps, text="Nombre del programa", fg="white", bg="#434343",
                        font=("Arial", "10"))
    name_label.pack(pady=2)
    nameapp_entry = Entry(window_apps, width=20)
    nameapp_entry.pack(pady=1)

    path_label = Label(window_apps, text="Comando del programa", fg="white", bg="#434343",
                        font=("Arial", "10"))
    path_label.pack(pady=2)
    pathapp_entry = Entry(window_apps, width=25)
    pathapp_entry.pack(pady=1)

    save_button = Button(window_apps, text="Guardar", bg="#16222A", fg="white", width=8, height=1, command=add_apps)
    save_button.pack(pady=4)

def add_apps():
    name_app = nameapp_entry.get().strip()
    path_app = pathapp_entry.get().strip()
    sites[name_app] = path_app
    save_data(name_app, path_app, "programs.txt")
    nameapp_entry.delete(0, "end")
    pathapp_entry.delete(0, "end")

def charge_data(name_dict, name_file):
    try:
        with open(name_file) as f:
            for line in f:
                (key, val) = line.split(",")
                val = val.rstrip("\n")
                name_dict[key] = val
    except FileNotFoundError as e:
        pass

def save_data(key, value, name):
    try:
        with open(name, "a") as f:
            f.write(key + ","+value + "\n")
    except FileNotFoundError:
        file = open(name, "a")
        file.write(key + ","+value + "\n")

sites=dict()
charge_data(sites, "pages.txt")
programs=dict()
charge_data(programs, "programs.txt")

def run_sarahi():
    text = "Hola César, Bienvenido"
    filename = "initiating.mp3"
    talk(text, filename)
    while True:
        try:
            rec = listen()
        except UnboundLocalError:
            print("Lo siento, no te entendí. Intenta de nuevo")
            continue

        if 'reproduce' in rec:
            music = rec.replace("reproduce", '')
            text = "Reproduciendo"+music
            filename = "play.mp3"
            print(text)
            talk(text, filename)
            pywhatkit.playonyt(music)
        
        elif 'busca' in rec:
            search = rec.replace("busca", '')
            wikipedia.set_lang("es")
            text = wikipedia.summary(search, 1)
            print(search+":\n"+text)
            filename = "search.mp3"
            talk(text, filename)
            write_text(text)
            break
        
        elif 'alarma' in rec:
            thread = tr.Thread(target=alarm, args=(rec,))
            thread.start()
        elif 'detente' in rec:
            mixer.music.stop()
            print('Alarma detenida')

        elif 'abre' in rec:
            task = rec.replace('abre', '').strip()
            if task in sites:
                for task in sites:
                    if task in rec:
                        text = f"Abriendo {task}"
                        filename = "opening.mp3"
                        print(text)
                        talk(text, filename)
                        sub.call(f'start chrome {sites[task]}', shell=True)
            elif task in programs:
                for task in programs:
                    if task in rec:
                        text = f"Abriendo {task}"
                        filename = "opening.mp3"
                        print(text)
                        talk(text, filename)
                        sub.Popen(programs[task])
            else:
                text = "Aun no se ha agregado esta aplicación o página\nUsa los botones para agregar"
                print(task)
                filename = "not_added.mp3"
                print(text)
                talk(text, filename)

        elif 'escribe' in rec:
            try:
                with open('media/pendientes.txt', 'a') as f:
                    write(f)
            except FileNotFoundError as e:
                file = open('media/pendientes.txt', 'w')
                write(file)

        elif 'termina' in rec:
            print("Cerrando...")
            text = "Adíos"
            filename="bye.mp3"
            talk(text, filename)
            break

button_listen = Button(main_window, text="Escuchar", fg="white", bg="#149FE0",
                       font=('Arial', '15', 'bold'), command=run_sarahi)
button_listen.pack(pady=10)

button_speak = Button(main_window, text="Hablar", fg="white", bg="#149FE0",
                        font=('Arial', '10', 'bold'), command=read_and_talk)
button_speak.place(x=720, y=100, width=120, height=30)

button_add_pages = Button(main_window, text="Agregar páginas", fg="white", bg="#149FE0",
                        font=('Arial', '10', 'bold'), command=open_w_pages)
button_add_pages.place(x=720, y=150, width=120, height=30)

button_add_apps = Button(main_window, text="Agregar apps", fg="white", bg="#149FE0",
                        font=('Arial', '10', 'bold'), command=open_w_apps)
button_add_apps.place(x=720, y=200, width=120, height=30)

main_window.mainloop()