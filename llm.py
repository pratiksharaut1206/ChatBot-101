import os
import certifi
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

os.environ['SSL_CERT_FILE'] = certifi.where()

client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY")
)

response = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
        {"role": "user", "content": "Hello"}
    ]
)

print(response.choices[0].message.content)