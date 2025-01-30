import csv

# Numele fișierelor CSV
input_file = "comenzi.csv"
output_file = "rezultate.csv"

# Citirea și procesarea fișierului CSV
with open(input_file, mode="r", encoding="utf-8") as infile:
    reader = csv.DictReader(infile)
    fieldnames = reader.fieldnames + ["Total"]  # Adăugăm o coloană pentru total
    rows = []

    for row in reader:
        cantitate = int(row["Cantitate"])
        pret_unitar = float(row["Pret unitar"])
        total = cantitate * pret_unitar  # Calculăm valoarea totală
        row["Total"] = round(total, 2)  # Rotunjim la 2 zecimale
        rows.append(row)

# Salvarea rezultatelor într-un nou fișier CSV
with open(output_file, mode="w", encoding="utf-8", newline="") as outfile:
    writer = csv.DictWriter(outfile, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(rows)

print(f"Fișierul '{output_file}' a fost generat cu succes!")
