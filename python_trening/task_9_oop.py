# class - ключевое слово создания класса
# Button - имя класс
# Тело класса (атрибуты и методы) пишутся с отступом подстрокой объявления класса
# def __init__(self) - Конструктор класса - это стандарт.метод для объявления атрибутов. Это метод-инициализатор, который запускается сразу же после создания объекта

class Button:

    type: str = 'Кнопка'

    def __init__(self, text, link):
        self.text = text
        self.link = link

# Создаем экземпляры класса
home = Button('Домой', '/home')
catalog_msk = Button('Каталог', '/msk/catalog')

# Получаем доступ к атрибутам
print(home.text)
print('Кнопка ' + home.text + ' имеет ссылку ' + home.link)

print('\n')

print(catalog_msk.text)
print('Кнопка ' + catalog_msk.text + ' имеет ссылку ' + catalog_msk.link)

class ButtonTwo:

    def __init__(self, text, link, loc):
        self.text = text
        self.link = link
        self.loc = loc

    def click(self):
        return "Клик по локатору - {}".format(self.loc)

# Создаем экземпляры класса
home_two = ButtonTwo('Домой', '/home', 'button#home')

# Вызываем метод
print(home_two.click())
