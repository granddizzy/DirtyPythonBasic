# Дана строка. Если она начинается на 'abc', то заменить их на 'www', иначе добавить в конец строки 'zzz'.

input_str = input("Введите строку: ")
length = len(input_str)

if length >= 3 and input_str[0:3] == "abc":
    input_str = "www" + input_str[4: length]
else:
    input_str += "zzz"

print(input_str)
