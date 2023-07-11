from doc_query.config import Config
from doc_query.pinecone_utils import vectorstore
from doc_query.chain import chain

config = Config(vectorstore=vectorstore, chain=chain)
