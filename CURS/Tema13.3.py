import requests
from bs4 import BeautifulSoup
import schedule
import time


# Funcția care extrage și salvează titlurile
def scrape_news():
    url = "https://www.bbc.com/news"
    headers = {"User-Agent": "Mozilla/5.0"}

    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        soup = BeautifulSoup(response.text, "html.parser")
        headlines = soup.find_all("h3", class_="gs-c-promo-heading__title", limit=5)

        with open("titluri.txt", "w", encoding="utf-8") as file:
            for index, headline in enumerate(headlines, start=1):
                file.write(f"{index}. {headline.text.strip()}\n")

        print("Titlurile au fost salvate cu succes în titluri.txt.")
    else:
        print(f"Eroare la accesarea paginii: {response.status_code}")


# Programare să ruleze zilnic la ora 08:00
schedule.every().day.at("20:59").do(scrape_news)

print("Scriptul rulează...")

while True:
    schedule.run_pending()
    time.sleep(60)  # Așteaptă 1 minut înainte de următoarea verificare
