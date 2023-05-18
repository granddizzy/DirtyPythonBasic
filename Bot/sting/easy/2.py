# Дана строка. Показать номера символов, совпадающих с последним символом строки.

from random import randint as ri

input_str = "".join(["абвгдеёжзийклмнопрстуфхцчшщъыьэюя "[ri(0, 33)] for _ in range(40)])
print(input_str)

length = len(input_str)
# for i in range(length-1):
#     if input_str[i] == input_str[length-1]:
#         print(i+1, end=" ")

print(*[i+1 for i in range(length-1) if input_str[i] == input_str[length-1]])
