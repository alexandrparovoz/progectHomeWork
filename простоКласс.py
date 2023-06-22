class Cars:
    def __init__(self, model, year, speed, value):
        self.__model = model
        self.__year = year
        self.__speed = speed
        self.__value = value

    def get_model(self):
        return self.__model

    def get_year(self):
        return self.__year

    def get_speed(self):
        return self.__speed

    def get_value(self):
        return self.__value

    def discriptiveName(self):
        fullName = f'{self.__year} year {self.__model}, value is {self.__value} sm3, speed - {self.__speed} km/h.'
        return fullName


car = Cars('Audi', 2020, '200', '2400')

print(car.discriptiveName())