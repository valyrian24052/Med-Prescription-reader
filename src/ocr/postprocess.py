from src.database.vector_db import VectorDatabase

class TextPostprocessor:
    def __init__(self, text, dataset_path):
        self.text = text
        self.dataset_path = dataset_path
        self.vector_db = VectorDatabase(dataset_path)
        self.medicine_name = None
        self.salt = None

    def _search_database(self, query):
        results = self.vector_db.search(query, top_k=1)
        if not results.empty:
            self.medicine_name = results['name'].values[0]
            self.salt = results['salt'].values[0]
        else:
            self.medicine_name = "Medicine name not found"
            self.salt = "Salt not found"

    def extract_medicine_info(self):
        words = self.text.split()
        for word in words:
            self._search_database(word)
            if self.medicine_name != "Medicine name not found":
                break

    def run(self):
        self.extract_medicine_info()
        return self.medicine_name, self.salt
