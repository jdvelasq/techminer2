# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
# pylint: disable=too-many-statements
# pylint: disable=too-many-branches
"""
Translate American to British Spelling
===============================================================================


Example:
    >>> import sys
    >>> from io import StringIO
    >>> # Redirecting stderr to avoid messages during doctests
    >>> original_stderr = sys.stderr
    >>> sys.stderr = StringIO()

    >>> # Create the thesaurus
    >>> from techminer2.thesaurus.descriptors import InitializeThesaurus
    >>> InitializeThesaurus(root_directory="examples/fintech/", quiet=True).run()

    >>> # Creates, configures, an run the translator
    >>> from techminer2.thesaurus.descriptors import AmericanToBritishSpelling
    >>> (
    ...     AmericanToBritishSpelling(tqdm_disable=True, use_colorama=False)
    ...     .where_root_directory_is("examples/fintech/")
    ...     .run()
    ... )

    >>> # Capture and print stderr output to test the code using doctest
    >>> output = sys.stderr.getvalue()
    >>> sys.stderr = original_stderr
    >>> print(output) # doctest: +ELLIPSIS +SKIP
    Converting American to British English...
      File : examples/fintech/data/thesaurus/descriptors.the.txt
      21 replacements made successfully
      Translation process completed successfully
    <BLANKLINE>
    Printing thesaurus header
      File : examples/fintech/data/thesaurus/descriptors.the.txt
    <BLANKLINE>
        A_COMPLETE_GENERALISATION
          A_COMPLETE_GENERALIZATION
        AN_ORGANISATION
          AN_ORGANIZATION
        BEHAVIOURAL_BIASES
          BEHAVIORAL_BIASES
        CATEGORISES_RESEARCH
          CATEGORIZES_RESEARCH
        CHARACTERISE_FINTECH
          CHARACTERIZE_FINTECH
        DECENTRALISED_FINTECH_MARKETS
          DECENTRALIZED_FINTECH_MARKETS
        DIGITISED_AGRICULTURE
          DIGITIZED_AGRICULTURE
        EXCESSIVELY_RISKY_BEHAVIOUR
          EXCESSIVELY_RISKY_BEHAVIOR
    <BLANKLINE>
    <BLANKLINE>



"""
from techminer2._internals.mixins import ParamsMixin
from techminer2.thesaurus.user import (
    AmericanToBritishSpelling as UserAmericanToBritishSpelling,
)


class AmericanToBritishSpelling(
    ParamsMixin,
):
    """:meta private:"""

    # -------------------------------------------------------------------------
    def run(self):
        return (
            UserAmericanToBritishSpelling()
            .update(**self.params.__dict__)
            .with_thesaurus_file("descriptors.the.txt")
            .run()
        )


# =============================================================================
