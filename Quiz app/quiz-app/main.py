import streamlit as st
import random

st.title(" 📂 Quiz Application")

# List of questions
Questions = [
    {
        "question": "What is the output of the following code?\n\nprint(type([]))",
        "options": ["<class 'list'>", "<class 'tuple'>", "<class 'dict'>", "<class 'set'>"],
        "answer": "<class 'list'>"
    },
    {
        "question": "Which keyword is used to define a function in Python?",
        "options": ["def", "function", "define", "lambda"],
        "answer": "def"
    },
    {
        "question": "What will be the output of the following code?\n\nprint(bool('False'))",
        "options": ["True", "False", "Error", "None"],
        "answer": "True"
    },
    {
        "question": "Which of the following data types is immutable in Python?",
        "options": ["List", "Dictionary", "Tuple", "Set"],
        "answer": "Tuple"
    },
    {
        "question": "How do you create an empty set in Python?",
        "options": ["{}", "set()", "[]", "set[]"],
        "answer": "set()"
    },
    {
        "question": "Which operator is used to compare two values in Python?",
        "options": ["=", "==", "!=", "<>"],
        "answer": "=="
    },
    {
        "question": "What is the output of 3 * 'Hello'?",
        "options": ["HelloHelloHello", "Hello * 3", "Error", "Hello3"],
        "answer": "HelloHelloHello"
    },
    {
        "question": "Which of the following is used for single-line comments in Python?",
        "options": ["//", "#", "/* */", "--"],
        "answer": "#"
    },
    {
        "question": "Which module in Python is used for mathematical operations?",
        "options": ["math", "random", "os", "sys"],
        "answer": "math"
    },
    {
        "question": "Which function is used to get input from the user in Python?",
        "options": ["input()", "get()", "read()", "scan()"],
        "answer": "input()"
    },
    {
        "question": "What is the output of 2 ** 3?",
        "options": ["6", "8", "9", "16"],
        "answer": "8"
    },
    {
        "question": "Which loop is used when the number of iterations is not known in advance?",
        "options": ["for", "while", "do-while", "foreach"],
        "answer": "while"
    },
    {
        "question": "Which function is used to find the length of a list in Python?",
        "options": ["size()", "len()", "count()", "length()"],
        "answer": "len()"
    },
    {
        "question": "Which keyword is used to exit a loop prematurely in Python?",
        "options": ["return", "exit", "break", "stop"],
        "answer": "break"
    },
    {
        "question": "Which of the following is a valid variable name in Python?",
        "options": ["2var", "_var", "var-name", "class"],
        "answer": "_var"
    },
    {
        "question": "How do you open a file in Python for reading?",
        "options": ["open('file.txt', 'r')", "open('file.txt', 'w')", "open('file.txt', 'a')", "open('file.txt', 'rb')"],
        "answer": "open('file.txt', 'r')"
    },
    {
        "question": "Which method is used to remove an item from a list by value?",
        "options": ["pop()", "remove()", "del", "discard()"],
        "answer": "remove()"
    },
    {
        "question": "What will be the output of the following code?\n\nprint(5 // 2)",
        "options": ["2.5", "2", "3", "Error"],
        "answer": "2"
    },
    {
        "question": "Which keyword is used to handle exceptions in Python?",
        "options": ["catch", "try", "except", "throw"],
        "answer": "except"
    },
    {
        "question": "Which data type is used to store a sequence of characters?",
        "options": ["int", "str", "list", "tuple"],
        "answer": "str"
    },
    {
        "question": "Which of the following is not a built-in data type in Python?",
        "options": ["int", "str", "boolean", "tuple"],
        "answer": "boolean"
    },
    {
        "question": "Which function is used to convert a string to an integer?",
        "options": ["int()", "float()", "str()", "chr()"],
        "answer": "int()"
    },
    {
        "question": "Which function is used to generate a random number in Python?",
        "options": ["random.random()", "rand()", "randomize()", "generate()"],
        "answer": "random.random()"
    },
    {
        "question": "What does the 'pass' statement do in Python?",
        "options": ["Stops the program", "Does nothing", "Continues the loop", "Skips an iteration"],
        "answer": "Does nothing"
    },
    {
        "question": "What will be the output of bool([])?",
        "options": ["True", "False", "Error", "None"],
        "answer": "False"
    },
    {
        "question": "Which keyword is used to define a class in Python?",
        "options": ["class", "define", "function", "object"],
        "answer": "class"
    },
    {
        "question": "Which function is used to check the type of a variable?",
        "options": ["typeof()", "checktype()", "type()", "isinstance()"],
        "answer": "type()"
    },
    {
        "question": "Which symbol is used for single-line string literals in Python?",
        "options": ["'", "\"", "'''", "#"],
        "answer": "\""
    },
    {
        "question": "Which keyword is used to define an anonymous function in Python?",
        "options": ["def", "lambda", "anon", "function"],
        "answer": "lambda"
    },
    {
        "question": "Which method is used to remove whitespace from both sides of a string?",
        "options": ["strip()", "trim()", "remove()", "cut()"],
        "answer": "strip()"
    },
    {
        "question": "Which operator is used to concatenate two strings in Python?",
        "options": ["+", "-", "*", "&"],
        "answer": "+"
    },
    {
        "question": "Which data type does not allow duplicate values?",
        "options": ["List", "Tuple", "Set", "Dictionary"],
        "answer": "Set"
    },
    {
        "question": "What will be the output of bool(0)?",
        "options": ["True", "False", "Error", "None"],
        "answer": "False"
    },
    {
        "question": "Which function is used to get the ASCII value of a character?",
        "options": ["ord()", "ascii()", "char()", "chr()"],
        "answer": "ord()"
    }
]


# Initialize session state variables
if "current_question" not in st.session_state:
    st.session_state.current_question = random.choice(Questions)
if "answer_shown" not in st.session_state:
    st.session_state.answer_shown = False
if "feedback" not in st.session_state:
    st.session_state.feedback = ""

# Display the current question
question = st.session_state.current_question
st.subheader(question["question"])

# Dropdown for answer selection (use a default value from options to avoid None issues)
selected_option = st.selectbox("Options", question["options"], key="selected_option", index=0)

# Handle answer submission
if st.button("Submit") and not st.session_state.answer_shown:
    if selected_option == question["answer"]:
        st.session_state.feedback = "✅ Correct Answer!"
    else:
        st.session_state.feedback = f"❌ Incorrect! The correct answer is: {question['answer']}"
    
    st.session_state.answer_shown = True  # Store that answer has been shown
    st.rerun()  # Force refresh to update feedback

# Show feedback after submission
if st.session_state.answer_shown:
    st.write(st.session_state.feedback)

    # Button to load the next question
    if st.button("Next Question"):
        st.session_state.current_question = random.choice(Questions)
        st.session_state.answer_shown = False  # Reset feedback state
        st.session_state.feedback = ""  # Clear feedback
        st.rerun()  # Refresh for a new question
