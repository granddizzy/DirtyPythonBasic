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
                name, comment = view.create_book()
                model.create_book(name, comment)
                view.print_message(tf.sucessfull_create_phone_book.replace("%name%", name))
            case 3:
                # удалить книгу
                view.show_books(model.get_books_list())
                id = view.select_book(model.get_books_ids())
                if id is not None:
                    name, _ = model.get_book_info(id)
                    model.delete_book(id)
                    view.print_message(tf.sucessfull_delete_phone_book.replace("%name%", name))
                    view.show_books(model.get_books_list())
            case 4:
                # просмотр контактов
                if curr_book_id >= 0:
                    view.show_book_contacts(model.get_curr_book())
            case 5:
                # найти контакт
                view.show_contacts(model.find_contacts(view.input_pattern()), message=tf.no_find_contacts)
            case 6:
                # добавить контакт
                if curr_book_id >= 0:
                    model.add_contact(*view.input_contact())
                    view.show_book_contacts(model.get_curr_book())
            case 7:
                # изменить контакт
                if curr_book_id >= 0:
                    view.show_book_contacts(model.get_curr_book())
                    id = view.select_contact(model.get_contacts_ids())
                    if id is not None:
                        model.change_contact(id, *view.input_contact())
                        view.show_book_contacts(model.get_curr_book())
            case 8:
                # удалить контакт
                if curr_book_id >= 0:
                    view.show_book_contacts(model.get_curr_book())
                    id = view.select_contact(model.get_contacts_ids())
                    if id is not None:
                        name, _, _ = model.get_contact_info(id)
                        model.del_contact(id)
                        view.print_message(tf.sucessfull_delete_contact.replace("%name%", name))
                        view.show_book_contacts(model.get_curr_book())
            case _:
                break
