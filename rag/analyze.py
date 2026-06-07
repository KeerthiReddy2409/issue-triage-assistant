# rag/analyze.py

import json

from rag.retrieve import retrieve_similar_issues
from rag.models_ollama import generate_response

def build_context(results):
    context = ""

    for doc in results["documents"][0]:
        context += doc[:250]
        context += "\n\n"

    return context


def analyze_issue(title, description):
    
    issue_text = f"""
Title: {title}

Description:
{description}
"""
    
    # Retrieve similar issues
    retrieved = retrieve_similar_issues(issue_text)
    
    # Build context
    context = build_context(retrieved)
    
    prompt = f"""
You are an AI Issue Triage Assistant.

Current Issue:
{issue_text}

Similar Historical Issues:
{context}

Tasks:

1. Determine the issue category using ONLY one of:

- Authentication
- UI/UX
- Backend
- Database
- Performance
- Security
- API
- Feature Request
- Bug

2. Determine severity:
- Critical
- High
- Medium
- Low

3. Estimate duplicate probability:
- High
- Medium
- Low

4. Generate a short summary.

5. Suggest a possible resolution.

Return ONLY valid JSON.

{{
    "category": "",
    "severity": "",
    "duplicate_probability": "",
    "summary": "",
    "resolution": ""
}}
"""
    
    response = generate_response(prompt)
    
    cleaned = (
        response
        .replace("```json", "")
        .replace("```", "")
        .strip()
    )
    
    return json.loads(cleaned)