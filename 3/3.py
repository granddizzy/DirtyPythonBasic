# 3. у нас есть шахматная доска. по горизонтали нумерована цифрами, по вертикали буквами.
# написать программу, которая определяет цвет клетки по ее координатам (например B7 = Черная), если точно знаем, что клетка А1 - черная

alphabet = "абвгдеёж"
y, x = list(input("Введите координаты клетки: "))
print("Черная" if ((int(x) + 1) % 2 if not (alphabet.index(y.lower()) + 1) % 2 else int(x) % 2) else "Белая")


# понятнее
alphabet = "абвгдеёж"
y = alphabet.index(y.lower()) + 1
x = int(x)

print("Черная" if ((x + 1) % 2 if not y % 2 else x % 2) else "Белая")


# еще понятнее
# if not y % 2:
#      x += 1
#
# print("Черная" if x % 2 else "Белая")

