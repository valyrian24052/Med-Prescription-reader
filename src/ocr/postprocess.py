import spacy
from src.database.vector_db import VectorDatabase

class TextPostprocessor:
    def __init__(self, text, dataset_path):
        self.text = text
        self.dataset_path = dataset_path
        self.vector_db = VectorDatabase(dataset_path)
        self.medicine_name = None
        self.salt = None
        self.nlp = spacy.load("en_core_web_sm")

    def _search_database(self, query):
        results = self.vector_db.search(query, top_k=1)
        if not results.empty:
            self.medicine_name = results['name'].values[0]
            self.salt = results['salt'].values[0]
        else:
            self.medicine_name = "Medicine name not found"
            self.salt = "Salt not found"

    def extract_medicine_info(self):
        doc = self.nlp(self.text)
        for ent in doc.ents:
            if ent.label_ == "PRODUCT": 
                self._search_database(ent.text)
                if self.medicine_name != "Medicine name not found":
                    break

    def run(self):
        self.extract_medicine_info()
        return self.medicine_name, self.salt

# Example usage
if __name__ == "__main__":
    sample_text = """
    Rx
    Paracetamol 500mg
    Take one tablet by mouth every 6 hours.
    """
    dataset_path = 'data/processed/preprocessed_medicine_data.csv'
    postprocessor = TextPostprocessor(sample_text, dataset_path)
    medicine_name, salt = postprocessor.run()
    print("Medicine Name:", medicine_name)
    print("Salt:", salt)
