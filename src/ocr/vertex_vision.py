import os
import cv2
from google.cloud import vision
from google.cloud.vision_v1 import types

class ImageProcessor:
    CREDENTIALS_PATH = 'config/credentials.json'

    def __init__(self, image_path):
        self.image_path = image_path
        self.preprocessed_image = None
        self.ocr_text = None

        os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = self.CREDENTIALS_PATH
        self.vision_client = vision.ImageAnnotatorClient()

        self._run_ocr()

    def load_image(self):
        return cv2.imread(self.image_path)

    def preprocess(self):
        image = self.load_image()
        if image is None:
            raise Exception(f"Error loading image: {self.image_path}")
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        self.preprocessed_image = cv2.resize(gray, (1280, 720))

    def _run_ocr(self):
        self.preprocess()

        if self.preprocessed_image is None:
            raise Exception("Image has not been preprocessed yet.")

        _, buffer = cv2.imencode('.png', self.preprocessed_image)
        image = types.Image(content=buffer.tobytes())

        response = self.vision_client.text_detection(image=image)
        if response.error.message:
            raise Exception(f"Error in Vision API request: {response.error.message}")

        texts = response.text_annotations
        self.ocr_text = texts[0].description if texts else ""

    def get_text(self):
        if self.ocr_text is not None:
            return self.ocr_text
        else:
            raise Exception("OCR has not been performed yet.")

    def save_preprocessed_image(self, output_path):
        if self.preprocessed_image is not None:
            cv2.imwrite(output_path, self.preprocessed_image)
        else:
            raise Exception("Image has not been preprocessed yet.")

