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
```sh
PINECONE_API_KEY=your-pinecone-api-key
GROQ_API_KEY=your-groq-api-key
```

- Replace your-pinecone-api-key and your-groq-api-key with your respective API keys.

4. Set up Pinecone
- Go to [Pinecone Dashboard](https://app.pinecone.io/).
- Create an index with the following settings:
    - Dimension: 768
    - Namespace: `codebase-rag`
- Note the environment (e.g., `us-west1-gcp`) and ensure it matches your code.

5. Run the Application
Launch the Streamlit app:
```sh
streamlit run app.py

```

## Usage Example

Below is an example interaction with the Codebase Chatbot:

### Question
What is the purpose of the `env.ts`?

### Answer
Based on the provided code, the purpose of `env.ts` is to:

1. Import and configure the `dotenv` library, which loads environment variables from a `.env` file.
2. Parse the environment variables and store them in a TypeScript object called `env`. This object has properties for:
   - `GITHUB_APP_ID`
   - `GITHUB_PRIVATE_KEY`
   - `GITHUB_WEBHOOK_SECRET`
   - `GROQ_API_KEY`
3. Perform validation checks on the environment variables:
   - It checks if all required variables are present and not empty.
   - It validates the format of the GitHub private key by attempting to create a private key object using the `createPrivateKey` function from the `crypto` module. If the format is invalid, it displays an error message.
4. If any validation checks fail, it logs an error message and exits the process with a non-zero status code using `process.exit(1)`.

The purpose of `env.ts` is to ensure that the required environment variables are present and properly formatted before running the application. This helps prevent issues with the application's dependencies or third-party APIs that may be affected by invalid or missing environment variables.


