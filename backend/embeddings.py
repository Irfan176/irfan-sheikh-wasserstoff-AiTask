import os
from sentence_transformers import SentenceTransformer
import faiss
import numpy as np

model = SentenceTransformer('paraphrase-MiniLM-L6-v2')
index = faiss.read_index("vector_database.faiss")

def extract_text(post):
    return post['content']

def generate_embeddings(text):
    return model.encode([text])

def update_vector_database(post_id, embeddings):
    ids = np.array([post_id], dtype=np.int64)
    index.add_with_ids(np.array(embeddings), ids)
    faiss.write_index(index, "vector_database.faiss")

def update_embeddings_on_new_post(post):
    text = extract_text(post)
    embeddings = generate_embeddings(text)
    update_vector_database(post['id'], embeddings)
