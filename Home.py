import streamlit as st  # Streamlit for web UI

st.set_page_config(page_title="Text Classifier", layout="centered")  # Set page title and layout


# Advanced custom CSS for glassmorphism, gradients, icons, and transitions
st.markdown("""
    <style>
        body {
            background: linear-gradient(135deg, #e0eafc 0%, #cfdef3 100%);
        }
        .main-title {
            font-size: 2.8rem;
            font-weight: 800;
            color: #1a2980;
            text-align: center;
            margin-bottom: 0.5em;
            letter-spacing: 2px;
            text-shadow: 0 2px 8px #b2bec3;
        }
        .subtitle {
            font-size: 1.3rem;
            color: #34495e;
            text-align: center;
            margin-bottom: 2em;
        }
        .glass-card {
            background: rgba(255, 255, 255, 0.35);
            box-shadow: 0 8px 32px 0 rgba(31, 38, 135, 0.37);
            backdrop-filter: blur(10px);
            -webkit-backdrop-filter: blur(10px);
            border-radius: 24px;
            border: 1px solid rgba(255, 255, 255, 0.18);
            padding: 40px 32px;
            margin: 32px auto;
            max-width: 600px;
        }
        .footer {
            position: fixed;
            left: 0;
            bottom: 0;
            width: 100%;
            background: linear-gradient(90deg, #e0eafc 0%, #cfdef3 100%);
            color: #555;
            text-align: center;
            padding: 10px 0;
            font-size: 1rem;
            border-top: 1px solid #eaeaea;
        }
        .stButton>button {
            background: linear-gradient(90deg, #2980b9 0%, #6dd5fa 100%);
            color: white;
            font-size: 1.2rem;
            font-weight: 600;
            border-radius: 12px;
            padding: 0.85em 2.2em;
            margin: 1em 0;
            border: none;
            box-shadow: 0 2px 8px #b2bec3;
            transition: background 0.3s, transform 0.2s;
        }
        .stButton>button:hover {
            background: linear-gradient(90deg, #6dd5fa 0%, #2980b9 100%);
            color: #fff;
            transform: scale(1.05);
        }
        .icon {
            font-size: 2.2rem;
            vertical-align: middle;
            margin-right: 0.5em;
        }
    </style>
""", unsafe_allow_html=True)


# Main title and subtitle with icons
st.markdown('<div class="main-title">🧠 Text Classification Hub</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">Choose what you want to analyze</div>', unsafe_allow_html=True)



# Center the buttons horizontally using Streamlit columns with spacers
spacer1, col1, col2, spacer2 = st.columns([1,2,2,1])
with col1:
    if st.button("📩 SMS Spam Detection"):
        st.switch_page("Pages/SMS.py")
with col2:
    if st.button("🛍️ Fake Review Detection"):
        st.switch_page("Pages/REVIEWS.py")



# Add a footer with links to GitHub and LinkedIn, and a fixed footer at the bottom
st.markdown("""
    <div style="text-align: center; margin-top: 2em;">
        <a href="https://github.com/Nithinvodlakonda" target="_blank" style="margin-right: 16px; text-decoration: none;">
            <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/github/github-original.svg" alt="GitHub" width="28" style="vertical-align: middle; margin-right: 6px;">
            GitHub
        </a>
        |
        <a href="https://www.linkedin.com/in/nithin-vodlakonda-86a450300" target="_blank" style="margin-left: 16px; text-decoration: none;">
            <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/linkedin/linkedin-original.svg" alt="LinkedIn" width="28" style="vertical-align: middle; margin-right: 6px;">
            LinkedIn
        </a>
    </div>
    <div class="footer">🚀 Built  by Nithin | SMS & Review Classification System using ML</div>
""", unsafe_allow_html=True)