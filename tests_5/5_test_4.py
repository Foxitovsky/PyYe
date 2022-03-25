mounth = int(input())

if mounth in [1, 12, 5, 3, 7, 8, 10]:
    print('31')
elif mounth in [4, 6, 9, 11]:
    print("30")
else:
    print("28")