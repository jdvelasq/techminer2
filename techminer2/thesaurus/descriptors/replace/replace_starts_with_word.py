# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
# pylint: disable=too-many-statements
# pylint: disable=too-many-branches
"""
Replace Starts With Word 
===============================================================================

>>> # TEST PREPARATION
>>> import sys
>>> from io import StringIO
>>> old_stderr = sys.stderr
>>> sys.stderr = StringIO()
>>> #
>>> from techminer2.thesaurus.descriptors import CreateThesaurus
>>> CreateThesaurus(root_directory="example/", quiet=True).run()


>>> from techminer2.thesaurus.descriptors import ReplaceStartsWithWord
>>> (
...     ReplaceStartsWithWord()
...     # 
...     # THESAURUS:
...     .having_word("FINTECH")
...     .having_replacement("fintech")
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
Replacing starting word in keys
         File : example/thesaurus/descriptors.the.txt
         Word : FINTECH
  Replacement : fintech
  35 replacements made successfully
  Word replacing completed successfully
<BLANKLINE>
Printing thesaurus header
  File : example/thesaurus/descriptors.the.txt
<BLANKLINE>
    fintech
      FINTECH; FINTECHS
    fintech_AND_FINANCIAL_INNOVATIONS
      FINTECH_AND_FINANCIAL_INNOVATIONS
    fintech_AND_REGTECH_:_IMPACT
      FINTECH_AND_REGTECH_:_IMPACT
    fintech_AND_SUSTAINABLE_DEVELOPMENT_:_EVIDENCE
      FINTECH_AND_SUSTAINABLE_DEVELOPMENT_:_EVIDENCE
    fintech_BANKING_INDUSTRY
      FINTECH_BANKING_INDUSTRY
    fintech_BASED_INNOVATION_DEVELOPMENT
      FINTECH_BASED_INNOVATION_DEVELOPMENT
    fintech_BASED_INNOVATIONS
      FINTECH_BASED_INNOVATIONS; FINTECH_INNOVATION
    fintech_CLUSTERS
      FINTECH_CLUSTERS
<BLANKLINE>
<BLANKLINE>

"""
from ...._internals.mixins import ParamsMixin
from ...user import ReplaceStartsWithWord as UserReplaceStartsWithWord


class ReplaceStartsWithWord(
    ParamsMixin,
):
    """:meta private:"""

    # -------------------------------------------------------------------------
    def run(self):
        return (
            UserReplaceStartsWithWord()
            .update(**self.params.__dict__)
            .with_thesaurus_file("descriptors.the.txt")
            .run()
        )


# ===============================================================================
