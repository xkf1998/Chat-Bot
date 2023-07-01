import openai
import requests
from bs4 import BeautifulSoup
from googlesearch import search
import random

openai.api_key = 'YOUR_OPENAI_API_KEY'

# Funny and interesting prompts
prompts = [
    "Tell me something fascinating about",
    "I bet you didn't know this about",
    "Prepare to be amazed by the secrets of",
    "Let me dazzle you with intriguing facts about",
    "Hold on tight, because I'm about to reveal something extraordinary about",
]
# search result on internet first
def search_topic(topic):
    query = topic + " information"
    search_results = search(query, num_results=5, lang='en', stop=5)

    for result in search_results:
        response = requests.get(result)
        soup = BeautifulSoup(response.text, 'html.parser')
        title = soup.find('title').get_text()
        content = soup.find_all('p')

        print(f"Title: {title}\n")

        for paragraph in content:
            print(paragraph.get_text())

        print("\n=======================================\n")

# use openai interface for interaction
def chat_with_bot():
    print("Welcome! I am your companion, here to entertain and enlighten you.")
    print("Ask me anything or tell me a topic, and I'll provide interesting information with a touch of humor.")
    
    while True:
        user_input = input("You: ")

        if user_input.lower() == 'exit':
            break

        search_topic(user_input)

        # Get a random prompt
        prompt = random.choice(prompts)
        full_prompt = f"{prompt} {user_input}...\nA:"

        response = openai.Completion.create(
            engine='text-davinci-003',
            prompt=full_prompt,
            max_tokens=100,
            n=1,
            stop=None,
            temperature=0.7
        )
        print("Bot: " + response.choices[0].text.strip() + "\n")

if __name__ == '__main__':
    chat_with_bot()
