from dotenv import load_dotenv
load_dotenv() ## loading all the environment variables

import streamlit as st
import os
import google.generativeai as genai

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

## function to load Gemini Pro model and get repsonses
model=genai.GenerativeModel("gemini-pro") 
chat = model.start_chat(history=[])
def get_gemini_response(question):
    
    response=chat.send_message(question,stream=True)
    return response
# tên, tiêu đề app

st.set_page_config(page_title="Q&A AI")

st.header("Gemini of HanBao")
st.write("Chào mừng đến với Gemini của HanBao")

# Khởi tạo trạng thái phiên cho lịch sử trò chuyện nếu nó không tồn tại
if 'chat_history' not in st.session_state:
    st.session_state['chat_history'] = []

input=st.text_input("Xin hãy nhập vào: ",key="input")
submit=st.button("Nhập vào")

if submit and input:
    response=get_gemini_response(input)
    # Add user query and response to session state chat history
    st.session_state['chat_history'].append(("Bạn", input))
    st.subheader("Trả lời là ")
    for chunk in response:
        st.write(chunk.text)
        st.session_state['chat_history'].append(("Bot", chunk.text))
st.subheader("Lịch sử chat")
    
for role, text in st.session_state['chat_history']:
    st.write(f"{role}: {text}")
    



    

