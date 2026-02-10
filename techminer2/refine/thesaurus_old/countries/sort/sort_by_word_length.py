# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
# pylint: disable=too-many-statements
# pylint: disable=too-many-branches
"""
Sort by Word Length
===============================================================================


Example:
    >>> from techminer2.refine.thesaurus_old.countries import InitializeThesaurus
    >>> (
    ...     InitializeThesaurus()
    ...     .where_root_directory("examples/small/")
    ... ).run()

    >>> from techminer2.refine.thesaurus_old.countries import SortByWordLength
    >>> (
    ...     SortByWordLength()
    ...     .where_root_directory("examples/small/")
    ...     .run()
    ... )

    >>> from techminer2.refine.thesaurus_old.countries import PrintHeader
    >>> (
    ...     PrintHeader()
    ...     .using_colored_output(False)
    ...     .where_root_directory("examples/small/")
    ... ).run()
    Netherlands
      Erasmus University Rotterdam, Burgemeester Oudlaan, Rotterdam, 50, Nether...
    Switzerland
      Department of Informatics, University of Zurich, Binzmuehlestrasse 14, Zu...
    Brunei Darussalam
      Universiti Brunei Darussalam, School of Business and Economics, Jln Tungk...
    Kazakhstan
      Department of Accounting and Finance, Bang College of Business, KIMEP Uni...
    Australia
      Centre for Law, Markets & Regulation, UNSW Australia, Australia; Charles ...
    Indonesia
      Department of Management, Faculty of Economics and Business, Universitas ...
    Singapore
      School of Information Systems, Singapore Management University (SMU), Sin...
    Slovenia
      Faculty of Economics, University of Ljubljana, Kardeljeva pl. 17, Ljublja...
    <BLANKLINE>


"""
from techminer2._internals import ParamsMixin
from techminer2.refine.thesaurus_old.user import (
    SortByWordLength as UserSortByWordLength,
)


class SortByWordLength(
    ParamsMixin,
):
    """:meta private:"""

    def run(self):
        return (
            UserSortByWordLength()
            .update(**self.params.__dict__)
            .with_thesaurus_file("countries.the.txt")
            .run()
        )
