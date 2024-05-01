import google.generativeai as genai
from google.generativeai.types import HarmCategory, HarmBlockThreshold
from PIL import Image


# load the image from a file

image = Image.open("images/")
image.show()

 # model object       
model = genai.GenerativeModel("gemini-1.5-pro-latest")

prompt = input("Enter the prompt")

# Generate content
response = model.generate_content(image)

# Print the generated content based on the image

print('Generated content based on image')
print(response.text)

response = model.generate_content[
            """<write whatever the promot you want to>""",
            image
],
stream = True,
safety_settings =[
    genai.types.HarmCategory.HARM_CATEGGORY_HATE_SPEECH: genai.types.HarmBlockThreshold.Block_NONE,
    genai.types.HarmCategory.HARM_CATEGGORY_HARASSMENT: genai.types.HarmBlockThreshold.Block_NONE
]

response.resolve()