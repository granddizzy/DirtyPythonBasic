# Дана строка. Разделить строку на фрагменты по три подряд идущих символа.
# В каждом фрагменте средний символ заменить на случайный символ, не совпадающий ни с одним из символов этого фрагмента.
# Показать фрагменты, упорядоченные по алфавиту.

from random import randint as ri

alphabet = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"

input_str = "".join([alphabet[ri(0, 32)] for _ in range(40)])
print(input_str)

length = len(input_str)

list1 = [input_str[3 * i:3 * i + 3] for i in range(0, length // 3 + (1 if length % 3 else 0))]
for i in range(0, len(list1)):
    if len(list1[i]) != 3:
        continue

    while True:
        new_sym = alphabet[ri(0, 32)]
        if list1[i][2] != new_sym != list1[i][0]:
            list1[i] = list1[i][0] + new_sym + list1[i][2]
            break

test_str = " ".join(list1)
print(test_str)

# без списков
test_str = ""
for i in range(0, length // 3 + (1 if length % 3 else 0)):
    test_str += input_str[3 * i:3 * i + 3] + " "
test_str = test_str.rstrip()
print(test_str)

new_str = ""
for i in range(0, len(test_str) // 4):
    while True:
        new_sym = alphabet[ri(0, 32)]
        if test_str[i*4] != new_sym != test_str[i*4+2]:
            new_str += test_str[i*4] + new_sym + test_str[i*4+2:i*4+4]
            break

print(new_str)
