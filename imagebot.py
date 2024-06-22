from dotenv import load_dotenv
load_dotenv()                                                                                                       # Load all the environment variables

import streamlit as st
import os
import google.generativeai as genai

from PIL import Image

genai.configure(api_key = os.getenv("GOOGLE_API_KEY"))
model = genai.GenerativeModel("gemini-pro-vision")

#Function to load Gemini Pro model and get response
def get_gemini_response(input, image):
    if input != "":
        response = model.generate_content([input, image])
    else:
        response = model.generate_content(image)
    return response.text

#Configure the streamlit app
st.set_page_config(page_title = "Image Chatbot")
st.header("My Chatbot")

input = st.text_input("Input Prompt: ", key = "input")

uploaded_file = st.file_uploader("Upload an image...", type=["jpg", "jpeg", "png"])
image = ""
if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption = "Uploaded Image", use_column_width = True)

submit = st.button("Know about the image!")

# If submit is clicked
if submit:
    response = get_gemini_response(input,image)
    st.subheader("Reply from AI:")
    st.write(response)