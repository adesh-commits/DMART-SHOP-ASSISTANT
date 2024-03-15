# DMART Shop Assistant

Welcome to the DMART Shop Assistant project! This Streamlit web application serves as a virtual assistant for querying information about DMART products using natural language.

## Overview

The DMART Shop Assistant provides users with an intuitive interface to interact with a dataset containing DMART product details. Users can ask questions about various product categories, and the virtual assistant retrieves relevant information using natural language processing (NLP) techniques.

## Features

- **Product Category Selection**: Users can choose a product category from predefined options.
- **Natural Language Querying**: Users can ask questions about DMART products using natural language input.
- **Conversational Responses**: The virtual assistant responds to user queries with relevant information.
- **Filtered Data Storage**: Filtered product data based on user queries is stored in a temporary CSV file (`store.csv`).
- **Conversational Interface**: Engage with the chatbot to ask questions and receive information about DMART products.
- **FAISS Vector Store**: Efficiently searches through product data using sentence-transformer embeddings.
- **Streamlit Chat**: Provides a user-friendly chat interface for interaction.

## Setup

1. Clone the repository:

   ```bash
   git clone https://github.com/yourusername/dmart-shop-assistant.git

2.Navigate to the project directory:

```bash
Copy code
cd dmart-shop-assistant
Install the required dependencies:

```bash
Copy code
pip install -r requirements.txt
Run the Streamlit application:

bash
Copy code
streamlit run app.py
Open your web browser and navigate to http://localhost:8501 to access the DMART Shop Assistant.

Dependencies
Streamlit
Langchain
Hugging Face Transformers
OpenAI
Usage
Select a product category from the dropdown menu.
Ask questions about DMART products using the text input field.
View the conversational history and responses in the UI.
Contributing
Contributions are welcome! If you find any bugs or have suggestions for improvements, please open an issue or submit a pull request.
