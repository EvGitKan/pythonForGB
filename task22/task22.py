# Задача 22: Даны два неупорядоченных набора целых чисел (может быть, с повторениями). Выдать без повторений в порядке возрастания все те числа,
# которые встречаются в обоих наборах. Пользователь вводит 2 числа. n — кол-во элементов первого множества. m — кол-во элементов второго множества. 
# Затем пользователь вводит сами элементы множеств.

n = int(input('Введите кол-во элементов первого множества: '))
m = int(input('Введите кол-во элементов второго множества: '))
array_n = []
array_m = []
array_new = []
for i in range(n):
    array_n.append(int(input(f'Введите {i + 1}-е число множества n: ')))
for i in range(m):
    array_m.append(int(input(f'Введите {i + 1}-е число множества m: ')))

for i in range(len(array_n)):
    if array_n[i] in array_m:
        array_new.append(array_n[i])

print(sorted(set(array_new)))
