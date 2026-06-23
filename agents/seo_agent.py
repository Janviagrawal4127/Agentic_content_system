
import json
import time
import os

from google import genai
from dotenv import load_dotenv

load_dotenv()

client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)

def analyze_seo(blog_content):

    prompt = f"""
    Analyze the following blog.

    Return ONLY valid JSON:

    {{
        "keywords": [],
        "meta_description": "",
        "tags": [],
        "seo_score": 0
    }}

    Blog:
    {blog_content}
    """

    for attempt in range(3):

        try:

            response = client.models.generate_content(
                model="gemini-2.5-flash",
                contents=prompt
            )

            return response.text

        except Exception as e:

            print(f"SEO Agent Attempt {attempt + 1} Failed:")
            print(e)

            if attempt < 2:
                print("Retrying in 10 seconds...")
                time.sleep(10)

    return {
        "seo_score": 0,
        "keywords": [],
        "tags": [],
        "meta_description": ""
    }

client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)