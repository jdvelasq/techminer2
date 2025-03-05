# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
# pylint: disable=too-many-statements
# pylint: disable=too-many-branches
"""
Sort by Word Match
===============================================================================


>>> # TEST PREPARATION
>>> import sys
>>> from io import StringIO
>>> old_stderr = sys.stderr
>>> sys.stderr = StringIO()
>>> #
>>> from techminer2.thesaurus.descriptors import CreateThesaurus
>>> CreateThesaurus(root_directory="example/", quiet=True).run()


>>> from techminer2.thesaurus.descriptors import SortByWordMatch
>>> (
...     SortByWordMatch()
...     # 
...     # THESAURUS:
...     .having_pattern("CREDIT")
...     #
...     # DATABASE:
...     .where_root_directory_is("example/")
...     #
...     .run()
... ) 


>>> # TEST EXECUTION
>>> output = sys.stderr.getvalue()
>>> sys.stderr = old_stderr
>>> print(output)
Sorting thesaurus file by word match
  File : example/thesaurus/descriptors.the.txt
  Word : CREDIT
  4 matching keys found
  Thesaurus sorting by word match completed successfully
<BLANKLINE>
Printing thesaurus header
  File : example/thesaurus/descriptors.the.txt
<BLANKLINE>
    ALTERNATIVE_CREDIT_SCORES
      ALTERNATIVE_CREDIT_SCORES
    CREDIT_ACCESS
      CREDIT_ACCESS
    CREDIT_COOPERATIVES
      CREDIT_COOPERATIVES
    LOWER_PRICED_CREDIT
      LOWER_PRICED_CREDIT
    A_A_)_THEORY
      A_A_)_THEORY
    A_A_THEORY
      A_A_THEORY
    A_BASIC_RANDOM_SAMPLING_STRATEGY
      A_BASIC_RANDOM_SAMPLING_STRATEGY
    A_BEHAVIOURAL_PERSPECTIVE
      A_BEHAVIOURAL_PERSPECTIVE
<BLANKLINE>
<BLANKLINE>



"""
from ...._internals.mixins import ParamsMixin
from ...user import SortByWordMatch as UserSortByWordMatch


class SortByWordMatch(
    ParamsMixin,
):
    """:meta private:"""

    # -------------------------------------------------------------------------
    def run(self):
        return (
            UserSortByWordMatch()
            .update(**self.params.__dict__)
            .with_thesaurus_file("descriptors.the.txt")
            .run()
        )


# =============================================================================
