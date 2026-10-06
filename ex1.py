n = int(input('Сколько чисел будете вводить?'))
sum_cube = 0

for i in range(n):
    x = float(input('Введите число:'))
    if x < 0:
        sum_cube = sum_cube + (-((-x) ** (1/3)))

print(sum_cube)