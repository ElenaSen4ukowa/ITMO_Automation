''' Задача
1. Создать класс Page, принимающий 1 аргумент при инициализации url
2. В этом классе реализовать метод get(), который выводит на печать url
3. Создать объект home и вызовите метод get()
'''

class Page:

    def __init__(self, url):
        self.url = url

    def get(self):
        print(self.url)

home = Page('https://stepik.ru')
home.get()