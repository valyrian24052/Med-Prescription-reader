import sys
import os

from src.ocr.vertex_vision import ImageProcessor
from src.ocr.postprocess import MedicalAssistant

sys.path.append(os.path.dirname(os.path.abspath(__file__)))


if __name__ == "__main__":
    pres=ImageProcessor(r'data\test\sample.png')
    text_input=pres.get_text()
    assistant = MedicalAssistant(text_input)
    output = assistant.get_prescription_info()
    print(output)