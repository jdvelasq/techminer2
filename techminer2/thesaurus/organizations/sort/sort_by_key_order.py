# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
# pylint: disable=too-many-statements
# pylint: disable=too-many-branches
"""
Sort by Key Order
===============================================================================


Example:
    >>> # TEST PREPARATION
    >>> import sys
    >>> from io import StringIO
    >>> from techminer2.thesaurus.organizations import CreateThesaurus, SortByKeyOrder

    >>> # Redirecting stderr to avoid messages
    >>> original_stderr = sys.stderr
    >>> sys.stderr = StringIO()

    >>> # Create thesaurus
    >>> CreateThesaurus(root_directory="example/", quiet=True).run()

    >>> # Create and run the sorter
    >>> sorter = (
    ...     SortByKeyOrder()
    ...     #
    ...     # THESAURUS:
    ...     .having_keys_ordered_by("alphabetical")
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
      File : example/thesaurus/organizations.the.txt
      Keys reduced from 90 to 90
      Keys reduction completed successfully
    <BLANKLINE>
    Sorting thesaurus alphabetically
      File : example/thesaurus/organizations.the.txt
      Thesaurus sorting completed successfully
    <BLANKLINE>
    Printing thesaurus header
      File : example/thesaurus/organizations.the.txt
    <BLANKLINE>
        Anhui Univ of Finan and Econ (CHN)
          School of Finance, Anhui University of Finance and Economics, Bengbu, 233...
        Baekseok Univ (KOR)
          Division of Tourism, Baekseok University, South Korea
        Baewha Women’s Univ (KOR)
          Department of Information Security, Baewha Women’s University, Seoul, Sou...
        Baylor Univ (USA)
          Baylor University, United States; Hankamer School of Business, Baylor Uni...
        Beihang Univ (CHN)
          School of Economics and Management, Beihang University, China
        Cent for Law (AUS)
          Centre for Law, Markets & Regulation, UNSW Australia, Australia
        Charles Sturt Univ Melbourne Study Group Cent (AUS)
          Charles Sturt University Melbourne Study Group Centre, Melbourne, VIC, Au...
        Chung-ang Univ (KOR)
          School of Business, Chung-ang University, Seoul, South Korea
    <BLANKLINE>
    <BLANKLINE>


    >>> # Capture and print stderr output
    >>> original_stderr = sys.stderr
    >>> sys.stderr = StringIO()

    >>> # with_keys_order_by: "alphabetical", "key_length", "word_length"
    >>> from techminer2.thesaurus.organizations import SortByKeyOrder
    >>> (
    ...     SortByKeyOrder()
    ...     #
    ...     # THESAURUS:
    ...     .having_keys_ordered_by("key_length")
    ...     #
    ...     # DATABASE:
    ...     .where_root_directory_is("example/")
    ...     #
    ...     .run()
    ... )


    >>> # Capture and print stderr output
    >>> output = sys.stderr.getvalue()
    >>> sys.stderr = original_stderr
    >>> print(output)
    Reducing thesaurus keys
      File : example/thesaurus/organizations.the.txt
      Keys reduced from 90 to 90
      Keys reduction completed successfully
    <BLANKLINE>
    Sorting thesaurus by key length
      File : example/thesaurus/organizations.the.txt
      Thesaurus sorting completed successfully
    <BLANKLINE>
    Printing thesaurus header
      File : example/thesaurus/organizations.the.txt
    <BLANKLINE>
        The Res center of information technology & economic and social development of...
          The Research center of information technology & economic and social devel...
        [UKN] Johns Hopkins SAIS, Washington, DC, United States (USA)
          Johns Hopkins SAIS, Washington, DC, United States
        [UKN] CESifo, Poschingerstr. 5, Munich, 81679, Germany (DEU)
          CESifo, Poschingerstr. 5, Munich, 81679, Germany
        [UKN] Hochschule für Wirtschaft Fribourg, Switzerland (CHE)
          Hochschule für Wirtschaft Fribourg, Switzerland
        [UKN] Stanford GSB and the Hoover Inst, United States (USA)
          Stanford GSB and the Hoover Institution, United States
        Univ of the Free State and Univ of Ghana Bus Sch (GHA)
          University of the Free State and University of Ghana Business School, Uni...
        Max Planck Inst for Innovation and Competition (DEU)
          Max Planck Institute for Innovation and Competition, Marstallplatz 1, Mun...
        Charles Sturt Univ Melbourne Study Group Cent (AUS)
          Charles Sturt University Melbourne Study Group Centre, Melbourne, VIC, Au...
    <BLANKLINE>
    <BLANKLINE>

    >>> # TEST PREPARATION
    >>> original_stderr = sys.stderr
    >>> sys.stderr = StringIO()

    >>> # with_keys_order_by: "alphabetical", "key_length", "word_length"
    >>> from techminer2.thesaurus.organizations import SortByKeyOrder
    >>> (
    ...     SortByKeyOrder()
    ...     #
    ...     # THESAURUS:
    ...     .having_keys_ordered_by("word_length")
    ...     #
    ...     # DATABASE:
    ...     .where_root_directory_is("example/")
    ...     #
    ...     .run()
    ... )

    >>> # Capture and print stderr output
    >>> output = sys.stderr.getvalue()
    >>> sys.stderr = original_stderr
    >>> print(output)
    Reducing thesaurus keys
      File : example/thesaurus/organizations.the.txt
      Keys reduced from 90 to 90
      Keys reduction completed successfully
    <BLANKLINE>
    Sorting thesaurus by word length
      File : example/thesaurus/organizations.the.txt
      Thesaurus sorting completed successfully
    <BLANKLINE>
    Printing thesaurus header
      File : example/thesaurus/organizations.the.txt
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
from ...user import SortByKeyOrder as UserSortByKeyOrder


class SortByKeyOrder(
    ParamsMixin,
):
    """:meta private:"""

    def run(self):
        return (
            UserSortByKeyOrder()
            .update(**self.params.__dict__)
            .with_thesaurus_file("organizations.the.txt")
            .run()
        )
