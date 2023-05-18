# 1. Для разминки. Дан список чисел. Создать новый список, который будет содержать только уникальные элементы исходного списка

from random import randint as ri

input_list = [ri(0, 10) for _ in range(20)]

print(input_list)

uniq_list = list(set(input_list))

print(uniq_list)