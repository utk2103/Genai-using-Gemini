import google.generativeai as genai
from PIL import Image


print("Available models")
for m in genai.list_models():
    if 'generateContent' in m.supported_generation_methods:
        print(m.name)


# load the image from a file

image = Image.open("images/")
image.show()

 # model object       
model = genai.GenerativeModel("gemini-1.5-pro-latest")

prompt = input("Enter the prompt")

# Generate content
response = model.generate_content(prompt, stream = True)

# Print the generated content in chunk

print(response.text)
for chunk in response:
    print(chunk.text)
    print("_"*50)
