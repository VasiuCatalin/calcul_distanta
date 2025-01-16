def filter_lines(input_file, output_file, keyword):
    try:
        with open(input_file, 'r', encoding='utf-8') as infile:
            with open(output_file, 'w', encoding='utf-8') as outfile:
                for line in infile:
                    if keyword in line:
                        outfile.write(line)
        print(f"Liniile ce conțin '{keyword}' au fost scrise în fișierul: {output_file}")
    except FileNotFoundError:
        print(f"Eroare: Fișierul '{input_file}' nu a fost găsit.")
    except Exception as e:
        print(f"A apărut o eroare: {e}")
