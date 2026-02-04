from pinecone import Pinecone
import os

def get_index():
    pc = Pinecone(api_key=os.environ["PINECONE_API_KEY"])
    return pc.Index(os.environ["PINECONE_INDEX_NAME"])
