import os
from dotenv import load_dotenv

import streamlit as st
from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain

load_dotenv()
OPENAI_API_KEY = os.getenv('OPENAI_API_KEY') 

# App framework
st.title('🦜️🔗 YouTube GPT Creator')
prompt = st.text_input('Enter your prompt here')

# Prompt templates
title_template = PromptTemplate(
    input_variables=['topic'],
    template='write me a youtube video title about deep {topic}'
)

#LLMs
llm = OpenAI(temperature=0.9)
title_chain = LLMChain(llm=llm, prompt=title_template, verbose=True)

# Show stuff to the screen if there is one
if prompt:
    response = title_chain.run(prompt)
    # render back to streamlit
    st.write(response)