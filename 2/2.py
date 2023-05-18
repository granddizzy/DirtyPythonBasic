# 2. ТАБЛИЦА УМНОЖЕНИЯ
# Напишите программу, которая будет выводить в консоль таблицу умножения от 1 до 10 (как в вконце старых тетрадок, квадратная такая

for n in range(2):

    if n == 0:
        x, y = 2, 6
    else:
        x, y = 6, 10

    for i in range(2, 11):
        for j in range(x, y):
            mult = i * j

            if mult < 10:
                shift = 5
            elif i == 10:
                shift = 3
            else:
                shift = 4

            print(f"{j} X {i} = {mult}", end=" " * shift)

        print()

    print()
