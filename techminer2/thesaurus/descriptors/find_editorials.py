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


>>> from techminer2.thesaurus.descriptors import FindEditorials
>>> (
...     FindEditorials()
...     #
...     # DATABASE:
...     .where_root_directory_is("example/")
...     #
...     .build()
... )
<BLANKLINE>
Thesaurus sorting by exact key match completed successfully: ...riptors.the.txt


"""
from ..._internals.mixins import ParamsMixin
from .sort_thesaurus_by_key_exact_match import SortThesaurusByKeyExactMatch

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


class FindEditorials(
    ParamsMixin,
):
    """:meta private:"""

    # -------------------------------------------------------------------------
    def build(self):
        """:meta private:"""

        (
            SortThesaurusByKeyExactMatch().update(**self.params.__dict__)
            #
            # THESAURUS:
            .having_keys_like(EDITORIALS)
            #
            .build()
        )
