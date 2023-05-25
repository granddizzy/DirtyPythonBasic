# классный журнал
import os
import json

"""
файл журнала:
первая строка: словарь предметов
вторая строка: словарь учеников
третья строка: словарь журнала
"""


def load_class_journal() -> tuple:
    if mode == 1:
        file_path = "class_journal_json.db"
        if os.path.exists(file_path) and os.stat(file_path).st_size > 0:
            with open(file_path, "r", encoding="UTF-8") as file:
                file_data = file.readlines()

                lessons_list_ = {int(k): v for k, v in json.loads(file_data[0]).items()}
                students_list_ = {int(k): v for k, v in json.loads(file_data[1]).items()}

                class_journal_ = {}
                for k, v in json.loads(file_data[2]).items():
                    class_journal_[int(k)] = {}
                    for k1, v1 in v.items():
                        class_journal_[int(k)][int(k1)] = v1
        else:
            lessons_list_ = {}
            students_list_ = {}
            class_journal_ = {}
    else:
        file_path = "class_journal_parsing.db"
        if os.path.exists(file_path) and os.stat(file_path).st_size > 0:
            with open(file_path, "r", encoding="UTF-8") as file:
                file_data = file.readlines()

                # список уроков
                lessons_list_ = {}
                for lesson_ in file_data[0].strip()[1: len(file_data[0]) - 2].split(","):
                    if lesson_:
                        list_str = lesson_.split(":")
                        lessons_list_[int(list_str[0])] = list_str[1].strip().replace("'", "")

                # список учеников
                students_list_ = {}
                for student_ in file_data[1].strip()[1: len(file_data[1]) - 2].split(","):
                    if student_:
                        list_str = student_.split(":")
                        students_list_[int(list_str[0])] = list_str[1].strip().replace("'", "")

                # журнал
                class_journal_ = {}
                str_ = file_data[2][1: len(file_data[2]) - 2].replace(" ", "")
                data = str_.split("},")

                for i in data:
                    lessons = i.split(":{")
                    students = lessons[1].replace("{", "").replace("}", "").split("],")

                    stud_dict = {}
                    for student_str in students:
                        student_ = student_str.split(":")
                        stud_dict[int(student_[0])] = list(
                            map(int, student_[1].replace("[", "").replace("]", "").split(",")))

                    class_journal_[int(lessons[0])] = stud_dict
        else:
            lessons_list_ = {}
            students_list_ = {}
            class_journal_ = {}

    return lessons_list_, students_list_, class_journal_


def save_class_journal(class_journal_: tuple):
    if mode == 1:
        with open("class_journal_json.db", "w", encoding="UTF-8") as file:
            file.write(
                json.dumps(class_journal_[0]) + "\n" + json.dumps(class_journal_[1]) + "\n" + json.dumps(
                    class_journal_[2]))
    else:
        with open("class_journal_parsing.db", "w", encoding="UTF-8") as file:
            print(class_journal_[0], file=file)
            print(class_journal_[1], file=file)
            print(class_journal_[2], file=file)


def add_lesson(class_journal_: (), lesson_: str):
    class_journal_[0][max(class_journal_[0]) + 1 if len(class_journal_[0]) else 1] = lesson_


def add_student(class_journal_: (), student_: str):
    class_journal_[1][max(class_journal_[1]) + 1 if len(class_journal_[1]) else 1] = student_


def show_lessons(class_journal_):
    print("\nПредметы:")
    for k, v in class_journal_[0].items():
        print(k, v)


def show_students(class_journal_):
    print("\n1Ученики:")
    for k, v in class_journal_[1].items():
        print(k, v)


def add_grade(class_journal_: (), student_: int, lesson_: int, grade_: int):
    if lesson_ not in class_journal_[2]:
        class_journal_[2][lesson_] = {}

    if student_ not in class_journal_[2][lesson_]:
        class_journal_[2][lesson_][student_] = []

    class_journal_[2][lesson_][student_].append(grade_)


def show_lesson_journal(class_journal_: (), lesson_: int):
    for k, v in class_journal_[1].items():
        print(k, v, end=" ")
        if lesson_ in class_journal_[2] and k in class_journal_[2][lesson_]:
            print(*class_journal_[2][lesson_][k], sep="\t", end="")
        print()


mode = 2  # 1 - json 2 - parsing
class_journal = load_class_journal()

operation = 0
while True:
    print(
        """\nМеню:
1 - Показать список предметов
2 - Добавить предмет
3 - Показать список учеников
4 - Добавить ученика
5 - Начать урок
6 - Завершить работу\n""")
    operation = input("Выберите режим: ")

    if len(operation) > 0 and operation.isdigit():
        operation = int(operation)

    match operation:
        case 1:
            show_lessons(class_journal)
        case 2:
            show_lessons(class_journal)
            lesson = input("Введите название предмета: ")
            if len(lesson) > 0:
                add_lesson(class_journal, lesson)
                show_lessons(class_journal)
        case 3:
            show_students(class_journal)
        case 4:
            show_students(class_journal)
            student = input("Введите ФИО ученика: ")
            if len(student) > 0:
                add_student(class_journal, student)
                show_students(class_journal)
        case 5:
            while True:
                show_lessons(class_journal)
                lesson = input("\nВыберите предмет (введите номер предмета): ")
                lessons = class_journal[0].keys()
                if len(lesson) > 0 and lesson.isdigit() and int(lesson) in lessons:
                    lesson = int(lesson)
                    print(f"\nИдет урок: {class_journal[0][lesson]}")

                    while True:
                        show_lesson_journal(class_journal, lesson)
                        student = input("\nК доске пойдет (введите номер ученика): ")
                        students = class_journal[1].keys()
                        if len(student) > 0 and student.isdigit() and int(student) in students:
                            while True:
                                grade = input("Поставьте оценку ученику: ")
                                if len(grade) > 0 and grade.isdigit() and int(grade) > 0:
                                    add_grade(class_journal, int(student), lesson, int(grade))
                                    break
                        elif len(student) == 0:
                            break
                else:
                    break
        case 6:
            save_class_journal(class_journal)
            break
        case _:
            pass
