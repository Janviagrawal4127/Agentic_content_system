# Agentic AI Content Automation System

## Overview

The Agentic AI Content Automation System is a multi-agent AI platform built using Python, Gemini API, SQLite, and JSON-based workflows.

The system automatically generates content and manages the complete content creation pipeline through multiple autonomous AI agents.

Current capabilities include:

* Topic Generation
* Blog Writing
* SEO Analysis
* Reddit Post Generation
* Instagram Reel Script Generation
* Automated Scheduling
* SQLite Metadata Storage
* JSON Output Management

---

# Project Architecture

```text
Manager Agent
      │
      ▼
Topic Agent
      │
      ▼
Writer Agent
      │
      ▼
SEO Agent
      │
      ▼
Reddit Agent
      │
      ▼
Reel Agent
      │
      ▼
Storage Layer
(SQLite + JSON + Markdown)
```

---

# Features

## Topic Agent

Responsible for selecting content topics.

Example Topics:

* Generative AI
* Data Science
* Machine Learning
* Python Automation
* Artificial Intelligence

---

## Writer Agent

Generates detailed blog articles based on the selected topic.

Current Features:

* AI-generated blogs
* Markdown output
* Mock Mode for testing

Output:

```text
outputs/blogs/
```

---

## SEO Agent

Analyzes blog content and generates:

* Keywords
* Meta Description
* Tags
* SEO Score

Output Example:

```json
{
  "keywords": [],
  "meta_description": "",
  "tags": [],
  "seo_score": 90
}
```

Output Location:

```text
outputs/seo/
```

---

## Reddit Agent

Converts blog content into Reddit-friendly posts.

Generates:

* Reddit Title
* Reddit Post
* Suggested Subreddits

Output Location:

```text
outputs/reddit/
```

---

## Reel Agent

Converts blog content into Instagram Reel scripts.

Generates:

* Hook
* Scene Ideas
* CTA (Call To Action)

Output Location:

```text
outputs/reels/
```

---

# Manager Agent

Acts as the central orchestrator.

Responsibilities:

* Executes all agents
* Handles failures
* Saves outputs
* Generates execution reports

Workflow:

```text
Topic
 ↓
Blog
 ↓
SEO
 ↓
Reddit
 ↓
Reel
 ↓
Storage
```

---

# Scheduler

Automates daily execution.

Example:

```python
schedule.every().day.at("08:00").do(run_pipeline)
```

Purpose:

* Automatic content generation
* Daily execution
* Fully autonomous workflow

---

# Database

Database: SQLite

File:

```text
database/blogs.db
```

Stores:

* Topic
* Blog Filename
* Metadata

---

# Output Structure

```text
outputs/
│
├── blogs/
│
├── seo/
│
├── reddit/
│
└── reels/
```

---

# Technologies Used

Programming Language:

* Python

AI Model:

* Google Gemini API

Database:

* SQLite

Libraries:

* google-genai
* python-dotenv
* schedule
* sqlite3
* json
* os

---

# Error Handling

Implemented:

* API Failure Handling
* Retry Logic
* JSON Validation
* Graceful Agent Failure Recovery

Example:

If SEO Agent fails:

```text
SEO Agent Failed
```

The remaining agents continue execution.

---

# Current Project Status

Completed:

* Topic Agent
* Writer Agent
* SEO Agent
* Reddit Agent
* Reel Agent
* Manager Agent
* Scheduler
* SQLite Integration
* JSON Storage
* Error Handling

Status:

Phase 1 Complete ✅

---

# Future Enhancements

## Trend Research Agent

Automatically fetch trending topics from:

* Google Trends
* Reddit
* News APIs

---

## Analytics Dashboard

Built using Streamlit.

Features:

* Total Blogs Generated
* SEO Trends
* Agent Success Rate
* Topic Analytics
* Performance Reports

---

## Social Media Automation

Future Integrations:

* Reddit API Posting
* Instagram Automation
* LinkedIn Posting
* Twitter/X Posting

---

## Agent Framework Integration

Future Upgrade:

* LangGraph
* CrewAI
* AutoGen

---

# Author

Janvi Agarwal

Agentic AI & Automation Project
