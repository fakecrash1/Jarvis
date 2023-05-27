import os
from datetime import datetime

def log_conversation(user_input, jarvis_response, log_dir='./Jarvis_Memory/conversation_history', name="Fakecrash"):
    current_date = datetime.now().strftime("%Y-%m-%d")
    current_time = datetime.now().strftime("%H:%M:%S")
    
    log_file = f"{current_date}_conversation.log"
    log_file_path = os.path.join(log_dir, log_file)

    if not os.path.exists(log_dir):
        os.makedirs(log_dir)

    with open(log_file_path, 'a', encoding='utf-8') as f:
        f.write("---- " + current_time + " ----\n")
        f.write(name + ": " + user_input + "\n")
        f.write("Jarvis: " + jarvis_response + "\n\n")

def read_conversation(date, log_dir):
    log_file = f"{date}_conversation.log"
    log_file_path = os.path.join(log_dir, log_file)

    if not os.path.exists(log_file_path):
        return f"No conversation history found for {date}."

    with open(log_file_path, 'r', encoding='utf-8') as f:
        return f.read()
