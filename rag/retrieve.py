from rag.vectordb import collection
from rag.models import embedding_model


def retrieve_similar_issues(
    query,
    n_results=3
):

    query_embedding = embedding_model.encode(
        query
    )

    results = collection.query(
        query_embeddings=[
            query_embedding.tolist()
        ],
        n_results=n_results
    )

    return results