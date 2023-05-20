from Database.DB import ClassDB


class Contact:
    def __init__(self, book_id, id, name, phone, comment):
        self.id = id
        self.name = name
        self.phone = phone
        self.comment = comment
        self.book_id = book_id

    def __str__(self):
        return f"{self.id:<3} | {self.name:<20} | {self.phone:<20} | {self.comment:<20}"


class Book:
    def __init__(self, database: ClassDB, book_id: int):
        self.id = book_id
        self.db = database
        self.name, self.comment = self.db.db_get_book_info(self.id)

    def get_contact(self, id):
        name, phone, comment = self.db.get_contact(id)
        return Contact(self.id, id, name, phone, comment)

    def get_contact_list(self):
        return [Contact(*item) for item in self.db.get_contact_list(self.id)]

    def get_contacts_ids(self):
        return [item[1] for item in self.db.get_contact_list(self.id)]

    def new_contact(self, name, phone, comment):
        self.db.create_contact(name, phone, comment, self.id)

    def del_contact(self, contact):
        self.db.delete_contact(contact.id)

    def change_contact(self, contact, name, phone, comment):
        self.db.change_contact(contact, name, phone, comment)

    def __str__(self):
        return "\n".join(map(str, self.get_contact_list()))
