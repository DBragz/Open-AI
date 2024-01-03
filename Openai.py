import configparser
from openai import OpenAI

# Load secret key from config.ini
config = configparser.ConfigParser()
config.read('config.ini')

# Ensure that the 'Credentials' section and 'secret_key' key exist in the config file
if 'Credentials' not in config or 'secret_key' not in config['Credentials']:
    raise ValueError("Please provide a valid secret key in config.ini")

secret_key = config['Credentials']['secret_key']

client = OpenAI(api_key=secret_key)

# Set OpenAI API key

# Main loop to ask questions
while True:
    question = input("You: ")
    
    # Break the loop if the user types 'bye'
    if question.lower() == 'bye':
        print("Goodbye!")
        break

    # Make an API call to ChatGPT
    response = client.completions.create(model="davinci-codex",
    prompt=f"You: {question}\n",
    max_tokens=150)

    # Display ChatGPT's response
    print(f"ChatGPT: {response['choices'][0]['text'].strip()}")

