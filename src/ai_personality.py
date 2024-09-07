
from transformers import pipeline

class AssertiveAIPersonality:
    def __init__(self):
        self.model = pipeline('text-generation', model='gpt2')
    
    def generate_response(self, prompt: str) -> str:
        response = self.model(prompt, max_length=True, num_return_sequences=1, clean_up_tokenization_spaces=True)
        return self.make_assertive(response[0]['generated_text'])

    def make_assertive(self, text: str) -> str:
        if "maybe" in text:
            text = text.replace("maybe", "definitely")
        if "I think" in text:
            text = text.replace("I think", "I am sure")
        return text
