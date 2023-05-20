from Database import ClassDB, create_tables
from classes import Book, Contact

db = ClassDB()
curr_book: Book


def get_books_list() -> list[tuple]:
    return db.db_get_book_list()


def get_books_ids() -> list:
    return [item[0] for item in db.db_get_book_list()]


def add_contact(name, phone, comment):
    global curr_book
    curr_book.new_contact(name, phone, comment)


def get_contact_list() -> list[tuple]:
    global curr_book
    return curr_book.get_contact_list()


def del_contact(id: int):
    global curr_book
    curr_book.del_contact(curr_book.get_contact(id))


def create_book(name: str, comment: str):
    db.db_create_book(name, comment)


def delete_book(id: int):
    db.db_delete_book(id)


def get_book_info(id: int):
    return db.db_get_book_info(id)


def create_db_tables():
    create_tables(db)


def get_curr_book() -> Book:
    return curr_book


def set_curr_book(id: int):
    global curr_book
    curr_book = Book(db, id)


def change_contact(id, name, phone, comment):
    global curr_book
    curr_book.change_contact(curr_book.get_contact(id), name, phone, comment)


def get_contact_info(id: int) -> tuple:
    global curr_book
    contact = curr_book.get_contact(id)
    return contact.name, contact.phone, contact.comment


def get_contacts_ids() -> list:
    return curr_book.get_contacts_ids()


def find_contacts(pattern) -> list[Contact]:
    return [Contact(*item) for item in db.get_like(pattern)]
