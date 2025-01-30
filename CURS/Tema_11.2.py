#simulare piata actiuni

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Setare seed pentru reproducibilitate
np.random.seed(42)

# Generarea datelor
num_days = 730
initial_price = 100

daily_changes = np.random.normal(loc=0, scale=0.02, size=num_days)
prices = initial_price * np.cumprod(1 + daily_changes)

dates = pd.date_range(start="2022-01-01", periods=num_days)
data = pd.DataFrame({
    "Data": dates,
    "Schimbare Zilnică (%)": daily_changes * 100,
    "Preț de Închidere": prices
})

# Calcularea mediei mobile
data["Media Mobilă 30 zile"] = data["Preț de Închidere"].rolling(window=30).mean()
data["Media Mobilă 100 zile"] = data["Preț de Închidere"].rolling(window=100).mean()

# Identificarea perioadelor când prețul este peste media mobilă de 100 de zile
data["Peste Media 100 zile"] = data["Preț de Închidere"] > data["Media Mobilă 100 zile"]

# Vizualizare
plt.figure(figsize=(12, 6))
plt.plot(data["Data"], data["Preț de Închidere"], label="Preț de Închidere", color='blue')
plt.plot(data["Data"], data["Media Mobilă 30 zile"], label="Media Mobilă 30 zile", color='orange')
plt.plot(data["Data"], data["Media Mobilă 100 zile"], label="Media Mobilă 100 zile", color='green')

# Evidențierea zonelor unde prețul este peste media mobilă de 100 zile
plt.fill_between(data["Data"], data["Preț de Închidere"], data["Media Mobilă 100 zile"],
                 where=data["Peste Media 100 zile"], color='lightgreen', alpha=0.5)

plt.xlabel("Data")
plt.ylabel("Preț ($)")
plt.title("Evoluția Prețului Acțiunilor și Mediile Mobile")
plt.legend()
plt.show()
