# 5. Вводим сегодняшнюю дату и сегодняшний день недели, затем вводим новую дату и программа должна выдать нам какой день недели будет в эту дату

# григорианский календарь предусматривает, что год, который делится без остатка на 100 (например, 1900)
# является високосным годом только в том случае, если он также без остатка делится на 400.
# not year % 4 or (not year % 100 and not year % 400):
# 365 ... 366

#from datetime import datetime

def is_leap_year(year):
    return not year % 4 and year % 100 or not year % 400


week_days = {1: "Понедельник", 2: "Вторник", 3 : "Среда", 4 : "Четверг", 5: "Пятница", 6: "Суббота", 0: "Воскресенье"}
month_days = {1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 6: 30, 7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31}

day_of_the_week = 4  # четверг
begin_day, begin_month, begin_year = list(map(int, "01.07.1970".split(".")))

input_date = input("Введите дату DD.MM.YYYY: ")
end_day, end_month, end_year = list(map(int, input_date.split(".")))

# если начальная дата больше конечной, то меняем их местами
reverse = False
if begin_year > end_year or begin_year == end_day and begin_month > end_month or begin_year == end_year and begin_month == end_month and begin_day > end_day:
    t_end_day, t_end_month, t_end_year = end_day, end_month, end_year
    end_day, end_month, end_year = begin_day, begin_month, begin_year
    begin_day, begin_month, begin_year = t_end_day, t_end_month, t_end_year
    reverse =  True

diff_days = 0

# подведем к началу следующего года (если начальная дата не с начала года)
if begin_day != 1 or begin_month != 1:
    leapyear_repair = 1 if is_leap_year(begin_year) else 0

    # добавляем дни месяца
    diff_days += month_days[begin_month] + (leapyear_repair if begin_month == 2 else 0) - begin_day + 1

    # добавляем оставшиеся месяцы
    for month in range(begin_month + 1, 13):
        diff_days += month_days[month] + (leapyear_repair if month == 2 else 0)

# количество дней полных лет
diff_days += sum([366 if is_leap_year(year) else 365 for year in range(begin_year, end_year - 1)])

leapyear_repair = 1 if is_leap_year(end_year) else 0

# количество дней полных месяцев в неполном году
for month in range(1, end_month):
    diff_days += month_days[month] + (leapyear_repair if month == 2 else 0)

# количество дней в неполном месяце и корректировка на день недели
diff_days += end_day - 1

#diff_days2 = (datetime(end_year, end_month, end_day) - datetime(begin_year, begin_month, begin_day)).days

diff_days -= day_of_the_week - (1 if reverse else 0)

week_day = diff_days % 7 if diff_days > 6 else diff_days

print(f"День недели {input_date} - {week_days[week_day]}")
