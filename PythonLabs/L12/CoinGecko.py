import requests
from bs4 import BeautifulSoup
from tabulate import tabulate


# Funcție pentru obținerea prețurilor Bitcoin și Ethereum
def get_crypto_prices():
    url = "https://api.coingecko.com/api/v3/simple/price?ids=bitcoin,ethereum&vs_currencies=usd"
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        data = response.json()
        return [
            ["Bitcoin", data["bitcoin"]["usd"]],
            ["Ethereum", data["ethereum"]["usd"]]
        ]
    except requests.exceptions.RequestException as e:
        print(f"Eroare la obținerea prețurilor criptomonedelor: {e}")
        return []


# Funcție pentru extragerea celor mai recente 5 știri de pe CoinDesk
def get_crypto_news():
    url = "https://www.coindesk.com/"
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, "html.parser")

        articles = soup.find_all("a", class_="card-title", limit=5)  # Selectează primele 5 titluri de știri
        news = [[article.text.strip(), "https://www.coindesk.com" + article["href"]] for article in articles]
        return news
    except requests.exceptions.RequestException as e:
        print(f"Eroare la obținerea știrilor: {e}")
        return []


# Afișare prețuri criptomonede
prices = get_crypto_prices()
if prices:
    print("\n📊 Prețurile criptomonedelor:")
    print(tabulate(prices, headers=["Criptomonedă", "Preț (USD)"], tablefmt="grid"))

# Afișare cele mai recente 5 știri
news = get_crypto_news()
if news:
    print("\n📰 Cele mai recente 5 știri despre criptomonede:")
    print(tabulate(news, headers=["Titlu", "Link"], tablefmt="grid"))
