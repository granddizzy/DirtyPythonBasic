import text_fields as tf
from classes import Contact, Book


def main_menu() -> int:
    print(tf.menu)
    return input_choice()


def input_choice():
    while True:
        num = input(tf.input_choice)
        if num.isdigit() and 0 < int(num) < 13:
            return int(num)
        # else:
        #     print(tf.wrong_choice)


def show_contacts(contacts: list[Contact], message: str):
    if contacts:
        print("\n" + "=" * 83)
        for contact in contacts:
            print(contact, f"Книга: {contact.book_id:<2}", sep=" | ")

        print("=" * 83 + "\n")
    else:
        print_message(message)


def show_book_contacts(book: Book):
    print("\n" + "=" * 72)
    str_book = str(book)
    if str_book != "":
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
    name = input(tf.input_book_name)
    comment = input(tf.input_book_comment)
    return name, comment


def input_contact():
    name = input(tf.input_contact_name)
    phone = input(tf.input_contact_phone)
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
