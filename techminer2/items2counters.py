"""items2counters utility function"""

import numpy as np

from .column_indicators import column_indicators


def items2counters(
    column,
    directory,
    database,
    use_filter,
):
    """Creates a dictionary to transform a 'item' to a 'item counter:counter'."""

    indicators = column_indicators(
        column=column,
        directory=directory,
        database=database,
        use_filter=use_filter,
    )

    num_docs = indicators.num_documents.values
    cited_by = indicators.global_citations.values
    n_zeros_docs = int(np.log10(max(num_docs))) + 1
    n_zeros_cited_by = int(np.log10(max(cited_by))) + 1

    fmt = "{} {:0" + str(n_zeros_docs) + "d}:{:0" + str(n_zeros_cited_by) + "d}"
    return {
        name: fmt.format(name, int(nd), int(tc))
        for name, nd, tc in zip(indicators.index, num_docs, cited_by)
    }
