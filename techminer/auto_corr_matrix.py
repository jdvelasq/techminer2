"""
Auto-correlation matrix
===============================================================================

Returns an auto-correlation matrix.

>>> from techminer import *
>>> directory = "/workspaces/techminer-api/tests/data/"
>>> auto_corr_matrix(directory, column='authors', min_occ=6)
authors                  Rabbani MR  Arner DW  Wojcik D Buckley RP  \\
#d                               10         9         7          7    
#c                               69       135        49        132   
authors          #nd #tc                                             
Rabbani MR       10  69    1.000000 -0.007449 -0.006565  -0.006565   
Arner DW         9   135  -0.007449  1.000000 -0.006225   0.881226   
Wojcik D         7   49   -0.006565 -0.006225  1.000000  -0.005486   
Buckley RP       7   132  -0.006565  0.881226 -0.005486   1.000000   
Reyes-Mercado P  7   0    -0.006565 -0.006225 -0.005486  -0.005486   
Wonglimpiyarat J 6   52   -0.006075 -0.005761 -0.005077  -0.005077   
Gozman DP        6   26   -0.006075 -0.005761 -0.005077  -0.005077   
Serrano W        6   15   -0.006075 -0.005761 -0.005077  -0.005077   
Khan S           6   49    0.773383 -0.005761 -0.005077  -0.005077   
Schwienbacher A  6   50   -0.006075 -0.005761 -0.005077  -0.005077   
Ozili PK         6   151  -0.006075 -0.005761 -0.005077  -0.005077   
-
authors                  Reyes-Mercado P Wonglimpiyarat J Gozman DP Serrano W  \
#nd                                    7                6         6         6    
#tc                                    0               52        26        15    
authors          #nd #tc                                                        
Rabbani MR       10  69        -0.006565        -0.006075 -0.006075 -0.006075   
Arner DW         9   135       -0.006225        -0.005761 -0.005761 -0.005761   
Wojcik D         7   49        -0.005486        -0.005077 -0.005077 -0.005077   
Buckley RP       7   132       -0.005486        -0.005077 -0.005077 -0.005077   
Reyes-Mercado P  7   0          1.000000        -0.005077 -0.005077 -0.005077   
Wonglimpiyarat J 6   52        -0.005077         1.000000 -0.004699 -0.004699   
Gozman DP        6   26        -0.005077        -0.004699  1.000000 -0.004699   
Serrano W        6   15        -0.005077        -0.004699 -0.004699  1.000000   
Khan S           6   49        -0.005077        -0.004699 -0.004699 -0.004699   
Schwienbacher A  6   50        -0.005077        -0.004699 -0.004699 -0.004699   
Ozili PK         6   151       -0.005077        -0.004699 -0.004699 -0.004699   
-
authors                     Khan S Schwienbacher A  Ozili PK  
#nd                              6               6         6   
#tc                             49              50       151  
authors          #nd #tc                                      
Rabbani MR       10  69   0.773383       -0.006075 -0.006075  
Arner DW         9   135 -0.005761       -0.005761 -0.005761  
Wojcik D         7   49  -0.005077       -0.005077 -0.005077  
Buckley RP       7   132 -0.005077       -0.005077 -0.005077  
Reyes-Mercado P  7   0   -0.005077       -0.005077 -0.005077  
Wonglimpiyarat J 6   52  -0.004699       -0.004699 -0.004699  
Gozman DP        6   26  -0.004699       -0.004699 -0.004699  
Serrano W        6   15  -0.004699       -0.004699 -0.004699  
Khan S           6   49   1.000000       -0.004699 -0.004699  
Schwienbacher A  6   50  -0.004699        1.000000 -0.004699  
Ozili PK         6   151 -0.004699       -0.004699  1.000000  

"""
import numpy as np
import pandas as pd

from .lib import index_terms2counters, load_filtered_documents
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

    # matrix = index_terms2counters(
    #     directory, matrix, axis="columns", column=column, sep=sep
    # )
    # matrix = index_terms2counters(
    #     directory, matrix, axis="index", column=column, sep=sep
    # )

    return matrix
