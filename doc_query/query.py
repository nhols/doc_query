from langchain.schema import Document
from app_config import config


class Query:
    def __init__(self, query: str, namespace: str, n_relevant_docs: int = 4):
        self.query = query
        self.namespace = namespace
        self.n_relevant_docs = n_relevant_docs
        self._relevant_docs: list[Document] = []
        self._answer: str | None = None

    @property
    def relevant_docs(self) -> list[Document]:
        if self._relevant_docs:
            return self._relevant_docs
        self._relevant_docs = config.vectorstore.similarity_search(
            self.query, namespace=self.namespace, k=self.n_relevant_docs
        )
        return self._relevant_docs

    @property
    def answer(self) -> str:
        if self._answer:
            return self._answer
        self._answer = config.chain.run(input_documents=self.relevant_docs, question=self.query)
        return self._answer
