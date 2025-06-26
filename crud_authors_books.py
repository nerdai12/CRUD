from crud_fun import*
from crud_fun import print_authors

authors = load_default_data()
id_counter = 3
books = load_default_data_books()

while True:
    print_info()
    choice = input()

    match choice:
        case '1':
            print_authors(authors)
        case '2':
            id_counter += 1
            authors.append(create_authors(id_counter))
        case '3':
            edit_authors(authors)
        case '4':
            delete_authors(authors)
        case '5':
            print("Programa sustabdyta")
            break

print(authors)
print(books)

print_authors_and_books(authors, books)