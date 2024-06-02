import streamlit as st
from langchain.schema import HumanMessage, SystemMessage, AIMessage
from langchain_groq import ChatGroq
from langchain.globals import set_verbose
from dotenv import load_dotenv
import os
from datetime import datetime
import json

# Load environment variables from .env file
load_dotenv()

# Fetch the Groq API key from environment variables
groq_api_key = os.getenv("GROQ_API_KEY")

# Ensure the API key is available
if not groq_api_key:
    st.error("Groq API key not found. Please set it in the .env file.")
    st.stop()

# Set verbosity
set_verbose(True)

# Define the history file path
history_file = "chat_history.json"

# Load chat history from the file
def load_history():
    if os.path.exists(history_file):
        with open(history_file, "r") as file:
            return json.load(file)
    return []

# Save chat history to the file
def save_history(history):
    with open(history_file, "w") as file:
        json.dump(history, file)

# Initialize chat history
if 'flowmessages' not in st.session_state:
    st.session_state['flowmessages'] = [
        SystemMessage(content="You are a comedian AI assistant")
    ]
    st.session_state['history'] = load_history()
    st.session_state['selected_question'] = None

# Initialize the ChatGroq model with the API key
chat = ChatGroq(temperature=0.5, groq_api_key=groq_api_key)

# Function to load Groq model and get response
def get_chatmodel_response(question):
    st.session_state['flowmessages'].append(HumanMessage(content=question))
    answer = chat.invoke(st.session_state['flowmessages'])
    st.session_state['flowmessages'].append(AIMessage(content=answer.content))
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    st.session_state['history'].append((question, answer.content, timestamp))
    # Save history after each interaction
    save_history(st.session_state['history'])
    # Remove the oldest entry if history exceeds 100
    if len(st.session_state['history']) > 100:
        st.session_state['history'] = st.session_state['history'][-100:]
    return answer.content

# Add title
st.title("Chat with ChatbotEVA🤖")

# Sidebar to display chat history
st.sidebar.title("Chat History")
for i, (question, response, timestamp) in enumerate(st.session_state['history']):
    if st.sidebar.button(f"{question[:20]}... ({timestamp})", key=f"button_{i}"):
        st.session_state['selected_question'] = i

# Display the selected question and response in the sidebar
if st.session_state['selected_question'] is not None:
    question, response, timestamp = st.session_state['history'][st.session_state['selected_question']]
    st.sidebar.subheader(f"Time: {timestamp}")
    st.sidebar.write(f"**Question:** {question}")
    st.sidebar.write(f"**Response:** {response}")

# Create a form for the input to handle enter key submission
with st.form(key='chat_form', clear_on_submit=True):
    input = st.text_input("Chat with EVA", placeholder="Type your message here...", key="input")
    submit = st.form_submit_button("Send")

# Check if the form is submitted
if submit:
    response = get_chatmodel_response(input)
    st.subheader("The Response is")
    st.write(response)

# Add animated background
st.markdown(
    """
    <style>
    .stApp {
        background: linear-gradient(-45deg, #4b0082, #e73c7e, #23a6d5, #23d5ab);
        background-size: 400% 400%;
        animation: gradientAnimation 15s ease infinite;
        position: absolute;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
    }

    .css-1d391kg .css-1g3a6xg {
        background: linear-gradient(-45deg, #4b0082, #e73c7e, #23a6d5, #23d5ab);
        background-size: 400% 400%;
        animation: gradientAnimation 15s ease infinite;
    }

    @keyframes gradientAnimation {
        0% {background-position: 0% 50%}
        50% {background-position: 100% 50%}
        100% {background-position: 0% 50%}
    }
    </style>
    """,
    unsafe_allow_html=True
)
