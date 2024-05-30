from dotenv import load_dotenv
import streamlit as st
import google.generativeai as genai


load_dotenv()  # take environment variables from .env.

import os
#os.environ['GOOGLE_API_KEY']='AIzaSyBL-0DayM_27UEiH6GXj8tzcB9Pxy9Ls7M'
genai.configure(api_key=os.environ['GOOGLE_API_KEY'])
#os.environ["GOOGLE_API_KEY"]=os.getenv("GOOGLE_API_KEY")


def get_gemini_response(question):
    model = genai.GenerativeModel('gemini-pro')
    response = model.generate_content(question)
    return response.text

st.set_page_config(page_title="Q&A intro Demo")
st.header("Gemini Application1")
input=st.text_input("Input: ",key="input")
submit=st.button("Ask the question")

if submit:    
    response=get_gemini_response(input)
    st.subheader("The Response is")
    st.write(response)
