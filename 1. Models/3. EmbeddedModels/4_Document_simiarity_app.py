from langchain_huggingface.embeddings import HuggingFaceEndpointEmbeddings
from dotenv import load_dotenv
from sklearn.metrics.pairwise import cosine_similarity

load_dotenv()

embedding = HuggingFaceEndpointEmbeddings(
    repo_id="sentence-transformers/all-MiniLM-L6-v2",
    task="feature-extraction"
)

doc = [
    "Delhi is the capital of India.",
    "Kolkata is the capital of West Bengal.",
    "Paris is the capital of France."
]

query = 'Tell me about capital of India?'

doc_embed = embedding.embed_documents(doc)
query_emb = embedding.embed_query(query) # it gives list of 384 dimension by default

# cosine_similarity gives a 2D array (1, n_docs), so we flatten it

# scores = cosine_similarity([query_emb], doc_embed)
scores = cosine_similarity([query_emb], doc_embed)[0]  # shape (1, 3)
# print(scores) # [0.70022859 0.51907234 0.33689925]

# Get index of max score
index = scores.argmax()
score = scores[index]
# index, score = sorted(list(enumerate(scores)), key=lambda x:x[1])[-1]

print(query)
print(doc[index])
print('Similarity score is:', score)
