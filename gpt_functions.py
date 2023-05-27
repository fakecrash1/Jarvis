import openai
from datetime import datetime
import os
import urllib.request
import pywhatkit


# API Key

api_key_path = './Api_keys/api_key_openai.txt'

# Read the API key from the text file
with open(api_key_path, 'r') as f:
    openai_api_key = f.read().strip()
openai.api_key = openai_api_key

# Define the path to the directory where the generated images will be saved
image_dir = "./Jarvis_Memory/images"
# Check if the directory exists, create it if it doesn't
if not os.path.exists(image_dir):
    os.makedirs(image_dir)


# Generate response
def generate_response(user_input, conversation_history):
    conversation_history += f"\nFakecrash: {user_input}\nJarvis: "

    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=conversation_history + user_input,
        max_tokens=320,
        n=1,
        stop=None,
        temperature=0.5,
        frequency_penalty=0.5,
        presence_penalty=0.5,
        best_of=1,
    )

    message = response.choices [0].text.strip()

    return message

# Generate image
def generate_image(image_prompt):
    image_response = openai.Image.create(
        prompt=image_prompt,
        n=1,
        size="1024x1024"
    )
    image_url = image_response['data'][0]['url']

    return image_url


# Play music
def play_music(song):
    pywhatkit.playonyt(song)

# Get help
def print_help():
    help_message = '''
    Here are some tips and commands for using the chatbot:

    1. Type your questions or statements normally, and the chatbot will respond.
    2. To generate an image, type "generate image:" followed by a description ("generate image: a beautiful sunset").
    3. Play anything from Youtube
    4. To exit the chat, type "exit" or "quit".
    
    Note: If the chatbot provides an unsatisfactory response, try rephrasing your question or statement.
    '''
    print(help_message)
