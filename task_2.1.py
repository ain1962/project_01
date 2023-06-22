# Задача 2.1. 

# Создайте две функции maximum и minimum,
# которые получают список целых чисел в качестве входных данных 
# и возвращают наибольшее и наименьшее число в этом списке соответственно.
# Например,
# * [4,6,2,1,9,63,-134,566]         -> max = 566, min = -134
# * [-52, 56, 30, 29, -54, 0, -110] -> min = -110, max = 56
# * [42, 54, 65, 87, 0]             -> min = 0, max = 87
# * [5]                             -> min = 5, max = 5
# функции sorted, max и min использовать нельзя!

a=[4,6,2,1,9,63,-134,566]
b=[-52, 56, 30, 29, -54, 0, -110]
c=[42, 54, 65, 87, 0]
d=[5]


def get_min(arr):
    
    minimum = arr[0]

    for num in arr[1:]:
        if num < minimum:
            minimum = num      

    return [minimum]

def get_max(arr):
    
    maximum = arr[0]

    for num in arr[1:]:
        if num > maximum:
            maximum = num      

    return [maximum]    
    
print('min=',get_min(a),', max=',get_max(a))
print('min=',get_min(b),', max=',get_max(b))
print('min=',get_min(c),', max=',get_max(c))
print('min=',get_min(d),', max=',get_max(d))
