# 4. Функция принимает предложение, вычислzет какой буквы в этом предложении
# больше и возdращает эту букву и процент ее вхождения предложение

input_str = "Функция принимает предложение, вычислzет какой буквы в этом предложении больше и возdращает эту букву и процент ее вхождения предложение"

list_letters = []
count_letters = []
for i in range(len(input_str)):
    if input_str[i].isalpha():
        if list_letters.count(input_str[i]):
            count_letters[list_letters.index(input_str[i])] += 1
        else:
            list_letters.append(input_str[i])
            count_letters.append(1)

percent = round(max(count_letters) * 100 / sum(count_letters), 2)

print(list_letters)
print(count_letters)
print(percent)




dict_ = {}
for i in range(len(input_str)):
    if input_str[i].isalpha():
        dict_[input_str[i]] = dict_.setdefault(input_str[i], 0) + 1

percent = round(max(dict_.values()) * 100 / sum(dict_.values()), 2)

print(dict_)
print(percent)
