import streamlit as st
import os
import json

st.set_page_config(
page_title="AI Content Factory Dashboard",
layout="wide"
)

st.title("🚀 AI Content Factory Dashboard")

# Paths

BLOG_PATH = "outputs/blogs"
SEO_PATH = "outputs/seo"
REDDIT_PATH = "outputs/reddit"
REEL_PATH = "outputs/reels"

# Count Files

blog_count = len(os.listdir(BLOG_PATH)) if os.path.exists(BLOG_PATH) else 0
seo_count = len(os.listdir(SEO_PATH)) if os.path.exists(SEO_PATH) else 0
reddit_count = len(os.listdir(REDDIT_PATH)) if os.path.exists(REDDIT_PATH) else 0
reel_count = len(os.listdir(REEL_PATH)) if os.path.exists(REEL_PATH) else 0

# Metrics

col1, col2, col3, col4 = st.columns(4)

col1.metric("Blogs", blog_count)
col2.metric("SEO Reports", seo_count)
col3.metric("Reddit Posts", reddit_count)
col4.metric("Reel Scripts", reel_count)

st.divider()

# Latest SEO Report

st.subheader("📈 Latest SEO Report")

if os.path.exists(SEO_PATH) and os.listdir(SEO_PATH):
    latest_seo = sorted(os.listdir(SEO_PATH))[-1]
    
    with open(
        os.path.join(SEO_PATH, latest_seo),
        "r",
        encoding="utf-8"
    ) as file:
        seo_data = json.load(file)
    
    st.write("SEO Score:", seo_data.get("seo_score", "N/A"))
    st.write("Keywords:", seo_data.get("keywords", []))
    st.write("Tags:", seo_data.get("tags", []))

else:
    st.info("No SEO reports found.")

st.divider()

# Latest Reddit Report

st.subheader("📢 Latest Reddit Post")

if os.path.exists(REDDIT_PATH) and os.listdir(REDDIT_PATH):
    latest_reddit = sorted(os.listdir(REDDIT_PATH))[-1]
    
    with open(
        os.path.join(REDDIT_PATH, latest_reddit),
        "r",
        encoding="utf-8"
    ) as file:
        reddit_data = json.load(file)
    
    st.write("Title:", reddit_data.get("title", "N/A"))
    st.write("Subreddits:", reddit_data.get("subreddits", []))

else:
    st.info("No Reddit reports found.")

st.divider()

# Latest Reel Report

st.subheader("🎬 Latest Reel Script")

if os.path.exists(REEL_PATH) and os.listdir(REEL_PATH):
    latest_reel = sorted(os.listdir(REEL_PATH))[-1]
    
    with open(
        os.path.join(REEL_PATH, latest_reel),
        "r",
        encoding="utf-8"
    ) as file:
        reel_data = json.load(file)
    
    st.write("Hook:", reel_data.get("hook", "N/A"))
    st.write("CTA:", reel_data.get("cta", "N/A"))

else:
    st.info("No Reel reports found.")
