# 3. функцию для проверки числа:
#   - четность - нечетность
#   - простое число (имеет всего два делителя - само себя и единицу)
#   - сумма всех цифр числа является делителем этого числа
#   - *принимает число и выдает его только простые делители

def is_even(num: int) -> bool:
    return not num % 2


def is_simple(num: int) -> bool:
    if num in [1, 2]:
        return True
    for i in range(3, num // 2 + 1):
        if not num % i:
            return False
    return True


def is_sum_divider(num: int) -> bool:
    return not num % sum(list(map(int, list(str(num)))))


def get_simple_dividers(num: int) -> list:
    list_ = [1, ]

    for i in range(2, num // 2 + 1):
        if num % i == 0:
            list_.append(i)

    list_.append(num)

    return list_


number = int(input("Введите число: "))

print(is_even(number))
print(is_simple(number))
print(is_sum_divider(number))
print(get_simple_dividers(number))
