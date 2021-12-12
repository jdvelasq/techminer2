"""
Co-occurrence Matrix
===============================================================================

>>> from techminer import *
>>> directory = "/workspaces/techminer-api/data/"
>>> co_occurrence_matrix(column='authors', min_occ=3,directory=directory)
authors           Wojcik D Rabbani MR Hornuf L
#d                       5          3        3
#c                     19         39       110
authors    #d #c                              
Wojcik D   5  19         5          0        0
Rabbani MR 3  39         0          3        0
Hornuf L   3  110        0          0        3



"""
from .occurrence_matrix import occurrence_matrix

# pyltin: disable=c0103
# pylint: disable=too-many-arguments
# pylint: disable=invalid-name


def co_occurrence_matrix(
    column,
    min_occ=1,
    max_occ=None,
    normalization=None,
    scheme=None,
    directory="./",
):

    return occurrence_matrix(
        column,
        min_occ=min_occ,
        max_occ=max_occ,
        normalization=normalization,
        scheme=scheme,
        directory=directory,
    )
