# Q&A Chatbot
#from langchain.llms import OpenAI

from dotenv import load_dotenv # type: ignore

load_dotenv()  # take environment variables from .env.

import streamlit as st # type: ignore
import os
import pathlib
import textwrap

import google.generativeai as genai # type: ignore

from IPython.display import display # type: ignore
from IPython.display import Markdown # type: ignore


os.getenv("GOOGLE_API_KEY")
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

## Function to load OpenAI model and get response
model = genai.GenerativeModel('gemini-pro')
chat = model.start_chat(history=[])
def get_gemini_response(question):
    
    response =chat.send_message(question,stream=True)
    return response

##initialize our streamlit app

st.set_page_config(page_title="Q&A Demo")

st.header("Gemini Application")

input=st.text_input("Input: ",key="input")


submit=st.button("Ask the question")

## If ask button is clicked

if submit:
    
    response=get_gemini_response(input)
    st.subheader("The Response is")
    for chunk in response:
        print(st.write(chunk.text))
        print("_"*80)
    
    st.write(chat.history)