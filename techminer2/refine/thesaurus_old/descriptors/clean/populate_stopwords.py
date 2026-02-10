# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
# pylint: disable=too-many-statements
# pylint: disable=too-many-branches
"""
Populate Stopwords
===============================================================================


Example:
    >>> # TEST PREPARATION
    >>> import sys
    >>> from io import StringIO
    >>> from techminer2.refine.thesaurus_old.descriptors import InitializeThesaurus, PopulateStopwords

    >>> # Redirecting stderr to avoid messages
    >>> original_stderr = sys.stderr
    >>> sys.stderr = StringIO()

    >>> # Create the thesaurus
    >>> InitializeThesaurus(root_directory="examples/fintech/", quiet=True).run()

    >>> # Populate stopwords
    >>> (
    ...     PopulateStopwords()
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
from techminer2._internals import ParamsMixin
from techminer2._internals.stopwords import load_user_stopwords, save_user_stopwords
from techminer2.refine.thesaurus_old.descriptors import IsStopword

# -----------------------------------------------------------------------------


class PopulateStopwords(
    ParamsMixin,
):
    """:meta private:"""

    def run(self):

        df = IsStopword().update(**self.params.__dict__).run()
        new_stopwords = df[df["is_stopword?"]]["descriptor"].tolist()
        stopwords = load_user_stopwords(params=self.params)
        stopwords = sorted(set(stopwords).union(set(new_stopwords)))
        save_user_stopwords(self.params, stopwords)
