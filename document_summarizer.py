# document_summarizer.py - Document Summarization Module

from transformers import pipeline
import json

INDEX_PATH = 'index/documents_index.json'

# Load summarization pipelines
summarizer_en = pipeline('summarization', model='facebook/bart-large-cnn')
summarizer_de = pipeline('summarization', model='mrm8488/bert2bert_shared-german-finetuned-summarization')


def load_index():
    with open(INDEX_PATH, 'r') as f:
        documents = json.load(f)
    return documents


def summarize_document(document_id):
    documents = load_index()
    document = next((doc for doc in documents if doc['file_name'] == document_id), None)

    if not document:
        return "Document not found."

    content = document['content']
    language = document['language']

    # Choose the appropriate summarizer
    if language == 'de':
        summary = summarizer_de(content[:1024], max_length=150, min_length=40, do_sample=False)[0]['summary_text']
    else:
        summary = summarizer_en(content[:1024], max_length=150, min_length=40, do_sample=False)[0]['summary_text']

    return summary


if __name__ == "__main__":
    doc_id = "example_document.txt"
    summary = summarize_document(doc_id)
    print("Summary:\n", summary)
