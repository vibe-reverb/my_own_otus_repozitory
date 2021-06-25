def power_numbers(*n):
    list_of_num = []
    for number in n:
        list_of_num.append(number ** 2)
    print(list_of_num)
    return list_of_num


ODD = "odd"
EVEN = "even"
PRIME = "prime"


def is_prime(n):
    d = 2
    while n % d != 0:
        d += 1
    if n == d:
        return True


def is_odd(n):
    return n % 2 != 0


def is_even(n):
    return n % 2 == 0


def filter_numbers(first_arg,filter_type):
    action = {
        ODD: is_odd,
        EVEN: is_even,
        PRIME: is_prime,
    }[filter_type]
    return list(filter(action,first_arg))




