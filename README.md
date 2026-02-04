
# Serverless RAG AI

## Overview
Serverless RAG AI is a modular framework for building Retrieval-Augmented Generation (RAG) applications using serverless infrastructure. It leverages AWS Lambda, Pinecone, and LLMs to ingest, index, and query documents efficiently.

## Features
- PDF ingestion and chunking
- Semantic search with Pinecone
- RAG-based Q&A
- Serverless deployment via AWS SAM

## Folder Structure
```
common/           # Shared utilities (LLM, Pinecone client)
infrastructure/   # AWS SAM templates
ingest/           # PDF ingestion scripts
query/            # Lambda handler and RAG pipeline
```

## Getting Started
1. **Clone the repository:**
	```bash
	git clone https://github.com/ydeepthi211-dev/serverless-rag-ai.git
	cd serverless-rag-ai
	```
2. **Install dependencies:**
	```bash
	pip install -r requirements.txt
	```
3. **Configure AWS credentials** and Pinecone API keys as environment variables.
4. **Deploy infrastructure:**
	```bash
	cd infrastructure
	sam deploy --guided
	```

## Usage
- Ingest PDFs using the scripts in `ingest/`
- Query documents via the Lambda handler in `query/`

## Contributing
Pull requests are welcome! For major changes, please open an issue first to discuss what you would like to change.

## License
This project is licensed under the MIT License.

