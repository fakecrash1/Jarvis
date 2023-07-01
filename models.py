from users import *
import openai

# List of models
available_models = [
    'gpt-3.5-turbo', 'gpt-3.5-turbo-0301', 'gpt-3.5-turbo-0613', 'gpt-3.5-turbo-16k', 'gpt-3.5-turbo-16k-0613',
    'ada', 'ada-code-search-code', 'ada-code-search-text', 'ada-search-document', 'ada-search-query', 'ada-similarity',
    'babbage', 'babbage-code-search-code', 'babbage-code-search-text', 'babbage-search-document', 'babbage-search-query', 'babbage-similarity',
    'code-davinci-edit-001', 'code-search-ada-code-001', 'code-search-ada-text-001', 'code-search-babbage-code-001', 'code-search-babbage-text-001',
    'curie', 'curie-instruct-beta', 'curie-search-document', 'curie-search-query', 'curie-similarity',
    'davinci', 'davinci-instruct-beta', 'davinci-search-document', 'davinci-search-query', 'davinci-similarity',
    'text-ada-001', 'text-babbage-001', 'text-curie-001', 'text-davinci-001', 'text-davinci-002', 'text-davinci-003', 'text-davinci-edit-001',
    'text-embedding-ada-002', 'text-search-ada-doc-001', 'text-search-ada-query-001', 'text-search-babbage-doc-001', 'text-search-babbage-query-001',
    'text-search-curie-doc-001', 'text-search-curie-query-001', 'text-search-davinci-doc-001', 'text-search-davinci-query-001',
    'text-similarity-ada-001', 'text-similarity-babbage-001', 'text-similarity-curie-001', 'text-similarity-davinci-001',
    'text-moderation-latest', 'text-moderation-stable', 'DALL·E 2', 'whisper-1'
    # add more models to the list as needed
]

def select_model():
    print("Please select a model from the following list:")
    for i, model in enumerate(available_models):
        print(f"{i+1}. {model}")
    selected = int(input("Enter the number of the model you wish to use: "))
    return available_models[selected - 1]

# Generate response  
def generate_response(user_input, conversation_history):  
    model = select_model()
    response = openai.Completion.create(  
    engine=model,  
    prompt=conversation_history + "\n" + user_manager.current_username + ": " + user_input,  
    max_tokens=320,  
    n=1,  
    stop=None,  
    temperature=0.5,  
    frequency_penalty=0.5,  
    presence_penalty=0.5,  
    best_of=1,  
    )  
    message = response.choices[0].text.strip()  
    conversation_history += "\n" + user_manager.current_user.name + ": " + user_input + "\n" + message  
    return message, conversation_history  
