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
import pyautogui as at
import webbrowser
import time

comandos = """
            Comandos que puedes usar:
            - Reproduce (cancion)
            - Busca (algo)
            - Abre (pagina web o app)
            - Alarma a las (hora en 24H)
            - Escribe (nota)
            - Mensaje (contacto)
            - Termina
"""



name = "sarahí"
listener = sr.Recognizer()

main_window = Tk()
main_window.title("Sarahí Assistent")
width = 900 
height = 450
x_window = main_window.winfo_screenwidth()//2 - (width//2)
y_window = main_window.winfo_screenheight()//2 - (height//2)
main_window.geometry(f"{width}x{height}+{x_window}+{y_window}")
main_window.resizable(0,0)
main_window.configure(bg="#85C1E9")

label_title = Label(main_window, text="Sarahí Assistant", fg="#212F3D", bg="#85C1E9",
                    font=("Lato", 26))
label_title.pack(pady=10)

canvas = Canvas(bg="#5DADE2", height="230", width="200")
canvas.place(y=0, x=0)
canvas.create_text(75, 80, text=comandos, fill="#212F3D", font="Lato 11")

text_info = Text(main_window, bg="#5499C7", fg="#000", font="Lato 10")
text_info.place(x=0, y=230, height=230, width=204)

photo = ImageTk.PhotoImage(Image.open("media/Sarahi.jpg"))
window_photo = Label(main_window, image=photo)
window_photo.pack(pady=5)

def open_w_pages():
    window_pages = Toplevel()
    window_pages.title("Acciones Páginas")
    window_pages.configure(bg="#FAD7A0")
    window_pages.geometry("300x200")
    window_pages.resizable(0, 0)
    main_window.eval(f'tk::PlaceWindow {str(window_pages)} center')

    title_label = Label(window_pages, text="Páginas", fg="white", bg="#FAD7A0",
                        font=("Consolas", "15", "bold"))
    title_label.pack(pady=5)

    button_add = Button(window_pages, text="Lista", fg="white", bg="#149FE0",
                        font=('Arial', '10', 'bold'), command=talk_pages)
    button_add.pack(pady=4)
    button_add = Button(window_pages, text="Agregar Páginas", fg="white", bg="#149FE0",
                        font=('Arial', '10', 'bold'), command=open_add_pages)
    button_add.pack(pady=4)
    button_add = Button(window_pages, text="Eliminar lista", fg="white", bg="#149FE0",
                        font=('Arial', '10', 'bold'), command=delete_pages)
    button_add.pack(pady=4)

def talk_pages():
    if bool(sites) == True:
        text = "Has agregado las siguientes páginas"
        filename = "added.mp3"
        talk(text, filename)
        for site in sites:
            filename = "app.mp3"
            talk(site, filename)
    else:
        text = "Aún no has agregado nada"
        filename = "notyet.mp3"
        talk(text, filename)

