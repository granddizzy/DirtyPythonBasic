import view
import model
import text_fields as tf

curr_book_id = -1


def start():
    global curr_book_id
    model.create_db_tables()

    while True:
        if curr_book_id >= 0:
            view.print_message(tf.current_phone_book.replace("%name%", model.get_curr_book().name))
        else:
            view.print_message(tf.no_phone_book)

        choice = view.main_menu()
        match choice:
            case 1:
                # выбрать книгу
                books = model.get_books_list()
                view.show_books(books)
                if len(books) > 0:
                    curr_book_id = view.select_book(model.get_books_ids())
                    if curr_book_id is not None:
                        model.set_curr_book(curr_book_id)
                    else:
                        curr_book_id = -1
            case 2:
                # добавить книгу
                view.show_books(model.get_books_list())
                name, comment = view.input_book()
                model.create_book(name, comment)
                view.print_message(tf.sucessfull_create_phone_book.replace("%name%", name))
            case 3:
                # изменить книгу
                view.show_books(model.get_books_list())
                id = view.select_book(model.get_books_ids())
                if id is not None:
                    model.change_book(id, *view.input_book())
                    view.show_books(model.get_books_list())
            case 4:
                # удалить книгу
                view.show_books(model.get_books_list())
                id = view.select_book(model.get_books_ids())
                if id is not None:
                    name, _ = model.get_book_info(id)
                    model.delete_book(id)
                    view.print_message(tf.sucessfull_delete_phone_book.replace("%name%", name))
                    view.show_books(model.get_books_list())
            case 5:
                # просмотр контактов
                if curr_book_id >= 0:
                    view.show_book_contacts(str(model.get_curr_book()))
            case 6:
                # найти контакт
                view.show_contacts(
                    [(str(contact), contact.book_id) for contact in model.find_contacts(view.input_pattern())],
                    message=tf.no_find_contacts)
            case 7:
                # добавить контакт
                if curr_book_id >= 0:
                    model.add_contact(*view.input_contact())
                    view.show_book_contacts(str(model.get_curr_book()))
            case 8:
                # изменить контакт
                if curr_book_id >= 0:
                    view.show_book_contacts(str(model.get_curr_book()))
                    id = view.select_contact(model.get_contacts_ids())
                    if id is not None:
                        model.change_contact(id, *view.input_contact())
                        view.show_book_contacts(str(model.get_curr_book()))
            case 9:
                # удалить контакт
                if curr_book_id >= 0:
                    view.show_book_contacts(str(model.get_curr_book()))
                    id = view.select_contact(model.get_contacts_ids())
                    if id is not None:
                        name, _, _ = model.get_contact_info(id)
                        model.del_contact(id)
                        view.print_message(tf.sucessfull_delete_contact.replace("%name%", name))
                        view.show_book_contacts(str(model.get_curr_book()))
            case 10:
                if curr_book_id >= 0:
                    path = view.input_file()
                    if path:
                        model.save_book_in_file(path)
            case 11:
                if curr_book_id >= 0:
                    path = view.input_file()
                    if path:
                        if not model.load_book_from_file(path):
                            view.print_message(tf.error_book_load)
            case _:
                break
