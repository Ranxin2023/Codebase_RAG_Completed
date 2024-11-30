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

## Project Structure
```sh
.
├── modules/
│   ├── clone_repository.py       # Clones the GitHub repository
│   ├── embeddings.py             # Generates embeddings using HuggingFace
│   ├── get_files_content.py      # Extracts content from code files
│   ├── perform_rag.py            # Implements RAG functionality
│   └── __init__.py               # Module initialization
├── app.py                        # Main Streamlit application
├── requirements.txt              # Python dependencies
├── .env                          # Environment variables (API keys)
└── README.md                     # Project documentation

```


## Usage
1. Open the App:
- After running the app, navigate to `http://localhost:8501` in your web browser.
2. Ask Questions:
- Enter your question about the codebase (e.g., "How is the JavaScript parser used?").

## How It Works
1. Codebase Retrieval:
- The `clone_repository` module clones a specified GitHub repository and extracts content from supported files.
2. Embedding Generation:
- Code files are vectorized using HuggingFace's `sentence-transformers`.
3. Pinecone Integration:
- Embeddings are stored in Pinecone, enabling efficient similarity search.
4. Query Processing:
- The `perform_rag` module retrieves relevant snippets and sends them to the LLM for contextual answers.
5. LLM Response:
- The LLM generates a response based on the retrieved code snippets.

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

The `env.ts` file essentially acts as a gatekeeper for the application's environment variable configuration. It ensures that the application has all the necessary variables and that they are in the correct format before proceeding.

By having this separate configuration file, the application's main logic can rely on these environment variables being properly set, allowing for easier maintenance and scalability.

