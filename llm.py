from dotenv import load_dotenv

load_dotenv()

import os
from PIL import Image
import google.generativeai as genai

genai.configure(api_key=os.getenv('GOOGLE_API_KEY'))

model=genai.GenerativeModel('gemini-pro-vision')

input_prompts="""
                You are an expert in understanding resume. We will upload a image as resume
                and you will have to answer any question based on the uploaded image"""


def get_gemini_response(input,image,prompt):
    response=model.generate_content([input,image[0],prompt])
    return response.text


# llm.py
import mimetypes

def input_image_details(file_path):
    if file_path is not None and os.path.exists(file_path):
        with open(file_path, 'rb') as file:
            bytes_data = file.read()

        mime_type, _ = mimetypes.guess_type(file_path)

        image_parts = [
            {
                'mime_type': mime_type,
                'data': bytes_data
            }
        ]
        return image_parts
    else:
        raise FileNotFoundError('File not found at specified path')
