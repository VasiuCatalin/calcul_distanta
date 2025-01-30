import requests
import urllib3

# Dezactivează avertismentele SSL
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


def get_weather(city):
    url = f"https://wttr.in/{city}?format=j1"  # API JSON

    try:
        response = requests.get(url, timeout=5, verify=False)  # Dezactivează verificarea SSL

        # Verificăm dacă răspunsul nu este gol
        if response.status_code == 200 and response.text.strip():
            try:
                data = response.json()  # Încercăm să convertim răspunsul în JSON

                if "current_condition" in data and data["current_condition"]:
                    weather = data["current_condition"][0]

                    conditions = weather["weatherDesc"][0]["value"]  # Condiții meteo
                    temperature = weather["temp_C"] + "°C"  # Temperatură în Celsius
                    wind_speed = weather["windspeedKmph"] + " km/h"  # Viteza vântului
                    wind_dir = weather["winddir16Point"]  # Direcția vântului

                    print(f"\nVremea pentru {city.capitalize()}:")
                    print(f"- Condiții meteo: {conditions}")
                    print(f"- Temperatură: {temperature}")
                    print(f"- Vânt: {wind_dir} {wind_speed}")
                else:
                    print("Nu s-au găsit date meteo pentru acest oraș.")

            except ValueError:
                print("Eroare: API-ul a returnat un răspuns invalid.")
        else:
            print("Eroare: Nu s-au putut obține date meteo.")

    except requests.exceptions.RequestException as e:
        print(f"Eroare la conectarea la API: {e}")


if __name__ == "__main__":
    city = input("Introduceți numele orașului: ").strip()
    if city:
        get_weather(city)
    else:
        print("Numele orașului nu poate fi gol.")
