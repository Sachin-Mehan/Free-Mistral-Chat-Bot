import streamlit as st
from langchain_mistralai import ChatMistralAI

from langchain.chains import ConversationChain
from langchain.memory import ConversationBufferMemory


st.title("Mistral Chat")

# Selecting our Model
llm = ChatMistralAI(model = "mistral-large-latest")

# Sesssion State Initializations

if 'memory' not in st.session_state:
    st.session_state.memory = ConversationBufferMemory()

if 'chat_history' not in st.session_state:
    st.session_state.chat_history = []

if 'chain' not in st.session_state:
    st.session_state.chain = ConversationChain(
        llm = llm,
        memory = st.session_state.memory,
        verbose = True # Will show the preprompt in terminal
    )

with st.sidebar:
    st.subheader("Controls")
    if st.button("Clear"):
        st.session_state.memory.clear()
        st.session_state.chat_history = []

        st.rerun()

# Display Chat History
# Loop through the stored messages and display them

for message in st.session_state.chat_history:
    with st.chat_message(message['role']):
        st.markdown(message['content'])


# Get User Input

user_prompt = st.chat_input("Ask Anything...")
if user_prompt:

    # Add the user message to chat history

    st.session_state.chat_history.append({"role": "user", "content": user_prompt})

    # Display the user's message in a chat bubble

    with st.chat_message("user"):
        st.markdown(user_prompt)

    
    # Get AI responde using the LangChain Chain and display it in a chat bubble

    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            ai_response = st.session_state.chain.predict(input = user_prompt)

            st.markdown(ai_response)

    
    # Add AI Response to chat history
    st.session_state.chat_history.append({"role": "assistant", "content": ai_response})

