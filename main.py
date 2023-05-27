#import functions / may be not everything needed
import os
import openai
from gpt_functions import generate_response, generate_image, print_help, play_music
import requests
import urllib.request
import shutil
from io import BytesIO
from PIL import Image
from datetime import datetime
from conversation_history import log_conversation

api_key_path = "./Api_keys/api_key_openai.txt"

with open(api_key_path, 'r') as f:
    openai_api_key = f.read().strip()

openai.api_key = openai_api_key

image_dir = "./Jarvis_Memory/images"
if not os.path.exists(image_dir):
    os.makedirs(image_dir)

conversation_history = ""
prompt = "Hello, how are you today?"

response = generate_response(prompt, conversation_history)
message = response.strip()
print("Jarvis: " + message)
conversation_history += f"\nFakecrash: {prompt}\nJarvis: {message}"

log_conversation(prompt, message, name="Fakecrash")

while True:
    user_input = input("Fakecrash: ")
    conversation_history += f"\nFakecrash: {user_input}"

    if user_input.lower() == "help":
        print_help()
        continue

    elif "generate image:" in user_input.lower():
        image_prompt = user_input.replace("generate image:", "").strip()
        image_url = generate_image(image_prompt)
        print("Generated image URL:", image_url)
        now = datetime.now()
        date_time = now.strftime("%Y-%m-%d_%H-%M-%S")
        image_filename = f"{date_time}.png"
        image_path = os.path.join(image_dir, image_filename)
        urllib.request.urlretrieve(image_url, image_path)
        conversation_history += f"\nJarvis: Generated image URL: {image_url}"
        log_conversation(user_input, f"Generated image URL: {image_url}", name="Fakecrash")
        continue

    elif "play:" in user_input.lower():
        song = user_input.lower().replace("play", "").strip()
        play_music(song)
        continue

    elif "exit" or "quit" in user_input.lower():
        exit()

    else:
        response = generate_response(user_input, conversation_history)
        message = response.strip()

        print("Fakecrash: " + user_input)
        print("Jarvis: " + message)
        conversation_history += f"\nJarvis: {message}"
        log_conversation(user_input, message, name="Fakecrash")

