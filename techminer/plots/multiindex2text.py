import numpy as np


def multindex2text(index):

    """
    Converts a MultiIndex into a string.

    Parameters
    ----------
    index : pandas.MultiIndex
        The MultiIndex to convert.

    Returns
    -------
    str
        The string representation of the MultiIndex.

    """

    names = [tuple_[0].title() for tuple_ in index]
    num_docs = [tuple_[1] for tuple_ in index]
    cited_by = [tuple_[2] for tuple_ in index]
    n_zeros_docs = int(np.log10(max(num_docs))) + 1
    n_zeros_cited_by = int(np.log10(max(cited_by))) + 1

    fmt = "{} {:0" + str(n_zeros_docs) + "d}:{:0" + str(n_zeros_cited_by) + "d}"
    text = [
        fmt.format(name, int(nd), int(tc))
        for name, nd, tc in zip(names, num_docs, cited_by)
    ]

    return text
