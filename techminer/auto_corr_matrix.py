"""
Auto-correlation matrix
===============================================================================

Returns an auto-correlation matrix.

>>> from techminer import *
>>> directory = "/workspaces/techminer-api/tests/data/"
>>> auto_corr_matrix(directory, column='authors', min_occ=6)
authors                 Rabbani MR  Arner DW  ...  Surjandy Schwienbacher A
#d                              10        9   ...        6               6 
#c                             72        154  ...       19              56 
authors          #d #c                        ...                          
Rabbani MR       10 72    1.000000 -0.119334  ... -0.095658       -0.095658
Arner DW         9  154  -0.119334  1.000000  ... -0.090181       -0.090181
Buckley RP       7  151  -0.103951  0.871096  ... -0.078556       -0.078556
Tan B            7  113  -0.103951 -0.097998  ... -0.078556       -0.078556
Reyes-Mercado P  7  0    -0.103951 -0.097998  ... -0.078556       -0.078556
Gozman DP        7  91   -0.103951 -0.097998  ... -0.078556       -0.078556
Wojcik D         7  51   -0.103951 -0.097998  ... -0.078556       -0.078556
Khan S           6  50    0.755701 -0.090181  ... -0.072289       -0.072289
Serrano W        6  15   -0.095658 -0.090181  ... -0.072289       -0.072289
Fernando E       6  19   -0.095658 -0.090181  ...  1.000000       -0.072289
Wonglimpiyarat J 6  55   -0.095658 -0.090181  ... -0.072289       -0.072289
Ashta A          6  41   -0.095658 -0.090181  ... -0.072289       -0.072289
Ozili PK         6  143  -0.095658 -0.090181  ... -0.072289       -0.072289
Giudici P        6  35   -0.095658 -0.090181  ... -0.072289       -0.072289
Zetzsche D       6  67   -0.095658  0.652974  ... -0.072289       -0.072289
Surjandy         6  19   -0.095658 -0.090181  ...  1.000000       -0.072289
Schwienbacher A  6  56   -0.095658 -0.090181  ... -0.072289        1.000000
<BLANKLINE>
[17 rows x 17 columns]


"""


from .tf_matrix import tf_matrix

# pyltin: disable=c0103
# pylint: disable=too-many-arguments
# pylint: disable=invalid-name


def auto_corr_matrix(
    directory,
    column,
    method="pearson",
    min_occ=1,
    max_occ=None,
    scheme=None,
    sep="; ",
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
