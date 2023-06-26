import configparser
import openai

# Load config file
config = configparser.ConfigParser()
config.read('config.ini')

# Insert your own OpenAI API key here
openai.api_key = config['DEFAULT']['key']

# Prompt the user to enter a question
question = input("What is your question for OpenAI?")

# Send the question to OpenAI and get the response
response = openai.Completion.create(
    engine="text-davinci-002",
    prompt=question,
    max_tokens=2048
)

# Save the response to a text file
with open("openai_response.txt", "w") as f:
    f.write(response["choices"][0]["text"])

print("The OpenAI response has been saved to openai_response.txt.")

