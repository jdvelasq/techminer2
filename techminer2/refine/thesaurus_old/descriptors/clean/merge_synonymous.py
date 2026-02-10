# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
# pylint: disable=too-many-statements
# pylint: disable=too-many-branches
"""
Merge Synonymous
===============================================================================


Example:
    >>> # TEST PREPARATION
    >>> import sys
    >>> from io import StringIO
    >>> from techminer2.refine.thesaurus_old.descriptors import InitializeThesaurus, MergeSynonymous

    >>> # Redirecting stderr to avoid messages
    >>> original_stderr = sys.stderr
    >>> sys.stderr = StringIO()

    >>> # Create the thesaurus
    >>> InitializeThesaurus(root_directory="examples/fintech/", quiet=True).run()

    >>> # Merge synonymous terms
    >>> (
    ...     MergeSynonymous()
    ...     .with_core_area("FINTECH - FINANCIAL TECHNOLOGIES")
    ...     .having_n_contexts(10)
    ...     .having_terms_in_top(40)
    ...     .having_terms_ordered_by("OCC")
    ...     .having_term_occurrences_between(None, None)
    ...     .having_term_citations_between(None, None)
    ...     .having_terms_in(None)
    ...     .where_root_directory("examples/small/")
    ... ).run()

    >>> # Capture and print stderr output
    >>> output = sys.stderr.getvalue()
    >>> sys.stderr = original_stderr
    >>> print(output)  # doctest: +SKIP



"""
import json
import os

import pandas as pd
from tqdm import tqdm  # type: ignore

from techminer2._internals import ParamsMixin
from techminer2._internals.stopwords import load_user_stopwords, save_user_stopwords

# -----------------------------------------------------------------------------


class MergeSynonymous(
    ParamsMixin,
):
    """:meta private:"""

    def run(self):

        from techminer2.refine.thesaurus_old.descriptors import AreSynonymous, MergeKeys

        df = AreSynonymous().update(**self.params.__dict__).run()

        for _, row in df.iterrows():

            if row["candidate_terms"].strip() != "":

                for candidate_term in row["candidate_terms"].split("; "):
                    self.params.with_patterns([row.lead_term, candidate_term])
                    MergeKeys().update(**self.params.__dict__).run()


# =============================================================================
