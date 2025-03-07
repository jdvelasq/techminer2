# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
# pylint: disable=too-many-statements
# pylint: disable=too-many-branches
"""
Sort by Key Match
===============================================================================

Finds a string in the terms of a thesaurus.

Example:
    >>> import sys
    >>> from io import StringIO
    >>> from techminer2.thesaurus.references import CreateThesaurus, SortByKeyMatch

    >>> # Redirecting stderr to avoid messages
    >>> original_stderr = sys.stderr
    >>> sys.stderr = StringIO()

    >>> # Create, configure, and run the sorter
    >>> sorter = (
    ...     SortByKeyMatch()
    ...     .having_pattern("ECON")
    ...     .where_root_directory_is("example/")
    ... )
    >>> sorter.run()

    >>> # Capture and print stderr output
    >>> output = sys.stderr.getvalue()
    >>> sys.stderr = original_stderr
    >>> print(output)
    Sorting thesaurus file by key match
                File : example/thesaurus/references.the.txt
             Pattern : ECON
      Case sensitive : False
         Regex Flags : 0
        Regex Search : False
      7 matching keys found
      Thesaurus sorting by key match completed successfully
    <BLANKLINE>
    Printing thesaurus header
      File : example/thesaurus/references.the.txt
    <BLANKLINE>
        Anagnostopoulos I., 2018, J ECON BUS, V100, P7
          Anagnostopoulos, Ioannis, FinTech and RegTech: Impact on regulators and b...
        Buchak G., 2018, J FINANC ECON, V130, P453
          Buchak G., Matvos G., Piskorski T., Seru A., Fintech, regulatory arbitrag...
        Chen L./1, 2016, CHINA ECON J, V9, P225
          Chen L., From Fintech to Finlife: The case of Fintech development in Chin...
        Gabor D., 2017, NEW POLIT ECON, V22, P423
          Gabor D., Brooks S., The Digital Revolution in Financial Inclusion: Inter...
        Gomber P., 2017, J BUS ECON, V87, P537
          Gomber P., Koch J., Siering M., Digital finance and fintech: current rese...
        Haddad C., 2019, SMALL BUS ECON, V53, P81
          Haddad C., Hornuf L., The emergence of the global fintech market: Economi...
        Jagtiani J., 2018, J ECON BUS, V100, P43
          Jagtiani J., Catharine L., Do fintech lenders penetrate areas that are un...
        Alt R., 2018, ELECTRON MARK, V28, P235
          Alt R., Beck R., Smits M.T., Fintech and the Transformation of the Financ...
    <BLANKLINE>
    <BLANKLINE>





"""
from ...._internals.mixins import ParamsMixin
from ...user import SortByKeyMatch as UserSortByKeyMatch


class SortByKeyMatch(
    ParamsMixin,
):
    """:meta private:"""

    def run(self):
        return (
            UserSortByKeyMatch()
            .update(**self.params.__dict__)
            .with_thesaurus_file("references.the.txt")
            .run()
        )
