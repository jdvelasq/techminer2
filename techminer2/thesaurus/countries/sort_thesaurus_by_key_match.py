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

>>> from techminer2.thesaurus.countries import SortThesaurusByKeyMatch
>>> (
...     SortThesaurusByKeyMatch()
...     # 
...     # THESAURUS:
...     .having_keys_like("China")
...     .having_keys_starting_with(None)
...     .having_keys_ending_with(None)
...     #
...     # DATABASE:
...     .where_directory_is("example/")
...     #
...     .build()
... ) 
Sorting thesaurus file by key match.
      Thesaurus file: example/thesaurus/countries.the.txt
           Keys like: China
  Keys starting with: None
    Keys ending with: None
  1 matching keys found
Printing thesaurus header
  Loading example/thesaurus/countries.the.txt thesaurus file
  Header:
    China
      Anhui University of Technology, Maanshan, China; Antai College of Econ...
    Argentina
      Sorin Capital Management, Argentina
    Australia
      Accounting Discipline, Business School, The University of Sydney, Buil...
    Austria
      Agro-Industries Branch, UNIDO, Austria; Department of Business Adminis...
    Belgium
      Brussels, Belgium; CERMi (Centre for European Research in Microfinance...
    Brazil
      Brazilian School of Public and Business Administration, Getulio Vargas...
    Brunei Darussalam
      Centre for Lifelong Learning, Universiti Brunei Darussalam, Gadong, Br...
    Bulgaria
      International University College, 3 Bulgaria Str, 9300 Dobrich, Bulgar...


>>> from techminer2.thesaurus.countries import SortThesaurusByKeyMatch
>>> (
...     SortThesaurusByKeyMatch()
...     # 
...     # THESAURUS:
...     .having_keys_like(None)
...     .having_keys_starting_with("Au")
...     .having_keys_ending_with(None)
...     #
...     # DATABASE:
...     .where_directory_is("example/")
...     #
...     .build()
... ) 
Sorting thesaurus file by key match.
      Thesaurus file: example/thesaurus/countries.the.txt
           Keys like: None
  Keys starting with: Au
    Keys ending with: None
  2 matching keys found
Printing thesaurus header
  Loading example/thesaurus/countries.the.txt thesaurus file
  Header:
    Australia
      Accounting Discipline, Business School, The University of Sydney, Buil...
    Austria
      Agro-Industries Branch, UNIDO, Austria; Department of Business Adminis...
    Argentina
      Sorin Capital Management, Argentina
    Belgium
      Brussels, Belgium; CERMi (Centre for European Research in Microfinance...
    Brazil
      Brazilian School of Public and Business Administration, Getulio Vargas...
    Brunei Darussalam
      Centre for Lifelong Learning, Universiti Brunei Darussalam, Gadong, Br...
    Bulgaria
      International University College, 3 Bulgaria Str, 9300 Dobrich, Bulgar...
    Cambodia
      Future Forum, Phnom Penh, Cambodia; National ICT Development Authority...

>>> from techminer2.thesaurus.countries import SortThesaurusByKeyMatch
>>> (
...     SortThesaurusByKeyMatch()
...     # 
...     # THESAURUS:
...     .having_keys_like(None)
...     .having_keys_starting_with(None)
...     .having_keys_ending_with("ia")
...     #
...     # DATABASE:
...     .where_directory_is("example/")
...     #
...     .build()
... )
Sorting thesaurus file by key match.
      Thesaurus file: example/thesaurus/countries.the.txt
           Keys like: None
  Keys starting with: None
    Keys ending with: ia
  20 matching keys found
Printing thesaurus header
  Loading example/thesaurus/countries.the.txt thesaurus file
  Header:
    Australia
      Accounting Discipline, Business School, The University of Sydney, Buil...
    Austria
      Agro-Industries Branch, UNIDO, Austria; Department of Business Adminis...
    Bulgaria
      International University College, 3 Bulgaria Str, 9300 Dobrich, Bulgar...
    Cambodia
      Future Forum, Phnom Penh, Cambodia; National ICT Development Authority...
    Colombia
      CGIAR Research Program on Climate Change,Agriculture and Food Security...
    Croatia
      Department of Economics and Tourism, Juraj Dobrila University of Pula,...
    Czechia
      Department of Applied Mathematics, Charles University, Prague, Czech R...
    Ethiopia
      Haramaya University, Ethiopia


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
            .with_thesaurus_file("countries.the.txt")
            .build()
        )
