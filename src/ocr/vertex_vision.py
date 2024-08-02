import os
from google.cloud import vision
from google.cloud.vision_v1 import types

def check_vertex_vision_credentials(image_path):
    # Set the environment variable for Google Cloud credentials
    os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "elated-nectar-425613-p8-4afb8278d0a4.json"

    # Initialize the Vision client
    client = vision.ImageAnnotatorClient()

    # Load the image
    with open(image_path, 'rb') as image_file:
        content = image_file.read()

    image = types.Image(content=content)

    # Perform text detection
    response = client.text_detection(image=image)
    texts = response.text_annotations

    # Check for errors
    if response.error.message:
        raise Exception(f"Error in Vision API request: {response.error.message}")

    # Print the detected text
    if texts:
        print("Detected text:")
        print(texts[0].description)
    else:
        print("No text detected")

# Example usage
if __name__ == "__main__":
    image_path = 'Screenshot 2024-08-03 012303.png'
    check_vertex_vision_credentials(image_path)
