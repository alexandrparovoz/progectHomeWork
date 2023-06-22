# рекурсия на примереподсчета вхождения символов в сторку

def count(st, ch):
    if st == '': # базовый случай к которому стремится рекурсия
        return 0
    tail = st[1: len(st)]  # каждую итерацию отбрезаем строку  на один элемент спереди
    if ch == st[0]:
        return 1 + count(tail,ch) # если есть совпадение прибавляем единицу
    else:
        return count(tail, ch)

string = input()
ch = input()
print("'%s' появляется '%d' раз в строке '%s'" % (ch, count(string, ch), string))

