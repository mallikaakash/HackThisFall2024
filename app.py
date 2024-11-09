# import streamlit as st

# # Initialize session state
# if 'page' not in st.session_state:
#     st.session_state.page = 'landing'

# # Function to navigate to the next page
# def next_page(page):
#     st.session_state.page = page

# # Page: Landing
# def landing_page():
#     st.title("Welcome to Your AI Chatbot")
#     st.subheader("Your AI-powered assistant at your fingertips")
#     st.write(
#         """
#         This app will help you interact with a powerful language model to assist you with various tasks. 
#         Click the 'Start' button to begin your journey!
#         """
#     )
#     if st.button("Start"):
#         next_page('selection')

# # Page: Selection (Ensure this function is defined)
# def selection_page():
#     st.title("Choose an Option")
#     # Add your selection page code here

# # Page routing
# if st.session_state.page == 'landing':
#     landing_page()
# elif st.session_state.page == 'selection':
#     selection_page()

import streamlit as st
from streamlit_lottie import st_lottie
import requests

def load_lottieurl(url: str):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

# Page config
st.set_page_config(page_title="CelebrityChat AI", page_icon="🎭", layout="wide")

# Custom CSS
st.markdown("""
<style>
    .main {
        padding: 0rem 5rem;
    }
    .stButton>button {
        color: #4F8BF9;
        border-radius: 50px;
        height: 3em;
        width: 100%;
    }
    .stTextInput>div>div>input {
        color: #4F8BF9;
    }
</style>
""", unsafe_allow_html=True)

# Header
st.title("🎭 CelebrityChat AI")
st.subheader("Chat with Historic Figures and Modern Celebrities!")

# Main content
col1, col2 = st.columns([2, 1])

with col1:
    st.markdown("""
    ## Bring History to Life!
    
    CelebrityChat AI uses cutting-edge artificial intelligence to let you 
    chat with a wide range of historic figures and modern celebrities. 
    Whether you want to discuss philosophy with Socrates, get leadership 
    advice from Napoleon, or just chat about music with Taylor Swift, 
    our AI makes it possible!
    
    ### Features:
    - Chat with hundreds of historic figures and celebrities
    - AI-powered responses based on extensive research
    - Learn history, get inspired, or just have fun!
    
    Start your journey through time and fame today!
    """)

    if st.button("Start Chatting Now!", key="start_button"):
        st.write("Redirecting to chat interface...")

with col2:
    lottie_chat = load_lottieurl("https://assets5.lottiefiles.com/packages/lf20_hu9cd9.json")
    st_lottie(lottie_chat, height=300, key="chat_animation")

# Example celebrities
st.markdown("## Chat with Amazing Personalities")
celeb_col1, celeb_col2, celeb_col3, celeb_col4 = st.columns(4)

celebrities = [
    ("Albert Einstein", "https://upload.wikimedia.org/wikipedia/commons/3/3e/Einstein_1921_by_F_Schmutzer_-_restoration.jpg"),
    ("William Shakespeare", "https://upload.wikimedia.org/wikipedia/commons/a/a2/Shakespeare.jpg"),
    ("Cleopatra", "https://upload.wikimedia.org/wikipedia/commons/3/3e/Kleopatra-VII.-Altes-Museum-Berlin1.jpg"),
    ("Leonardo da Vinci", "https://upload.wikimedia.org/wikipedia/commons/c/cb/Francesco_Melzi_-_Portrait_of_Leonardo_-_WGA14795.jpg"),
]

for i, (name, image_url) in enumerate(celebrities):
    with eval(f"celeb_col{i+1}"):
        st.image(image_url, width=150, caption=name)
        if st.button(f"Chat with {name.split()[-1]}", key=f"chat_{i}"):
            st.write(f"Starting chat with {name}...")

# Chat preview
st.markdown("## Experience the Magic of AI Conversation")
chat_preview_col1, chat_preview_col2 = st.columns([1, 2])

with chat_preview_col1:
    st.image("https://upload.wikimedia.org/wikipedia/commons/d/d3/Albert_Einstein_Head.jpg", width=100)

with chat_preview_col2:
    st.markdown("""
    **Albert Einstein**: Greetings! I'm Albert Einstein. What would you like to discuss? Perhaps we could explore the intricacies of relativity or ponder the nature of the universe itself.
    
    **You**: Hello, Dr. Einstein! I've always wondered about your famous equation E=mc². Could you explain it in simple terms?
    
    **Albert Einstein**: E=mc² is essentially about the relationship between energy (E) and mass (m). The 'c' represents the speed of light, which is a constant. This equation tells us that energy and mass are interchangeable - a small amount of mass can be converted into a vast amount of energy, because the speed of light squared is a very large number. It's like saying mass is just very concentrated energy!
    """)

user_input = st.text_input("Your response:")
if st.button("Send", key="send_button"):
    st.write("Sending your message...")

st.markdown("---")
st.markdown("© 2023 CelebrityChat AI. All rights reserved.")