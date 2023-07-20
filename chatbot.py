import os
from langchain.document_loaders import PyPDFLoader 
from langchain.embeddings import OpenAIEmbeddings 
from langchain.vectorstores import Chroma 
from langchain.chains import ConversationalRetrievalChain
from langchain.memory import ConversationBufferMemory
from langchain.llms import OpenAI
from langchain.chat_models import ChatOpenAI

os.environ["OPENAI_API_KEY"] ="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"
pdf_path = "terms.pdf"
loader = PyPDFLoader(pdf_path)
pages = loader.load_and_split()

embeddings = OpenAIEmbeddings()
vectordb = Chroma.from_documents(pages, embedding=embeddings, 
                                 persist_directory=".")
# vectordb.persist()
memory = ConversationBufferMemory(memory_key="chat_history", return_messages=True)
pdf_qa = ConversationalRetrievalChain.from_llm(ChatOpenAI(temperature=0.8, model_name='gpt-3.5-turbo') , vectordb.as_retriever(),  memory=memory)

def conv(prompt):
    no_ans = "\nGive the following  reply: 'I don't know please contact with support by email support@nifty-bridge.com' word by word, no changes if promt is not related to the context "
    query = prompt+no_ans
    result = pdf_qa({"question": query})

    # if this is the first message in the chat
    if len(result["chat_history"])==2:
        return "Hello I am NiftyBridge AI assistant. How could I help you?"
    
    return result["answer"]



