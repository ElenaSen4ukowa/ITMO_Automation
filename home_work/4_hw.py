'''
1. создайте класс прямоугольника.
a. атрибуты - прямоугольнику можно задать ширину и высоту
b. методы - реализуйте 2 метода:
i. расчет площади прямоугольника
ii. расчет периметра прямоугольника
c. создайте 3 объекта, рассчитайте площадь и периметр для каждого. Результаты выводить в консоль.
'''
class Rectangle:

    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area_of_rectangle(self):
        print(self.width * self.height)

    def perimeter_of_rectangle(self):
        print(2 * (self.width + self.height))

rectangle_first = Rectangle(2, 3)
rectangle_second = Rectangle(5, 10)
rectangle_third = Rectangle(9, 3)

rectangle_first.area_of_rectangle()
rectangle_first.perimeter_of_rectangle()
rectangle_second.area_of_rectangle()
rectangle_second.perimeter_of_rectangle()
rectangle_third.area_of_rectangle()
rectangle_third.perimeter_of_rectangle()


''' 2. Создайте класс Math.
a. Создайте два атрибута — a и b.
b. Напишите методы
i. addition — сложение,
ii. multiplication — умножение,
iii. division — деление,
iv. subtraction — вычитание.
При передаче в методы параметров a и b с ними нужно производить соответствующие действия и печатать ответ.'''

class Math:
    def __init__(self, a, b):
        self.a = a
        self.b = b
    def addition(self):
        print(self.a + self.b)
    def multiplication(self):
        print(self.a * self.b)
    def division(self):
        print(self.a / self.b)
    def subtraction(self):
        print(self.a - self.b)

task = Math(100, 20)

task.addition()
task.multiplication()
task.division()
task.subtraction()


'''3. откройте страницу https://demoqa.com/text-box
На странице присутствует сайдбар (меню слева)
a. Создайте объекты для каждой кнопки 2-го уровня вложенности (“Text Box” и т.п.)
Для этого опишите класс.
Каждый объект должен содержать в себе:
- текст кнопки (пример: “Text Box”)
- тип - одинаковый для всех “Кнопка”
- локатор - не заполнять, сделать по умолчанию пустой строкой
Также на кнопку можно нажать - реализуйте метод. Метод возвращает текст “Клик по кнопке { ТЕКСТ КНОПКИ }”
b. выведите текст для каждой кнопки
c. вызовите “Клик” для каждой кнопки'''

class Button:
    type: str = 'Кнопка'
    def __init__(self, text, loc=None):
        self.text = text
        self.loc = loc
    def click(self):
        return 'Клик по кнопке {}'.format(self.text)

button_one = Button('Text Box')
print(button_one.text)
print(button_one.click())

button_two = Button('Check Box')
print(button_two.text)
print(button_two.click())

button_three = Button('Radio Button')
print(button_three.text)
print(button_three.click())

button_four = Button('Web Tables')
print(button_four.text)
print(button_four.click())

button_five = Button('Buttons')
print(button_five.text)
print(button_five.click())

button_six = Button('Links')
print(button_six.text)
print(button_six.click())

button_seven = Button('Broken Links - Images')
print(button_seven.text)
print(button_seven.click())

button_eight = Button('Upload and Download')
print(button_eight.text)
print(button_eight.click())

button_nine = Button('Dynamic Properties')
print(button_nine.text)
print(button_nine.click())
