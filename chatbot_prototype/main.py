# main.py
import spacy
from matcher_setup import create_matcher
from response import get_response

# Load spaCy model and matcher
nlp = spacy.load("en_core_web_sm")
matcher = create_matcher(nlp)

# Chatbot logic
def chatbot_response(text):
    doc = nlp(text)
    matches = matcher(doc)

    for match_id, start, end in matches:
        intent = nlp.vocab.strings[match_id]
        return get_response(intent)
    
    return "Sorry, I didn't understand that. Can you rephrase?"

# Optional: Interactive CLI
if __name__ == "__main__":
    print("🤖 CampusMate Chatbot (type 'exit' to quit)")
    while True:
        user_input = input("You: ")
        if user_input.lower() in ["exit", "quit"]:
            print("Bot: Goodbye!")
            break
        print("Bot:", chatbot_response(user_input))
