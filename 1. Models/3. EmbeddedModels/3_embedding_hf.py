from langchain_huggingface.embeddings import HuggingFaceEndpointEmbeddings
from dotenv import load_dotenv
import os

load_dotenv()
# api_key = os.getenv("HUGGINGFACEHUB_API_TOKEN")

embedding = HuggingFaceEndpointEmbeddings(
    repo_id="sentence-transformers/all-MiniLM-L6-v2",
    task="feature-extraction"
    # huggingfacehub_api_token=api_key
)

doc = [
    "Delhi is the capital of India.",
    "Kolkata is the capital of West Bengal.",
    "Paris is the capital of France."
]

res = embedding.embed_documents(doc)
print(res)
