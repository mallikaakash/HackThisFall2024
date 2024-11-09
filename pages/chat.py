# import streamlit as st
# from datetime import datetime

# # Page config
# st.set_page_config(
#     page_title="TimeTalk AI | Chat",
#     page_icon="💭",
#     layout="wide",
#     initial_sidebar_state="collapsed"
# )

# # Custom CSS
# st.markdown("""
# <style>
#     @import url('https://fonts.googleapis.com/css2?family=Playfair+Display:wght@400;700&family=Inter:wght@400;500;600&display=swap');
    
#     .chat-message {
#         padding: 1.5rem;
#         border-radius: 1rem;
#         margin-bottom: 1rem;
#         max-width: 80%;
#     }
    
#     .user-message {
#         background-color: #f8f9fa;
#         margin-left: auto;
#     }
    
#     .celebrity-message {
#         background-color: #e3f2fd;
#         margin-right: auto;
#     }
    
#     .chat-container {
#         height: 600px;
#         overflow-y: auto;
#         padding: 1rem;
#         background-color: white;
#         border-radius: 1rem;
#         border: 1px solid #eee;
#     }
    
#     .input-container {
#         position: fixed;
#         bottom: 0;
#         left: 0;
#         right: 0;
#         padding: 1rem;
#         background-color: white;
#         border-top: 1px solid #eee;
#     }
# </style>
# """, unsafe_allow_html=True)

# # Initialize chat history
# if 'messages' not in st.session_state:
#     st.session_state.messages = []

# # Get selected celebrity from session state
# selected_celebrity = st.session_state.get('selected_celebrity', 'Albert Einstein')

# # Header
# st.title(f"Chat with {selected_celebrity}")

# # Chat container
# chat_container = st.container()

# # Display chat messages
# with chat_container:
#     for message in st.session_state.messages:
#         if message["role"] == "user":
#             st.markdown(f"""
#             <div class="chat-message user-message">
#                 <strong>You:</strong><br>{message["content"]}
#             </div>
#             """, unsafe_allow_html=True)
#         else:
#             st.markdown(f"""
#             <div class="chat-message celebrity-message">
#                 <strong>{selected_celebrity}:</strong><br>{message["content"]}
#             </div>
#             """, unsafe_allow_html=True)

# # Input form
# with st.form(key="chat_form", clear_on_submit=True):
#     user_input = st.text_input("Type your message:", key="user_input")
#     submit_button = st.form_submit_button("Send")

#     if submit_button and user_input:
#         # Add user message to chat history
#         st.session_state.messages.append({"role": "user", "content": user_input})
        
#         # Simulate AI response (replace with actual AI integration)
#         ai_response = f"As {selected_celebrity}, I would respond to your message about '{user_input}' ..."
#         st.session_state.messages.append({"role": "assistant", "content": ai_response})
        
#         # Rerun to update chat display
#         st.experimental_rerun()

# # Navigation buttons
# col1, col2 = st.columns(2)
# with col1:
#     if st.button("← Back to Celebrities"):
#         st.switch_page("pages/celebrities.py")
# with col2:
#     if st.button("Start New Chat"):
#         st.session_state.messages = []
#         st.experimental_rerun()

import streamlit as st
import google.generativeai as genai
from datetime import datetime
import json
import os
from typing import Dict, List
# Initialize Gemini API
GOOGLE_API_KEY = st.secrets["GOOGLE_API_KEY"]
genai.configure(api_key=GOOGLE_API_KEY)

class PromptManager:
    def __init__(self):
        self.system_prompts = {
            "Albert Einstein": """You are Albert Einstein, the renowned physicist. Respond in a way that reflects:
                - Your German accent and speaking style
                - Deep knowledge of physics and science
                - Your philosophical nature and wit
                - Your pacifist views and humanitarian concerns
                Keep responses concise but insightful. Use occasional German phrases naturally.""",
            
            "Marie Curie": """You are Marie Curie, the pioneering scientist. Your responses should:
                - Show your dedication to scientific research
                - Reflect your Franco-Polish background
                - Demonstrate your determination and work ethic
                - Include your perspectives on women in science
                Be precise and methodical in your explanations."""
            # Add more celebrity personas here
        }
        
    def get_prompt(self, celebrity: str, user_input: str) -> str:
        base_prompt = self.system_prompts.get(celebrity, "")
        context = f"""Current conversation context:
        - Speaking as: {celebrity}
        - User query: {user_input}
        
        Remember to stay in character while being informative and engaging."""
        
        return f"{base_prompt}\n\n{context}"

class ChatManager:
    def __init__(self):
        self.model = genai.GenerativeModel('gemini-pro')
        self.prompt_manager = PromptManager()
        self.chat_history: List[Dict] = []
        
    def generate_response(self, celebrity: str, user_input: str) -> str:
        try:
            # Get formatted prompt
            prompt = self.prompt_manager.get_prompt(celebrity, user_input)
            
            # Generate response
            response = self.model.generate_content(
                prompt + "\n\nUser: " + user_input,
                generation_config={
                    'temperature': 0.8,
                    'top_p': 0.8,
                    'top_k': 40,
                    'max_output_tokens': 1024,
                }
            )
            
            return response.text
            
        except Exception as e:
            st.error(f"Error generating response: {str(e)}")
            return "I apologize, but I'm having trouble responding right now. Please try again."

    def add_to_history(self, role: str, content: str):
        self.chat_history.append({
            "role": role,
            "content": content,
            "timestamp": datetime.now().isoformat()
        })

# Initialize session state
if 'chat_manager' not in st.session_state:
    st.session_state.chat_manager = ChatManager()

# Page config
st.set_page_config(
    page_title="TimeTalk AI | Chat",
    page_icon="💭",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Custom CSS (your existing CSS here)
st.markdown("""
<style>
    /* Your existing CSS */
</style>
""", unsafe_allow_html=True)

# Get selected celebrity from session state
selected_celebrity = st.session_state.get('selected_celebrity', 'Albert Einstein')

# Header
st.title(f"Chat with {selected_celebrity}")

# Chat container
chat_container = st.container()

# Display chat messages
with chat_container:
    for message in st.session_state.chat_manager.chat_history:
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
        st.session_state.chat_manager.add_to_history("user", user_input)
        
        # Generate and add AI response
        ai_response = st.session_state.chat_manager.generate_response(
            selected_celebrity, 
            user_input
        )
        st.session_state.chat_manager.add_to_history("assistant", ai_response)
        
        # Rerun to update chat display
        st.rerun()

# Navigation buttons
col1, col2 = st.columns(2)
with col1:
    if st.button("← Back to Celebrities"):
        st.switch_page("pages/celebrities.py")
with col2:
    if st.button("Start New Chat"):
        st.session_state.chat_manager = ChatManager()
        st.experimental_rerun()