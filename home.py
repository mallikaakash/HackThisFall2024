import streamlit as st
from streamlit_lottie import st_lottie
import requests

def load_lottieurl(url: str):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

# Page config
st.set_page_config(
    page_title="TimeTalk AI | Home",
    page_icon="🎭",
    layout="wide",
    initial_sidebar_state="collapsed",
    menu_items={
        'Get Help': None,
        'Report a bug': None,
        'About': None
    }
)

hide_streamlit_style = """
<style>
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    .stDeployButton {display: none;}
    [data-testid="stSidebar"][aria-expanded="true"]{
        visibility: hidden;
    }
    [data-testid="stSidebar"][aria-expanded="false"]{
        visibility: hidden;
    }
</style>
"""

# Custom CSS with improved typography and styling
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Playfair+Display:wght@400;700&family=Inter:wght@400;500;600&display=swap');
    /* Remove top padding/margin */
        .stApp {
            margin-top: -80px;
        }
        
        /* Remove padding from container */
        .css-1d391kg, .css-1egvi7u {
            padding-top: 0rem;
        }
        
        /* Remove whitespace at the top */
    body {
        background-color: #faf7f0;
        color: #333;
    }
    
    .main {
        padding: 0rem 5rem;
    }
    
    .stButton>button {
        color: #4A4947;
        border-radius: 50px;
        padding: 0.75rem 2rem;
        border: none;
        font-weight: 600;
        transition: all 0.3s ease;
    }
    
    .stButton>button:hover {
        background-color: #D8D2C2;
        transform: translateY(-2px);
    }
    
    .hero-text {
        font-family: 'Playfair Display', serif;
        font-size: 3.5rem;
        font-weight: 700;
        line-height: 1.2;
        color: #B17457;
    }
    
    .subtitle {
        font-family: 'Inter', sans-serif;
        font-size: 1.2rem;
        color: #4A4947;
        line-height: 1.5;
    }
    
    .feature-card {
        background-color: #fff;
        padding: 1.5rem;
        border-radius: 1rem;
        border: 1px solid #eee;
        transition: all 0.3s ease;
    }
    
    .feature-card:hover {
        transform: translateY(-5px);
        box-shadow: 0 10px 20px rgba(0,0,0,0.1);
    }
    
    .social-icons {
        display: flex;
        flex-direction: column;
        align-items: center;
        gap: 1rem;
        position: fixed;
        left: 20px;
        top: 50%;
        transform: translateY(-50%);
    }
    
    .social-icons a {
        color: #4A0E4E;
        font-size: 1.5rem;
    }
</style>
""", unsafe_allow_html=True)

# Social Icons
st.markdown("""
<div class="social-icons">
    <a href="#"><i class="fab fa-facebook-f"></i></a>
    <a href="#"><i class="fab fa-twitter"></i></a>
    <a href="#"><i class="fab fa-instagram"></i></a>
</div>
""", unsafe_allow_html=True)

# Header
st.markdown("""
<header style="display: flex; justify-content: space-between; align-items: center; padding: 1rem 0;">
    <h1 style="font-family: 'Playfair Display', serif; color: #4A4947;">TimeTalk AI</h1>
    <nav>
        <a href="#" style="color: #333; text-decoration: none; margin-left: 1rem;">Home</a>
        <a href="#" style="color: #333; text-decoration: none; margin-left: 1rem;">Celebrities</a>
        <a href="#" style="color: #4A0E4E; text-decoration: none; margin-left: 1rem;">Contact Us</a>
    </nav>
</header>
""", unsafe_allow_html=True)

# Hero Section
col1, col2 = st.columns([1, 1])

with col1:
    st.markdown('<p class="hero-text">Journey Through Time with AI Conversations</p>', unsafe_allow_html=True)
    st.markdown(
        '<p class="subtitle">Connect with history\'s greatest minds and today\'s icons through the power of artificial intelligence.</p>',
        unsafe_allow_html=True
    )
    
    st.write("")  # Spacing
    if st.button("Start Your Journey", key="start_button"):
        st.switch_page("pages/celebrities.py")

with col2:
    lottie_animation = load_lottieurl("https://assets8.lottiefiles.com/packages/lf20_M9p23l.json")
    st_lottie(lottie_animation, height=400)

# Features Section
st.write("")
st.write("")
st.markdown("## Why Choose TimeTalk AI?")

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("""
    <div class="feature-card">
        <h3 style="color: #4A0E4E;">🎯 Authentic Conversations</h3>
        <p>Experience meaningful dialogues that capture the essence of each personality's unique perspective and knowledge.</p>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="feature-card">
        <h3 style="color: #4A0E4E;">🔍 Deep Learning</h3>
        <p>Our AI is trained on extensive historical records and contemporary data to provide accurate and insightful responses.</p>
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown("""
    <div class="feature-card">
        <h3 style="color: #4A0E4E;">🌟 Endless Possibilities</h3>
        <p>From ancient philosophers to modern innovators, explore conversations that span centuries of human achievement.</p>
    </div>
    """, unsafe_allow_html=True)

# Footer
st.markdown("---")
st.markdown(
    "<p style='text-align: center; color: #666;'>© 2024 TimeTalk AI. All rights reserved.</p>",
    unsafe_allow_html=True
)