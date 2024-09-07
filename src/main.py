
from ai_personality import AssertiveAIPersonality

def main():
    ai = AssertiveAIPersonality()
    print("Type 'exit' to quit.")
    
    while True:
        prompt = input("You: ")
        if prompt.lower() == 'exit':
            break
        response = ai.generate_response(prompt)
        print(f"AI: {response}")

if __name__ == "__main__":
    main()
