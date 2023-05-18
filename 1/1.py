# 1. На вход поступает число: найти сумму цифр числа, в том числе если оно отрицательное или вещественное. (float)

number = input("Введите число: ")
sum = 0

# строкой
for symbol in number:
    if symbol.isdigit():
        sum += int(symbol)

print(f"Сумма цифр числа {number} равна {sum}")

# тест решения математически
number = float(number)
sum = 0
fraction_part = 0

integer_part = int(number)

i = 1
while True:
    digit = int(number * 10 ** i) % 10
    sum += digit
    fraction_part = round(fraction_part + digit / 10 ** i, i)
    i += 1

    if number == integer_part + fraction_part:
        break

while integer_part > 0:
    sum += integer_part % 10
    integer_part //= 10

print(f"Сумма цифр числа {number} равна {sum}")