# irfan-sheikh-wasserstoff-AiTask

# RAG-based Query Suggestion Chatbot for WordPress Sites

## Introduction

This project integrates a Retrieval-Augmented Generation (RAG)-based query suggestion chatbot with WordPress sites. The chatbot uses advanced natural language processing (NLP) techniques to understand user queries and provide relevant responses. The system leverages pre-trained models and vector embeddings to enhance user interaction and accessibility on WordPress platforms.

## System Architecture

The system architecture comprises three main components:

1. **WordPress Frontend**: Users interact with the chatbot embedded in WordPress pages.
2. **WordPress Plugin**: Manages the chatbot interface, handles settings, and communicates with the backend.
3. **Backend FastAPI Application**: Processes user queries using NLP models and vector embeddings, generating appropriate responses.

## Technical Stack

### Backend

- **FastAPI**: High-performance web framework for building APIs.
- **Transformers (Hugging Face)**: Provides state-of-the-art NLP models like BART.
- **FAISS (Facebook AI Similarity Search)**: Efficient vector database for similarity search.
- **Python**: Core programming language for backend development.

### Frontend

- **HTML, CSS, JavaScript**: Basic technologies for building the chatbot interface.
- **AJAX**: For asynchronous communication between the WordPress frontend and the backend API.

### Integration with WordPress

- **WordPress Plugin Development**: Integrates the chatbot into WordPress sites.
- **Admin Dashboard Integration**: Allows administrators to configure chatbot settings.

## Project Structure

AI_TASK/
├── backend/
│ ├── app.py
│ ├── embeddings.py
│ ├── rag_processor.py
│ ├── chain_of_thought.py
│ ├── vector_database.py
│ └── requirements.txt
├── wordpress_plugin/
│ ├── chatbot_plugin.php
│ ├── style.css
│ ├── index.js
├── frontend/
│ ├── index.html
│ ├── chat_interface.js
│ └── style.css
├── README.md
└── .env


## Setup and Installation

### Backend

1. **Install Dependencies**:
    ```bash
    pip install -r backend/requirements.txt
    ```

2. **Run FastAPI Application**:
    ```bash
    uvicorn backend.app:app --reload
    ```

### WordPress Plugin

1. **Install the Plugin**:
    - Copy the `wordpress_plugin` folder to the `wp-content/plugins` directory of your WordPress installation.

2. **Activate the Plugin**:
    - Go to the WordPress admin dashboard, navigate to the Plugins section, and activate the "RAG Chatbot" plugin.

3. **Configure the Plugin**:
    - Set the API URL in the plugin settings to point to your FastAPI backend (e.g., `http://localhost:8000`).

### Frontend

- The frontend files (`index.html`, `chat_interface.js`, `style.css`) are part of the WordPress plugin and are automatically enqueued when the plugin is activated.

## Usage

1. **Interact with the Chatbot**:
    - Users can interact with the chatbot by typing queries into the chat interface on WordPress pages.

2. **Admin Dashboard**:
    - Administrators can configure the API URL and other settings from the WordPress admin dashboard.

## Contributing

Contributions are welcome! Please fork the repository and submit pull requests for any enhancements or bug fixes.

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.

## Acknowledgements

- [Hugging Face](https://huggingface.co/) for the Transformers library.
- [Facebook AI](https://ai.facebook.com/tools/faiss/) for FAISS.
- [FastAPI](https://fastapi.tiangolo.com/) for the web framework.

## Contact

For any questions or support, please contact Irfan Sheikh at irfansheikh6990@gmail.com.
