# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
# pylint: disable=too-many-statements


import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity


def compute_cosine_similarity(matrix):
    """Computes cosine similarity between rows of a matrix."""

    similarity = cosine_similarity(matrix)

    term_similarities = []
    for i in range(similarity.shape[0]):
        values_to_sort = []
        for j in range(similarity.shape[1]):
            if i != j and similarity[i, j] > 0:
                values_to_sort.append(
                    (
                        matrix.index[j],
                        similarity[i, j],
                    )
                )
        sorted_values = sorted(values_to_sort, key=lambda x: x[1], reverse=True)
        sorted_values = [f"{x[0]} ({x[1]:>0.3f})" for x in sorted_values]
        sorted_values = "; ".join(sorted_values)
        term_similarities.append(sorted_values)

    term_similarities = pd.DataFrame(
        {"cosine_similariries": term_similarities},
        index=matrix.index,
    )

    return term_similarities
