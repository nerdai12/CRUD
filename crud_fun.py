def print_info():
    print("-------------------------------------------------------------------------------")
    print("1. Atvaizduoti autorių sąrašą")
    print("2. Įtraukti naują autorių")
    print("3. Koreguoti autorius")
    print("4. Šalinti autorius")
    print("5. Išeiti iš programos")
    print("------------------------------------Pasirinkite--------------------------------")

def load_default_data():
    return [
    {
        'id': 1,
        "name": "Jonas ",
        "surname": "Biliūnas"
    },
    {
        'id': 2,
        "name": "Tomas ",
        "surname": "Dirgėla"
    },
    {
        'id': 3,
        "name": "Janina ",
        "surname": "Degutytė"
    }
]

def print_authors(authors):
    for aut in authors:
        print(f"{aut['id']}), Autoriaus vardas {aut['name']} pavardė {aut['surname']}")

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

def load_default_data_books():
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

print(load_default_data_books())

