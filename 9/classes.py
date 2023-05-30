from Database.DB import ClassDB


class Contact:
    def __init__(self, database: ClassDB, book_id: int, id: int, name: str, phone: str, comment: str):
        self.id = id
        self.name = name
        self.phone = phone
        self.comment = comment
        self.book_id = book_id
        self.db = database

    def __str__(self):
        return f"{self.id:<3} | {self.name:<20} | {self.phone:<20} | {self.comment:<20}"

    def get_dump(self):
        return {"id": self.id, "name": self.name, "phone": self.phone, "comment": self.comment}

    def update_db(self):
        self.db.update_data("contacts", {"name": self.name, "phone": self.phone, "comment": self.comment},
                            {"contact_id": self.id})

    def del_contact(self):
        self.db.delete_data("contacts", {"contact_id": self.id})


class Book:
    def __init__(self, database: ClassDB, book_id: int, name: str, comment: str):
        self.id = book_id
        self.db = database
        self.name = name
        self.comment = comment

    def get_contact(self, id) -> Contact:
        name, phone, comment = self.db.get_data("contacts", ("name", "phone", "comment"), {"contact_id": id})
        return Contact(self.db, self.id, id, name, phone, comment)

    def get_contact_list(self) -> list[Contact]:
        return [Contact(self.db, *item) for item in
                self.db.get_data("contacts", ("book_id", "contact_id", "name", "phone", "comment"),
                                 {"book_id": self.id}, fetchall=True)]

    def get_contacts_ids(self) -> list[int]:
        return [item[1] for item in self.db.get_data("contacts", ("book_id", "contact_id", "name", "phone", "comment"),
                                                     {"book_id": self.id}, fetchall=True)]

    def __str__(self):
        return f"{self.id:<3} | {self.name:<20} | {self.comment:<20}"

    def update_db(self):
        self.db.update_data("books", {"name": self.name, "comment": self.comment}, {"book_id": self.id})

    def del_book(self):
        self.db.delete_data("contacts", {"book_id": self.id})
        self.db.delete_data("books", {"book_id": self.id})

    def add_contact(self, name: str, phone: str, comment: str):
        self.db.insert_data("contacts", {"name": name, "phone": phone, "comment": comment, "book_id": self.id})

    def clear(self):
        for contact in self.get_contact_list():
            self.db.delete_data("contacts", {"contact_id": contact.id})
