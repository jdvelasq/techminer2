# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
# pylint: disable=too-many-statements
# pylint: disable=too-many-branches
"""
Sort Thesaurus by Fuzzy Match
===============================================================================

>>> from techminer2.thesaurus.organizations import SortThesaurusByFuzzyKeyMatch
>>> (
...     SortThesaurusByFuzzyKeyMatch()
...     # 
...     # THESAURUS:
...     .having_keys_like("universidad")
...     .having_match_threshold(70)
...     #
...     # DATABASE:
...     .where_directory_is("example/")
...     #
...     .build()
... ) 
Sorting thesaurus by fuzzy match
  Thesaurus file: example/thesaurus/organizations.the.txt
       Keys like: universidad
  Match thresold: 70
  15 matching keys found
Printing thesaurus header
  Loading example/thesaurus/organizations.the.txt thesaurus file
  Header:
    Department of Business Finance, Universitat de Val...
      Department of Business Finance, Universitat de València, València, Spa...
    Department of Marketing, Universitat de València-I...
      Department of Marketing, Universitat de València-Ivie, València, Spain
    Facultad de Ingeniería, Universidad de Talca, CHL ...
      Facultad de Ingeniería, Universidad de Talca, Chile
    Faculty of Administration Sciences, Universidad de...
      Faculty of Administration Sciences, Universidad del Valle, Cali, Colom...
    School of Business, Universidad Adolfo Ibanez, San...
      School of Business, Universidad Adolfo Ibanez, Santiago, Chile
    Universidad de Carabobo, VEN (unknown)
      Universidad de Carabobo, Venezuela
    Universidad de Talca, CHL (unknown)
      Universidad de Talca, Chile
    Universidade Católica Portuguesa, Rua Diogo Botelh...
      Universidade Católica Portuguesa, Rua Diogo Botelho 1327, 4069-005 Por...


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
            .with_thesaurus_file("organizations.the.txt")
            .build()
        )
