# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
# pylint: disable=too-many-statements
# pylint: disable=too-many-branches
"""
Sort by Starts With Match
===============================================================================


Example:
    >>> import sys
    >>> from io import StringIO
    >>> from techminer2.thesaurus.countries import InitializeThesaurus, SortByStartsWithMatch

    >>> # Redirect stderr to capture output
    >>> original_stderr = sys.stderr
    >>> sys.stderr = StringIO()

    >>> # Create the thesaurus
    >>> InitializeThesaurus(root_directory="examples/fintech/", quiet=True).run()

    >>> sorter = (
    ...     SortByStartsWithMatch(use_colorama=False)
    ...     .having_pattern("Germ")
    ...     .where_root_directory_is("examples/fintech/")
    ... )
    >>> sorter.run()

    >>> # Capture and print stderr output
    >>> output = sys.stderr.getvalue()
    >>> sys.stderr = original_stderr
    >>> print(output)
    Sorting thesaurus by startswith match...
         File : examples/fintech/data/thesaurus/countries.the.txt
      Pattern : Germ
      1 matching keys found
      Sorting process completed successfully
    <BLANKLINE>
    Printing thesaurus header
      File : examples/fintech/data/thesaurus/countries.the.txt
    <BLANKLINE>
        Germany
          CESifo, Poschingerstr. 5, Munich, 81679, Germany; Chair of e-Finance, Goe...
        Australia
          Centre for Law, Markets & Regulation, UNSW Australia, Australia; Charles ...
        Belgium
          Brussels, Belgium
        Brunei Darussalam
          Universiti Brunei Darussalam, School of Business and Economics, Jln Tungk...
        China
          Cheung Kong Graduate School of Business, and Institute of Internet Financ...
        Denmark
          Copenhagen Business School, Department of IT Management, Howitzvej 60, Fr...
        France
          SKEMA Business School, Lille, France; University of Lille Nord de France,...
        Ghana
          University of the Free State and University of Ghana Business School, Uni...
    <BLANKLINE>
    <BLANKLINE>

"""
from techminer2._internals.mixins import ParamsMixin
from techminer2.thesaurus.user import SortByStartsWithMatch as UserSortByStartsWithMatch


class SortByStartsWithMatch(
    ParamsMixin,
):
    """:meta private:"""

    # -------------------------------------------------------------------------
    def run(self):
        return (
            UserSortByStartsWithMatch()
            .update(**self.params.__dict__)
            .with_thesaurus_file("countries.the.txt")
            .run()
        )


# =============================================================================
