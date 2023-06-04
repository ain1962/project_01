# Задача 1.1.

# Есть строка с перечислением песен

my_favorite_songs = 'Waste a Moment, Staying\' Alive, A Sorta Fairytale, Start Me Up, New Salvation'

# Выведите на консоль с помощью индексации строки, последовательно: первый трек, последний, второй, второй с конца
# Нельзя переопределять my_favorite_songs и запятая не должна выводиться.


print(len(my_favorite_songs)) # количество символов в строке (длина строки)
print(my_favorite_songs[0:14]) # первый трек
print(my_favorite_songs[-13:-1]) # последний трек
print(my_favorite_songs[16:23]) # второй трек
print(my_favorite_songs[-26:-15]) # второй трек с конца

a,b,c,d = my_favorite_songs[0:14],my_favorite_songs[16:23],my_favorite_songs[-26:-15],my_favorite_songs[-13:-1]
print(a,b,c,d) # вывод треков без запятой


