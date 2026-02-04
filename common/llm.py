from langchain_openai import ChatOpenAI, OpenAIEmbeddings


def get_embeddings():
    return OpenAIEmbeddings(model="text-embedding-3-small")


def get_llm():
    return ChatOpenAI(
        model="gpt-4o-mini",
        temperature=0
    )
