import re


def verifica_complexitate_parola(parola):
    criterii_neindeplinite = []

    # Lungimea parolei
    if len(parola) < 8:
        criterii_neindeplinite.append("Lungimea trebuie să fie de cel puțin 8 caractere.")

    # Litere majuscule
    if not any(c.isupper() for c in parola):
        criterii_neindeplinite.append("Trebuie să conțină cel puțin o literă majusculă.")

    # Litere minuscule
    if not any(c.islower() for c in parola):
        criterii_neindeplinite.append("Trebuie să conțină cel puțin o literă minusculă.")

    # Cifre
    if not any(c.isdigit() for c in parola):
        criterii_neindeplinite.append("Trebuie să conțină cel puțin o cifră.")

    # Caractere speciale
    if not any(c in "!@#$%^&*()-_+=<>?" for c in parola):
        criterii_neindeplinite.append("Trebuie să conțină cel puțin un caracter special (!@#$%^&*()-_+=<>?).")

    # Spații
    if " " in parola:
        criterii_neindeplinite.append("Nu trebuie să conțină spații.")

    if not criterii_neindeplinite:
        return "Parola dvs. este puternică."
    else:
        return f"Parola dvs. este slabă.\nLipsesc: {'; '.join(criterii_neindeplinite)}"


def verifica_parole_multiple(parole):
    parole = [parola.strip() for parola in parole.split(",")]
    rezultate = []
    for parola in parole:
        rezultat = verifica_complexitate_parola(parola)
        rezultate.append(f"Parola: '{parola}'\n{rezultat}\n")
    return "\n".join(rezultate)


# Program principal
def main():
    parole_input = input("Introduceți una sau mai multe parole separate prin virgulă: ")
    rezultate = verifica_parole_multiple(parole_input)
    print("\nRezultate:\n")
    print(rezultate)


if __name__ == "__main__":
    main()
