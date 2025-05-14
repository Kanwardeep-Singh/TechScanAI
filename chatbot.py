# chatbot.py - Chatbot Interface

from transformers import pipeline
from document_search import search_documents

# Load conversational models
chatbot_en = pipeline('text-generation', model='gpt2')
chatbot_de = pipeline('text-generation', model='dbmdz/german-gpt2')


def chatbot_response(question, language='en'):
    # Search for relevant documents
    search_results = search_documents(question, language)

    if not search_results:
        return "Sorry, I couldn't find any relevant documents."

    # Combine top 3 search results as context
    context = ' '.join([result['content'] for result in search_results[:3]])

    # Generate a response based on the context
    if language == 'de':
        response = chatbot_de(context, max_length=150, num_return_sequences=1)[0]['generated_text']
    else:
        response = chatbot_en(context, max_length=150, num_return_sequences=1)[0]['generated_text']

    return response


if __name__ == "__main__":
    question = "How does the engine control system work?"
    response = chatbot_response(question, language='en')
    print("Chatbot Response:\n", response)
