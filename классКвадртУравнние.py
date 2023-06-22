# класс квадратно уравнение с формулой в методе класса
# ax**2 + bx + c = 0
# d = b**2 - 4*a*c
import math
class Square_root:
    def __init__(self, a, b, c):
        self.__a = a
        self.__b = b
        self.__c = c
    def get_a_root(self):
        return self.__a
    def get_b_root(self):
        return self.__b
    def get_c_root(self):
        return self.__c

    def discrim_root(self):
        res = self.get_b_root() ** 2 - 4 * self.get_a_root() * self.get_c_root()
        if res < 0:
            return False
        return res

    def solution(self):
        if self.discrim_root() == 0:
            root = (- self.get_b_root()) / 2 * self.get_a_root()
            return root
        elif self.discrim_root() > 0:
            root1 = ((- self.get_b_root()) + math.sqrt(self.discrim_root()))/ 2 * self.get_a_root()
            root2 = ((- self.get_b_root()) - math.sqrt(self.discrim_root())) / 2 * self.get_a_root()
            return root1, root2







root1 = Square_root(3, 6, 3)  #  D=0
root2 = Square_root(2, 6, 4)  #  D>0
root3 = Square_root(3, 6, 4)  #  D<0
print(root2.solution())