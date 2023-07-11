from langchain.chains.question_answering import load_qa_chain
from doc_query.openai_utils import llm

chain = load_qa_chain(llm, chain_type="stuff")
