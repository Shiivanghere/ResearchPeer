import os

from rag import create_vector_db, ask_pdf


def process_pdf(uploaded_file):
    """
    Creates the vector database from the uploaded PDF.
    Returns True if successful.
    """

    if uploaded_file is None:
        return False

    create_vector_db(uploaded_file)

    return True


def answer_question(question):
    """
    Returns the answer for the given question
    from the uploaded PDF.
    """

    if not os.path.exists("chroma_db"):
        return "Please upload a PDF and create the vector database first."

    return ask_pdf(question)