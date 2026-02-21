import spliter
import embedding
import noLLM


fichiers = ["livreML.pdf"]

def assembleur ():
    docs= spliter.charger(fichiers) # attente de fichier chargement 
    chunks= spliter.spliter(docs)
    vectore =embedding.embedding(chunks)
    print("Nombre de vecteurs FAISS :", vectore.index.ntotal)
    
    querry= "c'est quoi la regression lineaire "
    test = noLLM.noLLM(querry)
    
    return ## la valeur de retour est encore à voir

assembleur()
