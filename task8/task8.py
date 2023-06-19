# Задача 8: Требуется определить, можно ли от шоколадки размером n × m долек отломить k долек, если разрешается сделать один разлом
# по прямой между дольками (то есть разломить шоколадку на два прямоугольника).

# *Пример:*

# 3 2 4 -> yes
# 3 2 1 -> no


n = int(input('Введите n: '))
m = int(input('Введите m: '))
k =int(input('Введите количество долек, которые нужно отломить за один раз: '))
if k == n or k == m:
    print('Столько отломить можно!')
elif n * m % k == n or n * m % k == m:
    print('Столько отломить можно!')
elif k == n * m / 2:
    print('Столько отломить можно!')
else:
    print('За один раз столько не отломишь :(')