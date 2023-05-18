# парсинг многочлена
from builtins import print
from random import randint as ri
from re import split
from typing import Dict


def create_dict():
    # degree = int(input("Введите максимальную степень: "))
    degree = ri(4, 7)
    dict_1 = {}
    for k in range(degree, -1, -1):
        dict_1[k] = ri(-100, 100)
    return dict_1


def create_equation(eq: dict[int, int]) -> str:
    res = []
    for degree, koef in eq.items():
        if koef != 0:
            res.append(f"{' + ' if koef >= 0 else ' - '}{koef if koef > 0 else -koef}*x**{degree}")

    str_ = "".join(res).replace("**1 ", " ").replace("*x**0", "") + " = 0"
    return str_[3: len(str_)]


def str_to_dict(eq: str) -> dict[int, int]:
    dict_1 = {}
    monomials = split(" [+,-] ", eq.replace(" = 0", ""))
    for item in monomials:
        data = item.replace("*", "").split("x")

        koef = int(data[0]) if data[0] else 1
        degree = (int(data[1]) if data[1] else 1) if len(data) > 1 else 0

        i = eq.find(item)
        sign = (eq[i - 2: i - 1].replace(" ", "")) if i > 0 else "+"

        dict_1[degree] = koef * (1 if sign == "+" else -1)

    return dict_1


def summ_eq(eq1: dict, eq2: dict) -> dict:
    new_dict = {}
    new_dict.update(eq1)
    new_dict.update(eq2)

    for key in new_dict:
        new_dict[key] = eq1.get(key, 0) + eq2.get(key, 0)

    return dict(sorted(new_dict.items(), reverse=True))


print(str_eq_1 := create_equation(create_dict()))
print(str_eq_2 := create_equation(create_dict()))

# print(str_to_dict(str_eq_1))
# print(str_to_dict(str_eq_2))

print("\nСумма многочленов: ")
print(create_equation(summ_eq(str_to_dict(str_eq_1), str_to_dict(str_eq_2))))
