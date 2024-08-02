import re

class TextPostprocessor:
    def __init__(self, text):
        self.text = text
        self.medicine_name = None
        self.salt = None

    def extract_medicine_info(self):
        # Example patterns for medicine name and salt extraction
        medicine_name_pattern = re.compile(r'\b[A-Z][a-z]+(?: [A-Z][a-z]+)*\b')
        salt_pattern = re.compile(r'\b[a-zA-Z]+(?: [a-zA-Z]+)*\b')

        # Split the text into lines for processing
        lines = self.text.split('\n')

        for line in lines:
            # Search for medicine name
            if self.medicine_name is None:
                match = medicine_name_pattern.search(line)
                if match:
                    self.medicine_name = match.group(0)

            # Search for salt
            if self.salt is None:
                match = salt_pattern.search(line)
                if match:
                    self.salt = match.group(0)

            # If both are found, we can stop the search
            if self.medicine_name and self.salt:
                break

        if not self.medicine_name:
            self.medicine_name = "Medicine name not found"
        if not self.salt:
            self.salt = "Salt not found"

    def extract(self):
        self.extract_medicine_info()
        return self.medicine_name, self.salt

# Example usage
if __name__ == "__main__":
    sample_text = """
    Rx
    Paracetamol 500mg
    Take one tablet by mouth every 6 hours.
    """
    postprocessor = TextPostprocessor(sample_text)
    medicine_name, salt = postprocessor.extract()
    print("Medicine Name:", medicine_name)
    print("Salt:", salt)
