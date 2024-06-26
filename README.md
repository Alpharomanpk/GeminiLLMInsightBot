# Gemini LLM Applications

This repository contains multiple applications demonstrating the usage of the Gemini Language Learning Model (LLM) for Q&A chatbots and image analysis. The applications are built using Streamlit for the frontend and Google Generative AI for the backend.

## Features

- **Text-Based Q&A Chatbots**: Users can input questions and receive text-based answers from the Gemini model.
  - **Basic Chatbot**: Simple Q&A functionality.
  - **Chatbot with Streaming Responses**: Displays responses as they are generated.
  - **Chatbot with Chat History**: Maintains a session history of the conversation.

- **Image-Based Analysis**: Users can upload images and receive detailed descriptions and analyses from the Gemini Vision model.

## Frontend Interface

- **Q&A Demo Page**: Users can input a question and receive a response.
- **Chat History Page**: Displays the conversation history.
- **Image Analysis Page**: Users can upload an image and receive a detailed analysis.

## Backend Implementation

- **Streamlit**: Provides a simple and interactive interface for users.
- **Google Generative AI**: Integrates with Google Generative AI to generate responses based on user inputs.

## Technologies Used

- **Frontend**: Streamlit
- **Backend**: Python, Google Generative AI
- **API Services**: Google Generative AI
- **Environment Management**: dotenv

## Getting Started

### Prerequisites

- Python 3.7+
- Streamlit
- Google Generative AI API key
- dotenv

### Installation

1. **Clone the repository:**
   - Clone the repository and navigate to the project directory.

2. **Create a virtual environment and activate it:**
   - Create and activate a virtual environment for the project.

3. **Install the required packages:**
   - Install the necessary Python packages listed in `requirements.txt`.

4. **Create a `.env` file:**
   - Add your Google API key to the `.env` file.

### Running the Applications

#### 1. Q&A Chatbot (APP.py)

This application uses the Gemini Language Learning Model to generate responses to user queries.

#### 2. Q&A Chatbot with Streaming Responses (Chat.py)

This application extends the basic Q&A Chatbot to stream responses from the Gemini model.

#### 3. Q&A Chatbot with Chat History (Qachat.py)

This application includes chat history, allowing users to see the conversation context.

#### 4. Vision Application (Vision.py)

This application allows users to upload an image and get a response from the Gemini Vision Model based on the image and an optional input prompt.

## File Descriptions

### APP.py

Basic Q&A chatbot that takes user input and generates a response using the Gemini model.

### Chat.py

Extends the basic chatbot by streaming responses as they are generated and maintaining the conversation history.

### Qachat.py

Enhances the chatbot experience by storing and displaying the chat history within the session.

### Vision.py

Allows users to upload an image and receive a detailed response from the Gemini Vision model, combining image and text analysis.

## Acknowledgments

- [Streamlit](https://streamlit.io/)
- [Google Generative AI](https://ai.google/)
- [dotenv](https://pypi.org/project/python-dotenv/)
