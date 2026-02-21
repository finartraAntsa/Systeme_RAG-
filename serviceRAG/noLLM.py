from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import HuggingFaceEmbeddings

def noLLM(query, index_path="faiss_index", k=3):
    """
    Recherche les k chunks les plus pertinents pour une query dans un index FAISS existant.
    
    query : texte à rechercher
    index_path : chemin du dossier de l'index FAISS
    k : nombre de résultats à retourner
    """
    
    # Recharger les embeddings
    embeddings = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")
    
    # Charger l'index FAISS existant
    vectorstore = FAISS.load_local(index_path, embeddings, allow_dangerous_deserialization=True)
    
    # Recherche par similarité
    docs = vectorstore.similarity_search(query, k=k)
    
    # Afficher les résultats
    print("===========================================RESULTATS=====================")
    for i, doc in enumerate(docs):
        print(f"\n--- Chunk {i+1} ---")
        print(doc.page_content[:150])  # afficher les 150 premiers caractères
    
    return docs



"""
def assembleur():
    # 1️⃣ Charger les documents
    docs = spliter.charger(fichiers)
    print(f"Documents chargés : {len(docs)}")
    
    # 2️⃣ Découper en chunks
    chunks = spliter.spliter(docs)
    print(f"Nombre de chunks créés : {len(chunks)}")
    
    # 3️⃣ Créer l'index FAISS
    vectorstore = embedding.embedding(chunks)
    
    # 4️⃣ Rechercher une query
    query = "c'est quoi la regression lineaire"
    result_docs = noLLM.noLLM(query)  # assure-toi que noLLM accepte query
    
    return result_docs
    
    """