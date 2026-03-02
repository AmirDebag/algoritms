numbers = [-999, -450, -123, -50, -7, -1, 0, 3, 8, 15, 27, 42, 64, 99, 150, 237, 389, 512, 777]

while True:
    src = int(input("введите число для поиска: "))

    if src in numbers:
        print("индекс найденного числа - ", numbers.index(src))
        break   
    else:
        print("такого числа нету в списке\n")
        pass