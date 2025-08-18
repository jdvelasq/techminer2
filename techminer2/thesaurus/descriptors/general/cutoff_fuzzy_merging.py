# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
# pylint: disable=too-many-statements
# pylint: disable=too-many-branches
"""
Cutoff Fuzzy Merging
===============================================================================


Example:
    >>> # Reset the thesaurus to initial state
    >>> from techminer2.thesaurus.descriptors import InitializeThesaurus
    >>> InitializeThesaurus(root_directory="examples/fintech/", quiet=True).run()

    >>> from techminer2.thesaurus.descriptors import ReduceKeys
    >>> (
    ...     ReduceKeys(use_colorama=False)
    ...     .where_root_directory_is("examples/fintech/")
    ...     .run()
    ... )


    >>> # Redirect stderr to capture output
    >>> import sys
    >>> from io import StringIO
    >>> original_stderr = sys.stderr
    >>> sys.stderr = StringIO()

    >>> # Cutoff Fuzzy Merging
    >>> from techminer2.thesaurus.descriptors import CutoffFuzzyMerging
    >>> (
    ...     CutoffFuzzyMerging(tqdm_disable=True, use_colorama=False)
    ...     .where_root_directory_is("examples/fintech/")
    ...     .having_cutoff_threshold(85)
    ...     .having_match_threshold(95)
    ...     .run()
    ... )

    >>> # Capture and print stderr output
    >>> output = sys.stderr.getvalue()
    >>> sys.stderr = original_stderr
    >>> print(output)





"""
from techminer2._internals.mixins import ParamsMixin
from techminer2.thesaurus.user import CutoffFuzzyMerging as UserCutoffFuzzyMerging


#
#
class CutoffFuzzyMerging(
    ParamsMixin,
):
    """:meta private:"""

    def run(self):

        (
            UserCutoffFuzzyMerging()
            .update(**self.params.__dict__)
            .update(
                field="raw_descriptors",
                thesaurus_file="descriptors.the.txt",
                root_directory=self.params.root_directory,
                tqdm_disable=self.params.tqdm_disable,
                cutoff_threshold=self.params.cutoff_threshold,
                match_threshold=self.params.match_threshold,
                quiet=self.params.quiet,
            )
            .run()
        )
