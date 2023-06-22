# создаем двухмерный массив

n = int(input())  # как правило ВЫСОТА строк - СТРОКИ
m = int(input())  # ШИРИНА строк _ СТОЛБЦЫ
massive = []
a = 1
for i in range(n):
    submassive = []
    for j in range(m):
        submassive.append(a)  # заполняем массив числами от единицыдо n
        a += 1
    massive.append(submassive)
    print(massive)  # выводит немного коряво

#а теперь вывод массива правильный
for i in massive:
    for j in i:
        print(j, end='\t') # каждая ячейка имеет 4 пробела
    print() # разделение по пустой строке

