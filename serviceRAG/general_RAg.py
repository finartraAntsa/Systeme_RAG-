import spliter
import embedding


fichiers = ["rag.txt" ,"rag2.csv","livre.pdf"]

def assembleur ():
    docs= spliter.charger(fichiers) # attente de fichier chargement 
    chunks= spliter.spliter(docs)
    vectorisation = embedding.embedding(chunks)
    
    return ## la valeur de retour est encore à voir


assembleur()