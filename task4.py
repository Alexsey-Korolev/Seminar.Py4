#Задана натуральная степень k.
# Сформировать случайным образом список коэффициентов(значения от 0 до 100) многочлена и записать в файл многочлен степени k.
# Пример k=2 => 2*x^2+4*x = 0

import random

degree = int(input('Введите степень k: '))


def write_file(s):
    with open('task4.txt', 'w') as data:
        data.write(s)


def create_coefficient(n):
    list = []
    for i in range(n + 1):
        list.append(random.randint(0, 100))
    return list


def result(s):
    list = s[::-1]
    string = ''
    if len(list) < 1:
        string = 'x = 0'
    else:
        for i in range(len(list)):
            if i != len(list) - 1 and list[i] != 0 and i != len(list) - 2:
                string += f'{list[i]}x**{len(list) - i - 1}'
                if list[i + 1] != 0:
                    string += ' + '
            elif i == len(list) - 2 and list[i] != 0:
                string += f'{list[i]}x'
                if list[i + 1] != 0:
                    string += ' + '
            elif i == len(list) - 1 and list[i] != 0:
                string += f'{list[i]} = 0'
            elif i == len(list) - 1 and list[i] == 0:
                string += ' = 0'
    return string


coefficient = create_coefficient(degree)
print(result(coefficient))
write_file(result(coefficient))