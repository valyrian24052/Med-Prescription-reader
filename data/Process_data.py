import pandas as pd
import os

class MedicineDataPreprocessor:
    def __init__(self, raw_data_path, processed_data_path):
        self.raw_data_path = raw_data_path
        self.processed_data_path = processed_data_path

    def load_data(self):
        return pd.read_csv(self.raw_data_path)

    def preprocess_data(self, df):
        df = df[['name', 'short_composition1']].rename(columns={'short_composition1': 'salt'})
        df = df.drop_duplicates().dropna(subset=['name', 'salt'])
        return df

    def save_data(self, df):
        os.makedirs(os.path.dirname(self.processed_data_path), exist_ok=True)
        df.to_csv(self.processed_data_path, index=False)

    def run(self):
        df = self.load_data()
        processed_df = self.preprocess_data(df)
        self.save_data(processed_df)
        print(f"Preprocessed data saved to {self.processed_data_path}")


if __name__ == "__main__":
    raw_data_path = 'data/raw/A_Z_medicines_dataset_of_India.csv'
    processed_data_path = 'data/processed/preprocessed_medicine_data.csv'
    preprocessor = MedicineDataPreprocessor(raw_data_path, processed_data_path)
    preprocessor.run()
