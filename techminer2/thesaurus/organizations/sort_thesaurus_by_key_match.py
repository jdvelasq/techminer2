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


>>> from techminer2.thesaurus.organizations import SortThesaurusByKeyMatch
>>> (
...     SortThesaurusByKeyMatch()
...     # 
...     # THESAURUS:
...     .having_keys_like("MIT")
...     .having_keys_starting_with(None)
...     .having_keys_ending_with(None)
...     #
...     # DATABASE:
...     .where_directory_is("example/")
...     #
...     .build()
... ) 
Sorting thesaurus file by key match.
      Thesaurus file: example/thesaurus/organizations.the.txt
           Keys like: MIT
  Keys starting with: None
    Keys ending with: None
  21 matching keys found
Printing thesaurus header
  Loading example/thesaurus/organizations.the.txt thesaurus file
  Header:
    Department of Economics, MIT, 50 Memorial Drive E5...
      Department of Economics, MIT, 50 Memorial Drive E52-371, Cambridge, MA...
    Graduate School of Business, RMIT University, Melb...
      Graduate School of Business, RMIT University, Melbourne, Australia
    MIT Center, USA (unknown)
      MIT Center, United States
    MIT Laboratory for Financial Engineering, USA (unk...
      MIT Laboratory for Financial Engineering, United States
    MIT Media Lab, 77 Massachusetts Avenue, Cambridge,...
      MIT Media Lab, 77 Massachusetts Avenue, Cambridge, MA  02139, United S...
    MIT Media Lab, Cambridge, MA 02139, USA (unknown)
      MIT Media Lab, Cambridge, MA 02139, United States
    MIT Media Lab, Cambridge, MA, USA (unknown)
      MIT Media Lab, Cambridge, MA, United States
    MIT Sloan School of Management and Department of E...
      MIT Sloan School of Management and Department of Economics, Massachuse...

>>> from techminer2.thesaurus.organizations import SortThesaurusByKeyMatch
>>> (
...     SortThesaurusByKeyMatch()
...     # 
...     # THESAURUS:
...     .having_keys_like(None)
...     .having_keys_starting_with("National")
...     .having_keys_ending_with(None)
...     #
...     # DATABASE:
...     .where_directory_is("example/")
...     #
...     .build()
... ) 
Sorting thesaurus file by key match.
      Thesaurus file: example/thesaurus/organizations.the.txt
           Keys like: None
  Keys starting with: National
    Keys ending with: None
  20 matching keys found
Printing thesaurus header
  Loading example/thesaurus/organizations.the.txt thesaurus file
  Header:
    National Agricultural Research Laboratories, Kampa...
      National Agricultural Research Laboratories, Kampala, Uganda
    National Bereau of Economics Research, Evanston, I...
      National Bereau of Economics Research, Evanston, IL, United States
    National Bureau for Economic Research, USA (unknow...
      National Bureau for Economic Research, United States
    National Bureau of Economic Researc, USA (unknown)
      National Bureau of Economic Researc, United States
    National Bureau of Economic Research, 1050 Massach...
      National Bureau of Economic Research, 1050 Massachusetts Avenue, Cambr...
    National Bureau of Economic Research, Ambridge, MA...
      National Bureau of Economic Research, Ambridge, MA  02138, United Stat...
    National Bureau of Economic Research, Cambridge, M...
      National Bureau of Economic Research, Cambridge, MA  02138, United Sta...
    National Bureau of Economic Research, Cambridge, M...
      National Bureau of Economic Research, Cambridge, MA 02138, United Stat...


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
            .with_thesaurus_file("organizations.the.txt")
            .build()
        )
