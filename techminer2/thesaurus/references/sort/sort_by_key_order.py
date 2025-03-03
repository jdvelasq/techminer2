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


>>> # with_keys_order_by: "alphabetical", "key_length", "word_length"
>>> from techminer2.thesaurus.references import SortByKeyOrder
>>> (
...     SortByKeyOrder()
...     # 
...     # THESAURUS:
...     .having_keys_ordered_by("alphabetical")
...     #
...     # DATABASE:
...     .where_root_directory_is("example/")
...     #
...     .run()
... )
Sorting thesaurus alphabetically
  File : example/thesaurus/references.the.txt
  Thesaurus sorting completed successfully
<BLANKLINE>
Printing thesaurus header
  File : example/thesaurus/references.the.txt
<BLANKLINE>
    Alt R., 2018, ELECTRON MARK, V28, P235
      Alt R., Beck R., Smits M.T., Fintech and the Transformation of the Financ...
    Anagnostopoulos I., 2018, J ECON BUS, V100, P7
      Anagnostopoulos, Ioannis, FinTech and RegTech: Impact on regulators and b...
    Arner D.W., 2017, NORTHWEST J INTL LAW BUS, V37, P373
      Arner D.W., Barberis J., Buckley R.P., Fintech, regtech, and the reconcep...
    Buchak G., 2018, J FINANC ECON, V130, P453
      Buchak G., Matvos G., Piskorski T., Seru A., Fintech, regulatory arbitrag...
    Cai C.W., 2018, ACCOUNT FINANC, V58, P965
      Cai C.W., Disruption of financial intermediation by FinTech: A review on ...
    Chen L./1, 2016, CHINA ECON J, V9, P225
      Chen L., From Fintech to Finlife: The case of Fintech development in Chin...
    Dorfleitner G., 2017, FINTECH IN GER, P1
      Dorfleitner G., Hornuf L., Schmitt M., Weber M., FinTech in Germany, (2017)
    Gabor D., 2017, NEW POLIT ECON, V22, P423
      Gabor D., Brooks S., The Digital Revolution in Financial Inclusion: Inter...
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
            .with_thesaurus_file("references.the.txt")
            .run()
        )
