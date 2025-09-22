import streamlit as st
import time
from src.helper import get_text_chunks, get_pdf_text, get_vectorstore, get_conversation_chain

def user_input(user_question):
    response = st.session_state.conversation({'question': user_question})
    st.session_state.chat_history = response['chat_history']
    for i, message in enumerate(st.session_state.chat_history):
        if i % 2 == 0:
            st.write("User:", message.content)

        else:
            st.write("Reply: ", message.content)


def main():
    st.set_page_config("Information Retrieval")
    st.header("Info-Retrieval-system App")

    user_question = st.text_input("Ask your question here from PDF:")

    if "conversation" not in st.session_state:
        st.session_state.conversation = None
    if "chat_history" not in st.session_state:
        st.session_state.chat_history = None
    if user_question:
        user_input = user_question

    with st.sidebar:
        st.title("Menu")
        pdf_docs = st.file_uploader("Upload your PDFs here and click on 'Submit & Process'", accept_multiple_files=True)
        if st.button("Submit & Process"):
            with st.spinner("Processing"):
                time.sleep(3)
                raw_text = get_pdf_text(pdf_docs)
                text_chunks = get_text_chunks(raw_text)
                st.session_state.conversation = get_vectorstore(text_chunks)


                st.success("Done! You can now ask questions about your documents.")

if __name__ == "__main__":
    main()