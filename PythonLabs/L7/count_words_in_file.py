def count_words_in_file():
    file_path = r'C:\Users\Admin\PycharmProjects\PythonProject\PythonLabs\L7'
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            text = file.read()
            words = text.split()
            return len(words)
    except FileNotFoundError:
        print(f"Eroare: Fișierul '{file_path}' nu a fost găsit.")
    except Exception as e:
        print(f"A apărut o eroare: {e}")
    return None

# Apelăm funcția
numar_cuvinte = count_words_in_file()
if numar_cuvinte is not None:
    print(f"Numărul total de cuvinte în fișier: {numar_cuvinte}")
