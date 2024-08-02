import faiss
import numpy as np
import pandas as pd

class VectorDatabase:
    def __init__(self, dataset_path):
        self.dataset_path = dataset_path
        self.medicine_data = pd.read_csv(self.dataset_path)
        self.index = None
        self._build_index()

    def _string_to_vector(self, text, vector_size=100):
        vector = np.zeros(vector_size, dtype=np.float32)
        for i, char in enumerate(text[:vector_size]):
            vector[i] = ord(char)
        return vector

    def _build_index(self):
        vectors = [self._string_to_vector(name) for name in self.medicine_data['name']]
        vectors = np.array(vectors)
        self.index = faiss.IndexFlatL2(vectors.shape[1])
        self.index.add(vectors)
        self.medicine_data['vector_id'] = np.arange(len(vectors))

    def search(self, query, top_k=1):
        query_vector = self._string_to_vector(query)
        distances, indices = self.index.search(np.array([query_vector]), top_k)
        results = self.medicine_data.iloc[indices[0]]
        return results

# Example usage
if __name__ == "__main__":
    dataset_path = 'data/processed/preprocessed_medicine_data.csv'
    vector_db = VectorDatabase(dataset_path)
    query = "Paracetamol"
    results = vector_db.search(query)
    print(results)
