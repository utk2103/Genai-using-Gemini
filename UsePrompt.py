import google.generativeai as genai


#whichever model being used
model = genai.GenerativeModel("gemini-1.5-pro-latest")

prompt = input("Enter the prompt")

# Generate content
response = model.generate_content(prompt)

# Print the generated content

print(response.text)

