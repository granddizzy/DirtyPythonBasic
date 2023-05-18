# 1. Реализовать алгоритм RLE (упрощенный - это на случай вдруг вы полезете в Wiki)
# что такое RLE? алгоритм сжатия данных, например
# ssssdddfffffgggggggghhkkk -> 4s3d5f8g2h3k
# запаковка и распаковка в обратную сторону
# делаем файл с рандомно созданными строками (как запакованными, так и распакованными)
# считываем файл функция определяет - запакована строка или распакована
# и выполнить соответствующий алгоритм - результаты записать в новый файл

from random import randint as ri


def gen_str() -> str:
    size, str_ = ri(10, 20), ""

    for _ in range(size):
        letter = chr(ri(97, 122))
        for _ in range(ri(1, 6)):
            str_ += letter

    return str_


def compress(str_: str) -> str:
    length = len(str_)

    if length <= 1:
        return str_

    res, count = "", 0

    for i in range(0, length):
        count += 1
        if i == length - 1 or str_[i] != str_[i + 1]:
            res += str(count) + str_[i]
            count = 0

    return res


def uncompress(str_: str) -> str:
    if len(str_) <= 1:
        return str_

    res = ""
    for i in range(0, len(str_), 2):
        res += int(str_[i]) * str_[i + 1]
    return res


def is_compress(str_: str) -> bool:
    if len(str_) == 0:
        return False

    if str_[0].isdigit():
        return True

    return False


def create_file():
    with open("rle.txt", "w", encoding="UTF-8") as file:
        size = ri(10, 30)
        for i in range(size):
            str_ = gen_str()

            if i % 2:
                print(str_, file=file)
            else:
                print(compress(str_), file=file)


create_file()

with open("rle.txt", "r", encoding="UTF-8") as file:
    for line in file.readlines():
        line = line.strip()
        if is_compress(line):
            print(uncompress(line))
        else:
            print(line)
