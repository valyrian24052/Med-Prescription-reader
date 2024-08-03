import sys
import os

from src.ocr.vertex_vision import ImageProcessor
from src.ocr.postprocess import MedicalAssistant


sys.path.append(os.path.dirname(os.path.abspath(__file__)))


if __name__ == "__main__":
    # pres=ImageProcessor(r'data\test\sample.png')
    # print(pres.get_text())


# Example usage:
    text_input = """
    Name: Armando
    Address: Went Rimbo
    Coqua
    makati
    9
    Age: 29
    Px
    Sex: M
    Date: 12-03-90
    City
    Hinox)
    Amoxicillin Joong Cap #21
    1.cap
    Sig: 1 cap 3x a day for
    Sween days.
    Physician's Sig.
    Lic. No.
    PTR No.
    S2 No.
    Idela Guy
    1234567
    """
    assistant = MedicalAssistant(text_input)
    output = assistant.get_prescription_info()
    print(output)