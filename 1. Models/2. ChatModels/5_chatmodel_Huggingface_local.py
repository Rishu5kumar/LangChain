# local open source model
from langchain_huggingface import ChatHuggingFace, HuggingFacePipeline

llm = HuggingFacePipeline.from_model_id(
    model_id = "mistralai/Mistral-7B-Instruct-v0.2",
    task = "text-generation",
    pipeline_kwargs=dict(
        temperature=0.5,
        max_new_tokens=100
    )
)
model = ChatHuggingFace(llm=llm)

res = model.invoke("What is the capital of India?")

print(res.content)

# here when i will run this, all required package will be downloaded.