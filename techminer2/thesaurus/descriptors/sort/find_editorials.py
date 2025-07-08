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

Example:
    >>> import sys
    >>> from io import StringIO
    >>> from techminer2.thesaurus.descriptors import CreateThesaurus, FindEditorials

    >>> # Redirecting stderr to avoid messages
    >>> original_stderr = sys.stderr
    >>> sys.stderr = StringIO()

    >>> # Create the thesaurus
    >>> CreateThesaurus(root_directory="example/", quiet=True).run()

    >>> # Configure and run the finder
    >>> finder = (
    ...     FindEditorials()
    ...     #
    ...     # DATABASE:
    ...     .where_root_directory_is("example/")
    ...     #
    ...     .run()
    ... )

    >>> # Capture and print stderr output
    >>> output = sys.stderr.getvalue()
    >>> sys.stderr = original_stderr
    >>> print(output)
    Reducing thesaurus keys
      File : example/data/thesaurus/descriptors.the.txt
      Keys reduced from 1726 to 1726
      Keys reduction completed successfully
    <BLANKLINE>
    Sorting thesaurus file by word match
      File : example/data/thesaurus/descriptors.the.txt
      Word : ['CONFERENCE', 'EDP_SCIENCES', 'ELSEVIER', 'EMERALD', 'FRANCIS', 'GMBH', 'IAEME_PUBLICATIONS', 'IEEE', 'IEOM_SOCIETY', 'INDERSCIENCE', 'INFORMA_UK', 'INTERNATIONAL_SOLAR_ENERGY_SOCIETY', 'IOS_PRESS', 'JOHN_WILEY', 'MDPI', 'NOVA_SCIENCE_PUBLISHERS', 'PROCEEDINGS', 'SCITEPRESS_SCIENCE', 'SONS_LTD', 'SPRINGER', 'SPRINGERVERLAG', 'VERLAG', 'WILEYVCH', 'WIT_PRESS', 'OXFORD_UNIVERSITY_PRESS', 'HENRY_STEWART_PUBLICATIONS', 'MACMILLAN', 'EXCLUSIVE_LICENSE', 'PRESS', 'PUBLISHERS']
      1 matching keys found
      Thesaurus sorting by word match completed successfully
    <BLANKLINE>
    Printing thesaurus header
      File : example/data/thesaurus/descriptors.the.txt
    <BLANKLINE>
        POPULAR_PRESS
          POPULAR_PRESS
        A_A_THEORY
          A_A_THEORY
        A_BASIC_RANDOM_SAMPLING_STRATEGY
          A_BASIC_RANDOM_SAMPLING_STRATEGY
        A_BEHAVIOURAL_PERSPECTIVE
          A_BEHAVIOURAL_PERSPECTIVE
        A_BETTER_UNDERSTANDING
          A_BETTER_UNDERSTANDING
        A_BLOCKCHAIN_IMPLEMENTATION_STUDY
          A_BLOCKCHAIN_IMPLEMENTATION_STUDY
        A_CASE_STUDY
          A_CASE_STUDY
        A_CHALLENGE
          A_CHALLENGE
    <BLANKLINE>
    <BLANKLINE>

"""
from ...._internals.mixins import ParamsMixin
from ..._internals import ThesaurusMixin
from .sort_by_word_key_match import SortByWordKeyMatch

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
    def run(self):
        """:meta private:"""

        (
            SortByWordKeyMatch().update(**self.params.__dict__)
            #
            # THESAURUS:
            .having_pattern(EDITORIALS)
            #
            .run()
        )
