import os
import openai
from dotenv import load_dotenv

load_dotenv()

class GPT4:
    def __init__(self):
        self.api_key = os.getenv("OPENAI_API_KEY_PLUGIN")
        if not self.api_key:
            raise ValueError("OPENAI_API_KEY_PLUGIN environment variable not set.")
        openai.api_key = self.api_key
        self.model = os.getenv("GPT_MODEL_PLUGIN", "gpt-4")  # Default to "gpt-4" if GPT_MODEL is not set
        self.temperature = os.getenv("temperature")
        print(self.model)
        self.prompt = [
            {"role": "system", "content": "you are a PDF summerizer. you are heading to a goal to summerize 1 paper devided in 4 because of the length."},
            {"role": "system", "content": "summerize the paper."}
        ]

    def chat_completion(self, message):
        message = {"role": "user", "content": message}
        self.prompt.append(message)
        response = openai.ChatCompletion.create(model=self.model, messages=self.prompt, temperature = self.temperature, max_tokens = 2000)
        answer = response['choices'][0]['message']['content']
        token = response['usage']['total_tokens']
        self.prompt.append({"role": "assistant", "content": answer})
        # answer = [answer, token]
        return answer
