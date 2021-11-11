"""
Cross-correlation matrix
===============================================================================


>>> from techminer import *
>>> directory = "/workspaces/techminer-api/tests/data/"
>>> cross_corr_matrix(directory, column='authors', min_occ=5, by='countries', min_occ_by=6)
authors                    Rabbani MR  Arner DW Reyes-Mercado P  Wojcik D  \\
#d                                 10        9                7         7    
#c                                 69         135             0        49    
authors          #d #c                                                      
Rabbani MR       10 69   1.000000e+00 -0.080748       -0.036886 -0.064826   
Arner DW         9  135 -8.074833e-02  1.000000       -0.044677  0.223477   
Reyes-Mercado P  7  0   -3.688556e-02 -0.044677        1.000000 -0.035867   
Wojcik D         7  49  -6.482601e-02  0.223477       -0.035867  1.000000   
Buckley RP       7  132 -8.053002e-02  0.989334       -0.044556  0.174684   
Khan S           6  49   9.898058e-01 -0.080823       -0.036920 -0.064886   
Ozili PK         6  151 -4.494666e-02 -0.015554       -0.024868  0.191633   
Gozman DP        6  26  -1.087213e-02  0.485357       -0.036092  0.607481   
Serrano W        6  15  -3.688556e-02  0.114883       -0.020408  0.929787   
Wonglimpiyarat J 6  52   1.449377e-01 -0.063837       -0.029161 -0.051249   
Schwienbacher A  6  50   3.491265e-02 -0.013089       -0.028975 -0.050923   
Ashta A          5  9   -1.010496e-02  0.086841       -0.033545  0.344161   
Faccia A         5  27  -1.112141e-02  0.039449       -0.036920  0.704597   
Tan B            5  105  3.145632e-17  0.683477       -0.036886  0.184505   
Mention A-L      5  35  -8.673582e-02  0.281181       -0.047989  0.106476   
Nieves EH        5  15  -2.006233e-02 -0.076371       -0.034886 -0.061312   
Baber H          5  12  -3.688556e-02 -0.044677       -0.020408 -0.035867   
Hamdan A         5  18   7.971921e-01 -0.066022       -0.030159 -0.053004   
Zetzsche DA      5  44  -8.357650e-02  0.966161       -0.046241  0.171766   
.
authors                 Buckley RP    Khan S  Ozili PK Gozman DP Serrano W  \\
#d                               7         6         6         6         6    
#c                             132        49        151       26        15    
authors          #d #c                                                       
Rabbani MR       10 69   -0.080530  0.989806 -0.044947 -0.010872 -0.036886   
Arner DW         9  135   0.989334 -0.080823 -0.015554  0.485357  0.114883   
Reyes-Mercado P  7  0    -0.044556 -0.036920 -0.024868 -0.036092 -0.020408   
Wojcik D         7  49    0.174684 -0.064886  0.191633  0.607481  0.929787   
Buckley RP       7  132   1.000000 -0.080605 -0.032576  0.512187  0.044556   
Khan S           6  49   -0.080605  1.000000 -0.044988 -0.019951 -0.036920   
Ozili PK         6  151  -0.032576 -0.044988  1.000000  0.065970  0.223814   
Gozman DP        6  26    0.512187 -0.019951  0.065970  1.000000  0.415061   
Serrano W        6  15    0.044556 -0.036920  0.223814  0.415061  1.000000   
Wonglimpiyarat J 6  52   -0.063665  0.167053 -0.035533 -0.051571 -0.029161   
Schwienbacher A  6  50   -0.007029  0.044652 -0.035307  0.091098 -0.028975   
Ashta A          5  9     0.073238 -0.004495  0.049960  0.407590  0.339182   
Faccia A         5  27   -0.013434  0.025974  0.142463  0.274776  0.732242   
Tan B            5  105   0.708664 -0.011121 -0.044947  0.804538 -0.036886   
Mention A-L      5  35    0.326644 -0.086816 -0.058477  0.539176 -0.047989   
Nieves EH        5  15   -0.076165 -0.063112 -0.042510 -0.061697 -0.034886   
Baber H          5  12   -0.044556 -0.036920 -0.024868 -0.036092 -0.020408   
Hamdan A         5  18   -0.065844  0.797931 -0.036750 -0.053336 -0.030159   
Zetzsche DA      5  44    0.985525 -0.083654 -0.029515  0.453678  0.063857   
.
authors                 Wonglimpiyarat J Schwienbacher A   Ashta A  Faccia A  \\
#d                                     6               6         5         5    
#c                                    52              50         9        27    
authors          #d #c                                                         
Rabbani MR       10 69          0.144938        0.034913 -0.010105 -0.011121   
Arner DW         9  135        -0.063837       -0.013089  0.086841  0.039449   
Reyes-Mercado P  7  0          -0.029161       -0.028975 -0.033545 -0.036920   
Wojcik D         7  49         -0.051249       -0.050923  0.344161  0.704597   
Buckley RP       7  132        -0.063665       -0.007029  0.073238 -0.013434   
Khan S           6  49          0.167053        0.044652 -0.004495  0.025974   
Ozili PK         6  151        -0.035533       -0.035307  0.049960  0.142463   
Gozman DP        6  26         -0.051571        0.091098  0.407590  0.274776   
Serrano W        6  15         -0.029161       -0.028975  0.339182  0.732242   
Wonglimpiyarat J 6  52          1.000000        0.188606  0.085213 -0.052753   
Schwienbacher A  6  50          0.188606        1.000000  0.893149 -0.052418   
Ashta A          5  9           0.085213        0.893149  1.000000  0.220268   
Faccia A         5  27         -0.052753       -0.052418  0.220268  1.000000   
Tan B            5  105        -0.052705       -0.052369  0.107786 -0.066728   
Mention A-L      5  35         -0.068571       -0.068134  0.050010 -0.086816   
Nieves EH        5  15         -0.049848       -0.049530 -0.057343 -0.063112   
Baber H          5  12         -0.029161       -0.028975 -0.033545 -0.036920   
Hamdan A         5  18         -0.043093       -0.042819 -0.049573  0.002273   
Zetzsche DA      5  44         -0.066073        0.003821  0.064748 -0.000664   
.
authors                         Tan B Mention A-L Nieves EH   Baber H  \\
#d                                  5           5         5         5    
#c                                105          35        15        12    
authors          #d #c                                                  
Rabbani MR       10 69   3.145632e-17   -0.086736 -0.020062 -0.036886   
Arner DW         9  135  6.834769e-01    0.281181 -0.076371 -0.044677   
Reyes-Mercado P  7  0   -3.688556e-02   -0.047989 -0.034886 -0.020408   
Wojcik D         7  49   1.845048e-01    0.106476 -0.061312 -0.035867   
Buckley RP       7  132  7.086642e-01    0.326644 -0.076165 -0.044556   
Khan S           6  49  -1.112141e-02   -0.086816 -0.063112 -0.036920   
Ozili PK         6  151 -4.494666e-02   -0.058477 -0.042510 -0.024868   
Gozman DP        6  26   8.045380e-01    0.539176 -0.061697 -0.036092   
Serrano W        6  15  -3.688556e-02   -0.047989 -0.034886 -0.020408   
Wonglimpiyarat J 6  52  -5.270463e-02   -0.068571 -0.049848 -0.029161   
Schwienbacher A  6  50  -5.236897e-02   -0.068134 -0.049530 -0.028975   
Ashta A          5  9    1.077863e-01    0.050010 -0.057343 -0.033545   
Faccia A         5  27  -6.672848e-02   -0.086816 -0.063112 -0.036920   
Tan B            5  105  1.000000e+00    0.551028 -0.063053 -0.036886   
Mention A-L      5  35   5.510276e-01    1.000000  0.027637 -0.047989   
Nieves EH        5  15  -6.305304e-02    0.027637  1.000000 -0.034886   
Baber H          5  12  -3.688556e-02   -0.047989 -0.034886  1.000000   
Hamdan A         5  18  -5.450886e-02   -0.070918 -0.051554 -0.030159   
Zetzsche DA      5  44   6.128944e-01    0.271993 -0.079046 -0.046241   
.
authors                  Hamdan A Zetzsche DA  
#d                              5           5   
#c                             18          44   
authors          #d #c                         
Rabbani MR       10 69   0.797192   -0.083577  
Arner DW         9  135 -0.066022    0.966161  
Reyes-Mercado P  7  0   -0.030159   -0.046241  
Wojcik D         7  49  -0.053004    0.171766  
Buckley RP       7  132 -0.065844    0.985525  
Khan S           6  49   0.797931   -0.083654  
Ozili PK         6  151 -0.036750   -0.029515  
Gozman DP        6  26  -0.053336    0.453678  
Serrano W        6  15  -0.030159    0.063857  
Wonglimpiyarat J 6  52  -0.043093   -0.066073  
Schwienbacher A  6  50  -0.042819    0.003821  
Ashta A          5  9   -0.049573    0.064748  
Faccia A         5  27   0.002273   -0.000664  
Tan B            5  105 -0.054509    0.612894  
Mention A-L      5  35  -0.070918    0.271993  
Nieves EH        5  15  -0.051554   -0.079046  
Baber H          5  12  -0.030159   -0.046241  
Hamdan A         5  18   1.000000   -0.068335  
Zetzsche DA      5  44  -0.068335    1.000000  

"""
import numpy as np
import pandas as pd

from .co_occurrence_matrix import co_occurrence_matrix
from .tf_matrix import tf_matrix
from .utils import index_terms2counters, load_filtered_documents

# pyltin: disable=c0103
# pylint: disable=too-many-arguments
# pylint: disable=invalid-name


def cross_corr_matrix(
    directory,
    column,
    by=None,
    method="pearson",
    min_occ=1,
    max_occ=None,
    min_occ_by=1,
    max_occ_by=None,
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

    co_occ_matrix = co_occurrence_matrix(
        directory=directory,
        column=column,
        by=by,
        min_occ=min_occ,
        max_occ=max_occ,
        min_occ_by=min_occ_by,
        max_occ_by=max_occ_by,
        scheme=scheme,
        sep=sep,
    )

    matrix = co_occ_matrix.corr(method=method)
    matrix = matrix.fillna(0)

    # repair NaN values in cross-correlation matrix
    np.fill_diagonal(matrix.values, 1.0)

    return matrix
