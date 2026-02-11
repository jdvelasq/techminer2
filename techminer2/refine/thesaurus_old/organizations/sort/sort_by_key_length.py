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


Smoke tests:
    >>> # TEST PREPARATION
    >>> import sys
    >>> from io import StringIO
    >>> from techminer2.refine.thesaurus_old.organizations import InitializeThesaurus, SortByKeyLength

    >>> # Redirecting stderr to avoid messages
    >>> original_stderr = sys.stderr
    >>> sys.stderr = StringIO()

    >>> # Create thesaurus
    >>> InitializeThesaurus(root_directory="examples/fintech/", quiet=True).run()

    >>> # Create and run the sorter
    >>> sorter = (
    ...     SortByKeyLength()
    ...     #
    ...     # DATABASE:
    ...     .where_root_directory("examples/small/")
    ... )
    >>> sorter.run()

    >>> # Capture and print stderr output
    >>> output = sys.stderr.getvalue()
    >>> sys.stderr = original_stderr
    >>> print(output)
    Sorting thesaurus by key length...
      File : examples/fintech/data/thesaurus/organizations.the.txt
      Sorting process completed successfully
    <BLANKLINE>
    Printing thesaurus header
      File : examples/fintech/data/thesaurus/organizations.the.txt
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




"""
from techminer2._internals import ParamsMixin
from techminer2.refine.thesaurus_old.user import SortByKeyLength as UserSortByKeyLength


class SortByKeyLength(
    ParamsMixin,
):
    """:meta private:"""

    def run(self):
        return (
            UserSortByKeyLength()
            .update(**self.params.__dict__)
            .with_thesaurus_file("organizations.the.txt")
            .run()
        )
