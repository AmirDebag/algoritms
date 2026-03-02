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
maximum = 0

for i in mat:
    for j in i:
        summ += j
        if j > maximum:
            maximum = j

print(f"\nсамое большое значение внутри матрицы: {maximum}", f"\nсумма всех чисел матрицы: {summ}")

row_sums = []

for i in range(row):
    row_sum = sum(mat[i])
    row_sums.append(row_sum)
    print(f"сумма строки {i+1}: ", row_sum)

coloumn_sums = []
for i in range(coloumn):
    coloumn_sum = sum(mat[i])
    coloumn_sums.append(coloumn_sum)
    print(f"сумма столбца {i+1}: ", coloumn_sum)

max_row = row_sums.index(max(row_sums))
print("номер строки с максимальным числом:", max_row + 1)
