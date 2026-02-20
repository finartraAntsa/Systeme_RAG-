#Nous utilisons cette route pour separer les document
#Type de document : PDF / DOCS / text 
from langchain_community.document_loaders import UnstructuredFileLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_core.documents import Document
import warnings
import logging

warnings.filterwarnings("ignore")
logging.getLogger("unstructured").setLevel(logging.ERROR)


#1)fonction qui charge les fichier quelque soit le type 
def charger (fichiers):
    all_docs = []

    for fichier in fichiers:
        loader = UnstructuredFileLoader(fichier)
        docs = loader.load()  # liste de Document
        all_docs.extend(docs)
        print(all_docs)
    return all_docs


#2) separation des text et formation d'un tableau de chunk 
def spliter(document):
    text_spliter= RecursiveCharacterTextSplitter(
    chunk_size=500,    # chaque chunk fait 500 caractères
    chunk_overlap=50   # on recoupe 50 caractères pour ne rien perdre
    )
    #les texte sont spliter dans cette étape 
    all_chunks = []
    for documen in document:
        chunks_text = text_spliter.split_text(documen.page_content)
        for chunk in chunks_text:
            all_chunks.append(
                Document(page_content=chunk, metadata=documen.metadata)
            )
    return all_chunks
            
            
warnings.filterwarnings("ignore")
logging.getLogger("unstructured").setLevel(logging.ERROR)