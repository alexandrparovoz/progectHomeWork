# функция генератор в другой функции геераторе

def gen(a):
    for i in x:
        yield from range(1, i + 1) # начинаем с единицы и добавляем единицу. чтобы захватить само число
        print()
x = [5, 10, 22]
for j in gen(x):
    print(j, end=' ')

