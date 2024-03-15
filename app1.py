import csv
import streamlit as st
from langchain.chains import ConversationalRetrievalChain
from langchain.embeddings import HuggingFaceEmbeddings
from langchain.vectorstores import FAISS
from streamlit_chat import message
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.document_loaders.csv_loader import CSVLoader
from langchain.llms import OpenAI

DB_FAISS_PATH = 'vectorstore/db_faiss'
OPENAI_API_KEY = st.text_input('Enter your OpenAI API key👇🏻')
def clear_file(file_path):
    with open(file_path, 'r') as file:
        first_row = next(csv.reader(file))  # Read the first row

    with open(file_path, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(first_row)
def searchbyprodcat(prodcat):
    clear_file('store.csv')

    matched_rows=[]
    with open('DMart.csv', 'r', errors="ignore") as csv_file:
        reader = csv.reader(csv_file)
        for row in reader:
            if prodcat in row[4]:
                matched_rows.append(row)

    # Now outside the loop, write all at once to minimize open/close operations
    with open('store.csv', 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(matched_rows)



st.header('DMART SHOP ASSISTANT')
st.write('Choose your product category to prepare the data')

categories = ["Grocery", "Dairy & Beverages", "Packaged Food", "Home & Kitchen", "Fruits & Vegetables", "Personal Care"]
selected_category = st.selectbox("Select a category", categories)

if selected_category:
    searchbyprodcat(selected_category)
    loader = CSVLoader(file_path='store.csv', encoding="utf-8", csv_args={
        'delimiter': ','})
    data = loader.load()
    # Split the text into Chunks
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=20)
    text_chunks = text_splitter.split_documents(data)
    st.write(len(text_chunks))
    # Download Sentence Transformers Embedding From Hugging Face
    embeddings = HuggingFaceEmbeddings(model_name='sentence-transformers/all-MiniLM-L6-v2')

    # COnverting the text Chunks into embeddings and saving the embeddings into FAISS Knowledge Base
    docsearch = FAISS.from_documents(text_chunks, embeddings)
    docsearch.save_local(DB_FAISS_PATH)

    # Loading the model
    llm = OpenAI(openai_api_key=OPENAI_API_KEY)
    chain = ConversationalRetrievalChain.from_llm(llm, retriever=docsearch.as_retriever())


    def conversational_chat(query):
        result = chain({"question": query, "chat_history": st.session_state['history']})
        st.session_state['history'].append((query, result["answer"]))
        return result["answer"]


    if 'history' not in st.session_state:
        st.session_state['history'] = []

    if 'generated' not in st.session_state:
        st.session_state['generated'] = ["Hello ! Ask me anything about Dmart Products" + " 🤗"]

    if 'past' not in st.session_state:
        st.session_state['past'] = ["Hey ! 👋"]

    # container for the chat history
    response_container = st.container()
    # container for the user's text input
    container = st.container()

    with container:
        with st.form(key='my_form', clear_on_submit=True):
            user_input = st.text_input("Query:", placeholder="Talk to your csv data here (:", key='input')
            submit_button = st.form_submit_button(label='Send')

        if submit_button and user_input:
            output = conversational_chat(user_input)

            st.session_state['past'].append(user_input)
            st.session_state['generated'].append(output)

    if st.session_state['generated']:
        with response_container:
            for i in range(len(st.session_state['generated'])):
                message(st.session_state["past"][i], is_user=True, key=str(i) + '_user', avatar_style="big-smile")
                message(st.session_state["generated"][i], key=str(i), avatar_style="thumbs")

