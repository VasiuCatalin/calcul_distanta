def inverted_index(documents):
    index={}

#parcurgem fiecare document si cuvantul din document
    for doc_id, document in enumerate(documents):
        words=document.split() #impart documentul in cuvinte
        for word in words:
            word=word.lower() #converim cuvantul la litera mica
            if word not in index:
                word