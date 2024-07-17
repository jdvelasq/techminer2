# flake8: noqa
# pylint: disable=too-many-arguments
# pylint: disable=line-too-long
"""
This module implements 




"""
import numpy as np

from ..core.metrics.calculate_global_performance_metrics import calculate_global_performance_metrics


def helper_compute_occurrences_and_citations(
    criterion,
    #
    # DATABASE PARAMS
    root_dir: str,
    database: str,
    year_filter: tuple,
    cited_by_filter: tuple,
    **filters,
):
    """Creates a dictionary to transform a 'item' to a 'item counter:counter'."""

    indicators = calculate_global_performance_metrics(
        field=criterion,
        #
        # DATABASE PARAMS
        root_dir=root_dir,
        database=database,
        year_filter=year_filter,
        cited_by_filter=cited_by_filter,
        **filters,
    )

    names = indicators.index.to_list()
    occ = indicators.OCC.to_list()
    cited_by = indicators.global_citations.to_list()

    n_zeros_occ = int(np.log10(max(occ))) + 1
    n_zeros_cited_by = int(np.log10(max(cited_by))) + 1

    fmt_occ = "{:0" + str(n_zeros_occ) + "d}"
    fmt_cited_by = "{:0" + str(n_zeros_cited_by) + "d}"
    fmt = "{} " + f"{fmt_occ}:{fmt_cited_by}"

    return {name: fmt.format(name, int(nd), int(tc)) for name, nd, tc in zip(names, occ, cited_by)}
