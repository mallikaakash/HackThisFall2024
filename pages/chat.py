import streamlit as st
from datetime import datetime

# Page config
st.set_page_config(
    page_title="TimeTalk AI | Chat",
    page_icon="💭",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Custom CSS
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Playfair+Display:wght@400;700&family=Inter:wght@400;500;600&display=swap');
    
    .chat-message {
        padding: 1.5rem;
        border-radius: 1rem;
        margin-bottom: 1rem;
        max-width: 80%;
    }
    
    .user-message {
        background-color: #f8f9fa;
        margin-left: auto;
    }
    
    .celebrity-message {
        background-color: #e3f2fd;
        margin-right: auto;
    }
    
    .chat-container {
        height: 600px;
        overflow-y: auto;
        padding: 1rem;
        background-color: white;
        border-radius: 1rem;
        border: 1px solid #eee;
    }
    
    .input-container {
        position: fixed;
        bottom: 0;
        left: 0;
        right: 0;
        padding: 1rem;
        background-color: white;
        border-top: 1px solid #eee;
    }
</style>
""", unsafe_allow_html=True)

# Initialize chat history
if 'messages' not in st.session_state:
    st.session_state.messages = []

# Get selected celebrity from session state
selected_celebrity = st.session_state.get('selected_celebrity', 'Albert Einstein')

# Header
st.title(f"Chat with {selected_celebrity}")

# Chat container
chat_container = st.container()

# Display chat messages
with chat_container:
    for message in st.session_state.messages:
        if message["role"] == "user":
            st.markdown(f"""
            <div class="chat-message user-message">
                <strong>You:</strong><br>{message["content"]}
            </div>
            """, unsafe_allow_html=True)
        else:
            st.markdown(f"""
            <div class="chat-message celebrity-message">
                <strong>{selected_celebrity}:</strong><br>{message["content"]}
            </div>
            """, unsafe_allow_html=True)

# Input form
with st.form(key="chat_form", clear_on_submit=True):
    user_input = st.text_input("Type your message:", key="user_input")
    submit_button = st.form_submit_button("Send")

    if submit_button and user_input:
        # Add user message to chat history
        st.session_state.messages.append({"role": "user", "content": user_input})
        
        # Simulate AI response (replace with actual AI integration)
        ai_response = f"As {selected_celebrity}, I would respond to your message about '{user_input}' ..."
        st.session_state.messages.append({"role": "assistant", "content": ai_response})
        
        # Rerun to update chat display
        st.experimental_rerun()

# Navigation buttons
col1, col2 = st.columns(2)
with col1:
    if st.button("← Back to Celebrities"):
        st.switch_page("pages/2_👥_celebrities.py")
with col2:
    if st.button("Start New Chat"):
        st.session_state.messages = []
        st.experimental_rerun()