mass = [-83, 47, -12, 95, -56, 18, -3, 72, -29]
even = []
positive = []
negative = []

for i in mass:
    if i % 2 == 0:
        even.append(i)

    if i > 0:
        positive.append(i)  
    else:
        negative.append(i)
            
print(f"количество чётных чисел - {len(even)}\nколичество положительных чисел - {len(positive)}\nколичество отрицательных чисел - {len(negative)}")
