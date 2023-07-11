from config import Config
from pinecone_utils import vectorstore
from chain import chain

config = Config(vectorstore=vectorstore, chain=chain)
