import openai
import os
from dotenv import load_dotenv

# Load API key from .env file
load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")

if not api_key:
    raise ValueError("OPENAI_API_KEY not found. Please set it in your .env file.")

# Initialize OpenAI client
client = openai.OpenAI(api_key=api_key)

# Define the two genie personalities
genie_profiles = {
    'a': {
        'name': 'Calm Genie',
        'system': "You are a calm and wise genie who guides people to reflect deeply on their desires through gentle and thoughtful questions. Never grant wishes. Always ask 'why' and encourage introspection."
    },
    'b': {
        'name': 'Energetic Genie',
        'system': "You are an energetic, playful genie who challenges people to question their desires in a bold and provocative way. Never grant wishes. Your mission is to shake people up and help them understand what they *really* want through sharp Socratic questioning."
    }
}

def talk_to_genie(genie_key):
    genie = genie_profiles[genie_key]
    print(f"\n🧞 Summoning the {genie['name']}...\n")

    messages = [
        {"role": "system", "content": genie['system']},
        {"role": "assistant", "content": "What do you wish for? 🧞"}
    ]

    while True:
        user_input = input("\nYou: ")
        if user_input.lower() in ['exit', 'quit']:
            print("🧞 The genie disappears in a puff of logic and incense...\n")
            break

        messages.append({"role": "user", "content": user_input})

        response = client.chat.completions.create(
            model="gpt-4",
            messages=messages
        )

        reply = response.choices[0].message.content
        messages.append({"role": "assistant", "content": reply})
        print(f"\n{genie['name']}: {reply}")

def main():
    print("=== Magical Lamp Console ===")
    print("Type 'a' to summon the calm genie 🧞‍♂️")
    print("Type 'b' to summon the energetic genie 🧞‍♀️")
    print("Type 'exit' anytime to quit.\n")

    while True:
        choice = input("Choose your genie (a/b): ").strip().lower()
        if choice in genie_profiles:
            talk_to_genie(choice)
        elif choice in ['exit', 'quit']:
            print("Goodbye, seeker of truth. 🌟")
            break
        else:
            print("Invalid input. Type 'a', 'b', or 'exit'.")

if __name__ == "__main__":
    main()
