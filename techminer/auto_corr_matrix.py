"""
Auto-correlation matrix
===============================================================================

Returns an auto-correlation matrix.

>>> from techminer import *
>>> directory = "/workspaces/techminer-api/tests/data/"
>>> auto_corr_matrix(directory, column='authors', min_occ=6)
authors                 Rabbani MR  Arner DW Reyes-Mercado P  Wojcik D  \\
#d                              10        9               7         7    
#c                             69        135             0         49    
authors          #d #c                                                   
Rabbani MR       10 69    1.000000 -0.177332       -0.153574 -0.153574   
Arner DW         9  135  -0.177332  1.000000       -0.144338 -0.144338   
Reyes-Mercado P  7  0    -0.153574 -0.144338        1.000000 -0.125000   
Wojcik D         7  49   -0.153574 -0.144338       -0.125000  1.000000   
Buckley RP       7  132  -0.153574  0.866025       -0.125000 -0.125000   
Khan S           6  49    0.746924 -0.132453       -0.114708 -0.114708   
Ozili PK         6  151  -0.140929 -0.132453       -0.114708 -0.114708   
Gozman DP        6  26   -0.140929 -0.132453       -0.114708 -0.114708   
Serrano W        6  15   -0.140929 -0.132453       -0.114708 -0.114708   
Wonglimpiyarat J 6  52   -0.140929 -0.132453       -0.114708 -0.114708   
Schwienbacher A  6  50   -0.140929 -0.132453       -0.114708 -0.114708   
.
authors                 Buckley RP    Khan S  Ozili PK Gozman DP Serrano W  \\
#d                              7         6         6         6         6    
#c                             132       49        151       26        15    
authors          #d #c                                                       
Rabbani MR       10 69   -0.153574  0.746924 -0.140929 -0.140929 -0.140929   
Arner DW         9  135   0.866025 -0.132453 -0.132453 -0.132453 -0.132453   
Reyes-Mercado P  7  0    -0.125000 -0.114708 -0.114708 -0.114708 -0.114708   
Wojcik D         7  49   -0.125000 -0.114708 -0.114708 -0.114708 -0.114708   
Buckley RP       7  132   1.000000 -0.114708 -0.114708 -0.114708 -0.114708   
Khan S           6  49   -0.114708  1.000000 -0.105263 -0.105263 -0.105263   
Ozili PK         6  151  -0.114708 -0.105263  1.000000 -0.105263 -0.105263   
Gozman DP        6  26   -0.114708 -0.105263 -0.105263  1.000000 -0.105263   
Serrano W        6  15   -0.114708 -0.105263 -0.105263 -0.105263  1.000000   
Wonglimpiyarat J 6  52   -0.114708 -0.105263 -0.105263 -0.105263 -0.105263   
Schwienbacher A  6  50   -0.114708 -0.105263 -0.105263 -0.105263 -0.105263   
.
authors                 Wonglimpiyarat J Schwienbacher A  
#d                                    6               6   
#c                                   52              50   
authors          #d #c                                    
Rabbani MR       10 69         -0.140929       -0.140929  
Arner DW         9  135        -0.132453       -0.132453  
Reyes-Mercado P  7  0          -0.114708       -0.114708  
Wojcik D         7  49         -0.114708       -0.114708  
Buckley RP       7  132        -0.114708       -0.114708  
Khan S           6  49         -0.105263       -0.105263  
Ozili PK         6  151        -0.105263       -0.105263  
Gozman DP        6  26         -0.105263       -0.105263  
Serrano W        6  15         -0.105263       -0.105263  
Wonglimpiyarat J 6  52          1.000000       -0.105263  
Schwienbacher A  6  50         -0.105263        1.000000  

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
