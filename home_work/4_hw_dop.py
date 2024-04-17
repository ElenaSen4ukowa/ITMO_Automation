''' Доп*
4. В отдельном файле напишите программу с классом Car.
a. Создайте конструктор класса Car. Создайте атрибуты класса Car — color (цвет), type (тип), year (год).
b. Напишите пять методов.
i. Первый — запуск автомобиля, при его вызове выводится сообщение «Автомобиль заведен».
ii. Второй — отключение автомобиля — выводит сообщение «Автомобиль заглушен».
iii. Третий — присвоение автомобилю года выпуска. Четвертый метод — присвоение автомобилю типа.
iv. Пятый — присвоение автомобилю цвета.'''

class Car:
    def __init__(self, color, type, year):
        self.color = color
        self.type = type
        self.year = year
    def starting_the_car(self):
        print('Автомобиль заведен')
    def switch_off_the_car(self):
        print('Автомобиль заглушен')
    def year_of_issue(self):
        print(self.year)
    def type_of_the_car(self):
        print(self.type)
    def color_of_the_car(self):
        print(self.color)
automobile = Car('red', 'pickup', 2000)
automobile.starting_the_car()
automobile.switch_off_the_car()
automobile.year_of_issue()
automobile.type_of_the_car()
automobile.color_of_the_car()
