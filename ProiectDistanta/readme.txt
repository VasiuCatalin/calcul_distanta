# Calculator de Trasee și Distanțe

Acest proiect este o aplicație GUI realizată cu Python și Tkinter, care permite utilizatorilor să calculeze distanța între două locații și să vizualizeze traseul pe o hartă interactivă generată cu Folium și Google Maps API.

## Caracteristici
- Introducerea a două locații pentru calculul distanței.
- Obținerea coordonatelor GPS ale locațiilor folosind Geopy.
- Calculul distanței dintre locații folosind geodesic.
- Generarea unei hărți interactive cu Folium.
- Afișarea traseelor alternative folosind Google Maps Directions API.
- Interfață prietenoasă cu Tkinter și un fundal personalizat.

## Cerințe
- Python 3.x
- Tkinter (integrat cu Python)
- Pachete suplimentare:
  - `requests`
  - `geopy`
  - `folium`
  - `Pillow`

Instalează aceste pachete cu comanda:
```sh
pip install requests geopy folium pillow
```

## Configurare
1. Clonează sau descarcă acest proiect.
2. Înlocuiește `API_KEY` din fișierul principal cu cheia ta Google Maps API.
3. Asigură-te că ai un fișier imagine numit `harta_fundal.jpg` în același director sau modifică calea imaginii în cod.

## Utilizare
1. Rulează scriptul Python:
```sh
python nume_fisier.py
```
2. Introdu locațiile dorite în interfață.
3. Apasă butonul "Calculează Traseul și Distanța".
4. Harta interactivă se va deschide într-un browser.


## Licență
Acest proiect este distribuit sub licența MIT.

