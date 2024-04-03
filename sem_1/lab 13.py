# 13 лаба
# Попов Ю.А
#  БД
from utils import input_number, output_list
import os

DELIMITER = ';'


class UnexpectedException(Exception):
    """Неожиданная ошибка"""


def ask_menu():
    print()
    print('Выберите действие')
    print('1 - Выбрать файл для работы (Переопределить изначально-выбранную)')
    # print('2 - Инициализировать базу данных') Реализовано
    print('2 - Вывести содержимое базы данных')
    print('3 - Добавить запись в конец базы данных')
    print('4 - Поиск по одному полю')
    print('5 - Поиск по двум полям')
    print('6 - Выход')
    command = input_number('Введите параметр от 1 до 6', int)
    while command not in range(1, 7):
        command = input_number('Введите параметр от 1 до 6', int)
    print()

    return command


def create_db(file: str):
    open(file, "w").close()
    return file


def find_database():
    files = os.listdir()
    db_count = 0
    db_names = []
    for file in files:
        if os.path.isfile(file) and file.endswith(".db"):
            db_count += 1
            db_names.append(file)

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
        name = create_db(name)
        return name


def print_database(file: str):
    with open(file, 'r') as file:
        while True:
            string = file.readline()
            if not string:
                break
            print(*[f"{i:15}" for i in string.strip().split(';')], sep="", end="\n")


def append_db(file: str, to_append: str):
    with open(file, mode='a') as file:
        file.write(str(to_append) + '\n')


def search_one_field(file: str, data: str):
    with open(file=file) as f:
        while True:
            line = f.readline().strip()
            if not line:
                break
            string = line.split(DELIMITER)
            if data in string:
                return line


def search_two_field(file: str, data: str):
    with open(file=file) as f:
        data = data.split(DELIMITER)
        while True:
            line = f.readline().strip()
            if not line:
                break
            string = line.split(DELIMITER)
            count = 0
            for el in data:
                if el in string:
                    count += 1
            if count == len(data) - 1:
                return line


def main():
    db_name = find_database()
    while True:
        command = ask_menu()
        if command == 1:
            db_name = find_database()
            print(f"Используемая база: {db_name}")
        elif command == 2:
            print_database(db_name)
        elif command == 3:
            to_append = input('Введите строку для добавления в БД (разделитель ;): ')
            append_db(db_name, to_append)
            print('Измененная БД')
            print_database(db_name)
        elif command == 4:
            data = input('Введите элемент для поиска: ')
            print(search_one_field(db_name, data))
        elif command == 5:
            data = input('Введите 2 элемента для поиска через ; : ')
            print(search_two_field(db_name, data))
        elif command == 6:
            print('Программа завершилась успешно')
            exit(1)
        else:
            raise UnexpectedException

if __name__ == '__main__':
    pass
    main()
