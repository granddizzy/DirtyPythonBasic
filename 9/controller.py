import view
import model
import text_fields as tf


def start():
    model.create_db_tables()

    while True:
        if model.get_curr_book():
            view.print_message(tf.current_phone_book.replace("%name%", model.get_curr_book().name))
        else:
            view.print_message(tf.no_phone_book)

        choice = view.main_menu()
        match choice:
            case 1:
                # выбрать книгу
                books = model.get_books_list()
                view.show_books(list(map(str, books)))
                if len(books) > 0:
                    book_id = view.select_book([book.id for book in model.get_books_list()])
                    if book_id:
                        model.set_curr_book(book_id)
            case 2:
                # создать книгу
                view.show_books(list(map(str, model.get_books_list())))
                name, comment = view.input_book()
                model.create_book(name, comment)
                view.print_message(tf.sucessfull_create_phone_book.replace("%name%", name))
            case 3:
                # изменить книгу
                if model.get_curr_book():
                    book = model.get_curr_book()
                    book.name, book.comment = view.input_book()
                    book.update_db()
                    view.show_books(list(map(str, model.get_books_list())))
            case 4:
                # удалить книгу
                if model.get_curr_book():
                    book = model.get_curr_book()
                    book.del_book()
                    view.print_message(tf.sucessfull_delete_phone_book.replace("%name%", book.name))
                    view.show_books(list(map(str, model.get_books_list())))
                    model.set_curr_book(None)
            case 5:
                # просмотр контактов
                if model.get_curr_book():
                    view.show_book_contacts([str(contact) for contact in model.get_curr_book().get_contact_list()])
            case 6:
                # найти контакт
                view.show_contacts(
                    [(str(contact), contact.book_id) for contact in model.find_contacts(view.input_pattern())],
                    message=tf.no_find_contacts)
            case 7:
                # создать контакт
                if model.get_curr_book():
                    model.get_curr_book().add_contact(*view.input_contact())
                    view.show_book_contacts([str(contact) for contact in model.get_curr_book().get_contact_list()])
            case 8:
                # изменить контакт
                if model.get_curr_book():
                    view.show_book_contacts([str(contact) for contact in model.get_curr_book().get_contact_list()])
                    id = view.select_contact(model.get_curr_book().get_contacts_ids())
                    if id:
                        contact = model.get_curr_book().get_contact(id)
                        contact.name, contact.phone, contact.comment = view.input_contact()
                        contact.update_db()
                        view.show_book_contacts([str(contact) for contact in model.get_curr_book().get_contact_list()])
            case 9:
                # удалить контакт
                if model.get_curr_book():
                    view.show_book_contacts([str(contact) for contact in model.get_curr_book().get_contact_list()])
                    id = view.select_contact(model.get_curr_book().get_contacts_ids())
                    if id:
                        contact = model.get_curr_book().get_contact(id)
                        model.get_curr_book().get_contact(id).del_contact()
                        view.print_message(tf.sucessfull_delete_contact.replace("%name%", contact.name))
                        view.show_book_contacts([str(contact) for contact in model.get_curr_book().get_contact_list()])
            case 10:
                # сохранить книгу в файл
                if model.get_curr_book():
                    path = view.input_file()
                    if path:
                        model.save_book_in_file(path)
            case 11:
                # загрузить книгу из файла
                if model.get_curr_book():
                    path = view.input_file()
                    if path:
                        if not model.load_book_from_file(path):
                            view.print_message(tf.error_book_load)
            case _:
                break
