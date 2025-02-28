# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
# pylint: disable=too-many-statements
# pylint: disable=too-many-branches
"""
Sort by Fuzzy Key Match
===============================================================================

>>> from techminer2.thesaurus.countries import CreateThesaurus
>>> CreateThesaurus(root_directory="example/", quiet=True).run()


>>> from techminer2.thesaurus.countries import SortByFuzzyKeyMatch
>>> (
...     SortByFuzzyKeyMatch()
...     # 
...     # THESAURUS:
...     .having_pattern("china")
...     .having_match_threshold(90)
...     #
...     # DATABASE:
...     .where_root_directory_is("example/")
...     #
...     .run()
... ) 
Sorting thesaurus by fuzzy match
            File : example/thesaurus/countries.the.txt
       Keys like : china
  Match thresold : 90
  1 matching keys found
  Thesaurus sorting completed successfully
<BLANKLINE>
Printing thesaurus header
  File : example/thesaurus/countries.the.txt
<BLANKLINE>
    China
      Cheung Kong Graduate School of Business, and Institute of Internet Financ...
    Australia
      Centre for Law, Markets & Regulation, UNSW Australia, Australia; Charles ...
    Belgium
      Brussels, Belgium
    Brunei Darussalam
      Universiti Brunei Darussalam, School of Business and Economics, Jln Tungk...
    Denmark
      Copenhagen Business School, Department of IT Management, Howitzvej 60, Fr...
    France
      SKEMA Business School, Lille, France; University of Lille Nord de France,...
    Germany
      CESifo, Poschingerstr. 5, Munich, 81679, Germany; Chair of e-Finance, Goe...
    Ghana
      University of the Free State and University of Ghana Business School, Uni...
<BLANKLINE>



"""
from ...._internals.mixins import ParamsMixin
from ...user import SortByFuzzyKeyMatch as UserSortByFuzzyKeyMatch


class SortByFuzzyKeyMatch(
    ParamsMixin,
):
    """:meta private:"""

    # -------------------------------------------------------------------------
    def run(self):
        return (
            UserSortByFuzzyKeyMatch()
            .update(**self.params.__dict__)
            .with_thesaurus_file("countries.the.txt")
            .run()
        )


# =============================================================================
