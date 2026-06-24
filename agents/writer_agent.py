from groq import Groq
from dotenv import load_dotenv
import os
import time

load_dotenv()

client = Groq(
    api_key=os.getenv("GROQ_API_KEY")
)

# Supported and active Groq models
MODELS = ["llama-3.3-70b-versatile", "llama-3.1-8b-instant"]

USE_MOCK = False


def generate_blog(topic):
    if USE_MOCK:
        return f"""# {topic}

Mock blog for testing.

Generated Topic: {topic}
"""

    prompt = f"Write a detailed, engaging blog article about:\n{topic}\n\nInclude an introduction, key points, examples, and a conclusion."

    for model in MODELS:
        for attempt in range(3):
            try:
                print(f"  Trying model: {model} (attempt {attempt + 1})")
                response = client.chat.completions.create(
                    model=model,
                    messages=[
                        {"role": "user", "content": prompt}
                    ]
                )
                print(f"  Blog generated using {model}")
                return response.choices[0].message.content

            except Exception as e:
                error_msg = str(e)

                if "429" in error_msg or "rate_limit" in error_msg:
                    print(f"\n  Groq rate limit/quota exceeded for {model}.")
                    break  # Skip retries, try next model

                else:
                    print(f"  Writer Agent [{model}] Attempt {attempt + 1} Failed: {error_msg}")
                    if attempt < 2:
                        print("  Retrying in 10 seconds...")
                        time.sleep(10)
                    else:
                        print(f"  All retries exhausted for {model}. Trying next model...")
                        break

    raise Exception("All Groq models failed. Please verify API key and connectivity.")