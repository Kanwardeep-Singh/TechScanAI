# document_search.py - RAG-based Document Search System

import json
import numpy as np
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity

INDEX_PATH = 'index/documents_index.json'

# Models
EN_MODEL = SentenceTransformer('sentence-transformers/all-mpnet-base-v2')
DE_MODEL = SentenceTransformer('sentence-transformers/distiluse-base-multilingual-cased-v1')


def load_index():
    with open(INDEX_PATH, 'r') as f:
        documents = json.load(f)
    return documents


def search_documents(query, language='en'):
    documents = load_index()

    # Generate embedding for the query
    model = DE_MODEL if language == 'de' else EN_MODEL
    query_embedding = model.encode(query)

    # Compare with document embeddings
    results = []
    for doc in documents:
        doc_embedding = np.array(doc['embedding'])
        similarity = cosine_similarity([query_embedding], [doc_embedding])[0][0]
        if similarity > 0.5:  # Threshold for relevance
            results.append({
                'file_name': doc['file_name'],
                'similarity': float(similarity),
                'content': doc['content'][:200] + '...'  # Displaying first 200 chars as a snippet
            })

    # Sort by similarity score
    results = sorted(results, key=lambda x: x['similarity'], reverse=True)

    return results


if __name__ == "__main__":
    query = "How does the engine control system work?"
    language = "en"
    results = search_documents(query, language)
    for result in results[:3]:  # Display top 3 results
        print(result)
