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
    >>> # TEST PREPARATION
    >>> import sys
    >>> from io import StringIO
    >>> from techminer2.thesaurus.organizations import CreateThesaurus

    >>> # Redirecting stderr to avoid messages
    >>> original_stderr = sys.stderr
    >>> sys.stderr = StringIO()

    >>> # Create thesaurus
    >>> CreateThesaurus(root_directory="example/", quiet=True).run()

    >>> # Create and run the sorter
    >>> from techminer2.thesaurus.organizations import SortByWordLength
    >>> sorter = (
    ...     SortByWordLength()
    ...     #
    ...     # DATABASE:
    ...     .where_root_directory_is("example/")
    ... )
    >>> sorter.run()

    >>> # Capture and print stderr output
    >>> output = sys.stderr.getvalue()
    >>> sys.stderr = original_stderr
    >>> print(output)
    Reducing thesaurus keys
      File : example/data/thesaurus/organizations.the.txt
      Keys reduced from 90 to 90
      Reduction process completed successfully
    <BLANKLINE>
    Sorting thesaurus by word length
      File : example/data/thesaurus/organizations.the.txt
      Sorting process completed successfully
    <BLANKLINE>
    Printing thesaurus header
      File : example/data/thesaurus/organizations.the.txt
    <BLANKLINE>
        Transport and Telecomunication Inst (LVA)
          Transport and Telecomunication Institute, Latvia
        Fraunhofer-Inst for Soft and Syst Eng ISST (DEU)
          Fraunhofer-Institute for Software and Systems Engineering ISST, Dortmund,...
        Univ Koblenz-Landau (DEU)
          Institute for Software Technology IST, Universität Koblenz-Landau, Koblen...
        [UKN] CESifo, Poschingerstr. 5, Munich, 81679, Germany (DEU)
          CESifo, Poschingerstr. 5, Munich, 81679, Germany
        Fed Reserv Bank of Philadelphia (USA)
          Federal Reserve Bank of Philadelphia, Philadelphia, PA, United States; Fe...
        Pennsylvania State Univ (USA)
          Department of Supply Chain and Information Systems, Smeal College of Busi...
        Sungkyunkwan Univ (KOR)
          Software College, Sungkyunkwan University, Suwon, South Korea; Sungkyunkw...
        Univ of Pennsylvania (USA)
          University of Pennsylvania, United States
    <BLANKLINE>
    <BLANKLINE>



"""
from ...._internals.mixins import ParamsMixin
from ...user import SortByWordLength as UserSortByWordLength


class SortByWordLength(
    ParamsMixin,
):
    """:meta private:"""

    def run(self):
        return (
            UserSortByWordLength()
            .update(**self.params.__dict__)
            .with_thesaurus_file("organizations.the.txt")
            .run()
        )
