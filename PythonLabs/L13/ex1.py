import os


def rename_files_in_folder(folder_path):
    if not os.path.isdir(folder_path):
        print(f"Eroare: {folder_path} nu este un director valid.")
        return

    for filename in os.listdir(folder_path):
        old_path = os.path.join(folder_path, filename)
        if os.path.isfile(old_path):  # Verifică dacă este un fișier
            new_filename = f"renamed_{filename}"
            new_path = os.path.join(folder_path, new_filename)
            os.rename(old_path, new_path)
            print(f"Redenumit: {filename} -> {new_filename}")


# Exemplu de utilizare
folder = input("Introduceti calea folderului: ")
rename_files_in_folder(folder)
