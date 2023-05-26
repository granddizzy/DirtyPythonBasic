import text_fields as tf


def main_menu() -> int:
    print(tf.menu)
    return input_choice()


def input_choice() -> int | None:
    while True:
        num = input(tf.input_choice)
        if num.isdigit() and 0 < int(num) < 13:
            return int(num)
        elif num == "":
            return None


def show_contacts(contacts: list[tuple], message: str):
    if contacts:
        print("\n" + "=" * 83)
        for contact in contacts:
            print(contact[0], f"Книга: {contact[1]:<2}", sep=" | ")

        print("=" * 83 + "\n")
    else:
        print_message(message)


def show_book_contacts(book: str):
    print("\n" + "=" * 72)
    if book != "":
        print(book)
    else:
        print(tf.no_contacts)
    print("=" * 72 + "\n")


def print_message(message: str):
    print("\n" + "=" * len(message))
    print(message)
    print("=" * len(message) + "\n")


def show_books(books: list):
    if len(books) == 0:
        print_message(tf.no_phone_books)
    else:
        print("\n" + "=" * 72)
        for book in books:
            print(f"{book[0]:<3} | {book[1]:<20} | {book[2]:<20}")
        print("=" * 72 + "\n")


def select_book(books_ids):
    while True:
        num = input(tf.select_book)
        if num.isdigit() and int(num) in books_ids:
            return int(num)
        elif num == "":
            return None


def input_book():
    while True:
        if len(name := input(tf.input_book_name)) > 0:
            break

    comment = input(tf.input_book_comment)
    return name, comment


def input_contact():
    while True:
        if len(name := input(tf.input_contact_name)) > 0:
            break

    while True:
        if len(phone := input(tf.input_contact_phone).replace(" ", "")) > 0 and phone.isdigit():
            break

    comment = input(tf.input_contact_comment)
    return name, phone, comment


def select_contact(contacts_ids):
    while True:
        num = input(tf.select_contact)
        if num.isdigit() and int(num) in contacts_ids:
            return int(num)
        elif num == "":
            return None


def input_pattern():
    return input(tf.input_pattern)


def input_file():
    return input(tf.input_file_path)
