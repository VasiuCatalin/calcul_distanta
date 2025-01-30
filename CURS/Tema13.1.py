import pandas as pd
import openpyxl

# Așteaptă ca utilizatorul să apese Enter
input("Apăsați Enter pentru a începe procesarea fișierului CSV...")

# Citirea fișierului CSV
csv_file = "contacte.csv"  # Înlocuiește cu calea către fișierul tău CSV
data = pd.read_csv(csv_file)

# Verifică dacă fișierul CSV are cel puțin trei coloane (Nume, Email, Telefon)
if set(["Nume", "Email", "Telefon"]).issubset(data.columns):
    # Salvează fișierul în format Excel
    excel_file = "contacte.xlsx"
    data.to_excel(excel_file, index=False, engine="openpyxl")
    print(f"Fișierul Excel a fost salvat cu succes ca {excel_file}")
else:
    print("Fișierul CSV nu conține toate coloanele necesare (Nume, Email, Telefon).")
