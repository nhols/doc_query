from pydoc import Doc
import streamlit as st
from streamlit.runtime.uploaded_file_manager import UploadedFile
from doc_query.doc_handler import DocHandler


def file_upload() -> str:
    file = st.file_uploader(
        label="Uplodad a document", help="Uploading a document will split, embed, and index it for querying."
    )
    doc_name = st.text_input(label="Name your document")
    upload = st.button(label="Upload")
    if upload:
        handle_uploaded_doc(file=file, doc_name=doc_name)


def handle_uploaded_doc(file: UploadedFile, doc_name: str) -> None:
    if not file or not doc_name:
        st.error("Please upload a file and name your document.")
        return

    filename = "/tmp/doc." + file.name.split(".")[-1]
    with open(filename, "wb") as f:
        f.write(file.getvalue())
    doc_handler = DocHandler(filename=filename, doc_name=doc_name)
    doc_handler.split_embed_doc()
    st.success("Document uploaded successfully.")
