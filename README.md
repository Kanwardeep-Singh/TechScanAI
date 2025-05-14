# 🤖 TechScanAI – GenAI-Powered Tool for Technical Document Search, Summarization, and Q&A

## 📌 Overview

**TechScanAI** is a Generative AI-powered solution built to streamline working with large collections of technical documents. It enables users to **search**, **summarize**, and **interact with documents** using natural language. Ideal for engineering documentation, manuals, whitepapers, and research articles, TechScanAI bridges the gap between complex documents and actionable insights.

Whether you're trying to understand a system, troubleshoot an issue, or extract key information quickly, TechScanAI helps you get there faster.

---

## 🧠 Key Features

- 🔍 **Semantic Document Search**: Find the most relevant sections using vector-based retrieval.
- 📝 **Summarization Engine**: Generate concise, context-aware summaries of long technical content.
- ❓ **Conversational Q&A**: Ask natural language questions and receive answers grounded in your documentation.
- 📁 **Modular Design**: Clean codebase with clear separation between indexing, search, summarization, and chatbot logic.

---

## 🗂️ Project Structure

TechScanAI
├── index/
│ └── document_index.json # Precomputed document embeddings and metadata
├── .gitignore # Standard Git exclusions
├── chatbot.py # LLM-based question answering interface
├── document_indexer.py # Embeds and indexes document content
├── document_search.py # Semantic document search logic
├── document_summarizer.py # Summarization pipeline
└── README.md # You're reading it!


---

## ⚙️ Installation

1. Clone the repository:

```
git clone https://github.com/yourusername/TechScanAI.git
cd TechScanAI
```

2. Install dependencies

```
pip install -r requirements.txt
```

## 🚀 How to Use

1. Index Your Documents

```
python document_indexer.py
```
This script loads your documents, creates embeddings, and saves them in index/document_index.json.

2. Search Documents

```
python document_search.py
```
Use this script to run semantic search queries on indexed documents and retrieve relevant chunks.

3. Summarize Documents

```
python document_summarizer.py
```
Generate summaries for full documents or for the top search results.

4. Ask Questions

```
python chatbot.py
```
Launch a CLI chatbot that takes your question and returns an answer based on the indexed documents.


## 📌 What's Next?
-Web-based front-end for easier interaction

-Support for PDF and DOCX parsing

-Document update and re-indexing support

-Integration with external LLM APIs (e.g., OpenAI, Anthropic)