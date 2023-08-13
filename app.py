import os
from dotenv import load_dotenv

import streamlit as st
from langchain.llms import OpenAI

load_dotenv()
OPENAI_API_KEY = os.getenv('OPENAI_API_KEY') 

# App framework
st.title('🦜️🔗 YouTube GPT Creator')
prompt = st.text_input('Enter your prompt here')

#LLMs
llm = OpenAI(temperature=0.9)

# Show stuff to the screen if there is one
if prompt:
    response = llm(prompt)
    # render back to streamlit
    st.write(response)