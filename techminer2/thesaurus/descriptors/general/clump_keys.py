# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
# pylint: disable=too-many-statements
# pylint: disable=too-many-branches
"""
Clump Keys
===============================================================================


Example:
    >>> import sys
    >>> from io import StringIO
    >>> from techminer2.thesaurus.descriptors import ClumpKeys, InitializeThesaurus

    >>> # Redirect stderr to capture output
    >>> original_stderr = sys.stderr
    >>> sys.stderr = StringIO()

    >>> # Create the thesaurus
    >>> InitializeThesaurus(root_directory="examples/fintech/", quiet=True).run()

    >>> # Clump the thesaurus
    >>> (
    ...     ClumpKeys(tqdm_disable=True, use_colorama=False)
    ...     .where_root_directory_is("examples/fintech/")
    ...     .run()
    ... )


    >>> # Capture and print stderr output
    >>> output = sys.stderr.getvalue()
    >>> sys.stderr = original_stderr
    >>> print(output)  # doctest: +SKIP
    Clumping thesaurus keys...
                   File : examples/fintech/data/thesaurus/descriptors.the.txt
      Keys reduced from 1721 to 1693
      Clumping process completed successfully
    <BLANKLINE>
    Printing thesaurus header
      File : examples/fintech/data/thesaurus/descriptors.the.txt
    <BLANKLINE>
        DATA_SECURITY
          DATA_SECURITY; DATA_SECURITY_AND_CONSUMER_TRUST; SECURITY_OF_DATA
        ELABORATION_LIKELIHOOD_MODEL
          ELABORATION_LIKELIHOOD_MODEL; THE_ELABORATION_LIKELIHOOD_MODEL
        FINANCIAL_TECHNOLOGY
          AN_EMERGING_FINANCIAL_TECHNOLOGY; FINANCIAL_TECHNOLOGY (FINTECH); FINANCI...
        INFORMATION_TECHNOLOGY
          INFORMATION_TECHNOLOGY; INFORMATION_TECHNOLOGY_INFRASTRUCTURE; PARTICULAR...
        INTENTION_TO_USE
          CONTINUOUS_INTENTION_TO_USE_MOBILE; CONTINUOUS_INTENTION_TO_USE_MOBILE_FI...
        LITERATURE_REVIEW
          LITERATURE_REVIEW; THE_CURRENT_LITERATURE_REVIEW
        MULTI_LEVEL_ANALYSIS
          A_MULTI_LEVEL_ANALYSIS; MULTI_LEVEL_ANALYSIS
        PEER_TO_PEER
          PEER_TO_PEER; PEER_TO_PEER_MONEY_EXCHANGES; PEER_TO_PEER_PLATFORMS
        SECURITY_AND_PRIVACY
          SECURITY_AND_PRIVACY; THE_SECURITY_AND_PRIVACY_DIMENSION
        START_UPS
          CONSUMER_ORIENTED_FINTECH_START_UPS; FINTECH_DIGITAL_BANKING_START_UPS; M...
    <BLANKLINE>
    <BLANKLINE>






"""
from techminer2._internals.mixins import ParamsMixin
from techminer2.thesaurus.user import ClumpKeys as UserClumpKeys


#
#
class ClumpKeys(
    ParamsMixin,
):
    """:meta private:"""

    def run(self):

        (
            UserClumpKeys()
            .update(**self.params.__dict__)
            .update(
                field="raw_descriptors",
                thesaurus_file="descriptors.the.txt",
                root_directory=self.params.root_directory,
                tqdm_disable=self.params.tqdm_disable,
                quiet=self.params.quiet,
            )
            .run()
        )
