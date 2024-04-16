import streamlit as st
import time

import google.generativeai as genai
with open('Gemini_API_Key.txt', 'r') as f:
    api_key = f.read().strip()

genai.configure(api_key=api_key)
model = genai.GenerativeModel('gemini-pro')

sys_instruction='''
        You are a code reviewer. Your job is to review code and provide feedback. You must provide a ordered list of bugs present within the code
        then the correct version of the code. As you only provide correct responses, I want to crosscheck your reponses five times. 
        
    
'''
def getReview(code):
    prompt=sys_instruction+'Instruction: Review the following code'+code
    
    response=model.generate_content(prompt)
    
    return response
    

#Title
st.title('Code Reviewer')

#User Input
st.header('User Input')
code=st.text_area('Enter your code')




#Processing the query
if code!='':
    review=getReview(code)
   
    if review.text:
        st.write(review.text)
    else:
        st.write('Try again')
    
