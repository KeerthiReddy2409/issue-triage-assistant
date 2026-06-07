import requests
import pandas as pd
from tqdm import tqdm
import os
from dotenv import load_dotenv

load_dotenv()

TOKEN = os.getenv("GITHUB_TOKEN")

OWNER = "microsoft"
REPO = "vscode"

headers = {
    "Authorization": f"token {TOKEN}",
    "Accept": "application/vnd.github+json"
}

issues_data = []

page = 1

while len(issues_data) < 10000:
    url = (
        f"https://api.github.com/repos/"
        f"{OWNER}/{REPO}/issues"
        f"?state=all&per_page=100&page={page}"
    )

    response = requests.get(url, headers=headers)

    if response.status_code != 200:
        print("Error:", response.status_code)
        print(response.text)
        break

    issues = response.json()

    if not issues:
        break

    for issue in issues:

        if "pull_request" in issue:
            continue

        issues_data.append({
            "issue_id": issue["number"],
            "title": issue["title"],
            "body": issue["body"],
            "labels": ",".join(
                [label["name"] for label in issue["labels"]]
            ),
            "state": issue["state"],
            "created_at": issue["created_at"],
            "closed_at": issue["closed_at"]
        })

        if len(issues_data) >= 1000:
            break

    print(f"Collected: {len(issues_data)} issues")
    page += 1

df = pd.DataFrame(issues_data)

df.to_csv(
    "data/vscode_issues_10k.csv",
    index=False
)

print("Saved", len(df), "issues")