import requests
import streamlit as st
from streamlit.runtime.uploaded_file_manager import UploadedFile
from doc_query.doc_handler import DocHandler
from doc_query.url_handler import URLHandler


def file_upload() -> str:
    st.markdown("#### Upload, split, embed and index a document")
    file = st.file_uploader(
        label="Uplodad a document", help="Uploading a document will split, embed, and index it for querying."
    )
    url = st.text_input(label="Or enter a URL")
    doc_name = st.text_input(label="Name your document")
    upload = st.button(label="Upload")
    if upload:
        if file:
            handle_uploaded_doc(file=file, doc_name=doc_name)
        elif url:
            resp = requests.get(url)
            if not resp.ok:
                st.error("Could not load url")
            elif resp.headers.get("content-type") == "application/pdf":
                handle_url_pdf(url=url, doc_name=doc_name)
            else:
                handle_url(url=url, doc_name=doc_name)
        else:
            st.error("Please upload a file or enter a URL")
            return
        st.success("Document uploaded successfully")


def handle_uploaded_doc(file: UploadedFile, doc_name: str) -> None:
    if not file or not doc_name:
        st.error("Please upload a file and name your document.")
        return

    filename = "/tmp/doc." + file.name.split(".")[-1]
    with open(filename, "wb") as f:
        f.write(file.getvalue())
    doc_handler = DocHandler(filename=filename, doc_name=doc_name)
    doc_handler.split_embed_doc()


def handle_url_pdf(url: str, doc_name: str) -> None:
    doc_handler = DocHandler(filename=url, doc_name=doc_name)
    doc_handler.split_embed_doc()


def handle_url(url: str, doc_name: str) -> None:
    url_handler = URLHandler(url=url, doc_name=doc_name)
    url_handler.split_embed_text()
