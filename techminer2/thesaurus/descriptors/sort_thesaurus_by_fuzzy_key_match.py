# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
# pylint: disable=too-many-statements
# pylint: disable=too-many-bramcbes
"""
Sort Thesaurus by Fuzzy Key Match
===============================================================================

>>> from techminer2.thesaurus.descriptors import SortThesaurusByFuzzyKeyMatch
>>> (
...     SortThesaurusByFuzzyKeyMatch()
...     # 
...     # THESAURUS:
...     .having_keys_like("INTELIGENCIA")
...     .having_match_threshold(70)
...     #
...     # DATABASE:
...     .where_directory_is("example/")
...     #
...     .build()
... ) 
Sorting thesaurus by fuzzy match
  Thesaurus file: example/thesaurus/descriptors.the.txt
       Keys like: INTELIGENCIA
  Match thresold: 70
  17 matching keys found
Printing thesaurus header
  Loading example/thesaurus/descriptors.the.txt thesaurus file
  Header:
    ANALYTICAL_INTELLIGENCE
      ANALYTICAL_INTELLIGENCE
    ARTIFICIAL_INTELLIGENCE
      ARTIFICIAL_INTELLIGENCE
    BUSINESS_INTELLIGENCE
      BUSINESS_INTELLIGENCE
    BUSINESS_INTELLIGENCE (BI)
      BUSINESS_INTELLIGENCE (BI)
    BUSINESS_INTELLIGENCE_FRAMEWORK
      BUSINESS_INTELLIGENCE_FRAMEWORK
    COLLECTIVE_INTELLIGENCES
      COLLECTIVE_INTELLIGENCE; COLLECTIVE_INTELLIGENCES
    COMPETITIVE_INTELLIGENCE
      COMPETITIVE_INTELLIGENCE
    EMPATHETIC_INTELLIGENCE
      EMPATHETIC_INTELLIGENCE





"""
from ..._internals.mixins import ParamsMixin
from ..user.sort_thesaurus_by_fuzzy_key_match import (
    SortThesaurusByFuzzyKeyMatch as SortUserThesaurusByFuzzyKeyMatch,
)


class SortThesaurusByFuzzyKeyMatch(
    ParamsMixin,
):
    """:meta private:"""

    def build(self):
        return (
            SortUserThesaurusByFuzzyKeyMatch()
            .update(**self.params.__dict__)
            .with_thesaurus_file("descriptors.the.txt")
            .build()
        )
