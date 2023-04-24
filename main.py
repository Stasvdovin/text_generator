from transformers import pipeline
import streamlit as st


@st.cache_data
def load():
    return pipeline("text-generation", model="openai-gpt")


text_generator = load()

st.title("Text generation application")
enter_text = st.text_input("Enter the text", value="")


def text_load(enter_text):
    return text_generator(enter_text, max_length=50, num_return_sequences=1)


if st.button("Output"):
    result = text_load(enter_text)
    st.success(result)
