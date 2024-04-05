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


import pyautogui as at
import subprocess as sub
import time

sub.call('start chrome "google.com tabla liga mx"', shell=True)
time.sleep(3)
at.write("Tabla Liga MX")
time.sleep(1)
at.press('enter')