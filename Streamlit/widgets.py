import streamlit as st
import pandas as pd

st.title("Streamlit text input")

## Input

name = st.text_input("Enter your name:")

if name:
    st.write(f"Hello, {name}")

## Slider

age = st.slider("Select your age: ", 0, 100, 19)
st.write(f"Your age is {age}")

## SelectBox

options = ['Python', 'Javascript', 'Java', 'C', 'C++']
choice = st.selectbox("Selectyour choice", options)
st.write(f"You Selected: {choice}")

## File Uploader

uploaded_file = st.file_uploader("Choose a CSV file", type='csv')
if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    st.write(df)
