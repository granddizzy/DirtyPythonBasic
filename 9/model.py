import os
from Database import db


def get_books_list():
    return db.db_get_book_list()


def add_contact():
    pass


def del_contact():
    pass


def update_contact():
    pass


def create_book(name, comment):
    db.db_create_book(name, comment)


def delete_book(id):
    db.db_delete_book(id)


def get_book_info(id: int):
    return db.db_get_book_info(id)


