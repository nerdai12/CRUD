import csv

headers = ['id', 'name', 'surname']

def load_authors():
    with open('english_authors_list.csv', mode='r', encoding='utf-8') as file:
        return list(csv.DictReader(file))

def save_authors(authors):
    with open('english_authors_list.csv', mode='w', newline='', encoding='utf-8') as file:
        writer = csv.DictWriter(file, fieldnames=headers)
        writer.writeheader()
        writer.writerows(authors)

def create_authors(authors):
    print("naujo autoriaus įtraukimas:")
    print("Įveskite vardą")
    name = input()
    print("Įveskite pavardę")
    surname = input()
    new_id = str(int(authors[-1]['id']) + 1) if len(authors) > 0 else 1
    authors.append({
                'id': new_id,
                "name": name,
                "surname": surname
            })
    save_authors(authors)

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
    save_authors(authors)

def delete_authors(authors):
    print("Autorių šalinimas. Pasirinkite autoriaus ID, kurį norite pašalinti")
    id = input()
    for aut in authors:
        if id == str(aut['id']):
            print(f"{aut['id']}. Šalinama Autoriaus vardas {aut['name']} pavardė {aut['surname']}")
            del authors[authors.index(aut)]
    save_authors(authors)


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