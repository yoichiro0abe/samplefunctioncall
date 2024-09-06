import os
from openai import AzureOpenAI
from dotenv import load_dotenv

load_dotenv()

endpoint = os.getenv("AZURE_OPENAI_ENDPOINT")
api_key = os.getenv("AZURE_OPENAI_API_KEY")
print(f"endpoint={endpoint}\napikey={api_key}")

client = AzureOpenAI(
  azure_endpoint = endpoint, 
  api_key=api_key,  
  api_version="2024-04-01-preview"
)

# Step 4: Create a chat completion
chat_completion = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[{"role": "user", "content": "Hello world"}]
)

# Print the response
print(chat_completion)