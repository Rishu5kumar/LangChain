from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv

load_dotenv()

embedding = OpenAIEmbeddings(model='text-embedding-3-large', dimensions=32)
# dimensions = 1536 for small models and 3072 for large models by default

# pass single sentence to it
res = embedding.embed_query("Delhi is the capital of India.")
print(str(res))