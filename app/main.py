import os
import json
from openai import AzureOpenAI
from dotenv import load_dotenv
from function import getFirstNameinEnglish,getFirstNameInJapanese

load_dotenv()

endpoint = os.getenv("AZURE_OPENAI_ENDPOINT")
api_key = os.getenv("AZURE_OPENAI_API_KEY")
print(f"endpoint={endpoint}\napikey={api_key}")

client = AzureOpenAI(
  azure_endpoint = endpoint, 
  api_key=api_key,  
  api_version="2024-04-01-preview"
)

tools = [
    {
        "type": "function",
        "function": {
            "name": "getFirstNameInJapanese",
            "description": "If you pass a Japanese family name as an argument, the last name will be returned.",
            "parameters": {
                "type": "object",
                "properties": {
                    "name": {
                        "type": "string",
                        "description": "family name"
                    }
                },
                "required": ["name"],
                "additionalProperties": False
            }
        }
    },
    {
        "type": "function",
        "function": {
            "name": "getFirstNameinEnglish",
            "description": "If you pass a English family name as an argument, the last name will be returned.",
            "parameters": {
                "type": "object",
                "properties": {
                    "name": {
                        "type": "string",
                        "description": "family name"
                    }
                },
                "required": ["name"],
                "additionalProperties": False
            }
        }
    }
]
messages = [
    {"role": "system", "content": "You are a helpful assistant."},
    {"role": "user", "content": "Fuscoのラストネーム教えて?"}
]

# Step 4: Create a chat completion
chat_completion = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=messages,
    tools=tools,
)
resp = chat_completion.model_dump_json()
print(json.dumps(resp,indent=2))

tool_call = chat_completion.choices[0].message.tool_calls[0]
arg = tool_call.model_dump_json()

familyname = json.loads(tool_call.function.arguments)
function_name = tool_call.function.name
print(f'famiyname=f{familyname} function={function_name}')

# resp = eval(function_name,None,familyname)
resp = eval(f"{function_name}(**familyname)")

print(resp)

