class BankAccount:
    def __init__(self, initial_balance=0):
        self._balance = initial_balance

    def deposit(self, amount):
        if amount > 0:
            self._balance += amount
            print(f"{amount} RON au fost depuși în cont.")
        else:
            print("Suma de depunere trebuie să fie mai mare decât zero.")

    def withdraw(self, amount):
        if 0 < amount <= self._balance:
            self._balance -= amount
            print(f"{amount} RON au fost retrași din cont.")
        else:
            print("Fonduri insuficiente sau sumă invalidă.")

    def get_balance(self):
        return self._balance


# Exemplu de utilizare
def main():
    initial_balance = float(input("Introduceți soldul inițial: "))
    cont = BankAccount(initial_balance)

    while True:
        print("\n1. Depunere\n2. Retragere\n3. Verificare Sold\n4. Ieșire")
        optiune = input("Alegeți o opțiune: ")

        if optiune == "1":
            amount = float(input("Introduceți suma de depus: "))
            cont.deposit(amount)
        elif optiune == "2":
            amount = float(input("Introduceți suma de retras: "))
            cont.withdraw(amount)
        elif optiune == "3":
            print(f"Sold curent: {cont.get_balance()} RON")
        elif optiune == "4":
            print("Ieșire din aplicație.")
            break
        else:
            print("Opțiune invalidă. Încercați din nou.")


if __name__ == "__main__":
    main()
