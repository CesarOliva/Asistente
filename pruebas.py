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



# import subprocess as sub
# from tkinter import *

# main_window = Tk()
# main_window.geometry("300x200")
# main_window.configure(bg="#00B4DB")

# def getContent():
#     pass

# def modificar():
#     try:
#         with open('programs.txt', 'r') as file:
#             content = file.read()
#             print(content)
#     except FileNotFoundError as e:
#         file = open('programs.txt', 'r')

#     Programs = content.split("\n")
    
#     val = nameEntry.get().strip()
#     val+=","
#     content = ""
#     for program in Programs:
#         if val in program:
#             newKey = pathEntry.get().strip()
#             program=f"{val}{newKey}"
#         content+=program+"\n"

#     with open('program.txt', 'w') as f:
#         f.write(content)

# nameLabel = Label(main_window, text="Nombre", fg="white", bg="#434343")
# nameLabel.pack(pady=2)
# nameEntry = Entry(main_window, width=30)
# nameEntry.pack(pady=1)

# pathLabel = Label(main_window, text="Ruta")
# pathLabel.pack(pady=2)
# pathEntry = Entry(main_window, width=30)
# pathEntry.pack(pady=1)

# button_change = Button(main_window, text="Guardar", command=modificar)
# button_change.pack(pady=2)
# main_window.mainloop()

# from tkinter import *

# root=Tk()
# root.geometry("900x450")
# root.eval(f'tk::PlaceWindow {str(root)} center')
# root.resizable(0,0)
# root.title("Ventana de ejemplo") 

# root.mainloop()