import csv

# Functie pentru citirea unui fisier CSV
def read_csv(file_path):
    """
    Citeste un fisier CSV si returneaza continutul ca o lista de dictionare.
    """
    data = []
    try:
        with open(file_path, mode='r', newline='', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            data = [row for row in reader]
    except FileNotFoundError:
        print(f"Eroare: Fisierul '{file_path}' nu a fost gasit.")
    return data

# Functie pentru filtrarea datelor dupa o pereche cheie-valoare
def filter_data(data, key, value):
    """
    Filtreaza lista de dictionare pe baza unei perechi cheie-valoare.
    """
    return [row for row in data if row.get(key) == value]

# Functie pentru scrierea datelor filtrate intr-un fisier CSV
def write_csv(data, file_path):
    """
    Scrie datele filtrate intr-un nou fisier CSV.
    """
    if not data:
        print("Nu exista date de scris.")
        return

    try:
        with open(file_path, mode='w', newline='', encoding='utf-8') as file:
            writer = csv.DictWriter(file, fieldnames=data[0].keys())
            writer.writeheader()
            writer.writerows(data)
        print(f"Datele au fost scrise in fisierul '{file_path}'.")
    except Exception as e:
        print(f"Eroare la scrierea fisierului: {e}")

# Functie pentru a adauga date introduse de utilizator intr-un fisier CSV
def add_user_data(file_path):
    """
    Permite utilizatorului sa introduca date noi si sa le salveze in fisierul CSV.
    """
    fieldnames = ['Name', 'Age', 'City']
    print("Introduceti datele persoanelor. Tastati 'stop' pentru a incheia.")

    with open(file_path, mode='a', newline='', encoding='utf-8') as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)

        while True:
            name = input("Nume: ")
            if name.lower() == 'stop':
                break
            age = input("Varsta: ")
            city = input("Oras: ")
            writer.writerow({'Name': name, 'Age': age, 'City': city})

    print(f"Datele au fost adaugate in fisierul '{file_path}'.")

# Functie pentru filtrare pe baza criteriilor introduse de utilizator
def filter_by_user_choice(data):
    """
    Permite utilizatorului sa aleaga un camp si o valoare pentru filtrare.
    """
    if not data:
        print("Nu exista date disponibile pentru filtrare.")
        return []

    print("Campuri disponibile pentru filtrare:")
    for key in data[0].keys():
        print(f"- {key}")

    key = input("Introduceti campul pe care doriti sa filtrati: ")
    value = input(f"Introduceti valoarea pentru campul '{key}': ")

    return filter_data(data, key, value)

# Demonstratie pentru utilizarea modulului
if __name__ == "__main__":
    # Creare fisier CSV initial pentru demonstratie
    with open('people.csv', mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(['Name', 'Age', 'City'])
        writer.writerows([
            ['John', '30', 'New York'],
            ['Alice', '25', 'Los Angeles'],
            ['Bob', '35', 'Chicago']
        ])

    print("Fisierul 'people.csv' a fost creat pentru demonstratie.")

    # Adauga date introduse de utilizator
    add_user_data('people.csv')

    # Citește datele din fișierul CSV
    data = read_csv('people.csv')

    # Filtreaza datele pe baza alegerii utilizatorului
    filtered_data = filter_by_user_choice(data)

    # Scrie datele filtrate într-un nou fișier CSV
    write_csv(filtered_data, 'filtered_people.csv')

    # Afișează datele filtrate
    print("Datele filtrate sunt:")
    for row in filtered_data:
        print(row)

