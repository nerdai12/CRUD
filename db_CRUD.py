import mysql.connector

DB_CONFIG = {
    'host':'localhost', #127.0.0.1 alternatyva rasymui "localhost" ;)
    'port': 3306,
    'user':'root',
    'password':"",
    'database':'library'
}

headers = ['id', 'name', 'surname']

def get_conn():
    return mysql.connector.connect(**DB_CONFIG)

def load_authors():
    conn = get_conn()
    cur = conn.cursor()
    cur.execute("select * from authors")
    rows = cur.fetchall()
    cur.close()
    conn.close()
    print(rows)

    authors = []
    for row in rows:
        author = {}
        for i in range(len(headers)):
            author[headers[i]] = str(row[i])
        authors.append(author)
    # authors = [dict(zip(headers, map(str, row))) for row in rows] #fancy pantsy alternatyva tam paciam
    return authors

def create_authors(authors):
    print("naujo autoriaus įtraukimas:")
    print("Įveskite vardą")
    name = input()
    print("Įveskite pavardę")
    surname = input()

    conn = get_conn()
    cur = conn.cursor()

    cur.execute("insert into authors (name, surname) values (%s, %s)", (name, surname))
    conn.commit()

    cur.close()
    conn.close()

def edit_authors(authors):
    print("autorių redagavimas. Pasirinkite įrašo ID, kurį norite redaguoti.")
    id = input()
    conn = get_conn()
    cur = conn.cursor()
    cur.execute("select * from authors where id = %s", (id,))
    row = cur.fetchone()
    if row:
        print(f"{row[0]}. Autoriaus vardas {row[1]} pavardė {row[2]}")
        print("Įveskite vardą")
        name = input()
        print("Įveskite pavardę")
        surname = input()
        cur.execute('update authors set name = %s, surname = %s where id = %s;',(name,surname,id))
        conn.commit()
    cur.close()
    conn.close()

def delete_authors(authors):
    print("Autorių šalinimas. Pasirinkite autoriaus ID, kurį norite pašalinti")
    id = input()
    for aut in authors:
        if id == str(aut['id']):
            print(f"{aut['id']}. Šalinama Autoriaus vardas {aut['name']} pavardė {aut['surname']}")

    conn = get_conn()
    cur = conn.cursor()

    cur.execute("delete from authors where id = %s", (id,))
    conn.commit()

    cur.close()
    conn.close()
    # print("Atlikome trynimo veiksmą")

book_headers = ['id', 'title', 'genre', 'author_id']

def load_books():
    conn = get_conn()
    cur = conn.cursor()
    cur.execute("select * from books")
    rows = cur.fetchall()
    cur.close()
    conn.close()
    print(rows)

    books = []
    for row in rows:
        book = {}
        for i in range(len(book_headers)):
            book[book_headers[i]] = str(row[i])
        books.append(book)
    # books = [dict(zip(headers, map(str, row))) for row in rows] #fancy pantsy alternatyva tam paciam
    return books

def assign_books_to_authors(authors, books):
    for author in authors:
        author_books = [book for book in books if book['author_id'] == author['id']]
        author['books'] = author_books

def get_data_from_db():
    conn = get_conn()
    cur = conn.cursor()

    cur.execute("SELECT id, name, surname FROM authors")
    authors_raw = cur.fetchall()

    cur.execute("SELECT id, title, genre, author_id FROM books")
    books_raw = cur.fetchall()

    cur.close()
    conn.close()

    authors = [{'id': a[0], 'name': a[1], 'surname': a[2]} for a in authors_raw]
    books = [{'id': b[0], 'title': b[1], 'genre': b[2], 'author_id': b[3]} for b in books_raw]

    return authors, books

def print_books_by_author(authors, books):
    print("Įveskite autoriaus ID, kurio knygas norite pamatyti:")
    try:
        author_id = int(input())
    except ValueError:
        print("Blogas autoriaus ID formatas.")
        return
    print("author_id:", author_id)
    print("authors sample:", authors[:3])

    matching_authors = [a for a in authors if int(a['id']) == author_id]
    if not matching_authors:
        print("Autorius nerastas.")
        return

    author = matching_authors[0]
    author_books = [book for book in books if book['author_id'] == author_id]

    print(f"\n{author['name']} {author.get('surname', '')} parašė šias knygas:")
    if author_books:
        for book in author_books:
            print(f"  - {book['title']} ({book['genre']})")
    else:
        print("  - Knygų nerasta.")

    authors, books = get_data_from_db()
    print_books_by_author(authors, books)

def add_book_to_author(books, authors):
    author_id = input("Įveskite autoriaus ID, kuriam norite pridėti knygą: ")
    # author = next((a for a in authors if a['id'] == author_id), None)
    # if not author:
    #     print("Toks autorius nerastas.")
    #     return
    title = input("Įveskite knygos pavadinimą: ")
    genre = input("Įveskite knygos žanrą: ")
    # # new_book_id = str(int(books[-1]['id']) + 1) if books else '1'
    # books.append({
    #     'id': new_book_id,
    #     'title': title,
    #     'genre': genre,
    #     'author_id': author_id
    # })
    print(f"Knyga '{title}' pridėta autoriui {authors[1]} {authors[2]}.")

    conn = get_conn()
    cur = conn.cursor()

    cur.execute("insert into books (title, genre, author_id) values (%s, %s, %s)", (title, genre, author_id))
    conn.commit()

    cur.close()
    conn.close()

def delete_book_by_author():
    print("Įveskite autoriaus ID, kurio autorių norite ištrinti:")
    # try:
    #     author_id = int(input())
    # except ValueError:
    #     print("Blogas autoriaus ID formatas.")
    #     return

    conn = get_conn()
    cur = conn.cursor()

    try:
        # Patikrinam, ar autorius turi knygų
        cur.execute("SELECT COUNT(*) FROM books WHERE author_id = %s", (author_id,))
        book_count = cur.fetchone()[0]

        if book_count > 0:
            print(f"Autorius turi {book_count} knygų ir jo ištrinti negalima.")
            return

        # Jei knygų nėra, ištrinam autorių
        cur.execute("DELETE FROM authors WHERE id = %s", (author_id,))
        conn.commit()
        print(f"Autorius su ID={author_id} sėkmingai ištrintas.")

    except Exception as e:
        conn.rollback()
        print("Įvyko klaida trinant duomenis:", e)

    finally:
        cur.close()
        conn.close()
#

# def delete_book_by_author(books, authors):
#     print("Įveskite autoriaus ID, kurio knygą norite ištrinti:")
#     author_id = input()
#
#
# author = next((a for a in authors if a['id'] == author_id), None)
# if not author:
#     print("Toks autorius nerastas.")
#
# author_books = [b for b in books if b['author_id'] == author_id]
# if not author_books:
#     print("Šis autorius neturi knygų.")
#
# print(f"Autoriaus {author['name']} {author['surname']} knygos:")
# for b in author_books:
#     print(f"  {b['id']}: {b['title']} ({b['genre']})")
#
# print("Įveskite knygos ID, kurią norite pašalinti:")
# book_id = input()
#
# book_to_delete = next((b for b in books if b['id'] == book_id and b['author_id'] == author_id), None)
# if not book_to_delete:
#     print("Tokia knyga nerasta arba nepriklauso šiam autoriui.")
#
# books.remove(book_to_delete)
# save_books(books)
# print(f"Knyga „{book_to_delete['title']}“ pašalinta sėkmingai.")


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

def print_authors(authors):
    for aut in authors:
        print(f"{aut['i']}), Autoriaus vardas {aut['name']} pavardė {aut['surname']}")