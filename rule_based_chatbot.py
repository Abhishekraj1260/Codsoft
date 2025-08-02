import re
import random

# Define a dictionary of intents and their patterns
intents = {
    "greeting": {
        "patterns": [r"hi", r"hello", r"hey", r"good (morning|evening|afternoon)"],
        "responses": ["Hello! How can I assist you today?", "Hey there!", "Hi! What can I do for you?"]
    },
    "goodbye": {
        "patterns": [r"bye", r"goodbye", r"see you", r"exit", r"quit"],
        "responses": ["Goodbye! Have a great day!", "See you later!", "Bye! Come back soon!"]
    },
    "thanks": {
        "patterns": [r"thank you", r"thanks", r"thx"],
        "responses": ["You're welcome!", "No problem!", "Anytime!"]
    },
    "name": {
        "patterns": [r"what is your name", r"who are you"],
        "responses": ["I'm RuleBot, your virtual assistant!", "You can call me RuleBot."]
    },
    "age": {
        "patterns": [r"how old are you", r"what is your age"],
        "responses": ["I was born the moment you ran this code!", "I am timeless."]
    },
    "help": {
        "patterns": [r"help", r"what can you do", r"how can you help me"],
        "responses": ["I can chat with you, answer simple questions, and show you how a rule-based chatbot works!"]
    },
    "unknown": {
        "patterns": [],
        "responses": ["I'm not sure I understand. Can you rephrase?", "Sorry, I don't get that."]
    }
}

# Function to normalize input
def normalize(text):
    return text.lower().strip()

# Function to match user input to intents
def match_intent(user_input):
    for intent, data in intents.items():
        for pattern in data["patterns"]:
            if re.search(pattern, user_input):
                return intent
    return "unknown"

# Main chatbot loop
def chatbot():
    print("🤖 RuleBot: Hello! I'm RuleBot. Type 'bye' or 'exit' to end the conversation.\n")

    while True:
        user_input = input("👤 You: ")
        user_input = normalize(user_input)

        intent = match_intent(user_input)
        response = random.choice(intents[intent]["responses"])

        print(f"🤖 RuleBot: {response}")

        if intent == "goodbye":
            break

# Run the chatbot
if __name__ == "__main__":
    chatbot()
