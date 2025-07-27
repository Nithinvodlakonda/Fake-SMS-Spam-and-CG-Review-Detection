import streamlit as st
import joblib

model = joblib.load("spam_classifier_model.pkl")
vectorizer = joblib.load("tfidf_vectorizer.pkl")
from cleaning import clean_SMS
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
    st.image("https://img.icons8.com/color/96/secured-letter.png", width=80)
    st.header("SMS Spam Classifier")
    st.markdown("""
        <div style='font-size:1.1em;'>
        Welcome to the <b>SMS Spam Classifier</b> app!<br>
        <ul>
        <li>Paste your SMS message</li>
        <li>Click <b>Predict</b></li>
        <li>Get instant spam detection</li>
        </ul>
        </div>
    """, unsafe_allow_html=True)


# Main UI
st.markdown("<h1 style='text-align:center;'>📩 SMS Spam Detector</h1>", unsafe_allow_html=True)
st.markdown("<h2 style='text-align:center; color:#00c6ff;'>Is your message SPAM or NOT?</h2>", unsafe_allow_html=True)

with st.expander("💡 Example Messages", expanded=False):
    st.markdown("""
    - *Hey John, are you free for a quick chat later today?*
    - *WINNER! You've won a free iPhone 15! Claim now: bit.ly/free-prize-xyz*
    - *URGENT: Your bank account has been suspended. Verify at secure-bank-login.com/update.*
    """)

user_input = st.text_area("Enter the message to classify 👇:", height=120)

col1, col2 = st.columns([2,1])
with col1:
    predict = st.button("🤔 Predict SMS")
with col2:
    back = st.button("🔙 Back to Home")

if predict:
    if user_input.strip() == "":
        st.warning("Please enter a message.")
    else:
        cleaned_text = clean_SMS(user_input)
        transformed_text = vectorizer.transform([cleaned_text])
        prediction = model.predict(transformed_text)[0]
        if prediction == 1:
            st.markdown(
                "<div class='result-box' style='border-left:8px solid #ff5252;'>"
                "<span style='font-size:2em;'>🚫</span><br>"
                "<b>This message is <span style='color:#ff5252;'>SPAM</span>.</b>"
                "</div>", unsafe_allow_html=True)
        else:
            st.markdown(
                "<div class='result-box' style='border-left:8px solid #00c853;'>"
                "<span style='font-size:2em;'>✅</span><br>"
                "<b>This message is <span style='color:#00c853;'>NOT SPAM</span>.</b>"
                "</div>", unsafe_allow_html=True)

if back:
    st.session_state['page'] = 'home'
    st.experimental_rerun()

# Footer
st.markdown("""
    <hr>
    <center>
    <small>
    &copy; 2024 SMS Spam Classifier | Powered by Streamlit & AI
    </small>
    </center>
""", unsafe_allow_html=True)