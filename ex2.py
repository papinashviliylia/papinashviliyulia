n = int(input('Введите количество чисел:'))
sum_mod = 0
count = 0

a = float(input())

for i in range(n - 1):
    b = float(input())
    if a * b < 0:
        count += 1
        sum_mod += abs(a * b)
    a = b 

print('Количество пар:', count)
print('Сумма модулей:', sum_mod)


