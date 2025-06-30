import csv

headers = ['id', 'title', 'genre', 'author_id']

def load_books():
    with open('books.csv', mode='r', encoding='utf-8') as file:
        return list(csv.DictReader(file))

def save_books(books):
    with open('books.csv', mode='w', newline='', encoding='utf-8') as file:
        writer = csv.DictWriter(file, fieldnames=headers)
        writer.writeheader()
        writer.writerows(books)

def create_book(books):
    print("Naujos knygos įtraukimas:")
    print("Įveskite pavadinimą:")
    title = input()
    print("Įveskite žanrą:")
    genre = input()
    print("Įveskite autoriaus ID:")
    author_id = input()
    new_id = str(int(books[-1]['id']) + 1) if len(books) > 0 else '1'
    books.append({
        'id': new_id,
        'title': title,
        'genre': genre,
        'author_id': author_id
    })
    save_books(books)

def edit_book(books):
    print("Knygos redagavimas. Pasirinkite įrašo ID, kurį norite redaguoti:")
    id = input()
    for book in books:
        if id == book['id']:
            print(f"{book['id']}. Pavadinimas: {book['title']}, Žanras: {book['genre']}, Autoriaus ID: {book['author_id']}")
            print("Įveskite naują pavadinimą:")
            book['title'] = input()
            print("Įveskite naują žanrą:")
            book['genre'] = input()
            print("Įveskite naują autoriaus ID:")
            book['author_id'] = input()
            break
    save_books(books)

def delete_book(books):
    print("Knygos šalinimas. Pasirinkite knygos ID, kuri norite pašalinti:")
    id = input()
    for book in books:
        if id == book['id']:
            print(f"{book['id']}. Šalinama knyga: {book['title']}")
            books.remove(book)
            break
    save_books(books)

def print_info():
    print("-------------------------------------------------------------------------------")
    print("1. Atvaizduoti knygų sąrašą")
    print("2. Įtraukti naują knygą")
    print("3. Koreguoti knygas")
    print("4. Šalinti knygą")
    print("5. Išeiti iš programos")
    print("------------------------------------Pasirinkite--------------------------------")

def print_books(books):
    for book in books:
        print(f"{book['id']}), Pavadinimas: {book['title']}, Žanras: {book['genre']}, Autoriaus ID: {book['author_id']}")
