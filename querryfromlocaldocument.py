from langchain.document_loaders import TextLoader
from langchain.embeddings import OpenAIEmbeddings
from langchain.text_splitter import CharacterTextSplitter
import os
loader=TextLoader(file_path="mypersonal.txt")
document=loader.load()
textChunk=CharacterTextSplitter(chunk_size=1000)
texts=textChunk.split_documents(document)
mykey="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"
myembedmodel=OpenAIEmbeddings(openai_api_key=mykey)
os.environ["OPENAI_API_KEY"]=mykey
len(texts)
print(loader.load()[0].page_content)
from langchain.vectorstores import Pinecone as lpcone
import pinecone
pinecone.init(api_key="ab9ff52f-d87d-4f84-9b21-669a0655c2ec",
              environment="us-west4-gcp-free")
docsearch=lpcone.from_documents(documents=texts, 
                      embedding=myembedmodel,
                      index_name='mysummmerindex')
from langchain.llms import OpenAI
from langchain.chains import RetrievalQA
qs=RetrievalQA.from_chain_type(
            llm=OpenAI(),
            chain_type="stuff",
            retriever=docsearch.as_retriever()
            )
myquery="tell me about iit kanpur in 10 words"
print(qs({"query":myquery}))

