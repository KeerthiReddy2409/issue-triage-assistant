from fastapi import FastAPI
from pydantic import BaseModel

from rag.analyze import analyze_issue

app = FastAPI()


class IssueRequest(BaseModel):
    title: str
    description: str


@app.post("/analyze")
def analyze(request: IssueRequest):

    try:
        result = analyze_issue(
            request.title,
            request.description
        )
        print("ANALYSIS COMPLETE")
        print(type(result))
        print(result)

        return result

    except Exception as e:
        print("ERROR:", e)
        return {
            "status": "error",
            "message": str(e)
        }