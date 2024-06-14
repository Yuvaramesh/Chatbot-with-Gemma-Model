# Chatbot-with-Gemma-Model

This repository contains system built using Google Gemma. The project leverages Google's Gemma for natural language understanding and processing, providing accurate answers to user queries.

## Features

- User-friendly interface for asking questions.
- Integration with Google Gemma for natural language processing.
- Backend server to handle requests and responses.
- Deployed application for easy access.

## Getting Started

Follow these instructions to get a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

- Python 3.12
- Google Cloud account
- Google Gemma API credentials

### Installation

1. **Clone the repository:**
    ```sh
    git clone https://github.com/Yuvaramesh/Chatbot-with-Gemma-Model.git
    ```

2. **Create and activate a virtual environment:**
    ```sh
    python3 -m venv venv
    source venv/bin/activate
    ```

3. **Install the required packages:**
    ```sh
    pip install -r requirements.txt
    ```

4. **Set up Google Gemma:**
    - Go to the Google Cloud Console.
    - Enable the Gemma API.
    - Download the credentials JSON file.
    - Set the environment variable to point to your credentials file:
      ```sh
      export GOOGLE_APPLICATION_CREDENTIALS="/path/to/your/credentials.json"
      ```
5. **Run the application:**
    ```sh
    python app.py
    ```
6. **Access the application:**
    Open your web browser and go to `http://localhost:5000`.

## Usage

1. Open the application in your browser.
2. Enter your question in the input field.
3. Press the "Submit" button.
4. Answers will be provided by the system.

## Project Structure
chatbot-with-gemma-model
```
├── app.py                # Main application file
├── requirements.txt      # List of required Python packages
├── README.md             # This file
└── .gitignore            # Git ignore file
