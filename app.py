import streamlit as st
from PIL import Image
import requests
import os
import json
#
image_path = "image.jpg"
image = Image.open(image_path)

st.set_page_config(page_title="Auto-Code Generator App", layout="centered")
st.image(image, caption='Auto-Code Generator')
#
# page header
st.title(f"Auto-Code Generator App")
with st.form("Extract"):
   text1 = st.text_input("Enter the texts here")
   submit = st.form_submit_button("Generate Pseudo-Code")
   #
   if submit:    
        print(text1)
        #
        with open("input.txt", "wb") as f:
            f.write(text1.encode("utf-8"))
        os.chmod("input.txt", 0o777)
        # Keyword Extraction API
        url = "https://app.aimarketplace.co/api/marketplace/models/auto-code-generator-e477b69d/predict/"
        payload={'data': open('input.txt','rb')}
        headers = {'Authorization': 'Api-Key Oda4IMK3.KXV9fQrtl624yE8zRhWtVy05s7q5PuzM','Cache-Control': 'no-cache'}

        response = requests.request("POST", url, headers=headers, files=payload)
        #
        print(response.text)
        # output header 
        st.header("Pseudo-Code Generated")
        # output results
        st.success(response.text)