import sys
import os

from src.ocr.vertex_vision import ImageProcessor
from src.ocr.postprocess import MedicalAssistant


sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python main.py <image_path>")
        sys.exit(1)

    image_path = sys.argv[1]

    pres = ImageProcessor(image_path)
    text_input = pres.get_text()
    assistant = MedicalAssistant(text_input)
    output = assistant.get_prescription_info()
    print(output)
