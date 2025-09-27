# integration package between langchain and openai
# inherit from BaseLLM class
from langchain_openai import OpenAI

# load secret keys from env file into current file
from dotenv import load_dotenv

load_dotenv()

llm = OpenAI(model='gpt-3.5-turbo-instruct')

# all langchain components has invoke()
res = llm.invoke("What is the capital of India?")
print(res)