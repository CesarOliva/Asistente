# # Python program showing
# # how to kill threads
# # using set/reset stop
# # flag

# import threading
# import time

# def run():
# 	while True:
# 		global stop_threads
# 		if stop_threads:
# 			break

# stop_threads = False
# t1 = threading.Thread(target = run)
# condicion = input(print("UN VIDEO MA MI GENTE"))
# if input != condicion:
#     stop_threads = True
# print('thread killed')


from playsound import playsound
from gtts import gTTS
import os

for i in range(5):
    text = input("Introduce el texto a reproducir: ")
    save = gTTS(text, lang="es")
    filename = "prueba.mp3"
    save.save(filename)
    playsound(filename)
    os.remove(filename)  # Eliminar el archivo para sobrescribirlo

