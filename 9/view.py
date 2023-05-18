import text_fields as tf


def main_menu() -> int:
    print(tf.menu)
    return input_choice()


def input_choice():
    while True:
        num = input(tf.input_choice)
        if num.isdigit() and 0 < int(num) < 9:
            return int(num)
        # else:
        #     print(tf.wrong_choice)


def show_contacts(contacts: list[dict[str]], message: str):
    if contacts:
        print("\n" + "=" * 72)
        # for i, contact in enumerate(contacts, 1):
        #     print(f"{i:<3} | {contact[0]:<20} | {contact[1]:<20} | {contact[2]:<20}")
        for contact in contacts:
            print(f"{contact[0]:<3} | {contact[1]:<20} | {contact[2]:<20} | {contact[3]:<20}")

        print("=" * 72 + "\n")
    else:
        print_message(tf.no_contacts)


def print_message(message: str):
    print("\n" + "=" * len(message))
    print(message)
    print("=" * len(message) + "\n")


# def input_contact(message: list) -> dict[str, str]:
#     name = input(message[0])
#     phone = input(message[1])
#     comment = input(message[2])
#     return {"name": name, "phone": phone, "comment": comment}


def show_books(books: list):
    if len(books) == 0:
        print_message(tf.no_phone_books)
    else:
        print("\n" + "=" * 72)
        for book in books:
            print(f"{book[0]:<3} | {book[1]:<20} | {book[2]:<20}")
        print("=" * 72 + "\n")


def select_book():
    while True:
        num = input(tf.select_book)
        if num.isdigit():  # and 0 < int(num) <= count:
            return int(num)


def create_book():
    name = input(tf.input_book_name)
    comment = input(tf.input_book_comment)
    return name, comment


def input_contact():
    name = input(tf.input_contact_name)
    phone = input(tf.input_contact_phone)
    comment = input(tf.input_contact_comment)
    return name, phone, comment


def select_contact():
    while True:
        num = input(tf.select_contact)
        if num.isdigit():  # and 0 < int(num) <= count:
            return int(num)
