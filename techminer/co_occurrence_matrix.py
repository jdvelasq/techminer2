"""
Co-occurrence matrix
===============================================================================

>>> from techminer import *
>>> directory = "/workspaces/techminer-api/tests/data/"
>>> co_occurrence_matrix(directory, column='authors', min_occ=5)
authors                  Rabbani MR Arner DW Wojcik D Buckley RP  \\
#d                               10        9        7          7    
#c                               69      135       49        132   
authors          #d  #c                                           
Rabbani MR       10  69          10        0        0          0   
Arner DW         9   135          0        9        0          7   
Wojcik D         7   49           0        0        7          0   
Buckley RP       7   132          0        7        0          7   
Reyes-Mercado P  7   0            0        0        0          0   
Wonglimpiyarat J 6   52           0        0        0          0   
Gozman DP        6   26           0        0        0          0   
Serrano W        6   15           0        0        0          0   
Khan S           6   49           6        0        0          0   
Schwienbacher A  6   50           0        0        0          0   
Ozili PK         6   151          0        0        0          0   
Tan B            5   105          0        0        0          0   
Zetzsche DA      5   44           0        5        0          5   
Hamdan A         5   18           0        0        0          0   
Nieves EH        5   15           0        0        0          0   
Baber H          5   12           0        0        0          0   
Mention A-L      5   35           0        0        0          0   
Faccia A         5   27           0        0        0          0   
Ashta A          5   9            0        0        0          0   
-
authors                  Reyes-Mercado P Wonglimpiyarat J Gozman DP Serrano W  \\
#d                                     7                6         6         6    
#c                                     0               52        26        15    
authors          #d  #c                                                         
Rabbani MR       10  69                0                0         0         0   
Arner DW         9   135               0                0         0         0   
Wojcik D         7   49                0                0         0         0   
Buckley RP       7   132               0                0         0         0   
Reyes-Mercado P  7   0                 7                0         0         0   
Wonglimpiyarat J 6   52                0                6         0         0   
Gozman DP        6   26                0                0         6         0   
Serrano W        6   15                0                0         0         6   
Khan S           6   49                0                0         0         0 
Schwienbacher A  6   50                0                0         0         0   
Ozili PK         6   151               0                0         0         0   
Tan B            5   105               0                0         1         0   
Zetzsche DA      5   44                0                0         0         0   
Hamdan A         5   18                0                0         0         0   
Nieves EH        5   15                0                0         0         0   
Baber H          5   12                0                0         0         0   
Mention A-L      5   35                0                0         0         0   
Faccia A         5   27                0                0         0         0   
Ashta A          5   9                 0                0         0         0   
-
authors                  Khan S Schwienbacher A Ozili PK Tan B Zetzsche DA  \
#d                            6               6        6     5           5    
#c                           49              50      151   105          44    
authors          #d  #c                                                      
Rabbani MR       10  69       6               0        0     0           0   
Arner DW         9   135      0               0        0     0           5   
Wojcik D         7   49       0               0        0     0           0   
Buckley RP       7   132      0               0        0     0           5   
Reyes-Mercado P  7   0        0               0        0     0           0   
Wonglimpiyarat J 6   52       0               0        0     0           0   
Gozman DP        6   26       0               0        0     1           0   
Serrano W        6   15       0               0        0     0           0   
Khan S           6   49       6               0        0     0           0   
Schwienbacher A  6   50       0               6        0     0           0   
Ozili PK         6   151      0               0        6     0           0   
Tan B            5   105      0               0        0     5           0   
Zetzsche DA      5   44       0               0        0     0           5   
Hamdan A         5   18       0               0        0     0           0   
Nieves EH        5   15       0               0        0     0           0   
Baber H          5   12       0               0        0     0           0   
Mention A-L      5   35       0               0        0     0           0   
Faccia A         5   27       0               0        0     0           0   
Ashta A          5   9        0               0        0     0           0   
-
authors                  Hamdan A Nieves EH Baber H Mention A-L Faccia A  \
#d                              5         5       5           5        5    
#c                             18        15      12          35       27    
authors          #d  #c
Rabbani MR       10  69         0         0       0           0        0
Arner DW         9   135        0         0       0           0        0
Wojcik D         7   49         0         0       0           0        0
Buckley RP       7   132        0         0       0           0        0
Reyes-Mercado P  7   0          0         0       0           0        0
Wonglimpiyarat J 6   52         0         0       0           0        0   
Gozman DP        6   26         0         0       0           0        0   
Serrano W        6   15         0         0       0           0        0
Khan S           6   49         0         0       0           0        0   
Schwienbacher A  6   50         0         0       0           0        0   
Ozili PK         6   151        0         0       0           0        0   
Tan B            5   105        0         0       0           0        0   
Zetzsche DA      5   44         0         0       0           0        0   
Hamdan A         5   18         5         0       0           0        0   
Nieves EH        5   15         0         5       0           0        0   
Baber H          5   12         0         0       5           0        0   
Mention A-L      5   35         0         0       0           5        0   
Faccia A         5   27         0         0       0           0        5   
Ashta A          5   9          0         0       0           0        0   
-
authors                  Ashta A  
#d                             5   
#c                             9    
authors          #d  #c          
Rabbani MR       10  69        0  
Arner DW         9   135       0  
Wojcik D         7   49        0  
Buckley RP       7   132       0  
Reyes-Mercado P  7   0         0  
Wonglimpiyarat J 6   52        0  
Gozman DP        6   26        0  
Serrano W        6   15        0  
Khan S           6   49        0  
Schwienbacher A  6   50        0  
Ozili PK         6   151       0  
Tan B            5   105       0  
Zetzsche DA      5   44        0  
Hamdan A         5   18        0  
Nieves EH        5   15        0  
Baber H          5   12        0  
Mention A-L      5   35        0  
Faccia A         5   27        0  
Ashta A          5   9         5  


"""
import numpy as np
import pandas as pd

