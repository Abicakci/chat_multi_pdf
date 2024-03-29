# Import des modules nécessaires
import streamlit as st
from dotenv import load_dotenv
from PyPDF2 import PdfReader
from langchain.text_splitter import CharacterTextSplitter
from langchain.embeddings import OpenAIEmbeddings, HuggingFaceInstructEmbeddings
from langchain.vectorstores import FAISS
from langchain.memory import ConversationBufferMemory
from langchain.chains import ConversationalRetrievalChain
from langchain.chat_models import ChatOpenAI
from htmlTemplates import bot_template, user_template, css

from transformers import pipeline  # Import de la fonction pipeline depuis le module transformers

# Fonction pour extraire le texte des fichiers PDF
def get_pdf_text(pdf_files):
    
    text = ""
    for pdf_file in pdf_files:
        reader = PdfReader(pdf_file)
        for page in reader.pages:
            text += page.extract_text()
    return text

# Fonction pour découper le texte en petits morceaux (chunks)
def get_chunk_text(text):
    
    text_splitter = CharacterTextSplitter(
    separator = "\n",
    chunk_size = 1000,
    chunk_overlap = 200,
    length_function = len
    )

    chunks = text_splitter.split_text(text)

    return chunks

# Fonction pour créer le magasin vectoriel à partir des chunks de texte
def get_vector_store(text_chunks):
    
    # Pour les embeddings OpenAI
    embeddings = OpenAIEmbeddings()
    
    # Pour les embeddings HuggingFace
    # embeddings = HuggingFaceInstructEmbeddings(model_name = "hkunlp/instructor-xl")

    vectorstore = FAISS.from_texts(texts = text_chunks, embedding = embeddings)
    
    return vectorstore

# Fonction pour créer la chaîne de conversation
def get_conversation_chain(vector_store):
    
    # Modèle OpenAI
    llm = ChatOpenAI()

    # Modèle HuggingFace
    # llm = HuggingFaceHub(repo_id="google/flan-t5-xxl", model_kwargs={"temperature":0.5, "max_length":512})

    memory = ConversationBufferMemory(memory_key='chat_history', return_messages=True)

    conversation_chain = ConversationalRetrievalChain.from_llm(
        llm = llm,
        retriever = vector_store.as_retriever(),
        memory = memory
    )

    return conversation_chain

# Fonction pour gérer l'entrée de l'utilisateur et afficher la conversation
def handle_user_input(question):

    response = st.session_state.conversation({'question':question})
    st.session_state.chat_history = response['chat_history']

    for i, message in enumerate(st.session_state.chat_history):
        if i % 2 == 0:
            st.write(user_template.replace("{{MSG}}", message.content), unsafe_allow_html=True)
        else:
            st.write(bot_template.replace("{{MSG}}", message.content), unsafe_allow_html=True)

# Fonction principale
def main():
    load_dotenv()
    st.set_page_config(page_title='Chat with Your own PDFs', page_icon=':books:')
    
    st.write(css, unsafe_allow_html=True)
    
    if "conversation" not in st.session_state:
        st.session_state.conversation = None

    if "chat_history" not in st.session_state:
        st.session_state.chat_history = None
    
    st.header('Chat with Your own PDFs :books:')
    question = st.text_input("Ask anything to your PDF: ")

    if question:
        handle_user_input(question)
    
    # Barre latérale pour télécharger les documents PDF
    with st.sidebar:
        st.subheader("Upload your Documents Here: ")
        pdf_files = st.file_uploader("Choose your PDF Files and Press OK", type=['pdf'], accept_multiple_files=True)

        if st.button("OK"):
            with st.spinner("Processing your PDFs..."):

                # Extraction du texte des PDF
                raw_text = get_pdf_text(pdf_files)

                # Découpage du texte en chunks
                text_chunks = get_chunk_text(raw_text)

                # Création du magasin vectoriel
                vector_store = get_vector_store(text_chunks)
                st.write("DONE")

                # Création de la chaîne de conversation
                st.session_state.conversation =  get_conversation_chain(vector_store)

if __name__ == '__main__':
    main()
