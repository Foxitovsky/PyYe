num = int(input())
one = num % 10
two = (num // 10) % 10
three = num // 100
sum = one + two + three
przv = one * two * three

print(one, two, three, sep=', ')
print(f'Сумма цифр = {sum}')
print(f'Произведение цифр = {przv}')