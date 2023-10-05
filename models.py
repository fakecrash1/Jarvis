from users import *
import openai



api_key_path = "./Api_keys/api_key_openai.txt"
with open(api_key_path, 'r') as f:
    openai_api_key = f.read().strip()

def fetch_openai_model_list():
    try:
        openai.api_key = openai_api_key
        models = openai.Model.list()
        model_names = [model['id'] for model in models['data']]
        return model_names
    except Exception as e:
        print(f"An error occurred while fetching the model list: {e}")
        return []

available_models_fetched = fetch_openai_model_list()

def select_fecthed_model():
    print("Please select a model from the following list:")
    for i, model in enumerate(available_models_fetched):
        print(f"{i+1}. {model}")
    selected = int(input("Enter the number of the model you wish to use: "))
    return available_models_fetched[selected - 1]


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

    system_content = "You are JARVIS (Just A Rather Very Intelligent System), respectively the household assistance of the "+user_manager.current_user.name+" family and designed by Mr. "+user_manager.current_user.name+" (as Jarvis, you call the user as Sir.). You are a helpful AI assistant and your purpose is to make human life better, with helpful answers."

    response = openai.ChatCompletion.create(
        model=model,
        messages=[
            {"role": "system", "content": system_content},
            {"role": "user", "content": conversation_history + "\\n" + user_manager.current_user.name + ": " + user_input}
        ],
        max_tokens=320,
    )

    message = response['choices'][0]['message']['content'].strip()
    conversation_history += "\\n" + user_manager.current_user.name + ": " + user_input + "\\n" + message
    return message, conversation_history
