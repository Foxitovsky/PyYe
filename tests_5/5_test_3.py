import statistics

a, b, c = int(input()), int(input()), int(input())
data = a + b + c - min(a, b, c) - max(a, b, c)
print(data)