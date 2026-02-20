"""
    ##recharger 
        vectorstore = FAISS.load_local(
    "vector_db",
    embeddings,
    allow_dangerous_deserialization=True
    )

==================================================================================
    ##ajout plutard 

        loader = TextLoader("nouveau_doc.txt", encoding="utf-8")
        new_docs = loader.load()

        new_chunks = splitter.split_documents(new_docs)

===================================================================================
## ressauvegarde local 

            vectorstore.add_documents(new_chunks)

            # Sauvegarder à nouveau
            vectorstore.save_local("vector_db")
            
====================================================================================           
## note

    FAISS n écrase rien

    Il ajoute des vecteurs

    Tu contrôles quand tu sauvegardes

"""

