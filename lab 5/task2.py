mass = [12, -5, 34, 0, -18, 27, 9, 141]
x = 0
max = 0
min = 0
arif = 0

for i in mass:
    x += i
    n = i

    if n > max:
        max = i
    
    if n < min:
        min = i

    arif = x / len(mass)
            
print(f"сумма - {x}, минимальное значение - {min}, максимальное значение - {max}, среднее арифметическое - {arif}")
