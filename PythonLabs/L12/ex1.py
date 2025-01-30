import requests
from tabulate import tabulate

# URL-ul API-ului
URL = "https://jsonplaceholder.typicode.com/users"


def get_users():
    try:
        response = requests.get(URL)
        response.raise_for_status()  # Verifică dacă răspunsul conține erori HTTP
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Eroare la interogarea API-ului: {e}")
        return []


def filter_users_by_city(users, city):
    return [user for user in users if user["address"]["city"].lower() == city.lower()]


def display_users(users):
    if not users:
        print("Nu există utilizatori de afișat.")
        return

    table = [
        [
            user["id"], user["name"], user["username"], user["email"],
            user["address"]["city"], user["company"]["name"],
            user["phone"], user["website"]
        ]
        for user in users
    ]

    headers = ["ID", "Nume", "Username", "Email", "Oraș", "Companie", "Telefon", "Website"]
    print(tabulate(table, headers=headers, tablefmt="grid"))


def main():
    users = get_users()

    if not users:
        return

    print("\nToți utilizatorii:")
    display_users(users)

    city = "Gwenborough"  # Orașul după care filtrăm
    filtered_users = filter_users_by_city(users, city)

    print(f"\nUtilizatorii din orașul {city}:")
    display_users(filtered_users)


if __name__ == "__main__":
    main()
