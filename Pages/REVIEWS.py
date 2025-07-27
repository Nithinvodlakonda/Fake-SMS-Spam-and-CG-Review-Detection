import joblib
import streamlit as st

# Load models
vectorizer = joblib.load('tfidf_vectorizer_reviews.pkl')
model = joblib.load('reviews_fake_detection_model.pkl')
from cleaning import clean_text
# Custom CSS for modern UI
st.markdown("""
    <style>
    body, .main {
        background: linear-gradient(135deg, #e0eafc 0%, #cfdef3 100%);
    }
    .stTextArea textarea {
        background: #f9fafc;
        border-radius: 12px;
        font-size: 1.15em;
        padding: 14px;
        border: 1px solid #b3c6e0;
        box-shadow: 0 2px 8px #e3eafc;
    }
    .stButton button {
        background: linear-gradient(90deg, #0072ff 0%, #00c6ff 100%);
        color: white;
        border-radius: 12px;
        font-size: 1.15em;
        padding: 10px 32px;
        margin: 10px 0;
        border: none;
        box-shadow: 0 2px 8px #b3c6e0;
        transition: background 0.3s;
    }
    .stButton button:hover {
        background: linear-gradient(90deg, #005bb5 0%, #0072ff 100%);
    }
    .result-box {
        background: #fff;
        border-radius: 12px;
        box-shadow: 0 2px 12px #e3eafc;
        padding: 24px;
        margin-top: 16px;
        font-size: 1.15em;
        text-align: center;
    }
    .stMarkdown h1, .stMarkdown h2 {
        color: #0072ff;
        font-weight: 800;
        letter-spacing: 1px;
    }
    </style>
""", unsafe_allow_html=True)

# Sidebar
with st.sidebar:
    st.image("https://img.icons8.com/color/96/spy.png", width=80)
    st.header("Review Detector")
    st.markdown("""
        <div style='font-size:1.1em;'>
        Welcome to the <b>Review Fake Detection</b> app!<br>
        <ul>
        <li>Paste your review text</li>
        <li>Click <b>Detect</b></li>
        <li>Get instant authenticity feedback</li>
        </ul>
        </div>
    """, unsafe_allow_html=True)


# Main UI
st.markdown("<h1 style='text-align:center;'>🕵️‍♂️ Review Authenticity Detector</h1>", unsafe_allow_html=True)
st.markdown("<h2 style='text-align:center; color:#00c6ff;'>Is your review real or Computer generated?</h2>", unsafe_allow_html=True)

with st.expander("💡 Example Reviews", expanded=False):
    st.markdown("""
    - *This product is acceptable.*
    - *Buy now! Best deal ever. Limited time offer, don't miss out!*
    - *I received the item quickly and it works as described. Satisfied with my purchase.*
    """)

input_text = st.text_area("📝 Enter Review Text here:", height=120)

col1, col2 = st.columns([2,1])
with col1:
    detect = st.button("🔍 Detect Review")
with col2:
    back = st.button("🔙 Back to Home")

if detect:
    if input_text.strip() == "":
        st.warning("Please enter a Review.")
    else:
        cleaned_text = clean_text(input_text)
        transformed_text = vectorizer.transform([cleaned_text])
        prediction = model.predict(transformed_text)[0]
        if prediction == 1:
            st.markdown(
                "<div class='result-box' style='border-left:8px solid #00c853;'>"
                "<span style='font-size:2em;'>✅</span><br>"
                "<b>This review appears to be <span style='color:#00c853;'>human-written</span> and authentic.</b>"
                "</div>", unsafe_allow_html=True)
        else:
            st.markdown(
                "<div class='result-box' style='border-left:8px solid #ff5252;'>"
                "<span style='font-size:2em;'>⚠️</span><br>"
                "<b>This review appears to be <span style='color:#ff5252;'>computer-generated</span> or fake.</b>"
                "</div>", unsafe_allow_html=True)

if back:
    st.session_state['page'] = 'home'
    st.experimental_rerun()

# Footer
st.markdown("""
    <hr>
    <center>
    <small>
    &copy; 2024 Review Detector | Powered by Streamlit & AI
    </small>
    </center>
""", unsafe_allow_html=True)