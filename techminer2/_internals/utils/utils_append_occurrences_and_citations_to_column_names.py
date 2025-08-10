# flake8: noqa
# pylint: disable=too-many-arguments
# pylint: disable=line-too-long
"""
This module implements 




"""
from .utils_compute_occurrences_and_citations import \
    _utils_compute_occurrences_and_citations


def _utils_append_occurrences_and_citations_to_column_names(
    criterion,
    table,
    name,
    #
    # DATABASE PARAMS
    root_dir: str,
    database: str,
    year_filter: tuple,
    cited_by_filter: tuple,
    **filters,
):
    """:meta private:"""
    new_column_names = _utils_compute_occurrences_and_citations(
        criterion=criterion,
        #
        # DATABASE PARAMS
        root_dir=root_dir,
        database=database,
        year_filter=year_filter,
        cited_by_filter=cited_by_filter,
        **filters,
    )
    table[name] = table[name].map(new_column_names)
    return table
