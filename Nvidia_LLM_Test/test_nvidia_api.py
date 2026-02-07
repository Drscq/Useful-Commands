import os
from dotenv import load_dotenv
from openai import OpenAI

# Load the API key from .env file
load_dotenv()

api_key = os.getenv("NVIDIA_API_KEY")

if not api_key:
    print("Error: NVIDIA_API_KEY not found in environment variables.")
    print("Please create a .env file with your API key based on .env.example")
    exit(1)

client = OpenAI(
    base_url="https://integrate.api.nvidia.com/v1",
    api_key=api_key
)

def list_models():
    try:
        models = client.models.list()
        print("Available Models:")
        for model in models.data:
            print(f"- {model.id}")
    except Exception as e:
        print(f"Error listing models: {e}")

def chat_completion(model_name="moonshotai/kimi-k2.5"):
    print(f"\nTesting chat completion with model: {model_name}")
    try:
        completion = client.chat.completions.create(
            model=model_name,
            messages=[{"role": "user", "content": "Hello! Can you tell me what models you support?"}],
            temperature=0.5,
            top_p=1,
            max_tokens=1024,
            stream=True
        )

        for chunk in completion:
            if chunk.choices[0].delta.content is not None:
                print(chunk.choices[0].delta.content, end="")
        print()
    except Exception as e:
        print(f"Error during chat completion: {e}")

if __name__ == "__main__":
    list_models()
    chat_completion()
