"""
Auto-correlation matrix
===============================================================================

Returns an auto-correlation matrix.

>>> from techminer import *
>>> directory = "/workspaces/techminer-api/data/"
>>> auto_corr_matrix(column='authors', min_occ=6, directory=directory)
authors                Rabbani MR Reyes-Mercado P    Khan S  Arner DW
#d                              8               7         6         6
#c                            65              0         52        125
authors         #d #c                                                
Rabbani MR      8  65    1.000000       -0.554700  0.806226 -0.496139
Reyes-Mercado P 7  0    -0.554700        1.000000 -0.447214 -0.447214
Khan S          6  52    0.806226       -0.447214  1.000000 -0.400000
Arner DW        6  125  -0.496139       -0.447214 -0.400000  1.000000



"""


from .tf_matrix import tf_matrix

# pyltin: disable=c0103
# pylint: disable=too-many-arguments
# pylint: disable=invalid-name


def auto_corr_matrix(
    column,
    method="pearson",
    min_occ=1,
    max_occ=None,
    scheme=None,
    sep="; ",
    directory="./",
):
    """
    Returns a co-occurrence matrix.

    :param directory_or_records:
        A directory or a list of records.
    :param column:
        The column to be used.
    :param by:
        The column to be used to group the records.
    :param min_occurrence:
        The minimum occurrence of a word.
    :param max_occurrence:
        The maximum occurrence of a word.
    :param stopwords:
        A list of stopwords.
    :param scheme:
        The scheme to be used.
    :param sep:
        The separator to be used.
    :return:
        A co-occurrence matrix.
    """

    doc_term_matrix = tf_matrix(
        directory=directory,
        column=column,
        min_occ=min_occ,
        max_occ=max_occ,
        scheme=scheme,
        sep=sep,
    )
    matrix = doc_term_matrix.corr(method=method)

    return matrix
