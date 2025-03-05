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


>>> # TEST PREPARATION
>>> import sys
>>> from io import StringIO
>>> old_stderr = sys.stderr
>>> sys.stderr = StringIO()
>>> #
>>> from techminer2.thesaurus.descriptors import CreateThesaurus
>>> CreateThesaurus(root_directory="example/", quiet=True).run()


>>> # with_keys_order_by: "alphabetical", "key_length", "word_length"
>>> from techminer2.thesaurus.descriptors import SortByKeyOrder
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


>>> # TEST EXECUTION
>>> output = sys.stderr.getvalue()
>>> sys.stderr = old_stderr
>>> print(output)
Sorting thesaurus alphabetically
  File : example/thesaurus/descriptors.the.txt
  Thesaurus sorting completed successfully
<BLANKLINE>
Printing thesaurus header
  File : example/thesaurus/descriptors.the.txt
<BLANKLINE>
    ACADEMIA
      ACADEMIA
    ACADEMICS
      ACADEMICS
    ACADEMIC_OBSERVERS
      ACADEMIC_OBSERVERS
    ACADEMIC_RESEARCH
      ACADEMIC_RESEARCH
    ACCELERATE_ACCESS
      ACCELERATE_ACCESS
    ACCEPTANCE
      ACCEPTANCE
    ACCEPTANCE_MODELS
      ACCEPTANCE_MODELS
    ACCESS
      ACCESS
<BLANKLINE>
<BLANKLINE>


>>> # TEST PREPARATION
>>> import sys
>>> from io import StringIO
>>> old_stderr = sys.stderr
>>> sys.stderr = StringIO()

>>> # with_keys_order_by: "alphabetical", "key_length", "word_length"
>>> from techminer2.thesaurus.descriptors import SortByKeyOrder
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


>>> # TEST EXECUTION
>>> output = sys.stderr.getvalue()
>>> sys.stderr = old_stderr
>>> print(output)
Sorting thesaurus by key length
  File : example/thesaurus/descriptors.the.txt
  Thesaurus sorting completed successfully
<BLANKLINE>
Printing thesaurus header
  File : example/thesaurus/descriptors.the.txt
<BLANKLINE>
    A_NOVEL_HYBRID_MULTIPLE_CRITERIA_DECISION_MAKING_METHOD
      A_NOVEL_HYBRID_MULTIPLE_CRITERIA_DECISION_MAKING_METHOD
    THE_MOST_IMPORTANT_AND_FASTEST_GROWING_FINTECH_SERVICES
      THE_MOST_IMPORTANT_AND_FASTEST_GROWING_FINTECH_SERVICES
    THE_HEFEI_SCIENCE_AND_TECHNOLOGY_RURAL_COMMERCIAL_BANK
      THE_HEFEI_SCIENCE_AND_TECHNOLOGY_RURAL_COMMERCIAL_BANK
    FUTURE_AND_PRESENT_MOBILE_FINTECH_PAYMENT_SERVICES
      FUTURE_AND_PRESENT_MOBILE_FINTECH_PAYMENT_SERVICES
    UNIFIED_THEORY_OF_ACCEPTANCE_AND_USE_OF_TECHNOLOGY
      UNIFIED_THEORY_OF_ACCEPTANCE_AND_USE_OF_TECHNOLOGY
    THE_FINANCIAL_AND_DIGITAL_INNOVATION_LITERATURE
      THE_FINANCIAL_AND_DIGITAL_INNOVATION_LITERATURE
    ECONOMIC_SUSTAINABILITY_AND_COST_EFFECTIVENESS
      ECONOMIC_SUSTAINABILITY_AND_COST_EFFECTIVENESS
    FINTECH_AND_SUSTAINABLE_DEVELOPMENT_:_EVIDENCE
      FINTECH_AND_SUSTAINABLE_DEVELOPMENT_:_EVIDENCE
<BLANKLINE>
<BLANKLINE>



>>> # TEST PREPARATION
>>> import sys
>>> from io import StringIO
>>> old_stderr = sys.stderr
>>> sys.stderr = StringIO()


>>> # with_keys_order_by: "alphabetical", "key_length", "word_length"
>>> from techminer2.thesaurus.descriptors import SortByKeyOrder
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


>>> # TEST EXECUTION
>>> output = sys.stderr.getvalue()
>>> sys.stderr = old_stderr
>>> print(output)
Sorting thesaurus by word length
  File : example/thesaurus/descriptors.the.txt
  Thesaurus sorting completed successfully
<BLANKLINE>
Printing thesaurus header
  File : example/thesaurus/descriptors.the.txt
<BLANKLINE>
    THE_FINTECHPHILANTHROPYDEVELOPMENT_COMPLEX
      THE_FINTECHPHILANTHROPYDEVELOPMENT_COMPLEX
    COMPETITION (ECONOMICS)
      COMPETITION (ECONOMICS)
    FINANCIAL_TECHNOLOGY (FINTECH)
      FINANCIAL_TECHNOLOGY (FINTECH)
    A_WIDE_RANGING_RECONCEPTUALIZATION
      A_WIDE_RANGING_RECONCEPTUALIZATION
    NETWORKS (CIRCUITS)
      NETWORKS (CIRCUITS)
    THE_RECONCEPTUALIZATION
      THE_RECONCEPTUALIZATION
    CLASSIFICATION (OF_INFORMATION)
      CLASSIFICATION (OF_INFORMATION)
    EXPLORE_INTERRELATIONSHIPS
      EXPLORE_INTERRELATIONSHIPS
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
            .with_thesaurus_file("descriptors.the.txt")
            .run()
        )
