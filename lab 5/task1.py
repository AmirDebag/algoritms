n = int(input("введите количество элементов массива: "))
mass = []

if n > 0:
    for i in range(1, n + 1):

        a = int(input(f"введите {i} число: "))

        mass.append(a)
else:
    print("введите число больше 0!")

print(mass)