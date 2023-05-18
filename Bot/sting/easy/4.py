# Дана строка. Если ее длина больше 10, то оставить в строке только первые 6 символов, иначе дополнить строку символами 'o' до длины 12.

input_str = input("Введите строку: ")
length = len(input_str)

if length > 10:
    input_str = input_str[0:6]
else:
    for i in range(12 - length):
        input_str += "o"

print(input_str)
