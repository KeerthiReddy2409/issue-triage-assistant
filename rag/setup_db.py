import pandas as pd
import chromadb

from sentence_transformers import SentenceTransformer


def create_vector_database():

    df = pd.read_csv("data/vscode_issues_clean.csv")

    model = SentenceTransformer(
        "all-MiniLM-L6-v2"
    )

    embeddings = model.encode(
        df["document"].tolist(),
        show_progress_bar=True
    )

    client = chromadb.PersistentClient(
        path="chroma_db"
    )

    collection = client.get_or_create_collection(
        name="vscode_rag"
    )

    if collection.count() > 0:
        print("Collection already exists")
        return

    collection.add(
        ids=[str(i) for i in range(len(df))],
        documents=df["document"].tolist(),
        embeddings=embeddings.tolist(),
        metadatas=[
            {
                "issue_id": int(row["issue_id"]),
                "title": row["title"]
            }
            for _, row in df.iterrows()
        ]
    )

    print("Vector database created")


if __name__ == "__main__":
    create_vector_database()