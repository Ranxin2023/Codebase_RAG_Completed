# Codebase Chatbot
This project implements a Retrieval-Augmented Generation (RAG)-based chatbot to help answer questions about a specific codebase. The chatbot leverages Pinecone for vector similarity search, HuggingFace embeddings for text representation, and a Groq/OpenAI large language model (LLM) for generating accurate responses based on the retrieved context.

## Features
• Retrieval-Augmented Generation (RAG): Retrieves relevant code snippets and uses an LLM to generate contextually aware answers.
• Embeddings: Uses sentence-transformers to create high-quality embeddings for code and text.
• Vector Database: Powered by Pinecone for efficient search and storage of vectorized code snippets.
• Streamlit Web App: Provides an interactive interface for querying the chatbot.


