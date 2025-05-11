import streamlit as st
import google.generativeai as genai

# Set your Google API key
GOOGLE_API_KEY = "AIzaSyA6_skJD8xkXN5wCMgwTIcDzkQRdyKQVUg"
genai.configure(api_key=GOOGLE_API_KEY)

# Gemini model
model = genai.GenerativeModel("gemini-1.5-flash")

# Session state initialization
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False
if "user_email" not in st.session_state:
    st.session_state.user_email = ""
if "users" not in st.session_state:
    st.session_state.users = {}

# Registration form
def register():
    st.title("🔐 Register")
    name = st.text_input("Name")
    email = st.text_input("Email")
    password = st.text_input("Password", type="password")
    if st.button("Register"):
        if email in st.session_state.users:
            st.warning("Email already exists.")
        else:
            st.session_state.users[email] = [name, password]
            st.success("Registered successfully. Please login.")
            st.rerun()

# Login form
def login():
    st.title("🔓 Login")
    email = st.text_input("Email")
    password = st.text_input("Password", type="password")
    if st.button("Login"):
        if email in st.session_state.users and st.session_state.users[email][1] == password:
            st.success("Login successful.")
            st.session_state.logged_in = True
            st.session_state.user_email = email
            st.rerun()
        else:
            st.error("Invalid email or password.")

# Sentiment analysis
def sentiment_analysis():
    st.subheader("🧠 Sentiment Analysis")
    user_text = st.text_area("Enter your text:")
    if st.button("Analyze Sentiment"):
        response = model.generate_content(f"Give me the sentiment of this sentence: {user_text}")
        st.success(response.text)

# Language translation
def language_translation():
    st.subheader("🌐 Language Translation")
    user_text = st.text_area("Enter text to translate into Urdu:")
    if st.button("Translate"):
        response = model.generate_content(f"Give me Urdu translation of this sentence: {user_text}")
        st.success(response.text)

# Language detection
def language_detection():
    st.subheader("🔍 Language Detection")
    user_text = st.text_area("Enter text to detect language:")
    if st.button("Detect Language"):
        response = model.generate_content(f"Detect the language of this sentence: {user_text}")
        st.success(response.text)

# Logged in menu
def dashboard():
    st.title("🎯 NLP Dashboard")
    st.write(f"Welcome, {st.session_state.users[st.session_state.user_email][0]}!")
    choice = st.selectbox("Choose an option:", [
        "Sentiment Analysis",
        "Language Translation",
        "Language Detection"
    ])
    if choice == "Sentiment Analysis":
        sentiment_analysis()
    elif choice == "Language Translation":
        language_translation()
    elif choice == "Language Detection":
        language_detection()
    st.button("Logout", on_click=logout)

# Logout
def logout():
    st.session_state.logged_in = False
    st.session_state.user_email = ""
    st.rerun()

# Main app logic
def main():
    st.set_page_config(page_title="NLP App with Gemini AI", layout="centered")
    st.title("💬 Gemini NLP App")
    menu = st.sidebar.radio("Menu", ["Login", "Register"] if not st.session_state.logged_in else ["Dashboard"])
    if st.session_state.logged_in:
        dashboard()
    elif menu == "Login":
        login()
    elif menu == "Register":
        register()

if __name__ == "__main__":
    main()