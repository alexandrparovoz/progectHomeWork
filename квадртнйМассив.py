# квадратный массив
# обратная диагональ - единицы, ниже - двойки, выше - нули

size = int(input())
for i in range(size):
    for j in range(size):
        if i + j == size - 1:
            print(1, end=' ')
        elif i >= size - j:
            print(2, end=' ')
        else:
            print(0, end=' ')
    print()