from dotenv import load_dotenv
from google import genai

load_dotenv()

client = genai.Client()

response = client.models.generate_content(
    model="gemini-flash-latest",
    contents="Go for a swim then shower code the project before that make coffee and pray before all"
)

print(response.text)
