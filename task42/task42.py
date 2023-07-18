# Задача 42: Узнать какая максимальная households в зоне минимального значения population

# Решение:

df[df['population']==df['population'].min()]['households'].max()
# 4.0

# Вариант 2:

df[df['population']==df['population'].min()]['households'].agg(['max'])
# max    4.0
# Name: households, dtype: float64