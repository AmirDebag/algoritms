import random

row = int(input("введите количество строк: "))
coloumn = int(input("введите количество столбцов: "))

mat = []

for i in range(coloumn):
    r = []
    
    for j in range(row):
        j = random.randint(1, 20)
        r.append(j)

    mat.append(r)

print("")

for i in mat:
    for j in i:
        print(j, "" ,end="")
    print()

summ = 0
max = 0

for i in mat:
    for j in i:
        summ += j
        if j > max:
            max = j

print(f"\nсамое большое значение внутри матрицы: {max}", f"\nсумма всех чисел матрицы: {summ}")