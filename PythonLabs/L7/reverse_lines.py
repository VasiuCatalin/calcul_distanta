def reverse_lines(input_file, output_file):
    try:
        with open(input_file, 'r', encoding='utf-8') as infile:
            with open(output_file, 'w', encoding='utf-8') as outfile:
                for line in infile:
                    # Eliminăm spațiile goale și inversăm linia
                    reversed_line = line.rstrip()[::-1]
                    outfile.write(reversed_line + '\n')
        print(f"Fișierul inversat a fost creat: {output_file}")
    except FileNotFoundError:
        print(f"Eroare: Fișierul '{input_file}' nu a fost găsit.")
    except Exception as e:
        print(f"A apărut o eroare: {e}")
