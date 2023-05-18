# 3. ИСТИННОСТЬ ПРЕДИКАТ
# ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z
# Данное выражение истинно при любых значениях предикат (предикат - переменная, которая может иметь только два значения True или False)
# Напишите программу, которая докажет это.
# https://ru.wikipedia.org/wiki/Список_логических_символов - вот вам ссылочка, если непонятно, что за символы)

print (" ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z")

for x in[True, False]:
    for y in [True, False]:
        for z in[True, False]:
            if not (x and y and z) == (not x or not y or not z):
                print("Условие выполнено")