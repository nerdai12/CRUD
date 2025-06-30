from fileCrud import *
from crud_fun import print_authors

authors = load_authors()
id_counter = 3

while True:
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
            break

