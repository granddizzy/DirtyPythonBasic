# В 4-значном числе поменять местами первую и последнюю цифру
# Попробовать решить максимальным количеством разных способов

str_number = input("Введите число: ")

# через строку и срез
number = str_number
if len(number) > 1:
    number = number[len(number)-1] + number[1: len(number)-1] + number[0]

print(number)

# через список
number = str_number
list_number = list(number)

if len(number) > 1:
    temp = list_number[0]
    list_number[0] = list_number[len(list_number)-1]
    list_number[len(list_number)-1] = temp

number = int("".join(list_number))

print(number)

# через строку и цикл
number = str_number
if len(number) > 1:
    new_str = number[len(number)-1]
    for i in range(1, len(number)-1):
        new_str += number[i]

    number = int(new_str + number[0])

print(number)

# математически
number = str_number
int_number = int(number)
count_dozens = 0
center_number = 0

while int_number > 0:
    count_dozens += 1

    if count_dozens == 1:
        last_digit = int_number % 10
    elif int_number // 10 != 0:
        center_number = int_number % 10 * 10 ** (count_dozens - 2) + center_number

    first_digit = int_number
    int_number //= 10

number = last_digit * 10 ** (count_dozens - 1) + center_number * 10 + first_digit

print(number)

