import os
from dotenv import load_dotenv

import streamlit as st
from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain, SimpleSequentialChain

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

script_template = PromptTemplate(
    input_variables=['title'],
    template='write me a youtube video script based on this title TITLE: {title}'
)

#LLMs
llm = OpenAI(temperature=0.9)
title_chain = LLMChain(llm=llm, prompt=title_template, verbose=True)
script_chain = LLMChain(llm=llm, prompt=script_template, verbose=True)
sequential_chain = SimpleSequentialChain(chains=[title_chain, script_chain])

# Show stuff to the screen if there is one
if prompt:
    response = sequential_chain.run(prompt)
    # render back to streamlit
    st.write(response)