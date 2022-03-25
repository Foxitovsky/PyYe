x, y, z = int(input()), int(input()), int(input())

if x == y == z:
    print("Равносторонний")
elif x == y != z or x != y == z or y != z == x:
    print("Равнобедренный")
else:
    print("Разносторонний")