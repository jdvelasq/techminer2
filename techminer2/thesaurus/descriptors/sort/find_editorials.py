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

>>> from techminer2.thesaurus.descriptors import CreateThesaurus
>>> CreateThesaurus(root_directory="example/", quiet=True).run()


>>> from techminer2.thesaurus.descriptors import FindEditorials
>>> (
...     FindEditorials()
...     #
...     # DATABASE:
...     .where_root_directory_is("example/")
...     #
...     .build()
... )
Sorting thesaurus file by word match
  File : example/thesaurus/descriptors.the.txt
  Word : ['CONFERENCE', 'EDP_SCIENCES', 'ELSEVIER', 'EMERALD', 'FRANCIS', 'GMBH', 'IAEME_PUBLICATIONS', 'IEEE', 'IEOM_SOCIETY', 'INDERSCIENCE', 'INFORMA_UK', 'INTERNATIONAL_SOLAR_ENERGY_SOCIETY', 'IOS_PRESS', 'JOHN_WILEY', 'MDPI', 'NOVA_SCIENCE_PUBLISHERS', 'PROCEEDINGS', 'SCITEPRESS_SCIENCE', 'SONS_LTD', 'SPRINGER', 'SPRINGERVERLAG', 'VERLAG', 'WILEYVCH', 'WIT_PRESS', 'OXFORD_UNIVERSITY_PRESS', 'HENRY_STEWART_PUBLICATIONS', 'MACMILLAN', 'EXCLUSIVE_LICENSE', 'PRESS', 'PUBLISHERS']
  18 matching keys found
  Thesaurus sorting by word match completed successfully
<BLANKLINE>
Printing thesaurus header
  File : example/thesaurus/descriptors.the.txt
<BLANKLINE>
    ELSEVIER_B
      ELSEVIER_B
    ELSEVIER_INC
      ELSEVIER_INC
    ELSEVIER_LTD
      ELSEVIER_LTD
    EMERALD_GROUP_PUBLISHING
      EMERALD_GROUP_PUBLISHING
    EMERALD_PUBLISHING
      EMERALD_PUBLISHING
    FRANCIS_GROUP
      FRANCIS_GROUP
    INFORMA_UK
      INFORMA_UK
    JOHN_WILEY
      JOHN_WILEY
<BLANKLINE>

"""
from ...._internals.mixins import ParamsMixin
from ..._internals import ThesaurusMixin
from .sort_by_word_match import SortByWordMatch

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
    ThesaurusMixin,
):
    """:meta private:"""

    # -------------------------------------------------------------------------
    def build(self):
        """:meta private:"""

        (
            SortByWordMatch().update(**self.params.__dict__)
            #
            # THESAURUS:
            .having_pattern(EDITORIALS)
            #
            .run()
        )
