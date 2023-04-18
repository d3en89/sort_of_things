import random
import time
import os
from playsound import playsound

#search script catalog
fdir = (os.path.abspath(__file__)).split("/")
name_script = fdir[-1]
fdir.remove(name_script)
dir = "/".join(fdir)
print("В течении 30 секунд надо назвать минимум 20 слов")
print("Буква сгенерируется автоматически и потом пойдет отсчет")
time.sleep(3)
## алфавит без  ь, ъ, ы
char_rus = ["а", "б", "в", "г", "д", "е", "ё", "ж", "з", "и", "й", "к", "л", "м", "н", "о", "п", "р", "с", "т", "у", "ф", "х", "ц", "ч", "ш", "щ", "э", "ю", "я"]
rand_char = random.choice(char_rus)
print("Сегодня на букву: " + rand_char.upper())
time.sleep(2)
loc_time = 31
for i in range(loc_time):
    print(f"\r{i} second...", end="", flush=True)
    time.sleep(1)
print("", end='\n')
stop = playsound("erro-2.mp3")
stop
print("Done")
