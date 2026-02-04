from langchain_pinecone import PineconeVectorStore
from langchain import RetrievalQA
from common.llm import get_llm, get_embeddings
import os

def run_rag(question: str):
    vectorstore = PineconeVectorStore(
        index_name=os.environ["PINECONE_INDEX_NAME"],
        embedding=get_embeddings()
    )

    qa = RetrievalQA.from_chain_type(
        llm=get_llm(),
        retriever=vectorstore.as_retriever(search_kwargs={"k": 3})
    )

    return qa.run(question)
