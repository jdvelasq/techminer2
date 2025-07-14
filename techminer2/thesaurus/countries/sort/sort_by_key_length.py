# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
# pylint: disable=too-many-statements
# pylint: disable=too-many-branches
"""
Sort by Key Length
===============================================================================


Example:
    >>> import sys
    >>> from io import StringIO
    >>> from techminer2.thesaurus.countries import InitializeThesaurus, SortByKeyLength

    >>> # Redirect stderr to capture output
    >>> original_stderr = sys.stderr
    >>> sys.stderr = StringIO()

    >>> # Create thesaurus
    >>> InitializeThesaurus(root_directory="example/", quiet=True).run()

    >>> # Sort thesaurus by key length
    >>> sorter = (
    ...     SortByKeyLength(use_colorama=False)
    ...     .where_root_directory_is("example/")
    ... )
    >>> sorter.run()

    >>> # Capture and print stderr output
    >>> output = sys.stderr.getvalue()
    >>> sys.stderr = original_stderr
    >>> print(output)
    Sorting thesaurus by key length...
      File : example/data/thesaurus/countries.the.txt
      Sorting process completed successfully
    <BLANKLINE>
    Printing thesaurus header
      File : example/data/thesaurus/countries.the.txt
    <BLANKLINE>
        Brunei Darussalam
          Universiti Brunei Darussalam, School of Business and Economics, Jln Tungk...
        United Kingdom
          Bristol Business School, University of the West of England, Bristol, Unit...
        United States
          Baylor University, United States; Columbia Graduate School of Business, U...
        Netherlands
          Erasmus University Rotterdam, Burgemeester Oudlaan, Rotterdam, 50, Nether...
        South Korea
          College of Business Administration, Soongsil University, South Korea; Dep...
        Switzerland
          Department of Informatics, University of Zurich, Binzmuehlestrasse 14, Zu...
        Kazakhstan
          Department of Accounting and Finance, Bang College of Business, KIMEP Uni...
        Australia
          Centre for Law, Markets & Regulation, UNSW Australia, Australia; Charles ...
    <BLANKLINE>
    <BLANKLINE>

/Volum


"""
from ...._internals.mixins import ParamsMixin
from ...user import SortByKeyLength as UserSortByKeyLength


class SortByKeyLength(
    ParamsMixin,
):
    """:meta private:"""

    def run(self):
        return (
            UserSortByKeyLength()
            .update(**self.params.__dict__)
            .with_thesaurus_file("countries.the.txt")
            .run()
        )
