import os
import openai #pip install openai
import datetime
import urllib.request

openai.api_key = os.getenv("OPENAI_API_KEY")
print("Greetings!")
print("I am Van Gogh! And I am a professional painter!")
user_prompt = input("Please. Tell me. What would you like me to paint today?\n")

response = openai.Image.create(prompt = user_prompt, n = 1, size = "512x512")

image_url = response['data'][0]
print(image_url)

file_name = "image" + datetime.now().strftime('%Y-%m-%d-%H-%M-%S') + ".png"
urllib.request.urlretrieve(image_url,file_name)