def open_add_pages():
    global namepage_entry, pathpage_entry
    window_pages = Toplevel()
    window_pages.title("Agregar paginas")
    window_pages.configure(bg="#434343")
    window_pages.geometry("300x200")
    window_pages.resizable(0,0)
    main_window.eval(f'tk::PlaceWindow {str(window_pages)} center')

    title_label = Label(window_pages, text="Agrega una página", fg="white", bg="#434343",
                        font=("Arial", "15", "bold"))
    title_label.pack(pady=3)
    
    name_label = Label(window_pages, text="Nombre de la página", fg="white", bg="#434343",
                        font=("Arial", "10"))
    name_label.pack(pady=2)
    namepage_entry = Entry(window_pages, width=20)
    namepage_entry.pack(pady=1)

    path_label = Label(window_pages, text="URL de la página", fg="white", bg="#434343",
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

def delete_pages():
    os.remove("pages.txt")

def open_w_apps():
    window_apps = Toplevel()
    window_apps.title("Acciones Programas")
    window_apps.configure(bg="#FAD7A0")
    window_apps.geometry("300x200")
    window_apps.resizable(0, 0)
    main_window.eval(f'tk::PlaceWindow {str(window_apps)} center')

    title_label = Label(window_apps, text="Programas", fg="white", bg="#FAD7A0",
                        font=("Consolas", "15", "bold"))
    title_label.pack(pady=5)

    button_add = Button(window_apps, text="Lista", fg="white", bg="#149FE0",
                        font=('Arial', '10', 'bold'), command=talk_programs)
    button_add.pack(pady=4)
    button_add = Button(window_apps, text="Agregar Programas", fg="white", bg="#149FE0",
                        font=('Arial', '10', 'bold'), command=open_add_apps)
    button_add.pack(pady=4)
    button_add = Button(window_apps, text="Eliminar lista", fg="white", bg="#149FE0",
                        font=('Arial', '10', 'bold'), command=delete_apps)
    button_add.pack(pady=4)

def talk_programs():
    if bool(programs) == True:
        text = "Has agregado los siguientes programas"
        filename = "added.mp3"
        talk(text, filename)
        for app in sites:
            filename = "app.mp3"
            talk(app, filename)
    else:
        text = "Aún no has agregado nada"
        filename = "notyet.mp3"
        talk(text, filename)

def open_add_apps():
    global nameapp_entry, pathapp_entry
    window_apps = Toplevel()
    window_apps.title("Agregar Programas")
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

def delete_apps():
    os.remove("programs.txt")

def add_apps():
    name_app = nameapp_entry.get().strip()
    path_app = pathapp_entry.get().strip()
    sites[name_app] = path_app
    save_data(name_app, path_app, "programs.txt")
    nameapp_entry.delete(0, "end")
    pathapp_entry.delete(0, "end")

def open_w_contacts():
    window_contacts = Toplevel()
    window_contacts.title("Acciones Contactos")
    window_contacts.configure(bg="#FAD7A0")
    window_contacts.geometry("300x200")
    window_contacts.resizable(0, 0)
    main_window.eval(f'tk::PlaceWindow {str(window_contacts)} center')

    title_label = Label(window_contacts, text="Contactos", fg="white", bg="#FAD7A0",
                        font=("Consolas", "15", "bold"))
    title_label.pack(pady=5)

    button_add = Button(window_contacts, text="Lista", fg="white", bg="#149FE0",
                        font=('Arial', '10', 'bold'), command=talk_contacts)
    button_add.pack(pady=4)
    button_add = Button(window_contacts, text="Agregar Contactos", fg="white", bg="#149FE0",
                        font=('Arial', '10', 'bold'), command=open_add_contacts)
    button_add.pack(pady=4)
    button_add = Button(window_contacts, text="Eliminar lista", fg="white", bg="#149FE0",
                        font=('Arial', '10', 'bold'), command=delete_contacts)
    button_add.pack(pady=4)

def talk_contacts():
    if bool(contacts) == True:
        text = "Has agregado los siguientes contactos"
        filename = "added.mp3"
        talk(text, filename)
        for contact in contacts:
            filename = "app.mp3"
            talk(contact, filename)
    else:
        text = "Aún no has agregado nada"
        filename = "notyet.mp3"
        talk(text, filename)

def open_add_contacts():
    global namecontact_entry, numbercontact_entry
    window_contacts = Toplevel()
    window_contacts.title("Agregar Contactos")
    window_contacts.configure(bg="#434343")
    window_contacts.geometry("300x200")
    window_contacts.resizable(0, 0)
    main_window.eval(f'tk::PlaceWindow {str(window_contacts)} center')

    title_label = Label(window_contacts, text="Agrega un contacto", fg="white", bg="#434343",
                        font=("Arial", "15", "bold"))
    title_label.pack(pady=3)

    name_label = Label(window_contacts, text="Nombre del contacto", fg="white", bg="#434343",
                        font=("Arial", "10"))
    name_label.pack(pady=2)
    namecontact_entry = Entry(window_contacts, width=20)
    namecontact_entry.pack(pady=1)

    number_label = Label(window_contacts, text="Número del contacto (+51)", fg="white", bg="#434343",
                        font=("Arial", "10"))
    number_label.pack(pady=2)
    numbercontact_entry = Entry(window_contacts, width=25)
    numbercontact_entry.pack(pady=1)

    save_button = Button(window_contacts, text="Guardar", bg="#16222A", fg="white", width=8, height=1, command=add_contacts)
    save_button.pack(pady=4)

def add_contacts():
    name_contact = namecontact_entry.get().strip()
    number_contact = numbercontact_entry.get().strip()
    sites[name_contact] = number_contact
    save_data(name_contact, number_contact, "contacts.txt")
    namecontact_entry.delete(0, "end")
    numbercontact_entry.delete(0, "end")

def delete_contacts():
    os.remove('contacts.txt')

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
contacts=dict()
charge_data(contacts, "contacts.txt")

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

def write(f):
    text = "¿Qué quieres que escriba?"
    filename = "WantForWrite.mp3"
    talk(text, filename)
    rec_write = listen()
    f.write(rec_write + os.linesep)
    f.close()
    text = "Listo, puedes revisarlo"
    filename = "textReady.mp3"
    talk(text, filename)
    sub.Popen('media\pendientes.txt', shell=True)

def clock(rec):
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


def reproduce(rec):
    music = rec.replace("reproduce", '')
    text = "Reproduciendo"+music
    filename = "play.mp3"
    talk(text, filename)
    pywhatkit.playonyt(music)

def busca(rec):
    search = rec.replace("busca", '')
    wikipedia.set_lang("es")
    text = wikipedia.summary(search, 1)
    filename = "search.mp3"
    talk(text, filename)
    write_text(text)

def abre(rec):
    task = rec.replace('abre', '').strip()
    if task in sites:
        for task in sites:
            if task in rec:
                text = f"Abriendo {task}"
                filename = "opening.mp3"
                talk(text, filename)
                sub.call(f'start chrome {sites[task]}', shell=True)
    elif task in programs:
        for task in programs:
            if task in rec:
                text = f"Abriendo {task}"
                filename = "opening.mp3"
                talk(text, filename)
                sub.Popen(programs[task])
    else:
        text = "Aun no se ha agregado esta aplicación o página\nUsa los botones para agregar"
        filename = "not_added.mp3"
        talk(text, filename)

def enviar_mensaje(rec):
    text = "¿A quién se enviará el mensaje?"
    filename = "message.mp3"
    talk(text, filename)
    contact = listen()
    contact = contact.strip()
    print(contact)
    if contact in contacts:
        for cont in contacts:
            if cont == contact:
                contact = contacts[cont]
                text = "¿Qué mensaje deseas enviar?"
                filename = "wantForSend.mp3"
                talk(text, filename)
                message = listen()
                webbrowser.open(f'https://web.whatsapp.com/send?phone={contact}&text={message}')
                time.sleep(15)
                at.press('enter')
    else:
        text = "Contacto no registrado"
        filename = "not_added.mp3"
        talk(text, filename)


def func_alarma(rec):
    thread = tr.Thread(target=clock, args=(rec,))
    thread.start()

def stop_alarma(rec):
    mixer.music.stop()

def cierra(rec):
    # for program in programs:
    #     kill_program = programs[program].split('\\')
    #     kill_program = kill_program[-1]
    #     if program in rec:
    #         text = ""
    #         filename = ""
    #         talk(text, filename)
    pass

key_words = {
    'reproduce': reproduce,
    'busca': busca,
    'alarma': func_alarma,
    'detente': stop_alarma,
    'abre': abre,
    'mensaje': enviar_mensaje,
    'cierra': cierra
}

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
    
        if 'busca' in rec:
            key_words['busca'](rec)
            break
        elif 'escribe' in rec:
            try:
                with open('media/pendientes.txt', 'a') as f:
                    write(f)
            except FileNotFoundError as e:
                file = open('media/pendientes.txt', 'w')
                write(file)
        else:
            for word in key_words:
                if word in rec:
                    key_words[word](rec)
                    
        if 'termina' in rec:
            text = "Adiós"
            filename="bye.mp3"
            talk(text, filename)
            break        

    main_window.update()

button_listen = Button(main_window, text="Escuchar", fg="white", bg="#149FE0",
                       font=('Arial', '15', 'bold'), command=run_sarahi)
button_listen.pack(pady=10)

button_speak = Button(main_window, text="Hablar", fg="white", bg="#149FE0",
                        font=('Arial', '10', 'bold'), command=read_and_talk)
button_speak.place(x=720, y=100, width=120, height=30)

button_pages = Button(main_window, text="Páginas", fg="white", bg="#149FE0",
                        font=('Arial', '10', 'bold'), command=open_w_pages)
button_pages.place(x=720, y=150, width=120, height=30)

button_apps = Button(main_window, text="Programas", fg="white", bg="#149FE0",
                        font=('Arial', '10', 'bold'), command=open_w_apps)
button_apps.place(x=720, y=200, width=120, height=30)

button_apps = Button(main_window, text="Contactos", fg="white", bg="#149FE0",
                        font=('Arial', '10', 'bold'), command=open_w_contacts)
button_apps.place(x=720, y=250, width=120, height=30)

main_window.mainloop()