# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
# pylint: disable=too-many-statements
# pylint: disable=too-many-branches
"""
Sort By Ends With Key Match
===============================================================================


>>> # TEST PREPARATION
>>> import sys
>>> from io import StringIO
>>> old_stderr = sys.stderr
>>> sys.stderr = StringIO()
>>> #
>>> from techminer2.thesaurus.countries import CreateThesaurus
>>> CreateThesaurus(root_directory="example/", quiet=True).run()


>>> from techminer2.thesaurus.countries import SortByEndsWithKeyMatch
>>> (
...     SortByEndsWithKeyMatch()
...     # 
...     # THESAURUS:
...     .having_pattern("Darussalam")
...     #
...     # DATABASE:
...     .where_root_directory_is("example/")
...     #
...     .run()
... ) 



>>> # TEST EXECUTION
>>> output = sys.stderr.getvalue()
>>> sys.stderr = old_stderr
>>> print(output)
Sorting thesaurus file by key match
     File : example/thesaurus/countries.the.txt
  Pattern : Darussalam
  1 matching keys found
  Thesaurus sorting by key match completed successfully
<BLANKLINE>
Printing thesaurus header
  File : example/thesaurus/countries.the.txt
<BLANKLINE>
    Brunei Darussalam
      Universiti Brunei Darussalam, School of Business and Economics, Jln Tungk...
    Australia
      Centre for Law, Markets & Regulation, UNSW Australia, Australia; Charles ...
    Belgium
      Brussels, Belgium
    China
      Cheung Kong Graduate School of Business, and Institute of Internet Financ...
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
from ...user import SortByEndsWithKeyMatch as UserSortByStartsWithKeyMatch


class SortByEndsWithKeyMatch(
    ParamsMixin,
):
    """:meta private:"""

    # -------------------------------------------------------------------------
    def run(self):
        return (
            UserSortByStartsWithKeyMatch()
            .update(**self.params.__dict__)
            .with_thesaurus_file("countries.the.txt")
            .run()
        )


# =============================================================================
