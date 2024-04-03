# Выполнил Попов Юрий ИУ7-12Б
# сортировки
# метод вставок с бинарным поиском
import math
import time
from utils import input_number, input_lst, generate_list, output_list


def input_data():
    """Ввод размерности"""
    n1 = input_number("Введите N1", int)
    n2 = input_number("Введите N2", int)
    n3 = input_number("Введите N3", int)
    return (n1, n2, n3)


def make_table(t1, t2, t3, t4, t5, t6, t7, t8, t9, k1, k2, k3, k4, k5, k6, k7, k8, k9):
    print()
    print('Таблица')
    print('—' * 105)
    print(f"|{' ':^25}|{'N1':^25}|{'N2':^25}|{'N3':^25}|")
    print('—' * 105)

    print(
        f"|{' ':^25}|{'время':^10}|{'перестановки':^14}|{'время':^10}|{'перестановки':^14}|{'время':^10}|"
        f"{'перестановки':^14}|")
    print('—' * 105)

    print(f"|{'Упорядоченный список':^25}|{t1:^10.6g}|{k1:^14.6g}|{t2:^10.6g}|{k2:^14.6g}|{t3:^10.6g}|{k3:^14.6g}|")
    print('—' * 105)

    print(f"|{'Случайный список':^25}|{t4:^10.6g}|{k4:^14.6g}|{t5:^10.6g}|{k5:^14.6g}|{t6:^10.6g}|{k6:^14.6g}|")
    print('—' * 105)

    print(f"|{'Упорядоченный в обратном':^25}|{t7:^10.6g}|{k7:^14.6g}|{t8:^10.6g}|{k8:^14.6g}|{t9:^10.6g}|{k9:^14.6g}|")
    print(f"|{'порядке':^25}|{'':^10}|{'':^14}|{'':^10}|{'':^14}|{'':^10}|{'':^14}|")
    print('—' * 105)
    return ""


def binary_search(lst, el, low, high):
    while low <= high:
        mid = (low + high) // 2
        if el > lst[mid]:
            low = mid + 1
        else:
            high = mid - 1
    return low


def insertion_binary(lst):
    count = 0
    start_time = time.time()
    for i in range(len(lst)):
        elem = lst[i]
        j1, j2 = 0, i - 1
        ll = binary_search(lst, elem, j1, j2)
        for k in range(i, ll, -1):
            lst[k] = lst[k - 1]
            count += 1
        lst[ll] = elem
    finish_time = time.time()
    spent_time = finish_time - start_time
    return (lst, spent_time, count)


def main():
    n1, n2, n3 = input_data()  # Ввод N
    user_list = input_lst()

    print()
    print(output_list(user_list, message='Вывод пользовательского списка', lst_name='user_lst'))

    sort_user_list, t1, count = insertion_binary(user_list)
    print(output_list(sort_user_list, message='Вывод отсортированного пользовательского списка',
                      lst_name='sort_user_lst'))

    list1 = generate_list(n1, 0, 1000)
    temp, t4, k4 = insertion_binary(list1)
    list1 = sorted(list1)
    temp, t1, k1 = insertion_binary(list1)
    list1 = sorted(list1, reverse=True)
    temp, t7, k7 = insertion_binary(list1)

    list2 = generate_list(n2, 0, 1000)
    temp, t5, k5 = insertion_binary(list2)
    list2 = sorted(list2)
    temp, t2, k2 = insertion_binary(list2)
    list2 = sorted(list2, reverse=True)
    temp, t8, k8 = insertion_binary(list2)

    list3 = generate_list(n3, 0, 1000)
    temp, t6, k6 = insertion_binary(list3)
    list3 = sorted(list3)
    temp, t3, k3 = insertion_binary(list3)
    list3 = sorted(list3, reverse=True)
    temp, t9, k9 = insertion_binary(list3)

    print(make_table(t1, t2, t3, t4, t5, t6, t7, t8, t9, k1, k2, k3, k4, k5, k6, k7, k8, k9))


def partition(array, low, high):
    pivot = array[high]
    i = low - 1
    for j in range(low, high):
        if array[j] <= pivot:
            i = i + 1
            array[i], array[j] = array[j], array[i]
    array[i + 1], array[high] = array[high], array[i + 1]

    return i + 1


def quick_sort(array, low, high):
    if low < high:
        pi = partition(array, low, high)
        quick_sort(array, low, pi - 1)
        quick_sort(array, pi + 1, high)


if __name__ == '__main__':
    data = generate_list(1000, 0, 1000)
    size = len(data)
    time1 = time.time()
    quick_sort(data, 0, size - 1)
    print(data)
    time2 = time.time()
    print(time2 - time1)
    main()
