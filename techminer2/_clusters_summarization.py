"""Clusters summarization"""
import os

from ._create_directory import create_directory
from .techminer2.reports.tm2__extractive_summarization import (
    tm2__extractive_summarization,
)


def clusters_summarization(
    criterion,
    communities,
    directory_for_summarization,
    n_keywords=10,
    n_abstracts=50,
    n_phrases_per_algorithm=50,
    directory="./",
    database="documents",
    start_year=None,
    end_year=None,
    **filters,
):
    """Clusters summarization."""

    create_directory(
        base_directory=directory,
        target_directory=directory_for_summarization,
    )

    communities = communities.head(n_keywords)
    for community_name in communities:

        community = communities[community_name].tolist()
        community = [x for x in community if x != ""]
        community = [" ".join(x.split()[:-1]) for x in community]

        file_name = os.path.join(directory_for_summarization, community_name + ".txt")
        tm2__extractive_summarization(
            criterion,
            custom_topics=community,
            file_name=file_name,
            n_abstracts=n_abstracts,
            n_phrases_per_algorithm=n_phrases_per_algorithm,
            directory=directory,
            database=database,
            start_year=start_year,
            end_year=end_year,
            **filters,
        )
