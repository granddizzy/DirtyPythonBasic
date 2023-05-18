# 6. ПРОСТЕЙШИЙ КАЛЬКУЛЯТОР
# Написать программу, которая выполняет над двумя вещественными числами одну из четырех арифметических операций (сложение, вычитание, умножение или деление):
# вводим первое число,
# потом операцию
# и второе число
# выводится результат
#
# Программа должна завершаться только по желанию пользователя: можно ввести enter и программа закончится, или еще операцию и еще число. Ну и помним, что на ноль делить нельзя.

from decimal import Decimal

flag = True
first_num, second_num, oper = "", "", ""
text = "Введите первое число"

while flag:
    if not first_num or not oper or not second_num:
        input_str = input(text + ": ").replace(" ", "")

    if input_str:
        if not first_num:
            if input_str.count(".") > 1 or input_str.count("-") > 1 or input_str.find(".") == len(input_str) - 1:
                print("И как это понять ?")
            else:
                i = 0
                for symbol in input_str:
                    if not symbol.isdigit():
                        if (i == 0 and symbol != "-" and symbol != ".") or (i > 0 and symbol != "."):
                            print("Дурачек что-ли ?")
                            break
                    i += 1
                else:
                    first_num = input_str
                    text = "Введите операцию (+ - * /)"

        elif not oper:
            if len(input_str) > 1:
                print("И как это понять ?")
            else:
                for symbol in input_str:
                    if not (symbol in "+-*/"):
                        print("Дурачек что-ли ?")
                        break
                else:
                    oper = input_str
                    text = "Введите второе число"
        elif not second_num:
            if input_str.count(".") > 1 or input_str.count("-") > 1 or input_str.find(".") == len(input_str) - 1:
                print("И как это понять ?")
            else:
                i, only_zero = 0, True
                for symbol in input_str:
                    if not symbol.isdigit():
                        if (i == 0 and symbol != "-" and symbol != ".") or (i > 0 and symbol != "."):
                            print("Дурачек что-ли ?")
                            break
                    else:
                        if int(symbol) != 0 and only_zero:
                            only_zero = False
                    i += 1
                else:
                    if only_zero and oper == "/":
                        print("0? Издеваешься ? За тобой уже выехали !!!")
                    else:
                        second_num = input_str
                        text = "Введите операцию (+ - * /)"
        else:
            if oper == "+":
                res = Decimal(first_num) + Decimal(second_num)
            elif oper == "-":
                res = Decimal(first_num) - Decimal(second_num)
            elif oper == "*":
                res = Decimal(first_num) * Decimal(second_num)
            elif oper == "/":
                res = Decimal(first_num) / Decimal(second_num)

            print(f"Результат: {Decimal(first_num)} {oper} {Decimal(second_num)} = {res}")

            first_num = res
            oper, second_num = "", ""
    else:
        flag = False
else:
    print("Всем спасибо - все свободны")
