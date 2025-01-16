def rle_encode(string):
    encoded = ""
    count = 1

    for i in range(1, len(string)):
        if string[i] == string[i - 1]:
            count += 1
        else:
            encoded += string[i - 1] + str(count)
            count = 1

    # Adăugăm ultimul caracter și numărul său de apariții
    if string:
        encoded += string[-1] + str(count)

    return encoded

# Introducerea unui șir de caractere de la tastatură
string = input("Introduceți un șir de caractere: ")

# Aplicăm RLE
encoded_string = rle_encode(string)
print("Șirul codificat (RLE):", encoded_string)
