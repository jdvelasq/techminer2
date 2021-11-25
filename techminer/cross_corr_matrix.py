"""
Cross-correlation matrix
===============================================================================


>>> from techminer import *
>>> directory = "/workspaces/techminer-api/tests/data/"
>>> cross_corr_matrix(directory, column='authors', min_occ=5, by='countries', min_occ_by=6)
authors                 Rabbani MR  Arner DW  ... Muthukannan P   Baber H
#d                              10        9   ...            5         5 
#c                             72        154  ...           8         12 
authors          #d #c                        ...                        
Rabbani MR       10 72    1.000000 -0.125643  ...      0.007419 -0.056425
Arner DW         9  154  -0.125643  1.000000  ...      0.487629 -0.065492
Buckley RP       7  151  -0.125288  0.988869  ...      0.553878 -0.065307
Tan B            7  113  -0.041177  0.642972  ...      0.942981 -0.048293
Reyes-Mercado P  7  0    -0.056425 -0.065492  ...     -0.034806 -0.029412
Gozman DP        7  91   -0.051628  0.467819  ...      0.851188 -0.051376
Wojcik D         7  51   -0.100093  0.196608  ...      0.215309 -0.052174
Khan S           6  50    0.987690 -0.129220  ...     -0.007044 -0.058031
Serrano W        6  15   -0.056425  0.098238  ...     -0.034806 -0.029412
Fernando E       6  19   -0.056425 -0.065492  ...     -0.034806 -0.029412
Wonglimpiyarat J 6  55    0.121495 -0.094013  ...     -0.049964 -0.042220
Ashta A          6  41   -0.044445  0.038690  ...      0.105095 -0.046334
Ozili PK         6  143  -0.068904 -0.039988  ...     -0.042504 -0.035916
Giudici P        6  35   -0.025103 -0.004856  ...     -0.067102 -0.056702
Zetzsche D       6  67   -0.133777  0.928413  ...      0.418912 -0.069732
Surjandy         6  19   -0.056425 -0.065492  ...     -0.034806 -0.029412
Schwienbacher A  6  56    0.008941 -0.041513  ...     -0.049640 -0.041946
Fenwick M        5  11   -0.053063  0.002566  ...     -0.060010 -0.050709
Nieves EH        5  16   -0.053063 -0.112915  ...     -0.060010 -0.050709
Faccia A         5  29   -0.045829  0.004987  ...     -0.063608 -0.053750
Hamdan A         5  18    0.789328 -0.097293  ...     -0.051707 -0.043693
Okoli TT         5  4    -0.076608 -0.088919  ...     -0.047257 -0.039933
Grobys K         5  30   -0.011129 -0.077504  ...     -0.041190 -0.034806
Kauffman RJ      5  511   0.042387 -0.012300  ...     -0.071903  0.132566
Mention A-L      5  37   -0.135415  0.247322  ...      0.633045 -0.070586
Iman N           5  69   -0.056425 -0.065492  ...     -0.034806 -0.029412
Hornuf L         5  165  -0.074100  0.221163  ...     -0.045709 -0.038625
Muthukannan P    5  8     0.007419  0.487629  ...      1.000000 -0.034806
Baber H          5  12   -0.056425 -0.065492  ...     -0.034806  1.000000
<BLANKLINE>
[29 rows x 29 columns]



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
