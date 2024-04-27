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


start_date = input("Fecha de inicio: ")
#26 de febrero a las 13:58
start_date = start_date.replace(' de ', ' ')
start_date = start_date.replace(' a las ', ' ')
print(start_date)
start_date = start_date.split(' ')
print(start_date)


months = {
    "enero": "01",
    "febrero": "02",
    "marzo": "03",
    "abril": "04",
    "mayo": "05",
    "junio": "06",
    "julio": "07",
    "agosto": "08",
    "septiembre": "09",
    "octubre": "10",
    "noviembre": "11",
    "diciembre": "12"
}

for month in months:
    if start_date[1] in months:
        month = months[start_date[1]]

new_date = f"2024-{month}-{start_date[0]} {start_date[2]}"
print(new_date)