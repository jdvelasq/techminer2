# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
# pylint: disable=too-many-statements
"""
Find Editorials
===============================================================================


>>> from techminer2.thesaurus.descriptors import find_editorials
>>> find_editorials(
...     #
...     # DATABASE PARAMS:
...     root_dir="example/", 
... )
--INFO-- The file example/thesauri/descriptors.the.txt has been reordered.

"""
from .find_string import find_string

EDITORIALS = [
    "CONFERENCE",
    "EDP_SCIENCES",
    "ELSEVIER",
    "EMERALD",
    "FRANCIS",
    "GMBH",
    "IAEME_PUBLICATIONS",
    "IEEE",
    "IEOM_SOCIETY",
    "INDERSCIENCE",
    "INFORMA_UK",
    "INTERNATIONAL_SOLAR_ENERGY_SOCIETY",
    "IOS_PRESS",
    "JOHN_WILEY",
    "MDPI",
    "NOVA_SCIENCE_PUBLISHERS",
    "PROCEEDINGS",
    "SCITEPRESS_SCIENCE",
    "SONS_LTD",
    "SPRINGER",
    "SPRINGERVERLAG",
    "VERLAG",
    "WILEYVCH",
    "WIT_PRESS",
    "OXFORD_UNIVERSITY_PRESS",
    "HENRY_STEWART_PUBLICATIONS",
    "MACMILLAN",
    "EXCLUSIVE_LICENSE",
    "PRESS",
    "PUBLISHERS",
]


def find_editorials(
    #
    # DATABASE PARAMS:
    root_dir="./",
):
    """:meta private:"""

    find_string(
        #
        # SEARCH PARAMS:
        contains=EDITORIALS,
        startswith=None,
        endswith=None,
        #
        # DATABASE PARAMS:
        root_dir=root_dir,
    )
