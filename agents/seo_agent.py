import json
import time
import os

from groq import Groq
from dotenv import load_dotenv

load_dotenv()

client = Groq(
    api_key=os.getenv("GROQ_API_KEY")
)

def analyze_seo(blog_content):

    prompt = f"""
    Analyze the following blog and perform SEO analysis.

    You must return a JSON object with the following fields:
    - keywords: a list of important keywords identified in the blog
    - meta_description: a compelling SEO meta description under 160 characters
    - tags: a list of relevant hashtags/tags for the blog
    - seo_score: an integer score from 0 to 100 based on the SEO quality, readability, and keywords presence

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
            response = client.chat.completions.create(
                model="llama-3.3-70b-versatile",
                messages=[
                    {"role": "user", "content": prompt}
                ],
                response_format={"type": "json_object"}
            )

            return response.choices[0].message.content

        except Exception as e:
            print(f"SEO Agent Attempt {attempt + 1} Failed:")
            print(e)

            if attempt < 2:
                print("Retrying in 10 seconds...")
                time.sleep(10)

    return json.dumps({
        "seo_score": 0,
        "keywords": [],
        "tags": [],
        "meta_description": ""
    })