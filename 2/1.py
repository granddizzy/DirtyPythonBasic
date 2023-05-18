# 1. ПАЛИНДРОМЫ
# а) на вход подается слово - проверить, является ли оно палиндромом
# Например на слово  ‘довод’ выводит  ‘да’, а на слово  ‘повод’ - нет.
# Больше примеров слов-палиндромов
# довод, доход, заказ, кабак, комок, мадам, олололо, потоп, радар, ротатор, топот, шалаш
# level deified noon Racecar radar repaper
# б) на вход подается фраза - проверить, является ли она палиндромом
# Не учитывается регистр, знаки препинания и пробелы.
# Примеры фраз-палиндромов
# А роза упала на лапу Азора
# Я иду с мечем судия
# Хил, худ, а дух лих. ——> точки и запятые?
# Тарту дорог, как город утрат
# А путана тупа
# И темен город. Мороз, узором дорог не мети.
# Леша на полке клопа нашел.
# Аргентина манит негра
# Straw? No, too stupid a fad. I put soot on warts
# Was it a cat I saw?
# Do geese see God?
# Madam, I'm Adam
# Pull up if I pull up
# No lemon, no melon
# SATOR AREPO TENET OPERA ROTAS

text = "".join(symbol for symbol in input("Введите строку: ") if symbol.isalpha())

is_palindrome = False
lenght = len(text)

# for i in range(lenght // 2):
#     if (text[i].upper() != text[lenght - 1 - i].upper()):
#         break
# else:
#     is_palindrome = True

if text == text[::-1]:
    is_palindrome = True

print("Да" if is_palindrome else "Нет")
