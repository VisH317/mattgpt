from langchain.document_loaders import PyPDFLoader
from langchain.text_splitter import CharacterTextSplitter
from langchain.llms import OpenAI

from langchain.embeddings.sentence_transformer import SentenceTransformerEmbeddings
from langchain.vectorstores import Chroma
from langchain.chains import RetrievalQA
from dotenv import load_dotenv

load_dotenv()

def get_chain(file_name: str):
    loader = PyPDFLoader(file_name)
    splitter = CharacterTextSplitter(chunk_size=500, chunk_overlap=50)
    documents = splitter.split_documents(loader)

    embedding_function = SentenceTransformerEmbeddings(model_name="all-MiniLM-L6-v2")
    db = Chroma.from_documents(documents, embedding_function)

    chain = RetrievalQA.from_chain_type(llm=OpenAI(), chain_type="stuff", retriever = db.as_retriever())

    return chain
