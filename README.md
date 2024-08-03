
```markdown
## Overview

The Medical Prescription Reader is a robust OCR (Optical Character Recognition) system designed to read and interpret medical prescriptions. Powered by Google Vertex Vision, this solution uses fine-tuned machine learning models to accurately recognize medication names and dosages. Integration with a comprehensive medical terminology database enables seamless medication identification and efficient web-based searches, ultimately improving healthcare workflows and patient experiences.


## Directory Structure

```
medical-prescription-reader/
├── config/
├── data/
│   ├── processed/
│   ├── raw/
│   └── test/
├── src/
│   ├── database/
│   │   ├── __init__.py
│   │   └── vector_db.py
│   ├── ocr/
│   │   ├── __init__.py
│   │   ├── postprocess.py
│   │   └── vertex_vision.py
│   └── __init__.py
├── tests/
├── utils/
├── web/
├── .gitignore
├── main.py
├── README.md
├── requirements.txt
└── vector_index
```

## Features

- OCR using Google Vertex Vision: High accuracy in reading handwritten and printed prescriptions.
- Medical Terminology Database Integration: Enables accurate identification of medications.
- Web Interface: Easy-to-use web interface for uploading prescriptions and viewing results.
- Logging and Configuration: Comprehensive logging and configuration management.

## Setup Instructions

### Prerequisites

- Python 3.x
- Google Cloud SDK with Vertex Vision API enabled
- A Google Cloud service account with credentials

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/medical-prescription-reader.git
   cd medical-prescription-reader
   ```

2. Create a virtual environment and activate it:
   ```bash
   python -m venv venv
   source venv/bin/activate
   ```

3. Install the required packages:
   ```bash
   pip install -r requirements.txt
   ```

4. Set up Google Cloud credentials:
   - Download the service account key file and set the environment variable:
     ```bash
     export GOOGLE_APPLICATION_CREDENTIALS="path/to/credentials.json"
     ```

5. Configure the project:
   - Edit the `config/config.yaml` file to set up necessary configurations.

### Running the Application

1. Run the main script:
   ```bash
   python src/main.py
   ```

2. Access the web interface:
   - Open your browser and navigate to `http://localhost:5000`.

### Testing

- Run the tests using `pytest`:
  ```bash
  pytest src/tests/
  ```

## Contribution

Contributions are welcome! Please open an issue or submit a pull request for any improvements or new features.

## Acknowledgements

- Thanks to Google Cloud for providing the Vertex Vision API.
- Inspired by the need to improve healthcare workflows and patient experience through technology.
```
