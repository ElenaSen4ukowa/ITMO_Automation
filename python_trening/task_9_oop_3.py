class Soda:

    def __init__(self, additive=None):
        self.additive = additive

    def show_my_drink(self):
        if self.additive:
            print(f'Газировка и {self.additive}')
        else:
            print('Обычная газировка')

drink_with = Soda('salted caramel')
drink_without = Soda()

drink_with.show_my_drink()
drink_without.show_my_drink()