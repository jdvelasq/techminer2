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


Smoke tests:
    >>> # Reset the thesaurus to initial state
    >>> from techminer2.refine.thesaurus_old.descriptors import InitializeThesaurus
    >>> InitializeThesaurus(root_directory="examples/fintech/", quiet=True).run()

    >>> from techminer2.refine.thesaurus_old.descriptors import ReduceKeys
    >>> (
    ...     ReduceKeys()
    ...     .where_root_directory("examples/small/")
    ...     .run()
    ... )


    >>> # Redirect stderr to capture output
    >>> import sys
    >>> from io import StringIO
    >>> original_stderr = sys.stderr
    >>> sys.stderr = StringIO()

    >>> # Cutoff Fuzzy Merging
    >>> from techminer2.refine.thesaurus_old.descriptors import CutoffFuzzyMerging
    >>> (
    ...     CutoffFuzzyMerging(tqdm_disable=True, )
    ...     # .where_root_directory("examples/fintech/")
    ...     .where_root_directory("../tm2_economics_of_wind_energy/")
    ...     .using_cutoff_threshold(85)
    ...     .using_match_threshold(95)
    ...     .run()
    ... )

    >>> # Capture and print stderr output
    >>> output = sys.stderr.getvalue()
    >>> sys.stderr = original_stderr
    >>> print(output) # doctest: +SKIP
    Cutoff-Fuzzy Merging thesaurus keys...
      File : examples/fintech/data/thesaurus/descriptors.the.txt
      Keys reduced from 1569 to 1554
      Merging process completed successfully
    <BLANKLINE>
    <BLANKLINE>





"""
from techminer2._internals import ParamsMixin
from techminer2.refine.thesaurus_old.user import (
    CutoffFuzzyMerging as UserCutoffFuzzyMerging,
)


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
                cutoff_threshold=self.params.similarity_cutoff,
                match_threshold=self.params.fuzzy_threshold,
                quiet=self.params.quiet,
            )
            .run()
        )
