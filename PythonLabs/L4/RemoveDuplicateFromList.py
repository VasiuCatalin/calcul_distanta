user_input=input("Introdu elementele listei, separate prin spatiu: ")

#transformam datele introduse intr-o lista si eleiminam duplicatele cu set
imput_list=user_input.split()
unique_list=list(set(imput_list))

print("Lista fara duplicate:", unique_list)