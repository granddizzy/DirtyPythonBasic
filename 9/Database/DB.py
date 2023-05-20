import sqlite3


class ClassDB:
    def __init__(self, db_path: str = "Database/book.db"):
        self.db_path = db_path

    @property
    def connection(self):
        return sqlite3.connect(self.db_path)

    def execute(self, querry: str, parametrs: tuple = tuple(), fetchone=False, fetchall=False, commit=False):
        connection = self.connection
        cursor = connection.cursor()
        data = None

        try:
            cursor.execute(querry, parametrs)
        except:
            print(f"DB QUERY FAILURE:\n{querry}")
            print(parametrs)

        if commit:
            connection.commit()
        if fetchone:
            data = cursor.fetchone()
        if fetchall:
            data = cursor.fetchall()
        connection.close()
        return data

    @staticmethod
    def extract_kwargs(querry: str, parameters: dict) -> tuple:
        querry += " AND ".join(f"{key} = ?" for key in parameters)
        return querry, tuple(parameters.values())

    def disconnect(self):
        self.connection.close()

    def db_get_book_list(self):
        query = """SELECT * FROM books"""
        return self.execute(query, fetchall=True)

    def db_create_book(self, name: str, comment: str):
        query = """INSERT INTO books(name, comment) VALUES (?, ?)"""
        self.execute(query, (name, comment), commit=True)

    def db_delete_book(self, id: int):
        query = """DELETE FROM contacts WHERE book_id=?"""
        self.execute(query, (id,), commit=True)
        query = """DELETE FROM books WHERE book_id=?"""
        self.execute(query, (id,), commit=True)

    def db_get_book_info(self, id: int) -> list[tuple]:
        query = """SELECT name, comment FROM books WHERE book_id=?"""
        return self.execute(query, (id,), fetchone=True)

    def get_contact(self, contact_id: int) -> tuple:
        query = """SELECT name, phone, comment FROM contacts WHERE contact_id=?"""
        return self.execute(query, (contact_id,), fetchone=True)

    def get_contact_list(self, id: int) -> list[tuple]:
        query = """SELECT book_id, contact_id, name, phone, comment FROM contacts WHERE book_id=?"""
        return self.execute(query, (id,), fetchall=True)

    def create_contact(self, name: str, phone: str, comment: str, book_id: int):
        query = """INSERT INTO contacts (book_id, name, phone, comment) VALUES (?, ?, ?, ?)"""
        self.execute(query, (book_id, name, phone, comment), commit=True)

    def delete_contact(self, contact_id: int):
        query = """DELETE FROM contacts WHERE contact_id=?"""
        self.execute(query, (contact_id,), commit=True)

    def change_contact(self, contact, name, phone, comment):
        query = """UPDATE contacts SET name=?, phone=?, comment=? WHERE contact_id=?"""
        self.execute(query, (name, phone, comment, contact.id), commit=True)

    def get_like(self, pattern) -> list[tuple]:
        query = """SELECT book_id, contact_id, name, phone, comment FROM contacts WHERE name LIKE ?"""
        return self.execute(query, ('%'+pattern+'%',), fetchall=True)


def create_tables(db_: ClassDB):
    query = """CREATE TABLE IF NOT EXISTS books (book_id INTEGER PRIMARY KEY AUTOINCREMENT,
              name VARCHAR, comment VARCHAR)"""
    db_.execute(query)

    query = """CREATE TABLE IF NOT EXISTS contacts (contact_id INTEGER PRIMARY KEY AUTOINCREMENT,
          book_id INTEGER, name VARCHAR, phone VARCHAR, comment VARCHAR)"""
    db_.execute(query)
