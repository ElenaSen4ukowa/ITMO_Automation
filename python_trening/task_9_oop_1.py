'''Задача
1. создать класс Input, принимающий 1 аргумент при инициализfции (Loc)
2. создать объект search (экземпляр класса Input)
3. выведите в консоль значение аргумента Loc, объекта search
'''

class Input:

    def __init__(self, loc):
        self.loc = loc

search = Input('input#search')

print(search.loc)