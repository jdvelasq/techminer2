# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
# pylint: disable=too-many-statements
# pylint: disable=too-many-branches
"""
Create Thesaurus
===============================================================================

>>> # TEST PREPARATION
>>> import sys
>>> from io import StringIO
>>> old_stderr = sys.stderr
>>> sys.stderr = StringIO()


>>> from techminer2.thesaurus.descriptors import CreateThesaurus
>>> (
...     CreateThesaurus()  
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
Creating thesaurus from 'raw_descriptors' field
  File : example/thesaurus/descriptors.the.txt
  1796 keys found
  Thesaurus creation completed successfully
<BLANKLINE>
Printing thesaurus header
  File : example/thesaurus/descriptors.the.txt
<BLANKLINE>
    A_A_)_THEORY
      A_A_)_THEORY
    A_A_THEORY
      A_A_THEORY
    A_BASIC_RANDOM_SAMPLING_STRATEGY
      A_BASIC_RANDOM_SAMPLING_STRATEGY
    A_BEHAVIOURAL_PERSPECTIVE
      A_BEHAVIOURAL_PERSPECTIVE
    A_BETTER_UNDERSTANDING
      A_BETTER_UNDERSTANDING
    A_BLOCKCHAIN_IMPLEMENTATION_STUDY
      A_BLOCKCHAIN_IMPLEMENTATION_STUDY
    A_CASE_STUDY
      A_CASE_STUDY
    A_CHALLENGE
      A_CHALLENGE
<BLANKLINE>
<BLANKLINE>



"""

from ...._internals.mixins import ParamsMixin
from ...user import CreateThesaurus as UserCreateThesaurus


#
#
class CreateThesaurus(
    ParamsMixin,
):
    """:meta private:"""

    def run(self):

        (
            UserCreateThesaurus(
                field="raw_descriptors",
                thesaurus_file="descriptors.the.txt",
                root_directory=self.params.root_directory,
                quiet=self.params.quiet,
            ).run()
        )
