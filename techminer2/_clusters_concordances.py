"""Clusters summarization"""
import os
import shutil

from ._create_directory import create_directory
from .tlab.concordances.concordances import concordances


def clusters_concordances(
    communities,
    directory_for_concordances,
    n_keywords=10,
    n_abstracts=50,
    directory="./",
    start_year=None,
    end_year=None,
    **filters,
):
    """Clusters summarization."""

    create_directory(
        base_dir=directory,
        target_dir=directory_for_concordances,
    )

    communities = communities.head(n_keywords)
    for i_community, community_name in enumerate(communities):
        path = os.path.join(
            directory,
            "reports",
            directory_for_concordances,
            "CL_{:02d}".format(i_community),
        )
        os.makedirs(path)

        community = communities[community_name].tolist()
        community = [x for x in community if x != ""]
        community = [" ".join(x.split()[:-1]) for x in community]

        for i_member, member in enumerate(community):
            concordances(
                search_for=member,
                top_n=n_abstracts,
                quiet=True,
                directory=directory,
                start_year=start_year,
                end_year=end_year,
                **filters,
            )

            src_file = os.path.join(directory, "reports/concordances.txt")
            member = member.replace("/", "_")
            dst_file = os.path.join(
                path, "{:02d}_".format(i_member) + member.replace(" ", "_") + ".txt"
            )
            shutil.copyfile(src_file, dst_file)
