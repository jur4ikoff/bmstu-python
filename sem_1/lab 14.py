# 14 лаба
# Попов Ю.А
#  Binary DB
from utils import input_number, output_list
import os
import struct

# BD STRUCTURE
# ID NAME AGE
# 0 YURI 18
# h 225s h

FORMAT = "<l255sl"
FORMAT_SIZE = struct.calcsize(FORMAT)
TYPES = [int, bytes, int]


# Скачать bin ed

class UnexpectedException(Exception):
    """Неожиданная ошибка"""


class UnexpectedFormat(Exception):
    """Неожиданный формат введеной строки"""


def ask_menu():
    print()
    print('Выберите действие')
    print('1 - Выбрать файл для работы (Переопределить изначально-выбранную)')
    # print('2 - Инициализировать базу данных') Реализовано
    print('2 - Вывести содержимое базы данных')
    print('3 - Добавить запись в произвольное место базы данных')
    print('4 - Удалить произвольную запись из базы данных')
    print('5 - Поиск по одному полю')
    print('6 - Поиск по двум полям')
    print('7 - Выход')
    command = input_number('Введите параметр от 1 до 7', int)
    while command not in range(1, 8):
        command = input_number('Введите параметр от 1 до 7', int)
    print()

    return command


def create_db(file: str):
    open(file, "wb").close()


def find_database():
    files = os.listdir()
    db_count = 0
    db_names = []
    for file in files:
        if os.path.isfile(file) and file.endswith(".db"):
            db_count += 1
            db_names.append(file)
    choice_mode = input('Создать новую базу данных(Y/N): ')
    if choice_mode.lower() == 'y':
        name = input("Введите название новой базы данных: ") + ".db"
        create_db(name)
        return name
    if db_count == 1:
        return db_names[0]
    if db_count > 1:
        print(output_list(db_names, message="Вывод возможных баз данных", n=db_count, lst_name='db_name'))
        db_number = input_number(f'Введите номер базы данных от 0 до {db_count - 1}', int)
        while db_number not in range(0, db_count):
            db_number = input_number(f'Введите номер базы данных от 0 до {db_count - 1}', int)
        return db_names[db_number]
    if db_count == 0:
        name = input("Введите название новой базы данных: ") + ".db"
        create_db(name)
        return name


def check_row(data):
    """Проверка на соответствие формату"""

    if len(data) != 3:
        return False
    for col, type in zip(data, TYPES):
        if not isinstance(col, type):
            return False
    return True


def add_row(file, row, index=-1):
    bd_size = os.path.getsize(file)
    if index < 0:
        try:
            index = FORMAT_SIZE // bd_size
        except ZeroDivisionError:
            index = 0
    if not check_row(row):
        raise UnexpectedFormat

    data = struct.pack(FORMAT, *row)
    with open(file, "r+b") as file:
        tmp_data = file.read()
        file.truncate(FORMAT_SIZE * index)
        file.seek(FORMAT_SIZE * index)
        file.write(data + tmp_data[FORMAT_SIZE * (index):])


def read_db(file):
    with open(file, "rb") as fp:
        while True:
            data = fp.read(FORMAT_SIZE)
            if not data:
                break
            (Id, Name, Age) = struct.unpack(FORMAT, data)
            yield Id, Name.decode().split("\x00")[0], Age


def delete_row(file, index):
    bd_size = os.path.getsize(file)
    with open(file, "r+b") as file:
        if bd_size < FORMAT_SIZE * index:
            raise ValueError
        tmp_file = file.read()
        file.truncate(FORMAT_SIZE * index)
        file.seek(FORMAT_SIZE * index)
        file.write(tmp_file[FORMAT_SIZE * (index + 1):])


def main():
    db_name = find_database()
    print(f"Инициализирована: {db_name}")
    while True:
        command = ask_menu()
        if command == 1:
            db_name = find_database()
            print(f"Используемая база: {db_name}")
        if command == 2:
            print('i;uid;name;age')
            for i, row in enumerate(read_db(db_name)):
                print(f'{i}: {row}')
        if command == 3:
            index = input_number('Введите индекс элемента', int)
            uid, name, age = input(f'Введите id пользователя, имя и возраст через пробел: ').split()
            try:
                uid, age = int(uid), int(age)
            except Exception:
                print('UID AND AGE MUST BE INT')
            name = name.encode()
            try:
                add_row(db_name, [uid, name, age], index)
            except Exception:
                raise UnexpectedException
        if command == 4:
            index = input_number('Введите индекс элемента для удаления', int)
            try:
                delete_row(db_name, index)
            except Exception as e:
                print(e)
                raise UnexpectedException
        if command == 5:
            to_search = input('Введите элемент для поиска: ')
            print('Найденные элементы')
            for row in read_db(db_name):
                if any(str(j) == to_search for j in row):
                    print(*[f"{c:^13}|" for c in row], sep="")
        if command == 6:
            to_search = input('Введите элемент для поиска через пробел: ').split()
            print('Найденные элементы')
            for row in read_db(db_name):
                if all(str(j) in list(map(str, row)) for j in to_search):
                    print(*[f"{c:^13}|" for c in row], sep="")
        if command == 7:
            print('Программа завершилось успешно')
            exit()


if __name__ == '__main__':
    pass
    main()
