import requests

API_URL = "https://api.exchangerate-api.com/v4/latest/"

def get_exchange_rates(base_currency):
    response = requests.get(API_URL + base_currency)
    if response.status_code == 200:
        return response.json()["rates"]
    else:
        print("Eroare la preluarea datelor de schimb valutar.")
        return None

def convert_currency(amount, from_currency, to_currency, rates):
    if from_currency in rates and to_currency in rates:
        exchange_rate = rates[to_currency]
        converted_amount = amount * exchange_rate
        return converted_amount, exchange_rate
    else:
        print("Monedă invalidă. Verificați codurile monedelor.")
        return None, None

def main():
    from_currency = input("Introduceți moneda de proveniență (ex: USD, EUR, RON): ").upper()
    to_currency = input("Introduceți moneda de destinație: ").upper()
    try:
        amount = float(input("Introduceți suma de convertit: "))
    except ValueError:
        print("Suma introdusă nu este validă.")
        return

    rates = get_exchange_rates(from_currency)
    if rates:
        converted_amount, exchange_rate = convert_currency(amount, from_currency, to_currency, rates)
        if converted_amount:
            print(f"\n{amount} {from_currency} = {converted_amount:.2f} {to_currency}")
            print(f"Curs de schimb: 1 {from_currency} = {exchange_rate:.4f} {to_currency}")

if __name__ == "__main__":
    main()
