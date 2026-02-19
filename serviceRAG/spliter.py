#Nous utilisons cette route pour separer les document
#Type de document : PDF / DOCS / text 
from langchain_community.document_loaders import UnstructuredFileLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter

fichiers = ["rag.txt"]

def charger (fichiers):
    all_docs = []

    for fichier in fichiers:
        loader = UnstructuredFileLoader(fichier)
        docs = loader.load()  # liste de Document
        all_docs.extend(docs)

    print(all_docs)
    return all_docs

def spliter(document):
    text_spliter= RecursiveCharacterTextSplitter(
          chunk_size=500,    # chaque chunk fait 500 caractères
    chunk_overlap=50   # on recoupe 50 caractères pour ne rien perdre

    )
    docs = text_spliter.split_documents(document) #les texte sont spliter dans cette étape 
    return docs