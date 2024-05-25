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

date = ["24", "2", "9:00"]
hour = date[2].strip()
if hour[0]!='0' and len(hour) <5:
        hour= '0'+hour
print(hour)