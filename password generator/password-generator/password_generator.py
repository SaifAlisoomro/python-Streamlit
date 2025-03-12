import streamlit as st
import random
import string

# Function to generate a password
def generate_password(length, use_digit, special_characters):
    characters = string.ascii_letters  # Includes uppercase and lowercase letters

    if use_digit:
        characters += string.digits  # Add numbers

    if special_characters:  # This should be outside the "use_digit" condition
        characters += string.punctuation  # Add special characters

    return ''.join(random.choice(characters) for _ in range(length))

# Streamlit UI components
st.title("Password Generator")
st.write("This is a simple password generator app")

length = st.slider("Length of password", min_value=4, max_value=30, value=10)
use_digit = st.checkbox("Use digits")
special_characters = st.checkbox("Use special characters")

if st.button("Generate password"):
    password = generate_password(length, use_digit, special_characters)
    st.write(f"**Generated Password:** `{password}`")

st.write("Created by: [Saifi Soomro](https://www.linkedin.com/in/saifi-soomro-7b0b3b1b4/)")
