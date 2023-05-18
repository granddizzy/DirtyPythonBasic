# from .DB import create_tables, db_get_book_list, db_create_book, db_get_book_info, db_delete_book

# __all__ = ["create_tables", "db_get_book_list", "db_create_book", "db_get_book_info","db_delete_book"]
from .DB import db, create_tables

__all__ = ["db", "create_tables"]