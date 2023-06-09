# Задача 1.2.

# Пункт A. 
# Приведем плейлист песен в виде списка списков
# Список my_favorite_songs содержит список названий и длительности каждого трека
# Выведите общее время звучания трех случайных песен в формате
# Три песни звучат ХХХ минут

my_favorite_songs = [
    ['Waste a Moment', 3.03],
    ['New Salvation', 4.02],
    ['Staying\' Alive', 3.40],
    ['Out of Touch', 3.03],
    ['A Sorta Fairytale', 5.28],
    ['Easy', 4.15],
    ['Beautiful Day', 4.04],
    ['Nowhere to Run', 2.58],
    ['In This World', 4.02],
]

# Решение

three_songs_sum = my_favorite_songs[3][1] + my_favorite_songs[5][1] + my_favorite_songs[8][1]
#three_songs = round(three_songs, 2)
print('Три песни звучат', three_songs_sum, 'минут')



# Пункт B. 
# Есть словарь песен 
# Распечатайте общее время звучания трех случайных песен
# Вывод: Три песни звучат ХХХ минут.

my_favorite_songs_dict = {
    'Waste a Moment': 3.03,
    'New Salvation': 4.02,
    'Staying\' Alive': 3.40,
    'Out of Touch': 3.03,
    'A Sorta Fairytale': 5.28,
    'Easy': 4.15,
    'Beautiful Day': 4.04,
    'Nowhere to Run': 2.58,
    'In This World': 4.02,
}

# Решение
from random import sample
time_songs=list(my_favorite_songs_dict.values())
# Выбирает параметр - время звучания песен

r = sample(time_songs, 3) # определяем колличество случайных песен

print(('Три песни звучат', sum(r), 'минут'))



# Дополнительно для пунктов A и B
# Пункт C.
# Сгенерируйте случайные песни с помощью модуля random


import random


a=random.choice(my_favorite_songs)
b=random.choice(my_favorite_songs)
c=random.choice(my_favorite_songs)

print("несколько случайных песен из списка списков", a, b, c)

three_songs=list(my_favorite_songs_dict.items())
# формитуем список песен
list_songs = sample(three_songs, 3)
print("несколько случайных песен из словоря:", list_songs)


# Дополнительно 
# Пункт D.
# Переведите минуты и секунды в формат времени. Используйте модуль datetime 

import datetime

# Ввод количества минут
minutes = int(input("Введите минуты: "))
# Вывод часов и минут
print(str(datetime.timedelta(minutes=minutes)))

# Ввод секунд
n= int(input("Введите секунды: "))
time_format = str(datetime.timedelta(seconds = n)) 
#Вывод времени
print("Формат времени:-",time_format) 
