import mysql.connector

DB_CONFIG = {
    'host':'localhost', #127.0.0.1 alternatyva rasymui "localhost" ;)
    'port': 3306,
    'user':'',
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




def print_info():
    print("-------------------------------------------------------------------------------")
    print("1. Atvaizduoti autorių sąrašą")
    print("2. Įtraukti naują autorių")
    print("3. Koreguoti autorius")
    print("4. Šalinti autorius")
    print("5. Išeiti iš programos")
    print("------------------------------------Pasirinkite--------------------------------")

def print_authors(authors):
    for aut in authors:
        print(f"{aut['id']}), Autoriaus vardas {aut['name']} pavardė {aut['surname']}")