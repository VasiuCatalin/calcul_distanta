def remove_vowels(input_string):
    vowels="aeiouyAEIOUY"
    result=''.join(char for char in input_string if char not in vowels)
    return result
text=input("Introdu un text")
text_fara_vocale=remove_vowels(text)
print("Textul fara vocale este: ", text_fara_vocale)
