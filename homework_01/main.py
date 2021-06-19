"""
Домашнее задание №1
Функции и структуры данных
"""
"""
Домашнее задание №1
Функции и структуры данных
"""
list_of_num = []


def power_numbers(*n):
    for number in n:
        list_of_num.append(number ** 2)
    print(list_of_num)
    list_of_num.clear()


ODD = "odd"
EVEN = "even"
PRIME = "prime"
odd_list = []
even_list = []


def is_prime(n):
    d = 2
    while n % d != 0:
        d += 1
    if n == d:
        return True


def filter_numbers(*some_list):
    if some_list[-1] == 'odd':
        for i in some_list[0]:
            if i % 2 != 0:
                odd_list.append(i)
        return odd_list
    elif some_list[-1] == 'even':
        for i in some_list[0]:
            if i % 2 == 0:
                even_list.append(i)
        return even_list
    elif some_list[-1] == 'prime':
        return list(filter(is_prime, some_list[0]))


ODD = "odd"
EVEN = "even"
PRIME = "prime"
odd_list = []
even_list = []


def is_prime(n):
    d = 2
    while n % d != 0:
        d += 1
    if n == d:
        return True


def filter_numbers(*some_list):
    if some_list[-1] == 'odd':
        for i in some_list[0]:
            if i % 2 != 0:
                odd_list.append(i)
        return odd_list
    elif some_list[-1] == 'even':
        for i in some_list[0]:
            if i % 2 == 0:
                even_list.append(i)
        return even_list
    elif some_list[-1] == 'prime':
        return list(filter(is_prime, some_list[0]))


power_numbers(1, 2, 3)
power_numbers(1, 2, 3)
print(power_numbers(1 ,2 ,3))