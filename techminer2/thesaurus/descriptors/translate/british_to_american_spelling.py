# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
# pylint: disable=too-many-statements
# pylint: disable=too-many-branches
"""
British to American Spelling
===============================================================================


Example:
    >>> import sys
    >>> from io import StringIO
    >>> from techminer2.thesaurus.descriptors import BritishToAmericanSpelling, InitializeThesaurus

    >>> # Redirecting stderr to avoid messages during doctests
    >>> original_stderr = sys.stderr
    >>> sys.stderr = StringIO()

    >>> # Create the thesaurus
    >>> InitializeThesaurus(root_directory="example/", quiet=True).run()

    >>> # Creates, configures, an run the translator
    >>> translator = (
    ...     BritishToAmericanSpelling(tqdm_disable=True, use_colorama=False)
    ...     .where_root_directory_is("example/")
    ... )
    >>> translator.run()

    >>> # Capture and print stderr output to test the code using doctest
    >>> output = sys.stderr.getvalue()
    >>> sys.stderr = original_stderr
    >>> print(output)
    Converting British to American English...
      File : example/data/thesaurus/descriptors.the.txt
      13 replacements made successfully
      Translation process completed successfully
    <BLANKLINE>
    Printing thesaurus header
      File : example/data/thesaurus/descriptors.the.txt
    <BLANKLINE>
        ANALOG_PROCESSES
          ANALOGUE_PROCESSES
        ANALYZE_THE_KEY_FACTORS
          ANALYSE_THE_KEY_FACTORS
        ANALYZE_THE_SYSTEMIC_CHARACTERISTICS
          ANALYSE_THE_SYSTEMIC_CHARACTERISTICS
        ANALYZE_THE_SYSTEMIC_INNOVATION_CHARACTERISTICS
          ANALYSE_THE_SYSTEMIC_INNOVATION_CHARACTERISTICS
        BEHAVIORAL_ECONOMICS
          BEHAVIOURAL_ECONOMICS
        ENTREPRENEURIAL_ENDEAVORS
          ENTREPRENEURIAL_ENDEAVOURS
        FAVOR
          FAVOUR
        HARMONIZE_TECHNOLOGICAL_ADVANCEMENTS
          HARMONISE_TECHNOLOGICAL_ADVANCEMENTS
    <BLANKLINE>
    <BLANKLINE>



"""
from ...._internals.mixins import ParamsMixin
from ...user import BritishToAmericanSpelling as UserBritishToAmericanSpelling


class BritishToAmericanSpelling(
    ParamsMixin,
):
    """:meta private:"""

    # -------------------------------------------------------------------------
    def run(self):
        return (
            UserBritishToAmericanSpelling()
            .update(**self.params.__dict__)
            .with_thesaurus_file("descriptors.the.txt")
            .run()
        )


# =============================================================================
