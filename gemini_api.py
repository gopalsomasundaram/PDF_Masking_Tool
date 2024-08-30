import os
import google.generativeai as genai


def initialize_model():
    api_key = os.getenv("API_KEY")
    if not api_key:
        raise ValueError("API key not found. Please set the API_KEY environment variable.")

    genai.configure(api_key=api_key)
    model = genai.GenerativeModel('gemini-1.5-flash')
    return model


def mask_sensitive_information(model, text):
    prompt = "from the information above i need you to identify data like the names of any person or institution(such as college names, clinic names, hospital names govt. bodies etc), phone numbers and email addresses. ONLY output a comma separated string with the data youve extracted without the headers. Also dont include words that have an apostrophe s at the end of them"
    response = model.generate_content([prompt, text])
    return response


# Example function to integrate initialization and masking
def mask_text(text):
    model = initialize_model()
    masked_text = mask_sensitive_information(model, text)
    return masked_text
