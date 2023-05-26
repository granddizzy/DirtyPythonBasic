import view
import model
import text_fields as tf


def start():
    model.create_db_tables()

    while True:
        if model.curr_book:
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
                    book_id = view.select_book(model.get_books_ids())
                    if book_id:
                        model.set_curr_book(book_id)
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
                if id:
                    model.change_book(id, *view.input_book())
                    view.show_books(model.get_books_list())
            case 4:
                # удалить книгу
                view.show_books(model.get_books_list())
                id = view.select_book(model.get_books_ids())
                if id:
                    name, _ = model.get_book_info(id)
                    model.delete_book(id)
                    view.print_message(tf.sucessfull_delete_phone_book.replace("%name%", name))
                    view.show_books(model.get_books_list())
            case 5:
                # просмотр контактов
                if model.curr_book:
                    view.show_book_contacts(str(model.get_curr_book()))
            case 6:
                # найти контакт
                view.show_contacts(
                    [(str(contact), contact.book_id) for contact in model.find_contacts(view.input_pattern())],
                    message=tf.no_find_contacts)
            case 7:
                # добавить контакт
                if model.curr_book:
                    model.add_contact(*view.input_contact())
                    view.show_book_contacts(str(model.get_curr_book()))
            case 8:
                # изменить контакт
                if model.curr_book:
                    view.show_book_contacts(str(model.get_curr_book()))
                    id = view.select_contact(model.get_contacts_ids())
                    if id:
                        model.change_contact(id, *view.input_contact())
                        view.show_book_contacts(str(model.get_curr_book()))
            case 9:
                # удалить контакт
                if model.curr_book:
                    view.show_book_contacts(str(model.get_curr_book()))
                    id = view.select_contact(model.get_contacts_ids())
                    if id:
                        name, _, _ = model.get_contact_info(id)
                        model.del_contact(id)
                        view.print_message(tf.sucessfull_delete_contact.replace("%name%", name))
                        view.show_book_contacts(str(model.get_curr_book()))
            case 10:
                # сохранить книгу в файл
                if model.curr_book:
                    path = view.input_file()
                    if path:
                        model.save_book_in_file(path)
            case 11:
                # загрузить книгу из файла
                if model.curr_book:
                    path = view.input_file()
                    if path:
                        if not model.load_book_from_file(path):
                            view.print_message(tf.error_book_load)
            case _:
                break
