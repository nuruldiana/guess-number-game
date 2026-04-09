import streamlit as st
import random

st.set_page_config(page_title="Guess Number Game")

st.title("🎯 Guess The Number Game")

# Simpan random number
if "number" not in st.session_state:
    st.session_state.number = random.randint(1, 10)

guess = st.number_input(
    "Enter your guess (1-10)",
    min_value=1,
    max_value=10
)

if st.button("Check"):
    if guess == st.session_state.number:
        st.success("🎉 Correct! You guessed the number!")
        st.session_state.number = random.randint(1, 10)
    elif guess < st.session_state.number:
        st.warning("Too low! Try again.")
    else:
        st.warning("Too high! Try again.")