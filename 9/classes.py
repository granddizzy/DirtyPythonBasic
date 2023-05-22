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

    def change_contact(self, name, phone, comment):
        self.name = name
        self.phone = phone
        self.comment = comment
        self.db.update_data("contacts", {"name": name, "phone": phone, "comment": comment}, {"contact_id": self.id})

    def del_contact(self):
        self.db.delete_data("contacts", {"contact_id": self.id})


class Book:
    def __init__(self, database: ClassDB, book_id: int):
        self.id = book_id
        self.db = database
        self.name, self.comment = self.db.get_data("books", ("name", "comment"), {"book_id": self.id}, fetchall=False)

    def get_contact(self, id):
        name, phone, comment = self.db.get_data("contacts", ("name", "phone", "comment"), {"contact_id": id})
        return Contact(self.db, self.id, id, name, phone, comment)

    def get_contact_list(self):
        return [Contact(self.db, *item) for item in
                self.db.get_data("contacts", ("book_id", "contact_id", "name", "phone", "comment"),
                                 {"book_id": self.id}, fetchall=True)]

    def get_contacts_ids(self):
        return [item[1] for item in self.db.get_data("contacts", ("book_id", "contact_id", "name", "phone", "comment"),
                                                     {"book_id": self.id}, fetchall=True)]

    def change_book(self, name, comment):
        self.name = name
        self.comment = comment
        self.db.update_data("books", {"name": name, "comment": comment}, {"book_id": self.id})

    def __str__(self):
        return "\n".join(map(str, self.get_contact_list()))

    def new_contact(self, contact: Contact):
        self.db.insert_data("contacts", {"name": contact.name, "phone": contact.phone, "comment": contact.comment,
                                         "book_id": contact.book_id})
