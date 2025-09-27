# go to console.anthropic.com to generate api key(close source model)

from langchain_anthropic import ChatAnthropic
from dotenv import load_dotenv

load_dotenv()

model = ChatAnthropic(model='claude-3.5-sonnet-20241022')

res = model.invoke("What is the capital of India?")
print(res.content)