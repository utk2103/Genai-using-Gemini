import google.generativeai as genai


# List of all available models
print("Available models")
for m in genai.list_models():
    if 'generateContent' in m.supported_generation_methods:
        print(m.name)

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

