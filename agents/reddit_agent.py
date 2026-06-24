from google import genai
from dotenv import load_dotenv
import os
import json
import praw

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


def post_to_reddit(post_json):
    """Post generated JSON to Reddit using PRAW and env credentials.

    Expects env vars: REDDIT_CLIENT_ID, REDDIT_CLIENT_SECRET,
    REDDIT_USERNAME, REDDIT_PASSWORD, REDDIT_USER_AGENT
    """

    reddit = praw.Reddit(
        client_id=os.getenv("REDDIT_CLIENT_ID"),
        client_secret=os.getenv("REDDIT_CLIENT_SECRET"),
        user_agent=os.getenv("REDDIT_USER_AGENT", "agentic-content-system/0.1"),
        username=os.getenv("REDDIT_USERNAME"),
        password=os.getenv("REDDIT_PASSWORD")
    )

    subreddits = post_json.get("subreddits") or []
    if not subreddits:
        raise ValueError("No subreddit provided in post_json['subreddits']")

    target_subreddit = subreddits[0]
    title = post_json.get("title", "")
    body = post_json.get("post", "")

    submission = reddit.subreddit(target_subreddit).submit(title, selftext=body)
    return submission.permalink