import pandas as pd  # type: ignore
from sklearn.metrics.pairwise import cosine_similarity  # type: ignore


def compute_cosine_similarity(matrix):
    """Computes cosine similarity between rows of a matrix."""

    similarity = cosine_similarity(matrix)

    df = pd.DataFrame(
        similarity,
        columns=matrix.columns,
        index=matrix.index,
    )

    return df
