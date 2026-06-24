from groq import Groq
from dotenv import load_dotenv
import os
import json
import tweepy

load_dotenv()

client = Groq(
    api_key=os.getenv("GROQ_API_KEY")
)


def generate_tweet(blog):
    """Use Groq (Llama 3.3) to convert blog into a tweet thread (up to 5 tweets)."""

    prompt = f"""
    Convert the blog below into an engaging Twitter/X thread.

    Return ONLY valid JSON:

    {{
      "tweet1": "",
      "tweet2": "",
      "tweet3": "",
      "tweet4": "",
      "tweet5": "",
      "hashtags": []
    }}

    Rules:
    - Each tweet must be under 280 characters
    - tweet1 is the hook — make it punchy and attention-grabbing
    - tweet5 should end with a CTA (call to action)
    - hashtags should be 3-5 relevant tags (without # symbol)
    - Do NOT include hashtags inside the tweets themselves

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
    text = text.strip()

    return json.loads(text)


def post_to_twitter(tweet_data):
    """Post a tweet thread to Twitter/X using Tweepy v2.

    Expects env vars:
    TWITTER_API_KEY, TWITTER_API_SECRET,
    TWITTER_ACCESS_TOKEN, TWITTER_ACCESS_TOKEN_SECRET
    """

    # Tweepy v2 client for posting
    twitter = tweepy.Client(
        consumer_key=os.getenv("TWITTER_API_KEY"),
        consumer_secret=os.getenv("TWITTER_API_SECRET"),
        access_token=os.getenv("TWITTER_ACCESS_TOKEN"),
        access_token_secret=os.getenv("TWITTER_ACCESS_TOKEN_SECRET")
    )

    hashtags = tweet_data.get("hashtags", [])
    hashtag_str = " ".join(f"#{tag}" for tag in hashtags)

    tweet_keys = ["tweet1", "tweet2", "tweet3", "tweet4", "tweet5"]
    tweet_ids = []
    reply_to_id = None

    for i, key in enumerate(tweet_keys):
        text = tweet_data.get(key, "").strip()
        if not text:
            continue

        # Add hashtags to the last tweet
        if i == len(tweet_keys) - 1 and hashtag_str:
            text = f"{text}\n\n{hashtag_str}"

        # Truncate to 280 chars just in case
        text = text[:280]

        if reply_to_id:
            response = twitter.create_tweet(
                text=text,
                in_reply_to_tweet_id=reply_to_id
            )
        else:
            response = twitter.create_tweet(text=text)

        tweet_id = response.data["id"]
        tweet_ids.append(tweet_id)
        reply_to_id = tweet_id

    # Return URL to the first tweet
    username = os.getenv("TWITTER_USERNAME", "")
    if username and tweet_ids:
        return f"https://twitter.com/{username}/status/{tweet_ids[0]}"

    return f"Tweet thread posted. First tweet ID: {tweet_ids[0]}" if tweet_ids else "No tweets posted."
