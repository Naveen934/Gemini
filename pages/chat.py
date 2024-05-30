from dotenv import load_dotenv
import streamlit as st
import google.generativeai as genai
load_dotenv()  # take environment variables from .env.

## Function to load OpenAI model and get respones
model = genai.GenerativeModel('gemini-pro')
chat = model.start_chat(history=[])

def get_gemini_response(question):    
    response =chat.send_message(question,stream=True)
    return response

st.set_page_config(page_title="Chat Demo")
st.header("Gemini Application2")
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
