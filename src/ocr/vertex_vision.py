import os
import cv2
from google.cloud import vision
from google.cloud.vision_v1 import types

class ImageProcessor:
    CREDENTIALS_PATH = 'config/credentials.json'

    def __init__(self, image_path):
        self.image_path = image_path
        self.ocr_text = None
        self.vision_client = None

        # Set the credentials
        if os.path.exists(self.CREDENTIALS_PATH):
            os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = self.CREDENTIALS_PATH
            self.vision_client = vision.ImageAnnotatorClient()
        else:
            raise FileNotFoundError(f"Credentials file not found at {self.CREDENTIALS_PATH}")

        self._run_ocr()

    def _load_image(self):
        image = cv2.imread(self.image_path)
        if image is None:
            raise ValueError(f"Failed to load image from {self.image_path}")
        return image

    def _preprocess_image(self, image):
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        preprocessed_image = cv2.resize(gray, (1280, 720))
        return preprocessed_image

    def _run_ocr(self):
        image = self._load_image()
        preprocessed_image = self._preprocess_image(image)
        _, buffer = cv2.imencode('.png', preprocessed_image)
        content = buffer.tobytes()
        image = types.Image(content=content)

        response = self.vision_client.text_detection(image=image)
        if response.error.message:
            raise ValueError(f"Error in Vision API request: {response.error.message}")

        texts = response.text_annotations
        if texts:
            self.ocr_text = texts[0].description
        else:
            self.ocr_text = ""

    def get_text(self):
        return self.ocr_text
