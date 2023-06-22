# создание бинарного дерева с сортировкой по возрстнию и убванию
# не я сделал но понятен код
class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data


class BinaryTree:    #  я понимаю - это вершина дрэва
    def __init__(self):
        self.root = None

    def insert(self, data): # а это вложение значения в вершину
        if not self.root:
            self.root = Node(data)
        else:
            self._insert(data, self.root)

    def _insert(self, data, node):
        if data < node.data:  # если элемент меньше чем значение узла то милости просим в левый ряд
            if node.left is None:  # если у  узла нет значения слева,то теперь передаваемое значение .....
                node.left = Node(data)  #не понятненько ?
            else:
                self._insert(data, node.left) # если у узла слева свободно - милости просим значение стать новым узлом слева
        else:     # а теперь если значение больше узла то все тоже самое но справа
            if node.right is None:
                node.right = Node(data)
            else:
                self._insert(data, node.right)

    def in_order_traversal(self, node, result): #  не совсем понятненько
        if node.left:
            self.in_order_traversal(node.left, result)
        result.append(node.data)
        if node.right:
            self.in_order_traversal(node.right, result)
        return result

    def get_ascending_order(self):
        result = []
        return self.in_order_traversal(self.root, result)

    def get_descending_order(self):
        result = []
        return self.in_order_traversal(self.root, result)[::-1] #  вот это хитро. Не надо новой функции - делаем перевертыш
    # def descendingNode(self):  # по убыванию с корнем в середине
    #     if self.data.right:
    #         self.data.right.descendingNode()  # та же рекурсия
    #     print(self.root, end=' ')
    #     if self.data.left:
    #         self.data.left.descendingNode()

def create_tree(numbers):
    tree = BinaryTree()
    for number in numbers:  # собираем дрэво как бусы на нитку
        tree.insert(number)
    return tree


numbers = [4, 2, 3,6, 11, 9,  1, 5]
tree = create_tree(numbers)
print("Ascending order:", tree.get_ascending_order())
print("Descending order:", tree.get_descending_order())
print(" order:", tree.descendingNode())