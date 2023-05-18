# выдать топ 5 самых встречаемы слов в Алисе длинна которых не меньше 5 букв
import string

with open("Alice in Wonderland.txt", "r", encoding="UTF-8") as file:
    text_ = file.read().lower()

for sym in string.punctuation + "\n\xa01234567890«»-–„":
    text_ = text_.replace(sym, " ")

words = text_.split()
dict_words = {word: words.count(word) for word in set(words) if len(word) > 4}

sorted_tuples = sorted(dict_words.items(), key=lambda el: el[1])
length = len(sorted_tuples)

# for item in sorted_tuples:
#     if item[0].find("алиса") >= 0:
#         print(*item, sep=" - ")


for i in range(length - 5, length):
    print(*sorted_tuples[i], sep=" - ")
