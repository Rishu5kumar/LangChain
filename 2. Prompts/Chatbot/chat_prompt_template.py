from langchain_core.prompts import ChatPromptTemplate

chat_template = ChatPromptTemplate([
    ('system', 'You are a helpful {domain} expert'),
    ('human', 'Explain in simple terms, what is {topic}')
])
# we can also use ChatPromptTemplate.from_messages, it will give same result

prompt = chat_template.invoke({'domain':'cricket','topic':'Dusra'})

print(prompt)