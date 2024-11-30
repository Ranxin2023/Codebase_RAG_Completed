
# from langchain_pinecone import PineconeVectorStore
# from langchain.embeddings import OpenAIEmbeddings
# from langchain_community.embeddings import HuggingFaceEmbeddings
from sentence_transformers import SentenceTransformer
# from sklearn.preprocessing import normalize


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

from transformers import AutoTokenizer, AutoModel
from sklearn.preprocessing import normalize
import torch

# def get_codebert_embeddings(text, model_name="microsoft/codebert-base"):
#     """
#     Generate embeddings using CodeBERT.

#     Args:
#         text (str): The text or code snippet to embed.
#         model_name (str): The name of the pre-trained CodeBERT model.

#     Returns:
#         numpy.ndarray: The normalized embeddings for the input text.
#     """
#     # Load CodeBERT tokenizer and model
#     tokenizer = AutoTokenizer.from_pretrained(model_name)
#     model = AutoModel.from_pretrained(model_name)
    
#     # Tokenize input text and generate input tensors
#     inputs = tokenizer(text, return_tensors="pt", max_length=512, truncation=True, padding="max_length")
    
#     # Generate embeddings
#     with torch.no_grad():
#         outputs = model(**inputs)
#         # Use the [CLS] token representation as the embedding
#         cls_embedding = outputs.last_hidden_state[:, 0, :]  # Shape: (batch_size, hidden_size)
    
#     # Normalize the embeddings
#     normalized_embedding = normalize(cls_embedding.numpy(), axis=1, norm="l2")
    
#     return normalized_embedding

from transformers import AutoTokenizer, AutoModel
from sklearn.preprocessing import normalize
import torch

class CodeBERTEmbedding:
    """
    A class to generate embeddings using CodeBERT.
    """

    def __init__(self, model_name="microsoft/codebert-base"):
        """
        Initialize the CodeBERTEmbedding class with a specified model.

        Args:
            model_name (str): The name of the pre-trained CodeBERT model.
        """
        self.model_name = model_name
        self.tokenizer = AutoTokenizer.from_pretrained(model_name)
        self.model = AutoModel.from_pretrained(model_name)

    def _generate_embedding(self, text):
        """
        Generate normalized embeddings for a single text.

        Args:
            text (str): The text or code snippet to embed.

        Returns:
            numpy.ndarray: The normalized embeddings for the input text.
        """
        # Tokenize input text and generate input tensors
        inputs = self.tokenizer(
            text, return_tensors="pt", max_length=512, truncation=True, padding="max_length"
        )
        
        # Generate embeddings
        with torch.no_grad():
            outputs = self.model(**inputs)
            # Use the [CLS] token representation as the embedding
            cls_embedding = outputs.last_hidden_state[:, 0, :]  # Shape: (batch_size, hidden_size)
        
        # Normalize the embeddings
        normalized_embedding = normalize(cls_embedding.numpy(), axis=1, norm="l2")
        
        return normalized_embedding[0]

    def embed_documents(self, texts):
        """
        Generate embeddings for a list of documents.

        Args:
            texts (list of str): List of texts or code snippets to embed.

        Returns:
            list of numpy.ndarray: A list of normalized embeddings for the input texts.
        """
        return [self._generate_embedding(text) for text in texts]

    def embed_query(self, text):
        """
        Generate embeddings for a single query.

        Args:
            text (str): The query text to embed.

        Returns:
            numpy.ndarray: The normalized embedding for the query text.
        """
        return self._generate_embedding(text)