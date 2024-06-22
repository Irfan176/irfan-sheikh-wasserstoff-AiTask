import faiss

def create_vector_database():
    index = faiss.IndexFlatL2(768)
    faiss.write_index(index, "vector_database.faiss")
    
if __name__ == "__main__":
    create_vector_database()
