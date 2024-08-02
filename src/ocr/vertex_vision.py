import os
from google.cloud import vision
from google.cloud.vision_v1 import types

class VertexVisionChecker:
    def __init__(self, credentials_path, image_path):
        self.credentials_path = credentials_path
        self.image_path = image_path
        os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = self.credentials_path
        self.client = vision.ImageAnnotatorClient()

    def load_image(self):
        with open(self.image_path, 'rb') as image_file:
            content = image_file.read()
        return types.Image(content=content)

    def perform_ocr(self, image):
        response = self.client.text_detection(image=image)
        if response.error.message:
            raise Exception(f"Error in Vision API request: {response.error.message}")
        return response.text_annotations

    def print_detected_text(self, texts):
        if texts:
            print("Detected text:")
            print(texts[0].description)
        else:
            print("No text detected")

    def run(self):
        image = self.load_image()
        texts = self.perform_ocr(image)
        self.print_detected_text(texts)

# Example usage
if __name__ == "__main__":
    credentials_path = 'config/credentials.json'
    image_path = 'path/to/your/image.jpg'
    checker = VertexVisionChecker(credentials_path, image_path)
    checker.run()
