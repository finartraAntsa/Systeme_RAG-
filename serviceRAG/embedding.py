from spliter import* ## j'importe toute les fonctiond de spliter 
from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import HuggingFaceEmbeddings

def embedding(dataSplited):
    # Créer des embeddings en local
    embeddings = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")

    # Créer un index FAISS pour la recherche
    vectorstore = FAISS.from_documents(dataSplited, embeddings)

    # Sauvegarder l'index pour l'utiliser plus tard
    vectorstore.save_local("faiss_index")
        
        
    return 