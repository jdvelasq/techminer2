"""Clusters summarization"""
import glob
import os
import shutil

from .tm2__abstracts_report import tm2__abstracts_report


def cluster_abstracts_report(
    criterion,
    communities,
    directory_for_abstracts,
    n_keywords=10,
    n_abstracts=30,
    directory="./",
    database="documents",
    start_year=None,
    end_year=None,
    **filters,
):
    """Clusters summarization."""

    _delete_directory(directory_for_abstracts, directory)

    communities = communities.head(n_keywords)
    for community_name in communities:

        community = communities[community_name].tolist()
        community = [x for x in community if x != ""]
        community = [" ".join(x.split()[:-1]) for x in community]

        file_name = os.path.join(directory_for_abstracts, community_name + ".txt")

        tm2__abstracts_report(
            criterion=criterion,
            custom_topics=community,
            file_name=file_name,
            n_abstracts=n_abstracts,
            use_textwrap=True,
            directory=directory,
            database=database,
            start_year=start_year,
            end_year=end_year,
            **filters,
        )


def _delete_directory(directory_for_abstracts, directory):
    path = os.path.join(directory, "reports", directory_for_abstracts)
    if os.path.exists(path):
        files = glob.glob(path + "/*.txt")
        for file in files:
            os.remove(file)
    else:
        os.makedirs(path)
