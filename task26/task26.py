# Напишите программу, которая на вход принимает два числа A и B, и возводит число А в целую степень B с помощью рекурсии.

# *Пример:*

# A = 3; B = 5 -> 243 (3⁵)
#     A = 2; B = 3 -> 8 

a = int(input('Введите число A: '))
b = int(input('Введите число B: '))
def degree(num1, num2):
    if num2 == 1:
        return num1
    else:
        return degree(num1 * a, num2 - 1)

print(degree(a, b))