# 1. Написать функцию, которая принимает на вход строку из рандомных цифр и букв, а возвращает:
#   - строку только из букв
#   - строку только из цифр
#   - сравнить длину строк из цифр и из букв и вернуть ту, которая длиннее

from random import randint as ri


def get_digits(str_: str) -> str:
    str_digits = ""

    for sym in str_:
        if sym.isdigit():
            str_digits += sym

    return str_digits


def get_letters(str_: str) -> str:
    str_letters = ""

    for sym in str_:
        if sym.isalpha():
            str_letters += sym

    return str_letters


def get_numbers_or_letters(str_: str) -> str:
    str_letters = get_letters(str_)
    str_digits = get_digits(str_)

    if len(str_letters) > len(str_digits):
        return str_letters
    else:
        return str_digits


dict_str = "abcdefghijklmnopqrstuvwxyz1234567890"
dict_str_length = len(dict_str)
input_str = ""
length = ri(10, 100)

for _ in range(length):
    input_str += dict_str[ri(0, dict_str_length - 1)]

print(input_str)

print(get_digits(input_str))
print(get_letters(input_str))
print(get_numbers_or_letters(input_str))


