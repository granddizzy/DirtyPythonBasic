import view
import model
import text_fields as tf
from Database import create_tables, db
from classes import Book, Contact
curr_book = None


def start():
    global curr_book
    create_tables(db)

    while True:
        if isinstance(curr_book, Book):
            view.print_message(tf.current_phone_book.replace("%name%", curr_book.name))

        choice = view.main_menu()
        match choice:
            case 1:
                # выбрать книгу
                books = model.get_books_list()
                view.show_books(books)
                if len(books) > 0:
                    curr_book_id = view.select_book()
                    curr_book = Book(db, curr_book_id)
            case 2:
                # добавить книгу
                books = model.get_books_list()
                view.show_books(books)
                name, comment = view.create_book()
                model.create_book(name, comment)
                view.print_message(tf.sucessfull_create_phone_book.replace("%name%", name))
            case 3:
                # удалить книгу
                books = model.get_books_list()
                view.show_books(books)
                id = view.select_book(len(books))
                name = db.db_get_book_info(id)[0]
                model.delete_book(id)
                view.print_message(tf.sucessfull_delete_phone_book.replace("%name%", name))
                view.show_books(books)
            case 4:
                # просмотр контактов
                if isinstance(curr_book, Book):
                    view.show_contacts(curr_book.get_contact_list(), message=tf.no_contacts)
                else:
                    view.print_message(tf.no_phone_book)
            case 5:
                # найти контакт
                pass
            case 6:
                # добавить контакт
                if isinstance(curr_book, Book):
                    name, phone, comment = view.input_contact()
                    curr_book.new_contact(name, phone, comment)
                    view.show_contacts(curr_book.get_contact_list(), message=tf.no_contacts)
                else:
                    view.print_message(tf.no_phone_book)
            case 7:
                # изменить контакт
                if isinstance(curr_book, Book):
                    view.show_contacts(curr_book.get_contact_list(), message=tf.no_contacts)
                    id = view.select_contact()
                    contact = curr_book.get_contact(id)
                    name, phone, comment = view.input_contact()
                    curr_book.change_contact(contact, name, phone, comment)
                    view.show_contacts(curr_book.get_contact_list(), message=tf.no_contacts)
                else:
                    view.print_message(tf.no_phone_book)
            case 8:
                # удалить контакт
                if isinstance(curr_book, Book):
                    view.show_contacts(curr_book.get_contact_list(), message=tf.no_contacts)
                    id = view.select_contact()
                    curr_book.del_contact(curr_book.get_contact(id))
                    view.show_contacts(curr_book.get_contact_list(), message=tf.no_contacts)
                else:
                    view.print_message(tf.no_phone_book)
            case _:
                break
