from app_config import config
import streamlit as st


def upload_doc(filename: str, doc_name: str) -> None:
    st.file_uploader(label="Uploda a new doc to query")
    doc_handler = config.doc_handler(filename=filename, doc_name=doc_name)
    doc_handler.split_embed_doc()
