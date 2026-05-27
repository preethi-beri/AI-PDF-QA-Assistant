import streamlit as st

from pdf_loader import extract_text
from embeddings import create_vector_store
from rag_pipeline import get_answer

st.set_page_config(
    page_title="AI PDF QA Assistant",
    page_icon="📄"
)

st.title("📄 AI PDF Question Answering Assistant")

uploaded_file = st.file_uploader(
    "Upload a PDF",
    type="pdf"
)

if uploaded_file:

    text = extract_text(uploaded_file)

    vector_store = create_vector_store(text)

    st.success("PDF processed successfully!")

    question = st.text_input(
        "Ask a question about the PDF:"
    )

    if question:

        docs = vector_store.similarity_search(
            question,
            k=3
        )

        answer = get_answer(
            question,
            docs
        )

        st.subheader("Answer")
        st.write(answer)