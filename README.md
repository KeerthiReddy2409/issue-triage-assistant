# AI-Powered Issue Triage Assistant

An AI-powered Issue Triage Assistant that automates software issue analysis using Retrieval-Augmented Generation (RAG), semantic search, vector databases, and local Large Language Models.

## Overview

Large software projects receive thousands of issue reports describing bugs, feature requests, performance problems, and security concerns. Manually reviewing and categorizing these issues is time-consuming.

This project automates the issue triage process by retrieving similar historical issues, analyzing the submitted issue, estimating severity, and generating actionable recommendations.

## Features

* Semantic similarity search over historical software issues
* Retrieval-Augmented Generation (RAG)
* Automatic issue categorization
* Severity assessment
* Duplicate issue estimation
* Issue summarization
* Resolution recommendations
* REST API using FastAPI
* Local LLM inference using Ollama

## Tech Stack

### Backend

* Python
* FastAPI

### AI / NLP

* Sentence Transformers
* Ollama
* Qwen

### Retrieval

* ChromaDB
* Vector Embeddings

### Dataset

* GitHub Issues Dataset (VS Code Issues)

## System Architecture

User Issue
↓
Embedding Generation
↓
ChromaDB Vector Search
↓
Retrieve Similar Issues
↓
Local LLM (Qwen via Ollama)
↓
Issue Analysis
↓
Structured Triage Report

## Project Structure

```text
issue-triage-assistant/
│
├── api/
│   └── main.py
│
├── rag/
│   ├── analyze.py
│   ├── retrieve.py
│   ├── vectordb.py
│   ├── models.py
│   └── models_ollama.py
│
├── scripts/
│   └── download_issues.py
│
├── data/
│
├── test_pipeline.py
├── requirements.txt
└── README.md
```

## Sample Input

```text
Title:
Login fails after password reset

Description:
After resetting the password, users cannot log in.
The system displays "Invalid Credentials" even when the new password is entered correctly.
```

## Sample Output

```json
{
  "category": "Authentication",
  "severity": "Critical",
  "duplicate_probability": "Low",
  "summary": "Users cannot log in after resetting their password and receive invalid credential errors.",
  "resolution": "Verify password reset workflow, credential storage, and authentication validation logic."
}
```

## Installation

### Clone Repository

```bash
git clone https://github.com/YOUR_USERNAME/issue-triage-assistant.git
cd issue-triage-assistant
```

### Create Virtual Environment

```bash
python -m venv venv
```

### Activate Environment

Windows:

```bash
venv\Scripts\activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

## Install Ollama

Download Ollama:

https://ollama.com

Pull the model:

```bash
ollama pull qwen3:4b
```

## Run FastAPI Backend

```bash
uvicorn api.main:app --reload
```

Open:

```text
http://127.0.0.1:8000/docs
```

## Future Improvements

* Streamlit Frontend
* Advanced Duplicate Detection
* LangGraph Multi-Agent Workflow
* Docker Deployment
* Issue Assignment Recommendations

## Author

Keerthi Reddy
