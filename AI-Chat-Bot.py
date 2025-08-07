import streamlit as st
from langchain_mistralai.chat_models import ChatMistralAI
from langchain.chains import ConversationChain
from langchain.memory import ConversationBufferMemory
from langchain.prompts import PromptTemplate

st.markdown("<h1 style='text-align: center;'>Mistral Chat</h1>", unsafe_allow_html=True)

llm = ChatMistralAI(model="mistral-large-latest")

# Step 2 & 3: Define and create the new prompt template
template = """
Current conversation:
{history}
Human: {input}
AI:
"""
PROMPT = PromptTemplate(input_variables=["history", "input"], template=template)

# --- SESSION STATE INITIALIZATION ---
# This is where we will store and manage the conversation.

if 'memory' not in st.session_state:
    st.session_state.memory = ConversationBufferMemory()

if 'chat_history' not in st.session_state:
    st.session_state.chat_history = []

if 'chain' not in st.session_state:
    # Langchain conversation chain

    st.session_state.chain = ConversationChain(
        llm = llm,
        memory = st.session_state.memory,
        prompt = PROMPT,
        verbose = False
    )

with st.sidebar:
    st.subheader("Controls")
    if st.button("Clear Conversation"):
        st.session_state.chat_history = []
        st.session_state.memory.clear()
        st.rerun()

# --- UI: DISPLAY CHAT HISTORY ---

# Loop through the stored messages and display them

for message in st.session_state.chat_history:
    with st.chat_message(message['role']):
        st.markdown(message['content'])


# --- UI: GET USER INPUT ---
# Use st.chat_input to get user input at the bottom of the page

user_prompt = st.chat_input("Ask anything...") # the walrus operator lets you do both the assignment and the condition check in one line.
if user_prompt:

     # 1. Add user message to chat history 
    st.session_state.chat_history.append({"role": "user", "content": user_prompt})
    
    # Display the user's message in a chat bubble
    with st.chat_message("user"):
        st.markdown(user_prompt)

    # 2. Get AI response using the LangChain chain
    with st.chat_message("Assistant"):
        with st.spinner("Thinking..."): # shows spinner until you get the prediction from the api
            ai_response = st.session_state.chain.predict(input = user_prompt)
            st.markdown(ai_response)

    # 3. Add AI response to chat history
    st.session_state.chat_history.append({"role": "assistant", "content": ai_response})

    