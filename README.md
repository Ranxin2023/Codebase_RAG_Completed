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
3. View Chat History:
- Chat history is displayed below the input field for seamless conversation.

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
The purpose of `env.ts` is to import environment variables from a `.env` file and validate their presence and format.

Step-by-step Explanation:
1. Importing dependencies:
The file imports dotenv, createPrivateKey from the `crypto` module, and `chalk` for colorful console output.

2. Loading `.env` file:
`dotenv.config()` loads the environment variables from a `.env` file in the project root directory.

3. Exporting `env` object:
The file exports an `env` object that contains the loaded environment variables, typed using the `const` keyword.

4. Validating environment variables:
The file checks if the required environment variables are present in the env object. If any are missing, it logs an error message and sets `valid` to `false`.

5. Validating GitHub private key format:
The file tries to create a private key using the `createPrivateKey` function from the `crypto` module. If the private key is invalid (e.g., it doesn't start or end with the expected RSA private key markers), it logs an error message and sets `valid` to `false`.

6. Exiting if invalid:
If valid is still false after checking all the environment variables, the file logs a warning message and exits the process using `process.exit(1)`.



