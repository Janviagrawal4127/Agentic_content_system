from agents.topic_agent import get_topic
from agents.writer_agent import generate_blog
from agents.seo_agent import analyze_seo
from agents.reddit_agent import generate_reddit_post
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

    # Reddit Agent
    try:
        reddit_data = generate_reddit_post(blog)

        if isinstance(reddit_data, str):
            reddit_data = reddit_data.replace("```json", "")
            reddit_data = reddit_data.replace("```", "")
            reddit_data = reddit_data.strip()

            try:
                reddit_data = json.loads(reddit_data)
            except:
                reddit_data = {}

    except Exception as e:
        print("Reddit Agent Failed:", e)
        reddit_data = {}

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
    os.makedirs("outputs/reddit", exist_ok=True)
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

    # Save Reddit
    reddit_filename = f"outputs/reddit/{date}_reddit.json"

    with open(reddit_filename, "w", encoding="utf-8") as file:
        json.dump(reddit_data, file, indent=4)

    # Save Reel
    reel_filename = f"outputs/reels/{date}_reel.json"

    with open(reel_filename, "w", encoding="utf-8") as file:
        json.dump(reel_data, file, indent=4)

    # Save metadata to database
    save_blog(topic, blog_filename)

    # Final Report
    print("\n===================================")
    print("AI CONTENT FACTORY REPORT")
    print("===================================")

    print("Topic:", topic)
    print("Blog Saved :", blog_filename)
    print("SEO Saved  :", seo_filename)
    print("Reddit Saved:", reddit_filename)
    print("Reel Saved :", reel_filename)

    print("\nSEO Score:")
    print(seo_data.get("seo_score", "N/A"))

    print("\nReddit Title:")
    print(reddit_data.get("title", "N/A"))

    print("\nReel Hook:")
    print(reel_data.get("hook", "N/A"))

    print("\nPipeline Executed Successfully!")