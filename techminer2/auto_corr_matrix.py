"""
Auto-correlation Matrix
===============================================================================

Returns an auto-correlation matrix.

>>> from techminer2 import *
>>> directory = "/workspaces/techminer2/data/"
>>> auto_corr_matrix(
...     column='authors', 
...     min_occ=3, 
...     directory=directory,
... )
authors            Wojcik D Rabbani MR  Hornuf L
#d                        5          3         3
#c                      19         39        110
authors    #d #c                                
Wojcik D   5  19   1.000000  -0.559017 -0.559017
Rabbani MR 3  39  -0.559017   1.000000 -0.375000
Hornuf L   3  110 -0.559017  -0.375000  1.000000


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
