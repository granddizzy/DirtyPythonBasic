# 4. Принимаем с консоли число и выводим две последовательности Фибоначчи и Негафибоначчи (можно прочитать в wiki что это)
# Пример: Вводим 8
# [-21, 13, -8, 5, -3, 2, -1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]

num = int(input("Введите число: "))

list1 = [0, ]

for i in range(num):
    if i > 0:
        list1.append(list1[-1] + list1[-2])
        list1.insert(0, list1[1] - list1[0])
    else:
        list1.append(1)
        list1.insert(0, 1)

print(list1)
