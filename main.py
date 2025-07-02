
from db_CRUD import *


authors = load_authors()


while True:
    authors = load_authors()
    books = load_books()
    print_info()
    choice = input()

    match choice:
        case '1':
            print_authors(authors)
        case '2':
            create_authors(authors)
        case '3':
            edit_authors(authors)
        case '4':
            delete_authors(authors)
        case '5':
            print("Programa sustabdyta")
        case '6':
            print_books_by_author(authors, books)
        case '7':
            add_book_to_author(books, authors)
        case '8':
            delete_book_by_author(books, authors)
        case _:
            print("Neteisingas pasirinkimas, bandykite dar kartą.")
            break


#
#
