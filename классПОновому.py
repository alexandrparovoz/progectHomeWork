
# новая генерация класса
# красиво!!!!
from dataclasses import dataclass
@dataclass
class User:
    user_id: int
    name: str
    age: int
    email: str
def get_info(user: User):  # обращаем внимание - табуляции нет
    return f' Возраст {user.name} - {user.age},\'' \
               f'а адрес {user.email}'

user1: User = User(22, 'ivan', 34, 'ivan@gmail.com')
print(get_info(user1)) # объект внутри метода

