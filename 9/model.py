from Database import ClassDB, create_tables
from classes import Book, Contact
import json

db = ClassDB()
curr_book: Book | None = None


def get_books_list() -> list[Book]:
    return [Book(db, item[0], item[1], item[2]) for item in
            db.get_data("books", ("book_id", "name", "comment"), fetchall=True)]


def get_book(book_id: int) -> Book:
    book_data = db.get_data("books", ("name", "comment"), {"book_id": book_id})
    if book_data:
        return Book(db, book_id, book_data[0], book_data[1])


def create_book(name: str, comment: str):
    db.insert_data("books", {"name": name, "comment": comment})


def create_db_tables():
    create_tables(db)


def get_curr_book() -> Book:
    return curr_book


def set_curr_book(id: int | None):
    global curr_book
    if id:
        curr_book = get_book(id)
    else:
        curr_book = None


def find_contacts(pattern) -> list[Contact]:
    return [Contact(db, *item) for item in
            db.get_data("contacts", ("book_id", "contact_id", "name", "phone", "comment"),
                        {"name": '%' + pattern + '%', "phone": '%' + pattern + '%',
                         "comment": '%' + pattern + '%'},
                        fetchall=True, like=True, or_and="OR")]


def save_book_in_file(path):
    with open(path, "w", encoding="UTF-8") as file:
        file.write(json.dumps(list(map(lambda x: x.get_dump(), get_curr_book().get_contact_list()))))


def load_book_from_file(path) -> bool:
    with open(path, "r", encoding="UTF-8") as file:
        get_curr_book().clear()
        try:
            for i in json.load(file):
                get_curr_book().add_contact(i["name"], i["phone"], i["comment"])
        except:
            return False

    return True
