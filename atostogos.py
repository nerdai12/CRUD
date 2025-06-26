
hollidays = [
    {
        'id': 1,
        "country":"Lithuania",
        "city":"Palanga",
        "price":20,
        "accomodation":"hotel"
    },
    {
        'id': 2,
        "country":"Turkija",
        "city":"Alanya",
        "price":60,
        "accomodation":"hostel"
    },
    {
        'id': 3,
        "country":"Cyprus",
        "city":"Larnaka",
        "price":70,
        "accomodation":"apartaments"
    }
]
id_counter = 3

while True:
    print("--------------------------------------------------------------------------")
    print("1. Atvaizduoti atostogu pasirinkimus")
    print("2. Įtraukti atostogas i sarasa")
    print("3. koreguoti atostogas")
    print("4. šalinti atostogas")
    print("5. išeiti iš programos")
    print("-----------------------------Pasirinkite:---------------------------------")
    choise = input()

    match choise:
        case '1':
            # print("--------------------------------------------------------------------------")
            for hol in hollidays:
                print(f"{hol['id']}. Atostogos {hol['country']} {hol['city']}. Kaina gyvenant {hol['accomodation']} "
                      f"parai {hol['price']}")
            print("--------------------------------------------------------------------------")

        case '2':
            print("atostogų pridėjimas:")
            print("Įveskite šalį")
            country = input()
            print("Įveskite miestą")
            city = input()
            print("Įveskite apgyvendinimo tipą")
            apt = input()
            print("Įveskite kainą")
            price = input()
            id_counter +=1
            hollidays.append(
                {
                    'id': id_counter,
                    "country":country,
                    "city":city,
                    "price":price,
                    "accomodation":apt
                }
            )
        case '3':
            print("atostogų redagavimas. Pasirinkite ID įrašo kurį norite redaguoti.")
            id = input()
            for hol in hollidays:
                if id == str(hol['id']):
                    print(f"{hol['id']}. Atostogos {hol['country']} {hol['city']}. Kaina gyvenant {hol['accomodation']} "
                          f"parai {hol['price']}")

                    print("Įveskite šalį")
                    hol['country'] = input()
                    print("Įveskite miestą")
                    hol['city'] = input()
                    print("Įveskite apgyvendinimo tipą")
                    hol['accomodation'] = input()
                    print("Įveskite kainą")
                    hol['price'] = input()
                    break
        case '4':
            print("atostogų šalinimas. Pasirinkite ID įrašo kurį norite redaguoti.")
            id = input()
            for hol in hollidays:
                if id == str(hol['id']):
                    print(
                        f"{hol['id']}. Šalinama: Atostogos {hol['country']} {hol['city']}. Kaina gyvenant"
                        f" {hol['accomodation']} "
                        f"parai {hol['price']}")
                    del hollidays[hollidays.index(hol)]
        case '5':
            print("programa sustabdyta")
            break




















