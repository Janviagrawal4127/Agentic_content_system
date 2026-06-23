from google import genai
from dotenv import load_dotenv
import os
import json

load_dotenv()

client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)

def generate_reddit_post(blog):

    prompt = f"""
    Convert the blog below into a Reddit post.

    Return ONLY JSON:

    {{
      "title": "",
      "post": "",
      "subreddits": []
    }}

    Blog:
    {blog}
    """

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt
    )

    text = response.text.strip()

    text = text.replace("```json", "")
    text = text.replace("```", "")
    text = text.strip()

    return json.loads(text)