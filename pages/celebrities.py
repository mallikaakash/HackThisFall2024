import streamlit as st

# Page config
st.set_page_config(
    page_title="TimeTalk AI | Celebrities",
    page_icon="👥",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Custom CSS
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Playfair+Display:wght@400;700&family=Inter:wght@400;500;600&display=swap');
    .stApp {
            background-color: white;
            }
    .celebrity-card {
        background-color: white;
        padding: 1.5rem;
        border-radius: 1rem;
        border: 1px solid #eee;
        transition: all 0.3s ease;
    }
    
    .celebrity-card:hover {
        transform: translateY(-5px);
        box-shadow: 0 10px 20px rgba(0,0,0,0.1);
    }
    
    .category-title {
        font-family: 'Playfair Display', serif;
        font-size: 2rem;
        color: #2C3E50;
        margin-bottom: 1.5rem;
    }
</style>
""", unsafe_allow_html=True)

st.title("Choose Your Conversation Partner")
st.write("Select from our curated list of historical figures and modern celebrities")

# Historical Figures
st.markdown("## Historical Figures")
col1, col2, col3, col4 = st.columns(4)

historical_figures = [
    {
        "name": "Leonardo da Vinci",
        "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/c/cb/Francesco_Melzi_-_Portrait_of_Leonardo_-_WGA14795.jpg/800px-Francesco_Melzi_-_Portrait_of_Leonardo_-_WGA14795.jpg",
        "description": "Renaissance polymath, artist, inventor",
        "era": "1452-1519"
    },
    {
        "name": "Marie Curie",
        "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/7/7e/Marie_Curie_c1920.jpg/800px-Marie_Curie_c1920.jpg",
        "description": "Physicist, chemist, pioneer in radioactivity",
        "era": "1867-1934"
    },
    {
        "name": "William Shakespeare",
        "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/a/a2/Shakespeare.jpg/800px-Shakespeare.jpg",
        "description": "Playwright, poet, actor",
        "era": "1564-1616"
    },
    {
        "name": "Cleopatra",
        "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/3/3e/Kleopatra-VII.-Altes-Museum-Berlin1.jpg/800px-Kleopatra-VII.-Altes-Museum-Berlin1.jpg",
        "description": "Last active ruler of the Ptolemaic Kingdom",
        "era": "69-30 BC"
    }
]

for i, figure in enumerate(historical_figures):
    with eval(f"col{i+1}"):
        st.markdown(f"""
        <div class="celebrity-card">
            <img src="{figure['image']}" style="width: 100%; border-radius: 0.5rem;">
            <h3>{figure['name']}</h3>
            <p>{figure['description']}</p>
            <p><small>{figure['era']}</small></p>
        </div>
        """, unsafe_allow_html=True)
        if st.button(f"Chat with {figure['name'].split()[-1]}", key=f"hist_{i}"):
            st.session_state['selected_celebrity'] = figure['name']
            st.switch_page("pages/chat.py")

# Modern Icons
st.write("")
st.markdown("## Modern Icons")
col1, col2, col3, col4 = st.columns(4)

modern_icons = [
    {
        "name": "Albert Einstein",
        "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/3/3e/Einstein_1921_by_F_Schmutzer_-_restoration.jpg/800px-Einstein_1921_by_F_Schmutzer_-_restoration.jpg",
        "description": "Theoretical physicist, Nobel laureate",
        "era": "1879-1955"
    },
    {
        "name": "Frida Kahlo",
        "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/4/4e/Frida_Kahlo%2C_by_Guillermo_Kahlo.jpg/800px-Frida_Kahlo%2C_by_Guillermo_Kahlo.jpg",
        "description": "Artist, feminist icon",
        "era": "1907-1954"
    },
    {
        "name": "Martin Luther King Jr.",
        "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/0/05/Martin_Luther_King%2C_Jr..jpg/800px-Martin_Luther_King%2C_Jr..jpg",
        "description": "Civil rights leader, Nobel Peace Prize laureate",
        "era": "1929-1968"
    },
    {
        "name": "Mother Teresa",
        "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/d/d6/Mother_Teresa_1.jpg/800px-Mother_Teresa_1.jpg",
        "description": "Religious sister, missionary",
        "era": "1910-1997"
    }
]

for i, icon in enumerate(modern_icons):
    with eval(f"col{i+1}"):
        st.markdown(f"""
        <div class="celebrity-card">
            <img src="{icon['image']}" style="width: 100%; border-radius: 0.5rem;">
            <h3>{icon['name']}</h3>
            <p>{icon['description']}</p>
            <p><small>{icon['era']}</small></p>
        </div>
        """, unsafe_allow_html=True)
        if st.button(f"Chat with {icon['name'].split()[-1]}", key=f"modern_{i}"):
            st.session_state['selected_celebrity'] = icon['name']
            st.switch_page("pages/chat.py")