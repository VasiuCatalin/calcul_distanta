import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Generare date
np.random.seed(42)  # Pentru reproducibilitate
days = pd.date_range(start="2024-01-01", periods=365, freq='D')
temperatura = np.random.uniform(5, 35, 365)
umiditate = np.random.uniform(30, 90, 365)
viteza_vantului = np.random.uniform(0, 20, 365)

# Creare DataFrame
df = pd.DataFrame({
    "Data": days,
    "Temperatura": temperatura,
    "Umiditate": umiditate,
    "Viteza Vantului": viteza_vantului
})

# Calcul temperatura resimțită
df["Temperatura Resimtita"] = df["Temperatura"] - 0.7 * (df["Umiditate"] / 100)

# Găsire zile cu temperaturile extreme
zi_min = df.loc[df["Temperatura Resimtita"].idxmin()]
zi_max = df.loc[df["Temperatura Resimtita"].idxmax()]
print(f"Ziua cu cea mai mică temperatură resimțită: {zi_min['Data']} ({zi_min['Temperatura Resimtita']:.2f}°C)")
print(f"Ziua cu cea mai mare temperatură resimțită: {zi_max['Data']} ({zi_max['Temperatura Resimtita']:.2f}°C)")

# Vizualizare temperatură pe parcursul anului
plt.figure(figsize=(12, 5))
plt.plot(df["Data"], df["Temperatura"], label="Temperatura", color='blue')
plt.plot(df["Data"], df["Temperatura Resimtita"], label="Temperatura Resimtita", color='red', linestyle='dashed')
plt.xlabel("Data")
plt.ylabel("Temperatura (°C)")
plt.title("Evoluția temperaturii pe parcursul anului")
plt.legend()
plt.grid()
plt.show()

# Calcul temperatura medie lunară
df["Luna"] = df["Data"].dt.month
medii_lunare = df.groupby("Luna")["Temperatura"].mean()

# Grafic temperatură medie lunară
plt.figure(figsize=(10, 5))
medii_lunare.plot(kind='bar', color='orange')
plt.xlabel("Luna")
plt.ylabel("Temperatura medie (°C)")
plt.title("Temperatura medie lunară")
plt.xticks(ticks=range(12), labels=["Ian", "Feb", "Mar", "Apr", "Mai", "Iun", "Iul", "Aug", "Sep", "Oct", "Noi", "Dec"], rotation=45)
plt.grid(axis='y')
plt.show()
