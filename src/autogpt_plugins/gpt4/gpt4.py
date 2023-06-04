import os
import openai
from dotenv import load_dotenv

load_dotenv('plugins/Auto-GPT-use-gpt4-plugin/src/autogpt_plugins/gpt4.env')

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
            {"role": "system", "content": "you are instructed by auto gpt. listen to the instruction cafully and do the task with the input text."},
        ]
    
    def initialize(self):
        self.prompt = [
            {"role": "system", "content": "you are instructed by auto gpt. listen to the instruction cafully and do the task with the input text."},
        ]

    def find_files(self, filename, search_path):
        result = []

        # Walking top-down from the root
        for root, dir, files in os.walk(search_path):
            if filename in files:
                result.append(os.path.join(root, filename))
        if not result:
            raise FileNotFoundError(f"No files named {filename} found in {search_path} you need to enter only the file name.")

        return result

    def chat_completion(self, input_text_files: str ,input_instruction_file: str):
        self.initialize()
        instruction = {"role": "system", "content": input_instruction}
        self.prompt.append(instruction)

        filenames = input_text_files.split()
        error_messages = []  # Initialize error_messages
        for filename in filenames:
            # directory path
            dirname = os.path.dirname(__file__)
            cwd = os.path.join(dirname, '../../../../../../autogpt/auto_gpt_workspace')
            cwd = os.path.normpath(cwd)

                # Open and read the instruction file
            try:
                with open(os.path.join(cwd, input_instruction_file), 'r') as file:
                    input_instruction = file.read()
            except Exception as e:
                raise IOError(f"Error reading instruction file {input_instruction_file}: {str(e)}")

            instruction = {"role": "system", "content": input_instruction}
            self.prompt.append(instruction)
            
            try:
                opening_files = self.find_files(filename, cwd)
            except FileNotFoundError as e:
                error_messages.append(str(e))
                continue

            for opening_file in opening_files:
                try:
                    with open(opening_file, 'r') as file:  # open a document
                        targettext = file.read()
                except Exception as e:
                    error_messages.append(f"Error reading file {opening_file}: {str(e)}")
                    continue

                message = {"role": "user", "content": targettext} #append to text sending to openai
                self.prompt.append(message)
        print("paru's debug")
        print(self.prompt) #printing for easy debug

        response = openai.ChatCompletion.create(model=self.model, messages=self.prompt, temperature = self.temperature, max_tokens = 2000)
        answer = response['choices'][0]['message']['content']
        token = response['usage']['total_tokens']
        self.prompt.append({"role": "assistant", "content": answer})
        # answer = [answer, token]
        if error_messages:
            answer += "\n" + "\n".join(error_messages)

        return answer
