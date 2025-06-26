

authors = [
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
id_counter = 3

while True:
    print("-------------------------------------------------------------------------------")
    print("1. Atvaizduoti autorių sąrašą")
    print("2. Įtraukti naują autorių")
    print("3. Koreguoti autorius")
    print("4. Šalinti autorius")
    print("5. Išeiti iš programos")
    print("------------------------------------Pasirinkite--------------------------------")
    choice = input()

    match choice:
        case '1':
            for aut in authors:
                print(f"{aut['id']}), Autoriaus vardas {aut['name']} pavardė {aut['surname']}")
        case '2':
            print("naujo autoriaus įtraukimas:")
            print("Įveskite vardą")
            name = input()
            print("Įveskite pavardę")
            surname = input()
            id_counter += 1
            authors.append({'id': id_counter, "name": name, "surname": surname})
        case '3':
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
        case '4':
            print("Autorių šalinimas. Pasirinkite autoriaus ID, kurį norite pašalinti")
            id = input()
            for aut in authors:
                if id == str(aut['id']):
                    print(f"{aut['id']}. Šalinama Autoriaus vardas {aut['name']} pavardė {aut['surname']}")
                    del authors[authors.index(aut)]
        case '5':
            print("Programa sustabdyta")
            break

