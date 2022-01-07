a = int(input())
b = int(input())
qs = (a + b)**2
sq = a**2 + b**2
print(*[
    f'Квадрат суммы {a} и {b} равен {qs}'
])
print(*[
    f'Сумма квадратов {a} и {b} равна {sq}'
])