# # Задача 32: Определить индексы элементов массива (списка), значения которых принадлежат заданному диапазону 
# (т.е. не меньше заданного минимума и не больше заданного максимума). 
# Список можно задавать рандомно
# На входе : [ 1, 5, 88, 100, 2, -4]
# 33
# 200
# Ответ: [2, 3]

from random import randint

def Task_32(minimum, maximum):
    array = [randint(0, 200) for _ in range(randint(5, 10))]
    print(array)
    result = [i for i in range(len(array)) if maximum > array[i] > minimum]
    return result
minimum = int(input('Введите минимум -> '))
maximum = int(input('Введите максимум -> '))
print(Task_32(minimum, maximum))