import faiss
import numpy as np
import pandas as pd
import os

class VectorDatabase:
    VECTOR_SIZE = 200

    def __init__(self, dataset_path, index_path='vector_index'):
        self.dataset_path = dataset_path
        self.index_path = index_path
        self.medicine_data = pd.read_csv(self.dataset_path)
        self.index = None
        self._load_or_build_index()

    def _string_to_vector(self, text, vector_size=VECTOR_SIZE):
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

        self.save_index()
        self.save_dataset()

    def _load_or_build_index(self):
        if os.path.exists(self.index_path):
            self.index = faiss.read_index(self.index_path)
        else:
            self._build_index()

    def save_index(self):
        faiss.write_index(self.index, self.index_path)

    def save_dataset(self):
        self.medicine_data.to_csv(self.dataset_path, index=False)

    def search(self, query, top_k=1):
        query_vector = self._string_to_vector(query)
        distances, indices = self.index.search(np.array([query_vector]), top_k)
        results = self.medicine_data.iloc[indices[0]]
        return results
