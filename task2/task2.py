# Задача 2: Найдите сумму цифр трехзначного числа.

number = int(input('Введите трехзначное число: '))
sum = int(number % 10 + number % 100 / 10 + number / 100)
print(sum)