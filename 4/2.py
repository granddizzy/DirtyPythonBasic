# 2. Написать функцию, которая будет возвращать список созданный по заданным критериям:
# размер, минимальное и максимальное значение, наличие повторяющихся элементов

from random import randint as ri


def get_list(size: int = 10, min_val: int = 0, max_val: int = 10, without_repeat: bool = False) -> list:
    list_ = []

    if without_repeat and max_val - min_val + 1 < size:
        return list_

    for _ in range(size):
        while True:
            random_value = ri(min_val, max_val+1)

            if list_.count(random_value) == 0 or not without_repeat:
                list_.append(random_value)
                break

    return list_


print(get_list(10, 3, 5))
