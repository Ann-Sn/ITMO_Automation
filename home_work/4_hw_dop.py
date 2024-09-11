
class Car:

    def __init__(self, color :str, type : str, year :int) -> str:
        self.color = color
        self.type = type
        self.year = year

    def start(self):
        return print('Автомобиль заведен')

    def stop(self):
        return print('Автомобиль заглушен')

    def year_of_car(self):
        return print('Год автомобиля - {}'.format(self.year))

    def type_of_car(self):
        return print('Тип автомобиля - {}'.format(self.type))

    def color_of_car(self):
        return print('Цвет автомобиля - {}'.format(self.color))

car_1 = Car('Красный', 'Хетчбек', '2007')
car_1.start()
car_1.stop()
car_1.year_of_car()
car_1.type_of_car()
car_1.color_of_car()
