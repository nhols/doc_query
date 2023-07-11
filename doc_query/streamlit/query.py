from doc_query.pinecone_utils import index
import streamlit as st
from doc_query.query import Query


def query_form() -> None:
    st.title("Query a document")
    with st.form(key="query_form"):
        doc_name = doc_selection()
        query = query_input()
        query_submitted = st.form_submit_button(label="Query")
    if query_submitted:
        handle_query(query=query, doc_name=doc_name)


def doc_selection() -> str:
    doc_names = list(index.describe_index_stats()["namespaces"].keys())
    doc_name = st.selectbox("Select a document to query", options=doc_names)
    return doc_name


def query_input() -> None:
    query = st.text_input("What would you like to ask about this document?")
    return query


def handle_query(query: str, doc_name: str):
    query_ = Query(query=query, namespace=doc_name)
    st.subheader("Answer")
    st.text(query_.answer)
    with st.expander("Show reference documents"):
        st.subheader("Reference Documents")
        for n, doc in enumerate(query_.relevant_docs, start=1):
            st.markdown(f"**Document {n}**")
            st.write(doc.page_content)
            st.divider()
