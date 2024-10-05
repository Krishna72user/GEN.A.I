"""
Install the Google AI Python SDK

$ pip install google-generativeai
"""

from gen1_key import API_key
import google.generativeai as genai
# Create a file named gen1_key and set your api key as a variable API_key
genai.configure(api_key=API_key)


# Create the model
generation_config = {
  "temperature": 1,
  "top_p": 0.95,
  "top_k": 64,
  "max_output_tokens": 8192,
  "response_mime_type": "text/plain",
}

model = genai.GenerativeModel(
  model_name="gemini-1.5-flash",
  generation_config=generation_config,
  # safety_settings = Adjust safety settings
  # See https://ai.google.dev/gemini-api/docs/safety-settings
)

chat_session = model.start_chat(
  history=[
  ]
)

def query(q):
    response = chat_session.send_message(q)
    
    return response.text.replace("*","")
