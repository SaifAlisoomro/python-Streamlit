import re
import streamlit as st

# ✅ Configure Streamlit Page
st.set_page_config(page_title="Password Strength Checker", page_icon="🗝️", layout="centered")

# ✅ Apply custom CSS for better styling
st.markdown("""
    <style>
        .stTextInput > div > div > input {
            width: 100% !important;
            text-align: center;
            font-size: 16px;
            padding: 10px;
            border-radius: 10px;
        }
        .stButton > button {
            width: 50%;
            background-color: #4caf50;
            color: white;
            font-size: 18px;
            border-radius: 10px;
            padding: 10px;
        }
        .stButton > button:hover {
            background-color: #45a049;
        }
    </style>
""", unsafe_allow_html=True)

# ✅ App Title
st.title("🔐 Password Strength Checker")
st.write("Enter your password below to check its strength and get improvement suggestions.")

# ✅ Function to check password strength
def password_strength(password):
    if len(password) < 8:
        return "🟥 Weak"
    elif len(password) < 12:
        return "🟨 Medium"
    elif re.search("[a-z]", password) and re.search("[A-Z]", password) and re.search("[0-9]", password) and re.search("[!@#$%^&*]", password):
        return "🟩 Strong"
    else:
        return "🟨 Medium"

# ✅ Function to provide suggestions
def password_suggestions(password):
    suggestions = []
    if len(password) < 8:
        suggestions.append("🔹 Use at least 8 characters.")
    if not re.search("[a-z]", password):
        suggestions.append("🔹 Add a lowercase letter (a-z).")
    if not re.search("[A-Z]", password):
        suggestions.append("🔹 Include an uppercase letter (A-Z).")
    if not re.search("[0-9]", password):
        suggestions.append("🔹 Add a number (0-9).")
    if not re.search("[!@#$%^&*]", password):
        suggestions.append("🔹 Use at least one special character (!@#$%^&*).")
    return suggestions

# ✅ Input field for password
password = st.text_input("🔑 Enter your password", type="password")

# ✅ Process password and display results
if password:
    strength = password_strength(password)
    suggestions = password_suggestions(password)

    # ✅ Show strength result
    st.subheader(f"Strength: {strength}")

    # ✅ Show improvement suggestions if needed
    if suggestions:
        st.warning("Suggestions to improve your password:")
        for suggestion in suggestions:
            st.write(f"- {suggestion}")
    else:
        st.success("Your password is very strong! 🎉")

# ✅ Footer
st.write("🔹 Created by [Saifi Soomro](https://www.linkedin.com/in/saifi-soomro-7b0b3b1b4/)")

