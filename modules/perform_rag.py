from modules.embeddings import get_huggingface_embeddings
from sklearn.metrics.pairwise import cosine_similarity

import numpy as np



def perform_rag(query, pinecone_index, client):
    # Generate embeddings for the query
    query_embedding = get_huggingface_embeddings(query).tolist()
    
    # Query Pinecone directly using the generated embeddings
    top_matches = pinecone_index.query(
        vector=query_embedding,
        top_k=5,
        include_metadata=True,
        namespace="https://github.com/CoderAgent/SecureAgent"
    )

    # Extract contexts (text) from the retrieved matches
    contexts = [item['metadata']['text'] for item in top_matches['matches'] if 'text' in item['metadata']]

    if not contexts:
        raise ValueError("No matching documents found in the vector store.")

    # Create the augmented query
    augmented_query = "<CONTEXT>\n" + "\n\n-------\n\n".join(contexts) + "\n-------\n</CONTEXT>\n\n\n\nMY QUESTION:\n" + query

    # System prompt for LLM
    system_prompt = f"""You are a Senior Software Engineer, specializing in TypeScript.

    Answer any questions I have about the codebase, based on the code provided. Always consider all of the context provided when forming a response.
    """

    # Call the LLM to get a response
    llm_response = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": augmented_query}
        ]
    )

    return llm_response.choices[0].message.content



# def perform_rag(query, pinecone_index, client):
#     raw_query_embedding = get_codebert_embeddings(query)

#     top_matches = pinecone_index.query(vector=raw_query_embedding.tolist(), top_k=5, include_metadata=True, namespace="https://github.com/CoderAgent/SecureAgent")

#     # Get the list of retrieved texts
#     contexts = [item['metadata']['text'] for item in top_matches['matches']]

#     augmented_query = "<CONTEXT>\n" + "\n\n-------\n\n".join(contexts[ : 10]) + "\n-------\n</CONTEXT>\n\n\n\nMY QUESTION:\n" + query

#     # Modify the prompt below as need to improve the response quality
#     system_prompt = f"""You are a Senior Software Engineer, specializing in TypeScript.

#     Answer any questions I have about the codebase, based on the code provided. Always consider all of the context provided when forming a response.
#     """

#     llm_response = client.chat.completions.create(
#         model="llama-3.1-8b-instant",
#         messages=[
#             {"role": "system", "content": system_prompt},
#             {"role": "user", "content": augmented_query}
#         ]
#     )

#     return llm_response.choices[0].message.content