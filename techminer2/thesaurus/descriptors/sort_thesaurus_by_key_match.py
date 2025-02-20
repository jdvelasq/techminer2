# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
# pylint: disable=too-many-statements
# pylint: disable=too-many-branches
"""
Sort Thesaurus by Key Match
===============================================================================

Finds a string in the terms of a thesaurus.


>>> from techminer2.thesaurus.descriptors import SortThesaurusByKeyMatch
>>> (
...     SortThesaurusByKeyMatch()
...     # 
...     # THESAURUS:
...     .having_keys_like("ARTIFICIAL_INTELLIGENCE")
...     .having_keys_starting_with(None)
...     .having_keys_ending_with(None)
...     #
...     # DATABASE:
...     .where_directory_is("example/")
...     #
...     .build()
... ) 
Sorting thesaurus file by key match.
      Thesaurus file: example/thesaurus/descriptors.the.txt
           Keys like: ARTIFICIAL_INTELLIGENCE
  Keys starting with: None
    Keys ending with: None
  2 matching keys found
Printing thesaurus header
  Loading example/thesaurus/descriptors.the.txt thesaurus file
  Header:
    ARTIFICIAL_INTELLIGENCE
      ARTIFICIAL_INTELLIGENCE
    EXPERT_LEVEL_ARTIFICIAL_INTELLIGENCE
      EXPERT_LEVEL_ARTIFICIAL_INTELLIGENCE
    'BEST_PRACTICE_ERP_PACKAGES
      'BEST_PRACTICE_ERP_PACKAGES
    'FRAUD
      'FRAUD
    3D_NAVIGATION
      3D_NAVIGATION
    3G_CELLULAR
      3G_CELLULAR
    3G_CELLULAR_COMMUNICATIONS
      3G_CELLULAR_COMMUNICATIONS
    3_D_TRAJECTORY
      3_D_TRAJECTORY


>>> (
...     SortThesaurusByKeyMatch()
...     # 
...     # THESAURUS:
...     .having_keys_like(None)
...     .having_keys_starting_with("ARTIFICIAL_INTELLIGENCE")
...     .having_keys_ending_with(None)
...     #
...     # DATABASE:
...     .where_directory_is("example/")
...     #
...     .build()
... ) 
Sorting thesaurus file by key match.
      Thesaurus file: example/thesaurus/descriptors.the.txt
           Keys like: None
  Keys starting with: ARTIFICIAL_INTELLIGENCE
    Keys ending with: None
  1 matching keys found
Printing thesaurus header
  Loading example/thesaurus/descriptors.the.txt thesaurus file
  Header:
    ARTIFICIAL_INTELLIGENCE
      ARTIFICIAL_INTELLIGENCE
    'BEST_PRACTICE_ERP_PACKAGES
      'BEST_PRACTICE_ERP_PACKAGES
    'FRAUD
      'FRAUD
    3D_NAVIGATION
      3D_NAVIGATION
    3G_CELLULAR
      3G_CELLULAR
    3G_CELLULAR_COMMUNICATIONS
      3G_CELLULAR_COMMUNICATIONS
    3_D_TRAJECTORY
      3_D_TRAJECTORY
    4TH_GENERATION_MOBILE
      4TH_GENERATION_MOBILE




>>> (
...     SortThesaurusByKeyMatch()
...     # 
...     # THESAURUS:
...     .having_keys_like(None)
...     .having_keys_starting_with(None)
...     .having_keys_ending_with("ARTIFICIAL_INTELLIGENCE")
...     #
...     # DATABASE:
...     .where_directory_is("example/")
...     #
...     .build()
... ) 
Sorting thesaurus file by key match.
      Thesaurus file: example/thesaurus/descriptors.the.txt
           Keys like: None
  Keys starting with: None
    Keys ending with: ARTIFICIAL_INTELLIGENCE
  2 matching keys found
Printing thesaurus header
  Loading example/thesaurus/descriptors.the.txt thesaurus file
  Header:
    ARTIFICIAL_INTELLIGENCE
      ARTIFICIAL_INTELLIGENCE
    EXPERT_LEVEL_ARTIFICIAL_INTELLIGENCE
      EXPERT_LEVEL_ARTIFICIAL_INTELLIGENCE
    'BEST_PRACTICE_ERP_PACKAGES
      'BEST_PRACTICE_ERP_PACKAGES
    'FRAUD
      'FRAUD
    3D_NAVIGATION
      3D_NAVIGATION
    3G_CELLULAR
      3G_CELLULAR
    3G_CELLULAR_COMMUNICATIONS
      3G_CELLULAR_COMMUNICATIONS
    3_D_TRAJECTORY
      3_D_TRAJECTORY


"""
from ..._internals.mixins import ParamsMixin
from ..user.sort_thesaurus_by_key_match import (
    SortThesaurusByKeyMatch as SortUserThesaurusByKeyMatch,
)


class SortThesaurusByKeyMatch(
    ParamsMixin,
):
    """:meta private:"""

    def build(self):
        return (
            SortUserThesaurusByKeyMatch()
            .update(**self.params.__dict__)
            .with_thesaurus_file("descriptors.the.txt")
            .build()
        )
