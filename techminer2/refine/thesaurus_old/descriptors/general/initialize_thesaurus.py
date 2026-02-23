"""
Initialiize Thesaurus
===============================================================================


Smoke tests:
    >>> import sys
    >>> from io import StringIO
    >>> # Redirect stderr to capture output
    >>> original_stderr = sys.stderr
    >>> sys.stderr = StringIO()

    >>> # Create the thesaurus
    >>> from techminer2.refine.thesaurus_old.descriptors import InitializeThesaurus
    >>> (
    ...     InitializeThesaurus()
    ...     .where_root_directory("tests/data/")
    ...     .run()
    ... )


    >>> # Capture and print stderr output
    >>> output = sys.stderr.getvalue()
    >>> sys.stderr = original_stderr
    >>> print(output)
    Initializing thesaurus from 'raw_descriptors' field...
      File : examples/fintech/data/thesaurus/descriptors.the.txt
      1721 keys found
      Initialization process completed successfully
    <BLANKLINE>
    Printing thesaurus header
      File : examples/fintech/data/thesaurus/descriptors.the.txt
    <BLANKLINE>
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
        A_CLUSTER_ANALYSIS
          A_CLUSTER_ANALYSIS
    <BLANKLINE>
    <BLANKLINE>



"""

from techminer2._internals import ParamsMixin
from techminer2.refine.thesaurus_old.user import (
    InitializeThesaurus as UserInitializeThesaurus,
)


class InitializeThesaurus(
    ParamsMixin,
):
    """:meta private:"""

    def run(self):

        (
            UserInitializeThesaurus(
                field="raw_descriptors",
                thesaurus_file="descriptors.the.txt",
                root_directory=self.params.root_directory,
                quiet=self.params.quiet,
                use_colorama=getattr(self.params, "use_colorama", False),
            ).run()
        )
