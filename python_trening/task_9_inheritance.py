class Mammal:
    className = 'Млекопитающее'

class Dog(Mammal):  # класс Dog наследуется из класса Mammal
    species = 'Canis lupus'


dog = Dog()
print(dog.className)  # Млекопитающее