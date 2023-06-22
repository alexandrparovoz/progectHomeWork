# генератор случайного пароля из заданного массива

import random
def pass_gen(count_char=8): # длина пароля 8 знаков
    arr = ['d', 'r', '4', 'i','w', 'x', 'n','q', 'u', 'z']
    passw = []
    for i in range(count_char):
        passw.append((random.choice(arr)))
    return ''.join(passw)

print(pass_gen())