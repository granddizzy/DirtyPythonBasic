# 2. На шахматной доске расположить 8 ферзей так, чтобы они не били друг друга
# приложить хотя бы один вариант такой расстановки

# 0 1
# 1 1
# 2 0
# 3 0
# 4 2
# 5 10
# 6 4
# 7 40
# 8 92
# 9 352
# 10 724
# 11 2680
# 12 14200
# 13 73712
# 14 365596
# 15 2279184
# 16 14772512
# 17 95815104
# 18 666090624
# 19 4968057848
# 20 39029188884
# 21 314666222712
# 22 2691008701644
# 23 24233937684440
# 24 227514171973736
# 25 2207893435808352
# 26 22317699616364044
# 27 234907967154122528

# https://oeis.org/A000170

def show_chessboard(chessboard_: list) -> None:
    for i in range(len(chessboard_)):
        for j in range(len(chessboard_[i])):
            print(chessboard_[i][j], end="\t")
        print()


def fill_chessboard(list_coordinates_queen: list, chessboard_: list) -> None:
    for item_ in list_coordinates_queen:
        chessboard_[item_[0]][item_[1]] = 1


def del_coordinates(coordinates: tuple, free_coordinates_) -> None:
    free_coordinates_.pop(free_coordinates_.index(coordinates))


def del_busy(coordinates: tuple, free_coordinates_) -> list:
    del_coordinates(coordinates, free_coordinates_)

    # лево
    for i in range(0, coordinates[0]):
        if (i, coordinates[1]) in free_coordinates_:
            del_coordinates((i, coordinates[1]), free_coordinates_)

    # право
    for i in range(coordinates[0] + 1, chessboard_size):
        if (i, coordinates[1]) in free_coordinates_:
            del_coordinates((i, coordinates[1]), free_coordinates_)

    # низ
    for j in range(0, coordinates[1]):
        if (coordinates[0], j) in free_coordinates_:
            del_coordinates((coordinates[0], j), free_coordinates_)

    # верх
    for j in range(coordinates[1] + 1, chessboard_size):
        if (coordinates[0], j) in free_coordinates_:
            del_coordinates((coordinates[0], j), free_coordinates_)

    # лево-низ
    if coordinates[0] > 0 and coordinates[1] > 0:
        for i in range(1, min([coordinates[0], coordinates[1]]) + 1):
            if (coordinates[0] - i, coordinates[1] - i) in free_coordinates_:
                del_coordinates((coordinates[0] - i, coordinates[1] - i), free_coordinates_)

    # право-верх
    if coordinates[0] < chessboard_size - 1 and coordinates[1] < chessboard_size - 1:
        for i in range(1, min([chessboard_size - coordinates[0], chessboard_size - coordinates[1]])):
            if (coordinates[0] + i, coordinates[1] + i) in free_coordinates_:
                del_coordinates((coordinates[0] + i, coordinates[1] + i), free_coordinates_)

    # лево-верх
    if coordinates[0] > 0 and coordinates[1] < chessboard_size - 1:
        for i in range(1, min([coordinates[0], chessboard_size - 1 - coordinates[1]]) + 1):
            if (coordinates[0] - i, coordinates[1] + i) in free_coordinates_:
                del_coordinates((coordinates[0] - i, coordinates[1] + i), free_coordinates_)

    # право-низ
    if coordinates[0] < chessboard_size - 1 and coordinates[1] > 0:
        for i in range(1, min([chessboard_size - 1 - coordinates[0], coordinates[1]]) + 1):
            if (coordinates[0] + i, coordinates[1] - i) in free_coordinates_:
                del_coordinates((coordinates[0] + i, coordinates[1] - i), free_coordinates_)

    return free_coordinates_


def set_queens(free_coordinates_: list, queens=None, level: int = 1) -> bool:
    if queens is None:
        queens = []

    if level == 1:
        count, length = 0, len(free_coordinates_)
        print(f"Прогресс {chessboard_size}x{chessboard_size} для {queens_max} ферзей: ", end="")

    for queen in free_coordinates_:
        if level == 1:
            count += 1
            print(str(100 * count // length), end="% ")

        # удаляем занятые ферзем координаты
        new_free_coordinates = del_busy(queen, free_coordinates_.copy())

        # если количество свободных полей больше либо равно оставшемуся количеству ферзей
        if len(new_free_coordinates) >= queens_max - level:
            # добавляем ферзя в список
            queens.append(queen)

            # если еще нужны ферзи
            if level < queens_max:
                set_queens(new_free_coordinates, queens, level + 1)

            # если установили последнего ферзя добавляем вариант в общий список
            if level == queens_max:
                full_queens.add(tuple(sorted(queens)))

            queens.pop()
    else:
        if level == 1:
            print("")


def convert_coordinates(coordinates):
    return chr(65 + coordinates[1]) + str(coordinates[0])


for i in range(10, 15):
    chessboard_size, queens_max = i, i
    # chessboard = [[0 for _ in range(chessboard_size)] for _ in range(chessboard_size)]
    full_queens = set()
    free_coordinates = [(i, j) for j in range(chessboard_size) for i in range(chessboard_size)]

    set_queens(free_coordinates)

    # i = 0
    with open(str(chessboard_size) + "x" + str(chessboard_size) + ".txt", "w", encoding="UTF-8") as file:
        for line in full_queens:
            # i += 1
            # print(i, end="\t", file=file)
            print(" ".join([convert_coordinates(item) for item in line]), file=file)

    print(f"Выполнено для {i}x{i} и {i} ферзей")

print("Программа завершена.")
