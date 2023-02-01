"""items2counters utility function"""

import numpy as np

from ._load_stopwords import load_stopwords
from .tm2__indicators_by_topic import tm2__indicators_by_topic


def items2counters(
    column,
    directory,
    database,
    start_year,
    end_year,
    **filters,
):
    """Creates a dictionary to transform a 'item' to a 'item counter:counter'."""

    indicators = tm2__indicators_by_topic(
        criterion=column,
        directory=directory,
        database=database,
        start_year=start_year,
        end_year=end_year,
        **filters,
    )

    ###
    num_docs = indicators.OCC.values
    cited_by = indicators.global_citations.values
    # stopwords = load_stopwords(directory)

    # num_docs = [
    #     value
    #     for value, index in zip(indicators.OCC.values, indicators.index)
    #     if index not in stopwords
    # ]
    # cited_by = [
    #     value
    #     for value, index in zip(indicators.global_citations.values, indicators.index)
    #     if index not in stopwords
    # ]
    n_zeros_docs = int(np.log10(max(num_docs))) + 1
    n_zeros_cited_by = int(np.log10(max(cited_by))) + 1

    fmt = "{} {:0" + str(n_zeros_docs) + "d}:{:0" + str(n_zeros_cited_by) + "d}"
    return {
        name: fmt.format(name, int(nd), int(tc))
        for name, nd, tc in zip(
            indicators.index, indicators.OCC.values, indicators.global_citations.values
        )
    }
