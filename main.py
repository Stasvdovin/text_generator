from transformers import pipeline
import streamlit as st


@st.cache_resource
def load():
    return pipeline("text-generation", model="openai-gpt")


text_generator = load()

st.title("Text generation application")
enter_text = st.text_input("Enter the text in English", value="")
length_text = st.slider("Text length", 10, 100, 30)
iteration_text = st.slider("How many iterations", 1, 3, 1)


def text_load(enter_text):
    return text_generator(
        enter_text, max_length=length_text, num_return_sequences=iteration_text
    )


if st.button("Output"):
    output_text = text_load(enter_text)
    st.success(output_text)
