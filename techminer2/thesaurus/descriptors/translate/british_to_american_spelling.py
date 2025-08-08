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
    >>> InitializeThesaurus(root_directory="examples/fintech/", quiet=True).run()

    >>> # Creates, configures, an run the translator
    >>> translator = (
    ...     BritishToAmericanSpelling(tqdm_disable=True, use_colorama=False)
    ...     .where_root_directory_is("examples/fintech/")
    ... )
    >>> translator.run()

    >>> # Capture and print stderr output to test the code using doctest
    >>> output = sys.stderr.getvalue()
    >>> sys.stderr = original_stderr
    >>> print(output)
    Converting British to American English...



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
