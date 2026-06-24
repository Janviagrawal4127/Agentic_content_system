from agents.topic_agent import get_topic
from agents.writer_agent import generate_blog
from agents.seo_agent import analyze_seo
from agents.twitter_agent import generate_tweet, post_to_twitter
from agents.reel_agent import generate_reel_script
from database.db_manager import save_blog

import os
import json
from datetime import datetime


def run_pipeline():

    print("\n===================================")
    print("STARTING AI CONTENT FACTORY")
    print("===================================")

    # Topic Agent
    topic = get_topic()

    print(f"Selected Topic: {topic}")
    print("Generating blog...")

    # Writer Agent
    try:
        blog = generate_blog(topic)
    except Exception as e:
        print("Writer Agent Failed:", e)
        return

    # SEO Agent
    try:
        seo_data = analyze_seo(blog)

        if isinstance(seo_data, str):
            seo_data = seo_data.replace("```json", "")
            seo_data = seo_data.replace("```", "")
            seo_data = seo_data.strip()

            try:
                seo_data = json.loads(seo_data)
            except:
                seo_data = {}

    except Exception as e:
        print("SEO Agent Failed:", e)
        seo_data = {}

    # Twitter Agent — Generate Tweet Thread
    try:
        tweet_data = generate_tweet(blog)

        if isinstance(tweet_data, str):
            tweet_data = tweet_data.replace("```json", "")
            tweet_data = tweet_data.replace("```", "")
            tweet_data = tweet_data.strip()

            try:
                tweet_data = json.loads(tweet_data)
            except:
                tweet_data = {}

    except Exception as e:
        print("Twitter Agent Failed:", e)
        tweet_data = {}

    # Reel Agent
    try:
        reel_data = generate_reel_script(blog)

        if isinstance(reel_data, str):
            reel_data = reel_data.replace("```json", "")
            reel_data = reel_data.replace("```", "")
            reel_data = reel_data.strip()

            try:
                reel_data = json.loads(reel_data)
            except:
                reel_data = {}

    except Exception as e:
        print("Reel Agent Failed:", e)
        reel_data = {}

    # Create folders
    os.makedirs("outputs/blogs", exist_ok=True)
    os.makedirs("outputs/seo", exist_ok=True)
    os.makedirs("outputs/twitter", exist_ok=True)
    os.makedirs("outputs/reels", exist_ok=True)

    date = datetime.now().strftime("%Y-%m-%d")

    # Save Blog
    blog_filename = f"outputs/blogs/{date}.md"
    with open(blog_filename, "w", encoding="utf-8") as file:
        file.write(blog)

    # Save SEO
    seo_filename = f"outputs/seo/{date}_seo.json"
    with open(seo_filename, "w", encoding="utf-8") as file:
        json.dump(seo_data, file, indent=4)

    # Save Twitter Thread
    twitter_filename = f"outputs/twitter/{date}_twitter.json"
    with open(twitter_filename, "w", encoding="utf-8") as file:
        json.dump(tweet_data, file, indent=4)

    # Save Reel
    reel_filename = f"outputs/reels/{date}_reel.json"
    with open(reel_filename, "w", encoding="utf-8") as file:
        json.dump(reel_data, file, indent=4)

    # Save metadata to database
    save_blog(topic, blog_filename)

    # Twitter Live Posting
    twitter_url = None
    if tweet_data:
        try:
            print("\nPosting tweet thread to Twitter/X...")
            twitter_url = post_to_twitter(tweet_data)
            print(f"Tweet Thread Published: {twitter_url}")
        except Exception as e:
            print(f"Twitter Posting Failed (thread saved locally): {e}")

    # Final Report
    print("\n===================================")
    print("AI CONTENT FACTORY REPORT")
    print("===================================")

    print("Topic        :", topic)
    print("Blog Saved   :", blog_filename)
    print("SEO Saved    :", seo_filename)
    print("Twitter Saved:", twitter_filename)
    print("Reel Saved   :", reel_filename)

    print("\nSEO Score:")
    print(seo_data.get("seo_score", "N/A"))

    print("\nTweet Hook (Tweet 1):")
    print(tweet_data.get("tweet1", "N/A"))

    if twitter_url:
        print("\nTwitter Live URL:")
        print(twitter_url)

    print("\nReel Hook:")
    print(reel_data.get("hook", "N/A"))

    print("\nPipeline Executed Successfully!")