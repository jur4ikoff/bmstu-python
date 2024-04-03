# Файл с частоиспользуемыми функциями
import math, random


def input_number(user_message, to_type: [int, float]) -> [int, float]:
    """Ввод числа"""
    while True:
        user_input = input(f"{user_message}: ")
        try:
            return to_type(user_input)
        except ValueError as e:
            print(f'Неверный ввод числа\nКод ошибки: {e}')
        # except ValueError as e:
        #    print


def input_lst(n=None, list_type=int):
    """Ввод списка"""
    if n == None:
        n = input_number('Введите количество элементов в списке', int)

    list_of_numbers = []
    for i in range(n):
        el = input_number(f'Введите {i + 1} элемент списка', list_type)
        list_of_numbers.append(el)

    return list_of_numbers


def output_list(lst, message="Вывод списка", n=None, lst_name='lst'):
    if n == None:
        n = len(lst)

    str_to_output = ''
    print(message)
    for i in range(n):
        str_to_output += (f"{lst_name}[{i}] = {lst[i]}\n")

    return str_to_output


def generate_list(n=None, left_border=0, right_border=100) -> list:
    """Генерация рандомного списка"""

    if n == None:
        n = input_number('Введите количество элементов в списке:', int)

    random_list = [random.randint(left_border, right_border) for i in range(n)]

    return random_list