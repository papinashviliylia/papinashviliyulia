stroka = input('Введите числа через пробел:')
numbers = []

for i in stroka.split():
    numbers.append(int(i))

for j in numbers:
    count = 0
    for k in numbers:
        if k == j:
            count += 1
    if count > 1:
        print('Число, которое повторяется:', j)
        break
