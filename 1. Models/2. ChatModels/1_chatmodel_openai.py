# inherit from BaseChatModel class
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()

# model = ChatOpenAI(model='gpt-4')
model = ChatOpenAI(model='gpt-4', temperature=0.4, max_completion_tokens=20)
# temperature is creativity
# token is roughly a word

res = model.invoke("What is the capital of India?")
print(res) # it gives answer with metadata

# to fetch the answer use content
print(res.content)