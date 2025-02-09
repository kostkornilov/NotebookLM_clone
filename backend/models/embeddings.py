import faiss
import numpy as np
from langchain_huggingface.embeddings import HuggingFaceEmbeddings

class VectorStore:
    def __init__(self, model_name='sentence-transformers/all-MiniLM-L6-v2'):
        self.embeddings = HuggingFaceEmbeddings(model_name=model_name)
        self.index = None
        self.text_data = []  # Stores text chunks

    def add_texts(self, texts):
        """Convert texts to vectors and store them."""
        vectors = np.array(self.embeddings.embed_documents(texts)).astype("float32")
        self.text_data.extend(texts)
        
        if self.index is None:
            self.index = faiss.IndexFlatL2(vectors.shape[1])
        
        self.index.add(vectors)

    def search(self, query, top_k=3):
        """Retrieve the most relevant text chunks for a given query."""
        query_vector = np.array([self.embeddings.embed_query(query)]).astype("float32")
        distances, indices = self.index.search(query_vector, top_k)

        results = [self.text_data[i] for i in indices[0] if i < len(self.text_data)]
        return results

vector_store = VectorStore()
