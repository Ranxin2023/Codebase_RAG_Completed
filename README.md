# Codebase Chatbot
This project implements a Retrieval-Augmented Generation (RAG)-based chatbot to help answer questions about a specific codebase. The chatbot leverages Pinecone for vector similarity search, HuggingFace embeddings for text representation, and a Groq/OpenAI large language model (LLM) for generating accurate responses based on the retrieved context.

## Features
- Retrieval-Augmented Generation (RAG): Retrieves relevant code snippets and uses an LLM to generate contextually aware answers.
- Embeddings: Uses sentence-transformers to create high-quality embeddings for code and text.
- Vector Database: Powered by Pinecone for efficient search and storage of vectorized code snippets.
- Streamlit Web App: Provides an interactive interface for querying the chatbot.


## Technologies Used

- Python
- Streamlit (Frontend for the chatbot)
- Pinecone (Vector database)
- LangChain (Framework for RAG)
- HuggingFace Transformers (Embeddings)
- Groq/OpenAI API (LLM for generating responses)

## Setup Instructions

1. Clone the Repository

```sh
git clone https://github.com/Ranxin2023/Codebase_RAG_Completed_Ranxin
cd codebase-chatbot
```

2. Install Dependencies
Ensure you have Python 3.8+ installed. Install required packages:
```sh
pip install -r requirements.txt
```

3. Set Up API Keys
- Create a `.env` file in the root directory and add the following: