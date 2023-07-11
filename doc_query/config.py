from pydantic import BaseModel

from langchain.vectorstores.base import VectorStore
from langchain.chains.combine_documents.base import BaseCombineDocumentsChain


class Config(BaseModel):
    vectorstore: VectorStore
    chain: BaseCombineDocumentsChain

    class Config:
        arbitrary_types_allowed = True
        frozen = True
