numbers = [42, 7, 89, 13, 56]
first = 0
second = 0


if len(numbers) > 2:
    for i in numbers:
        if i > first:
            first = i

    numbers.remove(first)
    for i in numbers:
        if i > second:
             second = i 
    
else:
    print("список должен исеть больше 2-х значений")


print(second)