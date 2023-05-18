# написать две функции - шифратор и дешифратор Цезаря

alphabets = ["АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ", "абвгдеёжзийклмнопрстуфхцчшщъыьэюя", "ABCDEFGHIJKLMNOPQRSTUVWXYZ",
             "abcdefghijklmnopqrstuvwxyz", "1234567890"]


def get_symbol(index_symbol: int, index_alphabet: int) -> str:
    length = len(alphabets[index_alphabet])
    return alphabets[index_alphabet][index_symbol - (index_symbol // length * length if index_symbol >= length else 0)]


def get_index(symbol_: str) -> tuple:
    if not symbol_.isalpha() and not symbol_.isdigit():
        return -1, -1

    for kit in alphabets:
        index = kit.find(symbol_)

        if index != -1:
            return index, alphabets.index(kit)

    return -1, -1


# def encoder(str_: str, shift_: int) -> str:
#     encrypted_string = ""
#
#     for sym in str_:
#         index_symbol, index_alphabet = get_index(sym)
#         encrypted_string += get_symbol(index_symbol + shift_, index_alphabet) if index_symbol >= 0 else sym
#
#     return encrypted_string
#
#
# def decoder(str_: str, shift_: int) -> str:
#     decrypted_string = ""
#
#     for sym in str_:
#         index_symbol, index_alphabet = get_index(sym)
#         decrypted_string += get_symbol(index_symbol - shift_, index_alphabet) if index_symbol >= 0 else sym
#
#     return decrypted_string


def enc_dec(str_: str, shift_: int, encode: bool = True) -> str:
    string_ = ""

    for sym in str_:
        index_symbol, index_alphabet = get_index(sym)
        string_ += get_symbol(index_symbol + (shift_ if encode else -shift_),
                              index_alphabet) if index_symbol != -1 else sym

    return string_


while True:
    text = input("Введите текст (Пустой для выхода): ")

    if not text:
        break

    mode = int(input("Выберите режим (1 - зашифровать, 2 - расшифровать): "))
    shift = int(input("Введите ключ: "))

    match mode:
        case 1:
            print(enc_dec(text, shift))
        case 2:
            print(enc_dec(text, shift, False))
