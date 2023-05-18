# 3. На вход поступает десятичное число, вывести его в виде двоичного

number = int(input("Введите десятичное число: "))
bin_number = ""
temp = number

while temp > 0:
    bin_number = str(temp % 2) + bin_number
    temp = temp // 2

if len(bin_number) % 2 != 0:
    bin_number = "0" + bin_number

print(f"Десятичное число {number} в двоичном виде равно {bin_number}")

# самопроврека
print(bin(number))