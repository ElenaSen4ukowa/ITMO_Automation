'''Задача*
1. добавить к классу Input, принимающему 1 аргумент при инициализfции (Loc), атрибут объекта text
2. в этом же файле создать: класс Button, класс Title, класс Link
3. для каждого класса пропишите атрибуты text и loc
4. создать каждому из 4х классов объекты с любыми данными
5. вывести в консоль text и loc каждого класса
'''

'''5. продолжение задачи*...
в файле task_9_oop_1.py
c. наследуйте все классы от класса Checks
i. чтобы использовать класс из другого файла его нужно импортировать
from название файла(без расширения) import название класса
d. переделайте все 4 класса в файле task_9_oop_1.py так чтоб в объектах можно было использовать методы родительского класса
e. распечатайте в консоль результаты метода .check_text() вызванного от каждого объекта классов файла task_9_oop_1.py
'''

from task_9_checks import Checks
class Input(Checks):
    def __init__(self, text, loc):
        super().__init__(loc)
        self.text = text
        self.loc = loc
class Button(Checks):
    def __init__(self, text, loc):
        super().__init__(loc)
        self.text = text
        self.loc = loc
class Title(Checks):
    def __init__(self, text, loc):
        super().__init__(loc)
        self.text = text
        self.loc = loc
class Link(Checks):
    def __init__(self, text, loc):
        super().__init__(loc)
        self.text = text
        self.loc = loc

search = Input('Поиск', 'input#search')

home = Button('Домой', 'button#home')

head = Title('Заголовок', 'title#head')

url = Link('Ссылка', 'link#url')

print(search.check_text())
print(home.check_text())
print(head.check_text())
print(url.check_text())
