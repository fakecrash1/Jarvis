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
from users import *
from search import *
# from models import *

selected_user = select_user()

api_key_path = "./Api_keys/api_key_openai.txt"

with open(api_key_path, 'r') as f:
    openai_api_key = f.read().strip()

openai.api_key = openai_api_key

image_dir = "./Jarvis_Memory/images"
if not os.path.exists(image_dir):
    os.makedirs(image_dir)

conversation_history = ""
prompt = "You are JARVIS (Just A Rather Very Intelligent System), respectively the household assistance of the "+selected_user.name+" family and designed by Mr. "+selected_user.name+" (as Jarvis, you call the user as Sir.). You are a helpful Ai assistant and your porpuse is to make the human life better, with helpful answers. If you understand your work, start the conversation with: 'Welcome back Sir, how can I help you today'?"

message, conversation_history = generate_response(prompt, conversation_history)

print(message)
log_conversation(prompt, message, selected_user.name)

while True:
    user_input = input(selected_user.name+": ")

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
        log_conversation(user_input, f"Generated image URL: {image_url}", selected_user.name)
        continue

    elif "play:" in user_input.lower():
        song = user_input.lower().replace("play", "").strip()
        play_music(song)
        continue

    elif user_input.lower().startswith("search:"):
        search_term = user_input.split("search:", 1)[1].strip()
        
        # Reading the Google API key and CSE ID
        with open("./Api_keys/api_key_google.txt", 'r') as f:
            google_api_key = f.read().strip()
        with open("./Api_keys/google_CSE.txt", 'r') as f:
            google_cse_id = f.read().split("cx=", 1)[1].split("\">")[0]

        search_results = google_search(search_term, google_api_key, google_cse_id)
        
        # Displaying the first search result
        first_result = search_results["items"][0]
        print("Jarvis: Here's what I found -", first_result["title"], first_result["link"])
        continue

    elif "exit" == user_input.lower() or "quit" == user_input.lower():
        exit()

    else:
        message, conversation_history = generate_response(user_input, conversation_history)
        print("Jarvis: "+message)
        log_conversation(user_input, message, selected_user.name)
