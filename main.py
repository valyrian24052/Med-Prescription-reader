from src.ocr.vertex_vision import ImageProcessor

if __name__ == "__main__":
    pres=ImageProcessor(r'data\test\sample.png')
    print(pres.get_text())


