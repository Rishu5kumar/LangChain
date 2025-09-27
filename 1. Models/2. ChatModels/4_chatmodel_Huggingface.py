# open source model
from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
# import HuggingFaceEndpoint to use it's api
from dotenv import load_dotenv
import os

load_dotenv()

llm = HuggingFaceEndpoint(
    repo_id = "mistralai/Mistral-7B-Instruct-v0.2",
    task = "text-generation"
    # api_key=os.getenv("HUGGINGFACEHUB_API_TOKEN")
)

# Pass api_key manually or use HUGGINGFACEHUB_API_TOKEN in .env

model = ChatHuggingFace(llm=llm)

res = model.invoke("What is the capital of India?")

print(res.content)