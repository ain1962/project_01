# Задача 1.3.

# Напишите скрипт, который принимает от пользователя номер месяца, 
# а возвращает количество дней в нем.
# Результат проверки вывести на консоль
# Допущение: в феврале 28 дней
# Если номер месяца некорректен - сообщить об этом

# Например,
    # Введите номер месяца: 3
    # Вы ввели март. 31 дней

    # Введите номер месяца: 2
    # Вы ввели февраль. 28 дней

    # Введите номер месяца: 15
    # Такого месяца нет!

# Решение

m= int(input("Введите номер месяца: "))
s={
    '1':31,
    '2':28,
    '3':31,
    '4':30,
    '5':31,
    '6':30,
    '7':31,
    '8':31,
    '9':30,
    '10':31,
    '11':30,
    '12':31,
}

if m==1 :
  print('Вы ввели январь.', s['1'],'дней')
if m==2:
   print('Вы ввели февраль.', s['2'], 'дней')
if m==3 :
   print('Вы ввели март.', s['3'],'дней')
if m==4 :
   print('Вы ввели апрель.', s['4'],'дней')
if m==5 :
   print('Вы ввели май.', s['5'],'дней')
if m==6 :
  print('Вы ввели июнь.', s['6'],'дней')
if m==7 :
  print('Вы ввели июль.', s['7'],'дней')
if m==8 :
  print('Вы ввели август.', s['8'],'дней')
if m==9 :
  print('Вы ввели сентябрь.', s['9'],'дней')
if m==10 :
  print('Вы ввели октябрь.', s['10'],'дней')
if m==11 :
  print('Вы ввели ноябрь.', s['11'],'дней')
if m==12 :
  print('Вы ввели декабрь.', s['12'],'дней')  

if 0<m>12 or m==0:
  print('Такого месяца нет!')