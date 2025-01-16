import string

def word_frequency(text):
    # Convertim textul la litere mici
    text = text.lower()

    # Îndepărtăm semnele de punctuație
    text = text.translate(str.maketrans('', '', string.punctuation))

    # Împărțim textul în cuvinte
    words = text.split()

    # Cream un dicționar pentru a număra frecvența fiecărui cuvânt
    freq_dict = {}
    for word in words:
        if word in freq_dict:
            freq_dict[word] += 1
        else:
            freq_dict[word] = 1

    return freq_dict

# Citirea textului de la tastatură
text_input = input("Introduceti un text: ")

# Apelarea funcției și afișarea rezultatului
result = word_frequency(text_input)
print("Frecventa cuvintelor:", result)
