# пузырьковый метод сортировки массива списков

from random import randint
n = 10
a = []
for i in range(10):  # создаем рандомный массив
    a.append(randint(1, 100))
print(a)

for i in range(n-1):   # пузырьковый метод
    for j in range(n - i - 1): # пчему n - i - 1. чтобы не включать в итерацию уже стоящие в конце
        if a[j] > a[j + 1]:    # массива большие элементы, ставшие там за первую итерацию
            a[j], a[j + 1] = a[j + 1], a[j]
print(a)

# этот же метод с циклом while
# сначала тот же рандомный массив
i = 0
while i< n - 1:
    j = 0
    while j < n - i - 1:
        if a[j] > a[j + 1]:
            a[j], a[j + 1] = a[j + 1], a[j]
            j += 1
        i += 1
    print(a)