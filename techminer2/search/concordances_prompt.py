# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
"""
Concordances Prompt
=========================================================================================


>>> from techminer2.search import concordances_prompt
>>> prompt = concordances_prompt( # doctest: +SKIP
...     search_for='FINTECH',
...     top_n=2,
...     root_dir="example/",
... )
>>> print(prompt) # doctest: +SKIP



"""
from .._core.read_filtered_database import read_filtered_database
from .concordances_prompt_from_records import concordances_prompt_from_records


def concordances_prompt(
    #
    # FUNCTION PARAMS:
    search_for: str,
    top_n: int,
    #
    # DATABASE PARAMS:
    root_dir: str = "./",
    database: str = "main",
    year_filter: tuple = (None, None),
    cited_by_filter: tuple = (None, None),
    **filters,
):
    """Checks the occurrence contexts of a given text in the abstract's phrases."""

    #
    # MAIN CODE:
    #
    records = read_filtered_database(
        root_dir=root_dir,
        database=database,
        year_filter=year_filter,
        cited_by_filter=cited_by_filter,
        **filters,
    )

    return concordances_prompt_from_records(search_for=search_for, top_n=top_n, records=records)
