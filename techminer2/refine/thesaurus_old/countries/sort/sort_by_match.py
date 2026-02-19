# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
# pylint: disable=too-many-statements
# pylint: disable=too-many-branches
"""
Sort By Match
===============================================================================


Smoke tests:
    >>> from techminer2.refine.thesaurus_old.countries import InitializeThesaurus
    >>> (
    ...     InitializeThesaurus()
    ...     .where_root_directory("examples/tests/")
    ... ).run()

    >>> from techminer2.refine.thesaurus_old.countries import SortByMatch
    >>> (
    ...     SortByMatch()
    ...     #
    ...     # THESAURUS:
    ...     .having_pattern("china")
    ...     .having_case_sensitive(False)
    ...     .having_regex_flags(0)
    ...     .having_regex_search(False)
    ...     #
    ...     # DATABASE:
    ...     .where_root_directory("examples/tests/")
    ...     #
    ...     .run()
    ... )

    >>> from techminer2.refine.thesaurus_old.countries import PrintHeader
    >>> (
    ...     PrintHeader()
    ...     .using_colored_output(False)
    ...     .where_root_directory("examples/tests/")
    ... ).run()
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
from techminer2._internals import ParamsMixin
from techminer2.refine.thesaurus_old.user import SortByMatch as UserSortByMatch


class SortByMatch(
    ParamsMixin,
):
    """:meta private:"""

    # -------------------------------------------------------------------------
    def run(self):
        return (
            UserSortByMatch()
            .update(**self.params.__dict__)
            .with_thesaurus_file("countries.the.txt")
            .run()
        )


# ===============================================================================
