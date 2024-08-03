import os
import json
from google.oauth2 import service_account
from google.auth.transport.requests import Request
import requests

class MedicalAssistant:
    CREDENTIALS_PATH = 'config/credentials.json'
    GEMINI_API_URL = "https://generativelanguage.googleapis.com/v1beta2/models/text-bison-001:generateText"  # Gemini Pro API endpoint

    def __init__(self, text):
        self.text = text
        self.credentials = None

        # Set the credentials
        if os.path.exists(self.CREDENTIALS_PATH):
            os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = self.CREDENTIALS_PATH
            self.credentials = service_account.Credentials.from_service_account_file(self.CREDENTIALS_PATH)
        else:
            raise FileNotFoundError(f"Credentials file not found at {self.CREDENTIALS_PATH}")

    def get_prescription_info(self):
        payload = {
            'system': 'You are a specialized medical assistant designed to extract prescription information from unstructured text. Your output must strictly adhere to the following format:\nProblem: [Medical Condition]\nSymptoms: [Patient\'s Reported Symptoms OR \'Not stated\']\nMedications:\n- [Medication 1 Name]: [Dosage 1 Instructions]\n- [Medication 2 Name]: [Dosage 2 Instructions]\n- [Medication 3 Name]: [Dosage 3 Instructions]',
            'user': self.text
        }

        # Refresh the credentials to get the access token
        request = Request()
        self.credentials.refresh(request)

        headers = {
            'Authorization': f'Bearer {self.credentials.token}',
            'Content-Type': 'application/json'
        }

        response = requests.post(self.GEMINI_API_URL, json=payload, headers=headers)

        if response.status_code == 200:
            data = response.json()
            if "candidates" in data and data["candidates"]:
                return data["candidates"][0]["output"]
            else:
                raise ValueError("Unexpected response format from Gemini API.")
        else:
            raise ValueError(f"Error in Gemini API request: {response.status_code}, {response.text}")

# Example usage (Ensure GOOGLE_APPLICATION_CREDENTIALS environment variable is set):
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
