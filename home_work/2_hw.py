# Задача 1
def task_1() -> (int, float, str, list, bool):
    a: int = 3
    b: float = 5.13
    string: str = 'Hello, World!'
    lst: list = [1, 2, 3, 4, 5, 6, 7]
    flag: bool = True

    return type(a), type(b), type(string), type(lst), type(flag)  # возврат типов данных каждой переменной

print(task_1())

# Задача 2
def task_2() -> list:
    a: list = [1, 2, 3, 5, 8, 13, 21]  # последовательность Фибоначчи
    return a[0:3]                      # возврат первых 3 значений последовательности Фибоначчи из списка а

print(task_2())

# Задача 3
def task_3(x: int) -> int:
    return x ** 2  # возврат квадрата числа x

digit = 5

print(task_3(digit))