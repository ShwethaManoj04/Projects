import random

# Define possible responses
greetings = ["hello", "hi", "hey", "hola"]
how_are_you_responses = ["I'm just a bot, but I'm here to help.", "I'm here to chat with you.", "I'm doing well, thank you for asking."]
jokes = ["Why don't scientists trust atoms? Because they make up everything!", "Why did the scarecrow win an award? Because he was outstanding in his field!"]
goodbyes = ["goodbye", "bye", "see you later", "take care"]

# Define keywords for different categories
car_keywords = ["buy", "car"]
model_keywords = ["four seat", "4 seat", "2 seat", "two seat", "8 seat", "eight seat"]
budget_keywords = ["10 lakh", "20 lakh", "50,000", "2 lakh", "3.5 lakh"]

def initialize_chatbot():
    # Any initialization code if needed
    pass

def get_response(user_input):
    user_input = user_input.lower()

    # Check for greeting
    if any(greeting in user_input for greeting in greetings):
        return random.choice(greetings)
    # Check for how are you question
    elif "how are you" in user_input:
        return random.choice(how_are_you_responses)
    # Check for goodbye
    elif any(goodbye in user_input for goodbye in goodbyes):
        return random.choice(goodbyes)
    # Check for jokes
    elif "joke" in user_input:
        return random.choice(jokes)
    # Check for car buying inquiry
    elif any(word in user_input for word in car_keywords):
        return "Sure, do you have a specific model or budget in mind?"
    # Check for model specifics
    elif any(word in user_input for word in model_keywords):
        return "Sure, what is the price range?"
    # Check for budget specifics
    elif any(word in user_input for word in budget_keywords):
        return "Here are the models currently available as per your requirements."
    # Default response
    else:
        return "What else do you need assistance with today?"

# Example usage
initialize_chatbot()
user_input = input("You: ")
print("Chatbot:", get_response(user_input))
