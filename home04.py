# Напишите функцию для транспонирования матрицы
import random
from collections.abc import Hashable
from typing import Any

SIZE_W = 4
SIZE_H = 4

matrix = [[0 for x in range(SIZE_W)] for y in range(SIZE_H)]

for i in range(len(matrix)):
    for j in range(len(matrix[0])):
        matrix[i][j] = random.randint(0, 20)


# print(matrix)


def my_func(my_matrix: list) -> list:
    matrix_trance = [[0 for x in range(len(my_matrix))] for y in range(len(my_matrix[0]))]
    for i in range(len(my_matrix)):
        for j in range(len(my_matrix[0])):
            matrix_trance[j][i] = my_matrix[i][j]

    return matrix_trance


# print(my_func(matrix))


# Напишите функцию принимающую на вход только ключевые параметры и возвращающую словарь,
# где ключ - значение переданного аргумента, а значение - имя аргумента.
# Если ключ не хешируем, используйте его строковое представление.


def f(**kwargs) -> dict:
    my_dict = {}
    for key, item in kwargs.items():
        if not isinstance(item, Hashable):
            item = str(item)
        my_dict[item] = key

    return my_dict


# print(f(a=5, b=6, my=[1, 2]))


# Возьмите задачу о банкомате из семинара 2. Разбейте её
# на отдельные операции — функции. Дополнительно сохраняйте
# все операции поступления и снятия средств в список.

TAKE_OFF_TAX = 0.015
EVERY_THIRD_OPERATION_TAX = 0.03

WEALTH_TAX = 0.1
WEALTH = 5_000_000

START = 0

MIN_TAKE_OFF_TAX = 30
MAX_TAKE_OFF_TAX = 600

MULTIPLICITY = 50

sum_ = START
operation_count = 0


while True:
    choice = int(input('Choose an action: '
                       '\n1 - Put money'
                       '\n2 - Take off money'
                       '\n3 - Exit\n'))
    match choice:
        case 1:
            ...
        case 2:
            ...
        case 3:
            break

# ✔ Функция получает на вход список чисел и два индекса.
# ✔ Вернуть сумму чисел между между переданными индексами.
# ✔ Если индекс выходит за пределы списка, сумма считается
# до конца и/или начала списка.


my_list = [11, 33, 22, 44, 2, 4, 55]
index1, index2 = -2, 66


def my_func_01(my_list: list[int], index01: int, index02: int) -> int:
    sum_0 = 0
    max_index = max(index01, index02)
    min_index = min(index01, index02)

    if max_index >= len(my_list):
        max_index = len(my_list) - 1
    if min_index < 0:
        min_index = 0

    for i in range(min_index, max_index + 1):
        sum_0 += my_list[i]

    return sum_0


# print(my_func_01(my_list, index1, index2))


# ✔ Функция получает на вход словарь с названием компании в качестве ключа
# и списком с доходами и расходами (3-10 чисел) в качестве значения.
# ✔ Вычислите итоговую прибыль или убыток каждой компании. Если все компании
# прибыльные, верните истину, а если хотя бы одна убыточная — ложь.

dict_ = {'Google': [23, 45, -67, 34, -5],
         'Яндекс': [56, 12, 78, -5, 3, -90],
         'Amazon': [4, 4, 4, -5, 12, 90]}


def funct(my_d: dict) -> bool:
    for item in my_d.values():
        profit = sum(item)
        if profit < 0:
            return False

    return True


# print(funct(dict_))

# Создайте несколько переменных заканчивающихся и не оканчивающихся на «s».
# ✔ Напишите функцию, которая при запуске заменяет содержимое переменных
# оканчивающихся на s (кроме переменной из одной буквы s) на None.
# ✔ Значения не удаляются, а помещаются в одноимённые переменные без s на конце.


def funct_02(**kwargs: str) -> dict[Any, Any | None]:
    dict_0 = {}
    for key, item in kwargs.items():
        if item[-1] == 's' and len(item) != 1:
            dict_0[item[:-1:]] = item[:-1:]
            dict_0[key] = None
        else:
            dict_0[key] = item
    return dict_0

# print(funct_02(a='rs', b='s', c='1s', d='f'))
