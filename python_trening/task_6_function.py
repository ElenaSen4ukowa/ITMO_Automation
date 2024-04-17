def add(x, y):
    return x + y

# вызываем функцию
print(add(2, 2))
print(add('i a', 'm tester'))


# аргументы с и d не обязательные, их значения по умолчанию
def arg(a, b, c=2, d=3):
    return a + b + c + d

print(arg(1, 1, 1, 1))

print(arg(2, 2))

# В третьем аргументе тип данных int! Поэтому будет ошибка:
# print(arg(2, 2, '1', 1))

def range_arg(a, b, c, d):
    return a + ' ' + b + ' ' + c + ' ' + d

print(range_arg('1', '2', '3', '4'))

print(range_arg('1', '2', d='3', c='4'))


def task_1(a=(1, 2, 3, 4)):
    return a[1]



def task_2(radius, pi=3.14159):
    return pi * radius ** 2