# 2. Функция на вход получает два произвольных числа. Вывести в консоль наибольшее из чисел.
def max_digit(a, b):
    if a > b:
        return a
    elif a == b:
        return 'Числа равны'
    else:
        return b

print(max_digit(15, 1))


# 3. Функция на вход получает два произвольных числа. Вывести в консоль “yes”, если они отличаются друг от друга на 135, иначе вывести на экран “No”
def difference(a, b) -> str:
    if abs(a - b) == 135:
        return 'yes'
    else:
        return 'No'

print(difference(1, 139))


# 4. Функция на вход получает произвольное число от 1 до 12 (номер месяца). Вывести название сезона года в консоль (зима, весна, лето, осень)
def season(month: int) -> str:
    if 1 <= month <= 12:
        if month in range(3, 6):
            return 'spring'
        elif month in range(6, 9):
            return 'summer'
        elif month in range(9, 12):
            return 'autumn'
        else:
            return 'winter'
    else:
        return 'Error input!'

print(season(12))

# 5. Функция на вход получает три произвольных числа. Если все числа больше 10, то вывести на экран “yes”, иначе “no”;
def func(a, b, c) -> str:
    if a > 10 and b > 10 and c > 10:
        return 'yes'
    else:
        return 'no'

print(func(9, 16, 99))

# 6. Функция на вход получает список, состоящий из 5 произвольных чисел. Найти количество положительных чисел среди них.
def func_lst(lst: list) -> (int, str):
    if len(lst) == 5:
        count = 0
        for el in lst:
            if el > 0:
                count += 1
        return count
    else:
        return 'Введите корректное количество чисел'

a = [1, 0, -8, 63, -3]

print(func_lst(a))

'''
7. Функция на вход получает 2 переменные.
a. Кол-во лет (int)
b. Кол-во месяцев (int)
Вывести в консоль количество дней за это время. Считать, что в каждом месяце 29 дней.
'''
def days(year: int, month: int) -> int:
    return (year * 12 + month) * 29

print(days(2, 11))