from doc_query.pinecone_utils import index
import streamlit as st
from doc_query.query import Query


def query_form() -> None:
    st.title("Query a document")
    doc_selection()
    query = query_input()
    query_submitted = st.button(label="Query")
    if query_submitted:
        doc_name: str = st.session_state.selected_doc
        handle_query(query=query, doc_name=doc_name)


def doc_selection() -> None:
    doc_names = list(index.describe_index_stats()["namespaces"].keys())
    current_selection = st.session_state.get("selected_doc", doc_names[0])

    st.selectbox(
        "Select a document to query",
        options=doc_names,
        key="selected_doc",
        index=doc_names.index(current_selection),
    )


def query_input() -> None:
    query = st.text_input("What would you like to ask about this document?")
    return query


def delete_button() -> None:
    st.button(
        label="Delete document",
        on_click=index.delete(delete_all=True, namespace=st.session_state.selected_doc),
        type="primary",
    )


def handle_query(query: str, doc_name: str):
    query_ = Query(query=query, namespace=doc_name)
    st.subheader("Answer")
    st.markdown(query_.answer)
    with st.expander("Show reference documents"):
        st.subheader("Reference Documents")
        for n, doc in enumerate(query_.relevant_docs, start=1):
            st.markdown(f"**Document {n}**")
            st.write(doc.page_content)
            st.divider()
