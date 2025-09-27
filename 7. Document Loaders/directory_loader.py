from langchain_community.document_loaders import DirectoryLoader, PyPDFLoader

loader = DirectoryLoader(
    path='books',
    glob='*.pdf',
    loader_cls=PyPDFLoader
)
# docs = loader.load()
# it takes time and all pdfs are loading in memory
# these two problems are solved by lazy_loader()
docs = loader.lazy_load()

for document in docs:
    print(document.metadata)