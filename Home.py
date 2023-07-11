from doc_query.streamlit.query import query_form
import streamlit as st

from doc_query.streamlit.upload import file_upload

st.set_page_config(page_title="Doc query", page_icon="🔍")
with st.sidebar:
    file_upload()
query_form()
