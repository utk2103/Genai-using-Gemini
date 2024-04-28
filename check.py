from urlib import response
import google.generativeai as genai

model = genai.GenerativeModel("gemini-pro")

response = model.generate_content("Say hi to me!")

print(response.text)