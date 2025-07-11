# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
# pylint: disable=too-many-statements
# pylint: disable=too-many-branches
"""
Sort by Alphabet
===============================================================================


Example:
    >>> import sys
    >>> from io import StringIO
    >>> from techminer2.thesaurus.countries import CreateThesaurus, SortByAlphabet

    >>> # Redirect stderr to capture output
    >>> original_stderr = sys.stderr
    >>> sys.stderr = StringIO()

    >>> # Create thesaurus
    >>> CreateThesaurus(root_directory="example/", quiet=True).run()

    >>> # Sort thesaurus by alphabetical order
    >>> sorter = (
    ...     SortByAlphabet()
    ...     .where_root_directory_is("example/")
    ... )
    >>> sorter.run()

    >>> # Capture and print stderr output
    >>> output = sys.stderr.getvalue()
    >>> print(output)
    Reducing thesaurus keys
      File : example/data/thesaurus/countries.the.txt
      Keys reduced from 24 to 24
      Reduction process completed successfully
    <BLANKLINE>
    Sorting thesaurus alphabetically
      File : example/data/thesaurus/countries.the.txt
      Sorting process completed successfully
    <BLANKLINE>
    Printing thesaurus header
      File : example/data/thesaurus/countries.the.txt
    <BLANKLINE>
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
        Germany
          CESifo, Poschingerstr. 5, Munich, 81679, Germany; Chair of e-Finance, Goe...
        Ghana
          University of the Free State and University of Ghana Business School, Uni...
    <BLANKLINE>
    <BLANKLINE>


"""
from ...._internals.mixins import ParamsMixin
from ...user import SortByAlphabet as UserSortByAlphabet


class SortByAlphabet(
    ParamsMixin,
):
    """:meta private:"""

    def run(self):
        return (
            UserSortByAlphabet()
            .update(**self.params.__dict__)
            .with_thesaurus_file("countries.the.txt")
            .run()
        )
