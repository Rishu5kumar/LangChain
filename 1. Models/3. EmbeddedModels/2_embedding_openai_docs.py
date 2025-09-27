from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv

load_dotenv()

embedding = OpenAIEmbeddings(model='text-embedding-3-large', dimensions=32)

doc = [
    "Delhi is the capital of India.",
    "Kolkata is the capital of west bengal.",
    "Paris is the capital of France."
]

# pass document to it
res = embedding.embed_documents(doc)
print(str(res))