import csv

book_headers = ['id', 'title', 'genre', 'author_id']


def print_info():
    print("-------------------------------------------------------------------------------")
    print("1. Atvaizduoti autorių sąrašą")
    print("2. Įtraukti naują autorių")
    print("3. Koreguoti autorius")
    print("4. Šalinti autorius")
    print("5. Išeiti iš programos")
    print("6. Rodyti autoriaus knygas pagal ID")
    print("7. Pridėti knygą autoriui")
    print("8. Pašalinti autoriaus knygą")
    print("Pasirinkite veiksmą: ", end='')
    print("------------------------------------Pasirinkite--------------------------------")

def load_authors():
    with open('english_authors_list.csv', mode='r', encoding='utf-8') as file:
        return list(csv.DictReader(file))
#     return [
#     {
#         'id': 1,
#         "name": "Jonas ",
#         "surname": "Biliūnas"
#     },
#     {
#         'id': 2,
#         "name": "Tomas ",
#         "surname": "Dirgėla"
#     },
#     {
#         'id': 3,
#         "name": "Janina ",
#         "surname": "Degutytė"
#     }
# ]

def delete_authors(authors):
    print("Autorių šalinimas. Pasirinkite autoriaus ID, kurį norite pašalinti")
    id = input()
    for aut in authors:
        if id == str(aut['id']):
            print(f"{aut['id']}. Šalinama Autoriaus vardas {aut['name']} pavardė {aut['surname']}")
            del authors[authors.index(aut)]

def create_authors(id_counter):
    print("naujo autoriaus įtraukimas:")
    print("Įveskite vardą")
    name = input()
    print("Įveskite pavardę")
    surname = input()
    id_counter += 1
    return {
                'id': id_counter,
                "name": name,
                "surname": surname
            }

def edit_authors(authors):
    print("autorių redagavimas. Pasirinkite įrašo ID, kurį norite redaguoti.")
    id = input()
    for aut in authors:
        if id == str(aut['id']):
            print(f"{aut['id']}. Autoriaus vardas {aut['name']} pavardė {aut['surname']}")
            print("Įveskite vardą")
            aut['name'] = input()
            print("Įveskite pavardę")
            aut['surname'] = input()
            break

def delete_authors(authors):
    print("Autorių šalinimas. Pasirinkite autoriaus ID, kurį norite pašalinti")
    id = input()
    for aut in authors:
        if id == str(aut['id']):
            print(f"{aut['id']}. Šalinama Autoriaus vardas {aut['name']} pavardė {aut['surname']}")
            del authors[authors.index(aut)]

def books():
    return [
    {
        'id': 1,
        "title": "Laimės žiburys ",
        "genre": "Novelė",
        "author_id": 1
    },
    {
        'id': 2,
        "title": "Raketų medžioklė ",
        "genre": "Vaikų literatūra",
        "author_id": 2
    },
    {
        'id': 3,
        "title": "Pelėdžiuko sapnas ",
        "genre": "Poezija",
        "author_id": 3
    }
]


# def print_authors_and_books(authors, books):
#     for aut in authors:
#         print(f"{aut['id']}), Autoriaus vardas {aut['name']} pavardė {aut['surname']}")
#     for book in books:
#         print(f"{book['id']}), Pavadinimas {book['title']} žanras {book['genre']} autoriaus id {book['author_id']}")
#
def save_books(books):
    with open('books.csv', mode='w', newline='', encoding='utf-8') as file:
        writer = csv.DictWriter(file, fieldnames=book_headers)
        writer.writeheader()
        writer.writerows(books)

def assign_books_to_authors(authors, books):
    for author in authors:
        author_books = [book for book in books if book['author_id'] == author['id']]
        author['books'] = author_books

def print_books_by_author(authors, books):
    print("Įveskite autoriaus ID, kurio knygas norite pamatyti:")
    author_id = input()
    matching_authors = [a for a in authors if a['id'] == author_id]
    if not matching_authors:
        print("Autorius nerastas.")
        return

    author = matching_authors[0]
    author_books = [book for book in books if str(book['author_id']) == author_id]

    print(f"\n{author['name']} {author['surname']} parašė šias knygas:")
    if author_books:
        for book in author_books:
            print(f"  - {book['title']} ({book['genre']})")
    else:
        print("  - Knygų nerasta.")

def add_book_to_author(books, authors):
    author_id = input("Įveskite autoriaus ID, kuriam norite pridėti knygą: ")
    author = next((a for a in authors if a['id'] == author_id), None)
    if not author:
        print("Toks autorius nerastas.")
        return
    title = input("Įveskite knygos pavadinimą: ")
    genre = input("Įveskite knygos žanrą: ")
    new_book_id = str(int(books[-1]['id']) + 1) if books else '1'
    books.append({
        'id': new_book_id,
        'title': title,
        'genre': genre,
        'author_id': author_id
    })
    save_books(books)
    print(f"Knyga '{title}' pridėta autoriui {author['name']} {author['surname']}.")

def delete_book_by_author(books, authors):
    print("Įveskite autoriaus ID, kurio knygą norite ištrinti:")
    author_id = input()

author = next((a for a in authors if a['id'] == author_id), None)
if not author:
        print("Toks autorius nerastas.")

author_books = [b for b in books if b['author_id'] == author_id]
if not author_books:
    print("Šis autorius neturi knygų.")


print(f"Autoriaus {author['name']} {author['surname']} knygos:")
for b in author_books:
    print(f"  {b['id']}: {b['title']} ({b['genre']})")

print("Įveskite knygos ID, kurią norite pašalinti:")
book_id = input()

book_to_delete = next((b for b in books if b['id'] == book_id and b['author_id'] == author_id), None)
if not book_to_delete:
    print("Tokia knyga nerasta arba nepriklauso šiam autoriui.")


books.remove(book_to_delete)
save_books(books)
print(f"Knyga „{book_to_delete['title']}“ pašalinta sėkmingai.")