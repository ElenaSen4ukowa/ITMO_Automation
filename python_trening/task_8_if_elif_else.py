# Программа проверяет, является ли число положительным
# или отрицательным и выводит соответствующее сообщение

num = 3

if num >= 0:
    print('Число больше или равно 0')
else:
    print('Число отрицательное')

# str_2 сожержит ли в себе str_1?
def task_yes_no(str_1, str_2):
    if str_1 in str_2:
        return 'Да'
    else:
        return 'Нет'

task_yes_no(str_1='test', str_2='testing')

num_float = 3.4

if num_float > 0:
    print('Положительное число')
elif num_float == 0:
    print('Ноль')
else:
    print('Число отрицательное')

permit_print = True

if num > 0 and permit_print:
    print('num - положительное число')
elif not permit_print:
    print('Печать запрещена')

# Напишите программу, которая отвечает, какое Ваше текущее звание, исходя из курса
def student_rank(year_of_study):
    if year_of_study in range(1, 5):
        return 'Вы - бакалавр'
    elif year_of_study in range(5, 7):
        return 'Вы - магистр'
    elif year_of_study in range(7, 10):
        return 'Вы - аспирант'
    else:
        return 'Введите корректный год обучения'

student_rank(5)

a = 5

if a > 100 or a < -100:
    print('-')
else:
    print('+')
