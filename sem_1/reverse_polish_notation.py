# Защита 11 лабораторной работы. Выполнил Жижин Никита. ИУ7-11Б
# Примечание: пока что можно вводить все операнды и операторы только разделенными через пробел
import re


def convert_to_polish(exp: str) -> str:
    result = ""

    op_stack = ["#"]  # Необходимо, чтобы избежать проверок на пустоту
    stack = []

    for el in exp:
        if re.fullmatch(r"^[+-]?[0-9]+$", el):  # Если число
            stack.append(int(el))
        else:  # Если оператор
            if el == "(":
                op_stack.append(el)
            elif el == ")":
                while op_stack[-1] != "(":
                    stack.append(op_stack.pop())
                op_stack.pop()
            elif el in ("+", "-"):
                if op_stack[-1] == "(":
                    op_stack.append(el)
                else:
                    while op_stack[-1] not in ("#", "("):
                        stack.append(op_stack.pop())
                    op_stack.append(el)
            elif el in ("*", "/"):
                if op_stack[-1] == "(":
                    op_stack.append(el)
                else:
                    while op_stack[-1] not in ("#", "(", "+", "-"):
                        stack.append(op_stack.pop())
                    op_stack.append(el)

    while op_stack[-1] != "#":
        stack.append(op_stack.pop())

    result = " ".join(map(str, stack))

    return result


print(convert_to_polish('(8+2*5)/(1+3*2-4)'))