import speech_recognition as sr
from gtts import gTTS
from playsound import playsound
import os

listener = sr.Recognizer()
name = ""

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