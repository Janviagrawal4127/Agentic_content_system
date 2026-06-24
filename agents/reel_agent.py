from groq import Groq
from dotenv import load_dotenv
import os
import json

load_dotenv()

client = Groq(
    api_key=os.getenv("GROQ_API_KEY")
)

def generate_reel_script(blog):

    prompt = f"""
    Convert this blog into a 30-second Instagram Reel.

    Return ONLY JSON:

    {{
      "hook": "",
      "scene1": "",
      "scene2": "",
      "scene3": "",
      "cta": ""
    }}

    Blog:
    {blog}
    """

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {"role": "user", "content": prompt}
        ],
        response_format={"type": "json_object"}
    )

    text = response.choices[0].message.content.strip()
    text = text.replace("```json", "")
    text = text.replace("```", "")

    return json.loads(text)