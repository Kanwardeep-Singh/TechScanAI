# document_indexer.py - Indexing and embedding documents

import os
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sentence_transformers import SentenceTransformer
import json

# Paths
DOCUMENTS_PATH = 'documents/'  # Folder containing documents
INDEX_PATH = 'index/'

# Models
EN_MODEL = SentenceTransformer('sentence-transformers/all-mpnet-base-v2')  # English Model
DE_MODEL = SentenceTransformer('sentence-transformers/distiluse-base-multilingual-cased-v1')  # German & Multilingual Model



def index_documents():
    if not os.path.exists(INDEX_PATH):
        os.makedirs(INDEX_PATH)

    documents = []
    for file_name in os.listdir(DOCUMENTS_PATH):
        if file_name.endswith('.txt'):  # Only indexing text files
            with open(os.path.join(DOCUMENTS_PATH, file_name), 'r', encoding='utf-8') as f:
                content = f.read()
                language = 'de' if 'de' in file_name else 'en'  # Simple heuristic to determine language

                # Generate embeddings
                model = DE_MODEL if language == 'de' else EN_MODEL
                embedding = model.encode(content)

                # Save document metadata
                documents.append({
                    'file_name': file_name,
                    'content': content,
                    'embedding': embedding.tolist(),
                    'language': language
                })

    # Save indexed documents to a JSON file
    with open(os.path.join(INDEX_PATH, 'documents_index.json'), 'w') as f:
        json.dump(documents, f)

    print('Documents indexed successfully!')


if __name__ == "__main__":
    index_documents()
