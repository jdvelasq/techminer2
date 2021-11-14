"""
Cross-correlation matrix
===============================================================================


>>> from techminer import *
>>> directory = "/workspaces/techminer-api/tests/data/"
>>> cross_corr_matrix(directory, column='authors', min_occ=5, by='countries', min_occ_by=6)
authors                 Rabbani MR  Arner DW Reyes-Mercado P  Wojcik D  \\
#d                              10        9               7         7    
#c                             69        135             0         49    
authors          #d #c                                                   
Rabbani MR       10 69    1.000000 -0.137159       -0.061130 -0.108886   
Arner DW         9  135  -0.137159  1.000000       -0.074790  0.184455   
Reyes-Mercado P  7  0    -0.061130 -0.074790        1.000000 -0.059374   
Wojcik D         7  49   -0.108886  0.184455       -0.059374  1.000000   
Buckley RP       7  132  -0.136765  0.988656       -0.074575  0.133243   
Khan S           6  49    0.989371 -0.137292       -0.061189 -0.108991   
Ozili PK         6  151  -0.074720 -0.050932       -0.040743  0.169708   
Gozman DP        6  26   -0.052972  0.459728       -0.059761  0.591604   
Serrano W        6  15   -0.061130  0.090817       -0.033333  0.931711   
Wonglimpiyarat J 6  52    0.116506 -0.107578       -0.047946 -0.085403   
Schwienbacher A  6  50    0.002912 -0.054286       -0.047633 -0.084845   
Ashta A          5  9    -0.049098  0.043893       -0.055391  0.319602   
Faccia A         5  27   -0.054238 -0.010624       -0.061189  0.692375   
Tan B            5  105  -0.042601  0.667670       -0.061130  0.150765   
Mention A-L      5  35   -0.148057  0.231755       -0.080733  0.057911   
Nieves EH        5  15   -0.061072 -0.129434       -0.057687 -0.102753   
Baber H          5  12   -0.061130 -0.074790       -0.033333 -0.059374   
Hamdan A         5  18    0.790758 -0.111362       -0.049633 -0.088407   
Zetzsche DA      5  44   -0.142287  0.963963       -0.077586  0.128580   
.
authors                 Buckley RP    Khan S  Ozili PK Gozman DP Serrano W  \\
#d                              7         6         6         6         6    
#c                             132       49        151       26        15    
authors          #d #c                                                       
Rabbani MR       10 69   -0.136765  0.989371 -0.074720 -0.052972 -0.061130   
Arner DW         9  135   0.988656 -0.137292 -0.050932  0.459728  0.090817   
Reyes-Mercado P  7  0    -0.074575 -0.061189 -0.040743 -0.059761 -0.033333   
Wojcik D         7  49    0.133243 -0.108991  0.169708  0.591604  0.931711   
Buckley RP       7  132   1.000000 -0.136897 -0.068548  0.488012  0.017898   
Khan S           6  49   -0.136897  1.000000 -0.074792 -0.062470 -0.061189   
Ozili PK         6  151  -0.068548 -0.074792  1.000000  0.040176  0.211866   
Gozman DP        6  26    0.488012 -0.062470  0.040176  1.000000  0.403390   
Serrano W        6  15    0.017898 -0.061189  0.211866  0.403390  1.000000   
Wonglimpiyarat J 6  52   -0.107268  0.139356 -0.058605 -0.085960 -0.047946   
Schwienbacher A  6  50   -0.047837  0.012954 -0.058222  0.061677 -0.047633   
Ashta A          5  9     0.029742 -0.043308  0.025577  0.385277  0.326192   
Faccia A         5  27   -0.066167 -0.015601  0.118421  0.244546  0.729174   
Tan B            5  105   0.694217 -0.054238 -0.074720  0.796406 -0.061130   
Mention A-L      5  35    0.280494 -0.148200 -0.098680  0.515110 -0.080733   
Nieves EH        5  15   -0.129062 -0.105896 -0.070511 -0.103424 -0.057687   
Baber H          5  12   -0.074575 -0.061189 -0.040743 -0.059761 -0.033333   
Hamdan A         5  18   -0.111042  0.791522 -0.060667 -0.088984 -0.049633   
Zetzsche DA      5  44    0.984618 -0.142424 -0.066835  0.425581  0.036946   
.
authors                 Wonglimpiyarat J Schwienbacher A   Ashta A  Faccia A  \\
#d                                    6               6         5         5    
#c                                   52              50        9         27    
authors          #d #c                                                         
Rabbani MR       10 69          0.116506        0.002912 -0.049098 -0.054238   
Arner DW         9  135        -0.107578       -0.054286  0.043893 -0.010624   
Reyes-Mercado P  7  0          -0.047946       -0.047633 -0.055391 -0.061189   
Wojcik D         7  49         -0.085403       -0.084845  0.319602  0.692375   
Buckley RP       7  132        -0.107268       -0.047837  0.029742 -0.066167   
Khan S           6  49          0.139356        0.012954 -0.043308 -0.015601   
Ozili PK         6  151        -0.058605       -0.058222  0.025577  0.118421   
Gozman DP        6  26         -0.085960        0.061677  0.385277  0.244546   
Serrano W        6  15         -0.047946       -0.047633  0.326192  0.729174   
Wonglimpiyarat J 6  52          1.000000        0.167481  0.057542 -0.088014   
Schwienbacher A  6  50          0.167481        1.000000  0.890233 -0.087439   
Ashta A          5  9           0.057542        0.890233  1.000000  0.190181   
Faccia A         5  27         -0.088014       -0.087439  0.190181  1.000000   
Tan B            5  105        -0.087929       -0.087355  0.073365 -0.112216   
Mention A-L      5  35         -0.116126       -0.115367  0.001754 -0.148200   
Nieves EH        5  15         -0.082977       -0.082435 -0.095861 -0.105896   
Baber H          5  12         -0.047946       -0.047633 -0.055391 -0.061189   
Hamdan A         5  18         -0.071392       -0.070925 -0.082477 -0.032268   
Zetzsche DA      5  44         -0.111600       -0.038130  0.019100 -0.054822   
.
authors                     Tan B Mention A-L Nieves EH   Baber H  Hamdan A  \\
#d                             5           5         5         5         5    
#c                            105         35        15        12        18    
authors          #d #c                                                        
Rabbani MR       10 69  -0.042601   -0.148057 -0.061072 -0.061130  0.790758   
Arner DW         9  135  0.667670    0.231755 -0.129434 -0.074790 -0.111362   
Reyes-Mercado P  7  0   -0.061130   -0.080733 -0.057687 -0.033333 -0.049633   
Wojcik D         7  49   0.150765    0.057911 -0.102753 -0.059374 -0.088407   
Buckley RP       7  132  0.694217    0.280494 -0.129062 -0.074575 -0.111042   
Khan S           6  49  -0.054238   -0.148200 -0.105896 -0.061189  0.791522   
Ozili PK         6  151 -0.074720   -0.098680 -0.070511 -0.040743 -0.060667   
Gozman DP        6  26   0.796406    0.515110 -0.103424 -0.059761 -0.088984   
Serrano W        6  15  -0.061130   -0.080733 -0.057687 -0.033333 -0.049633   
Wonglimpiyarat J 6  52  -0.087929   -0.116126 -0.082977 -0.047946 -0.071392   
Schwienbacher A  6  50  -0.087355   -0.115367 -0.082435 -0.047633 -0.070925   
Ashta A          5  9    0.073365    0.001754 -0.095861 -0.055391 -0.082477   
Faccia A         5  27  -0.112216   -0.148200 -0.105896 -0.061189 -0.032268   
Tan B            5  105  1.000000    0.526909 -0.105793 -0.061130 -0.091022   
Mention A-L      5  35   0.526909    1.000000 -0.023909 -0.080733 -0.120211   
Nieves EH        5  15  -0.105793   -0.023909  1.000000 -0.057687 -0.085896   
Baber H          5  12  -0.061130   -0.080733 -0.057687  1.000000 -0.049633   
Hamdan A         5  18  -0.091022   -0.120211 -0.085896 -0.049633  1.000000   
Zetzsche DA      5  44   0.592861    0.220022 -0.134273 -0.077586 -0.115525   
.
authors                 Zetzsche DA  
#d                               5   
#c                              44   
authors          #d #c               
Rabbani MR       10 69    -0.142287  
Arner DW         9  135    0.963963  
Reyes-Mercado P  7  0     -0.077586  
Wojcik D         7  49     0.128580  
Buckley RP       7  132    0.984618  
Khan S           6  49    -0.142424  
Ozili PK         6  151   -0.066835  
Gozman DP        6  26     0.425581  
Serrano W        6  15     0.036946  
Wonglimpiyarat J 6  52    -0.111600  
Schwienbacher A  6  50    -0.038130  
Ashta A          5  9      0.019100  
Faccia A         5  27    -0.054822  
Tan B            5  105    0.592861  
Mention A-L      5  35     0.220022  
Nieves EH        5  15    -0.134273  
Baber H          5  12    -0.077586  
Hamdan A         5  18    -0.115525  
Zetzsche DA      5  44     1.000000  

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

    return matrix
