from langchain_community.document_loaders import PyPDFLoader
from langchain import RecursiveCharacterTextSplitter
from langchain_pinecone import PineconeVectorStore
from common.llm import get_embeddings
import os


def ingest_pdf(path: str):
    loader = PyPDFLoader(path)
    docs = loader.load()

    splitter = RecursiveCharacterTextSplitter(chunk_size=800, chunk_overlap=100)
    chunks = splitter.split_documents(docs)

    PineconeVectorStore.from_documents(
        chunks,
        embedding=get_embeddings(),
        index_name=os.environ["PINECONE_INDEX_NAME"]
    )


if __name__ == "__main__":
    ingest_pdf("sample.pdf")
