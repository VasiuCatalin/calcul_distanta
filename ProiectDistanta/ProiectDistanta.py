import tkinter as tk
from tkinter import messagebox
from geopy.geocoders import Nominatim
from geopy.distance import geodesic
import requests
import folium
import webbrowser
from PIL import Image, ImageTk  # Pentru a lucra cu imagini

# Înlocuiește cu cheia ta API Google
API_KEY = "AIzaSyDwhgVB4vALoQNSINXL0BwoZSsJXDkBbjY"

# Listă de culori pentru trasee
route_colors = ["blue", "red", "green", "purple", "orange", "brown", "pink"]

def calculate_route():
    loc1 = entry_location1.get().strip()
    loc2 = entry_location2.get().strip()

    if not loc1 or not loc2:
        messagebox.showerror("Eroare", "Introduceți ambele locații!")
        return

    geolocator = Nominatim(user_agent="route_calculator")
    try:
        # Geocodare locații
        location1 = geolocator.geocode(loc1)
        location2 = geolocator.geocode(loc2)

        if not location1 or not location2:
            messagebox.showerror("Eroare", "Nu s-au găsit locațiile specificate!")
            return

        coords1 = (location1.latitude, location1.longitude)
        coords2 = (location2.latitude, location2.longitude)

        # Calcul distanță între puncte
        distance_km = geodesic(coords1, coords2).kilometers

        # Cerere către API Directions cu multiple alternative
        url = f"https://maps.googleapis.com/maps/api/directions/json?origin={location1.latitude},{location1.longitude}&destination={location2.latitude},{location2.longitude}&key={API_KEY}&mode=driving&alternatives=true"
        response = requests.get(url)
        data = response.json()

        # Debug: Verificare răspuns API
        print("Răspuns API:", data)

        if data['status'] != 'OK':
            messagebox.showerror("Eroare", f"Eroare la obținerea traseului: {data.get('status')}")
            return

        # Creare hartă
        map_ = folium.Map(location=[location1.latitude, location1.longitude], zoom_start=12)
        folium.Marker((location1.latitude, location1.longitude), popup=f"Start: {location1.address}").add_to(map_)
        folium.Marker((location2.latitude, location2.longitude), popup=f"Destinație: {location2.address}").add_to(map_)

        # Extragem toate traseele disponibile și le colorăm diferit
        for index, route in enumerate(data['routes']):
            route_points = [(step['start_location']['lat'], step['start_location']['lng'])
                            for step in route['legs'][0]['steps']]
            route_points.append((location2.latitude, location2.longitude))

            # Selectează culoarea corespunzătoare traseului
            color = route_colors[index % len(route_colors)]

            # Adaugă traseul pe hartă
            folium.PolyLine(route_points, color=color, weight=3, opacity=0.8, tooltip=f"Traseu {index+1}").add_to(map_)

        label_result.config(text=f"Distanța: {distance_km:.2f} km între {location1.address} și {location2.address}")

        map_file = "trasee_detaliate.html"
        map_.save(map_file)

        # Deschide harta în browserul intern al aplicației
        webbrowser.open(map_file)

    except requests.RequestException as e:
        messagebox.showerror("Eroare", f"Eroare de rețea: {str(e)}")
    except KeyError as e:
        messagebox.showerror("Eroare", f"Eroare în răspunsul API: {str(e)}")
    except Exception as e:
        messagebox.showerror("Eroare", f"A apărut o eroare: {str(e)}")

# Crearea interfeței grafice
root = tk.Tk()
root.title("Calculator de Trasee și Distanțe")

# Setarea imaginii de fundal
background_image = Image.open("harta_fundal.jpg")  # Înlocuiește cu calea imaginii tale
background_image = background_image.resize((800, 577), Image.Resampling.LANCZOS)  # Redimensionare imagine
bg_image = ImageTk.PhotoImage(background_image)

# Crearea unui label pentru fundal
bg_label = tk.Label(root, image=bg_image)
bg_label.place(relwidth=1, relheight=1)

# Crearea unui frame transparent pentru interfața de utilizator
frame = tk.Frame(root, padx=10, pady=10, bg='white', bd=5)
frame.place(relx=0.5, rely=0.5, anchor='center')

# Adăugarea câmpurilor de introducere și butoanelor
label_location1 = tk.Label(frame, text="Locația 1:", bg='white')
label_location1.grid(row=0, column=0, sticky="w")
entry_location1 = tk.Entry(frame, width=40)
entry_location1.grid(row=0, column=1)

label_location2 = tk.Label(frame, text="Locația 2:", bg='white')
label_location2.grid(row=1, column=0, sticky="w")
entry_location2 = tk.Entry(frame, width=40)
entry_location2.grid(row=1, column=1)

button_calculate = tk.Button(frame, text="Calculează Traseul și Distanța", command=calculate_route, bg='#4CAF50', fg='white', font=('Helvetica', 12, 'bold'))
button_calculate.grid(row=2, columnspan=2, pady=10)

label_result = tk.Label(frame, text="Distanța va fi afișată aici.", bg='white', font=('Helvetica', 10))
label_result.grid(row=3, columnspan=2)

root.mainloop()
