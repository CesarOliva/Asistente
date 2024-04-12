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


from googletrans import Translator
import requests

translator = Translator()
text ="안녕하세요"
print(translator.translate(text, dest='es').text)

city = "Monterrey"
url = f'https://es.wttr.in/{city}?format=j1'
res = requests.get(url)
weather_dic = res.json()

temp = weather_dic["current_condition"][0]["temp_C"]
desc_temp = weather_dic["current_condition"][0]["lang_es"][0]["value"]
max_temp = weather_dic["weather"][0]["maxtempC"]
min_temp = weather_dic["weather"][0]["mintempC"]

print(f"La temperatura actual es de {temp}°C")
print(f"{desc_temp} con temperaturas maximas de {max_temp}°C y minimas de {min_temp}°C")