from .utils import *
from .utils import index_terms2counters
from .tf_matrix import tf_matrix

# pyltin: disable=c0103
# pylint: disable=too-many-arguments
# pylint: disable=invalid-name


def co_occurrence_matrix(
    directory,
    column,
    by=None,
    min_occ=1,
    max_occ=None,
    min_occ_by=1,
    max_occ_by=None,
    association=None,
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

    if by is None or column == by:
        by = column
        matrix_in_columns = tf_matrix(
            directory=directory,
            column=column,
            min_occ=min_occ,
            max_occ=max_occ,
            scheme=scheme,
            sep=sep,
        )
        matrix_in_columns = matrix_in_columns.dropna()
        matrix_in_rows = matrix_in_columns.copy()
    else:

        matrix_in_columns = tf_matrix(
            directory=directory,
            column=column,
            min_occ=min_occ,
            max_occ=max_occ,
            scheme=scheme,
            sep=sep,
        )

        matrix_in_columns = matrix_in_columns.dropna()

        matrix_in_rows = tf_matrix(
            directory=directory,
            column=by,
            min_occ=min_occ_by,
            max_occ=max_occ_by,
            scheme=scheme,
            sep=sep,
        )

        matrix_in_rows = matrix_in_rows.dropna()

        common_documents = matrix_in_columns.index.intersection(matrix_in_rows.index)
        matrix_in_columns = matrix_in_columns.loc[common_documents, :]
        matrix_in_rows = matrix_in_rows.loc[common_documents, :]

    matrix_values = np.matmul(
        matrix_in_rows.transpose().values, matrix_in_columns.values
    )

    co_occ_matrix = pd.DataFrame(
        matrix_values,
        columns=matrix_in_columns.columns,
        index=matrix_in_rows.columns,
    )

    co_occ_matrix = association_index(
        matrix=co_occ_matrix,
        association=association,
    )

    return co_occ_matrix
