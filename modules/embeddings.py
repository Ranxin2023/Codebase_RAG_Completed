
from langchain_pinecone import PineconeVectorStore
from langchain.embeddings import OpenAIEmbeddings
from langchain_community.embeddings import HuggingFaceEmbeddings
from sentence_transformers import SentenceTransformer
from sklearn.preprocessing import normalize
"""# Embeddings"""

def get_huggingface_embeddings(text, model_name="sentence-transformers/all-mpnet-base-v2"):
    # Preprocess the text
    text = text.strip().lower()
    
    # Load the model
    model = SentenceTransformer(model_name)
    
    # Generate embeddings
    embeddings = model.encode(text)
    
    # Normalize embeddings
    embeddings = normalize(embeddings.reshape(1, -1), axis=1, norm='l2')
    
    return embeddings

# text = "I am a programmer"

# embeddings = get_huggingface_embeddings(text)

# embeddings