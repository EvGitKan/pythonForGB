# Задача 24: В фермерском хозяйстве в Карелии выращивают чернику. Она растёт на круглой грядке, причём кусты высажены только по окружности.
# Таким образом, у каждого куста есть ровно два соседних. Всего на грядке растёт N кустов. Эти кусты обладают разной урожайностью, поэтому ко
# времени сбора на них выросло различное число ягод — на i-ом кусте выросло ai ягод. В этом фермерском хозяйстве внедрена система автоматического
# сбора черники. Эта система состоит из управляющего модуля и нескольких собирающих модулей. Собирающий модуль за один заход, находясь 
# непосредственно перед некоторым кустом, собирает ягоды с этого куста и с двух соседних с ним. Напишите программу для нахождения максимального 
# числа ягод, которое может собрать за один заход собирающий модуль, находясь перед некоторым кустом заданной во входном файле грядки.

import random
N = int(input('Введите количество кустов: '))
berries = list(random.randint(0, 100) for i in range(N))
print(f'Количество ягод на кустах: {berries}')

count_berries = []
max_count_berries = 0
if N == 1:
    print(f'Максимальное числа ягод, которое может собрать за один заход собирающий модуль = {berries[0]}')
elif N < 1:
    print(f'Максимальное числа ягод, которое может собрать за один заход собирающий модуль = 0')
else:
    for i in range(len(berries)):
        if i > 0 and i < len(berries) - 1:
            count_berries.append(berries[i] + berries[i - 1] + berries[i + 1])
        elif i == 0:
            count_berries.append(berries[i] + berries[len(berries) - 1 - i] + berries[i + 1])
        else:
            count_berries.append(berries[i] + berries[len(berries) - 1 - i] + berries[i - 1])
    print(f'Максимальное числа ягод, которое может собрать за один заход собирающий модуль = {max(count_berries)}')
