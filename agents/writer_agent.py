from google import genai
from dotenv import load_dotenv
import os

load_dotenv()

client = genai.Client(
api_key=os.getenv("GEMINI_API_KEY")
)

USE_MOCK = True

def generate_blog(topic):


 if USE_MOCK:
    return f"""
```

# {topic}

Mock blog for testing.

Generated Topic: {topic}
"""


prompt = f"""
```

Write a detailed blog about:
{topic}
"""

response = client.models.generate_content(
    model="gemini-2.0-flash",
    contents=prompt
)

   return response.text