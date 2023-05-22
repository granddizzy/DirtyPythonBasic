from Database import ClassDB, create_tables
from classes import Book, Contact
import json

db = ClassDB()
curr_book: Book


def get_books_list() -> list[tuple]:
    return db.get_data("books", ("*",), fetchall=True)


def get_books_ids() -> list:
    return [item[0] for item in db.get_data("books", ("*",), fetchall=True)]


def add_contact(name, phone, comment):
    global curr_book
    curr_book.new_contact(Contact(curr_book.db, curr_book.id, 0, name, phone, comment))


def get_contact_list() -> list[Contact]:
    global curr_book
    return curr_book.get_contact_list()


def del_contact(id: int):
    global curr_book
    curr_book.get_contact(id).del_contact()


def create_book(name: str, comment: str):
    db.insert_data("books", {"name": name, "comment": comment})


def delete_book(id: int):
    db.delete_data("contacts", {"book_id": id})
    db.delete_data("books", {"book_id": id})


def get_book_info(id: int):
    return db.get_data("books", ("name", "comment"), {"book_id": id})


def create_db_tables():
    create_tables(db)


def get_curr_book() -> Book:
    return curr_book


def set_curr_book(id: int):
    global curr_book
    curr_book = Book(db, id)


def change_contact(id, name, phone, comment):
    global curr_book
    curr_book.get_contact(id).change_contact(name, phone, comment)


def change_book(id, name, comment):
    Book(db, id).change_book(name, comment)


def get_contact_info(id: int) -> tuple:
    global curr_book
    contact = curr_book.get_contact(id)
    return contact.name, contact.phone, contact.comment


def get_contacts_ids() -> list:
    return curr_book.get_contacts_ids()


def find_contacts(pattern) -> list[Contact]:
    return [Contact(db, *item) for item in
            db.get_data("contacts", ("book_id", "contact_id", "name", "phone", "comment"),
                        {"name": '%' + pattern + '%', "phone": '%' + pattern + '%', "comment": '%' + pattern + '%'},
                        fetchall=True, like=True, or_and="OR")]


def save_book_in_file(path):
    with open(path, "w", encoding="UTF-8") as file:
        file.write(json.dumps(list(map(lambda x: x.get_dump(), get_contact_list()))))


def load_book_from_file(path) -> bool:
    with open(path, "r", encoding="UTF-8") as file:
        clean_book()
        try:
            for i in json.load(file):
                curr_book.new_contact(Contact(db, curr_book.id, i["id"], i["name"], i["phone"], i["comment"]))
        except:
            return False

    return True


def clean_book():
    for contact in get_contact_list():
        db.delete_data("contacts", {"contact_id": contact.id})
