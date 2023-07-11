from typing import Type
from langchain.document_loaders import TextLoader, UnstructuredEPubLoader, UnstructuredPDFLoader
from langchain.document_loaders.base import BaseLoader
from langchain.schema import Document
from langchain.text_splitter import RecursiveCharacterTextSplitter

from doc_query.app_config import config


class DocHandler:
    loader_map: dict[str, Type[BaseLoader]] = {
        "pdf": UnstructuredPDFLoader,
        "epub": UnstructuredEPubLoader,
    }

    def __init__(self, filename: str, doc_name: str):
        self.filename = filename
        self.doc_name = doc_name
        self.loader: Type[BaseLoader] = self.get_loader()

    @property
    def file_suffix(self) -> str:
        return self.filename.split(".")[-1]

    def get_loader(self) -> Type[BaseLoader]:
        return self.loader_map.get(self.file_suffix, TextLoader)

    @property
    def doc(self) -> list[Document]:
        return self.loader(self.filename).load()

    def split_doc(self) -> list[Document]:
        text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=50)
        return text_splitter.split_documents(self.doc)

    def split_embed_doc(self) -> None:
        split_docs = self.split_doc()
        config.vectorstore.add_texts(
            texts=[split_doc.page_content for split_doc in split_docs],
            namespace=self.doc_name,
        )
