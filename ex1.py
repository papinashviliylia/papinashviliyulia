stroka = input('Введите числа через пробел:')
numbers = []

for i in stroka.split():
    numbers.append(int(i))

for j in range(1, len(numbers)+1):
    if j not in numbers:
        print('Пропущенное число:', j)