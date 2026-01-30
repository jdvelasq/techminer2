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
    >>> from techminer2.thesaurus.countries import InitializeThesaurus
    >>> (
    ...     InitializeThesaurus()
    ...     .where_root_directory("examples/small/")
    ... ).run()


    >>> from techminer2.thesaurus.countries import SortByKeyLength
    >>> (
    ...     SortByKeyLength()
    ...     .where_root_directory("examples/small/")
    ...     .run()
    ... )

    >>> from techminer2.thesaurus.countries import PrintHeader
    >>> (
    ...     PrintHeader()
    ...     .using_colored_output(False)
    ...     .where_root_directory("examples/small/")
    ... ).run()
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



"""
from techminer2._internals import ParamsMixin
from techminer2.thesaurus.user import SortByKeyLength as UserSortByKeyLength


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
