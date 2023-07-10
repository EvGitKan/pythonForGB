# Задача 32: Определить индексы элементов массива (списка), значения которых принадлежат заданному диапазону (т.е. не меньше заданного
# минимума и не больше заданного максимума)
from random import randint

print(list:=[randint(1, 50) for i in range(randint(5, 15))])
min_number = int(input('Введите минимум: '))
max_number = int(input('Введите максимум: '))
for i in range(len(list)):
    if min_number <= list[i] <= max_number:
        print(i)