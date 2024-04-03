import string
import unittest


def test_input_data(number, status):
    number = str(number)
    if number == '':
        return ''
    if any(i in number for i in string.ascii_letters):
        return 'letters in number'
    if number.count('.') > 1:
        return 'too match pounds'
    if status == 1:
        if any(str(i) in number for i in range(3, 10)):
            return 'incorrect digits for 3cc'
    return '1'


def convert10to3(number, precision=10):
    number = float(number)
    number = str(number)
    if number[0] == '.':
        number = '0' + number
    elif number[-1] == '.':
        number += '0'
    number = float(number)

    integer_part = int(number)
    fractional_part = number - integer_part

    ternary_integer = ""
    while integer_part > 0:
        remainder = integer_part % 3
        ternary_integer = str(remainder) + ternary_integer
        integer_part //= 3

    ternary_fractional = ""
    for _ in range(precision):
        fractional_part *= 3
        integral_part, fractional_part = divmod(fractional_part, 1)
        ternary_fractional += str(int(integral_part))

    if ternary_integer == '':
        ternary_integer = '0'
    return f"{ternary_integer}.{ternary_fractional}"


def convert3to10(number, precision=10):
    number = str(number)
    if number[0] == '.':
        number = '0' + number
    elif number[-1] == '.':
        number += '0'

    try:
        integer_part, fractional_part = str(number).split(".")
    except ValueError:
        integer_part = str(int(number))
        fractional_part = '0'

    decimal_integer = sum(int(digit) * (3 ** position) for position, digit in enumerate(integer_part[::-1]))
    decimal_fractional = sum(int(digit) * (3 ** -(position + 1)) for position, digit in enumerate(fractional_part))
    res = decimal_integer + decimal_fractional
    return str(round(res, precision))
