"""
StemmingMatch
===============================================================================

Smoke test:
    >>> from techminer2 import CorpusField
    >>> from techminer2.refine.descriptors import CreateThesaurus
    >>> (
    ...     CreateThesaurus()
    ...     .using_colored_output(False)
    ...     .where_root_directory("tests/fintech/")
    ...     .run()
    ... )
    INFO: Thesaurus initialized successfully.
      Success      : True
      File         : examples/tests/refine/thesaurus/descriptors.the.txt
      Source field : DESCRIPTOR_TOK
      Status       : 2441 items added to the thesaurus.
    <BLANKLINE>


    >>> from techminer2.refine.descriptors import PreProcessThesaurus
    >>> (
    ...     PreProcessThesaurus()
    ...     .using_colored_output(False)
    ...     .where_root_directory("tests/fintech/")
    ...     .run()
    ... )
    INFO: Fuzzy cutoff matching completed.
      Success        : True
      Field          : _UNSPECIFIED_
      Thesaurus      : descriptors.the.txt
    <BLANKLINE>


    >>> from techminer2.refine.descriptors import StemMatch
    >>> (
    ...     StemMatch()
    ...     .using_colored_output(False)
    ...     .where_root_directory("tests/fintech/")
    ...     .run()
    ... )
    INFO: Stem matching completed.
      Success        : True
      Field          : _UNSPECIFIED_
      Thesaurus      : descriptors.the.txt
    <BLANKLINE>


"""

import sys

from tm2p import CorpusField
from tm2p._internals import ParamsMixin
from tm2p.refine._internals.objs.thesaurus_match_result import ThesaurusMatchResult
from tm2p.refine._internals.rules import apply_stemming_rule

from .._internals.data_access import load_thesaurus_as_dataframe


class StemMatch(
    ParamsMixin,
):
    """:meta private:"""

    _HEADER_WIDTH = 70
    _STEP_PREFIX = "  → "

    def _write(self, text: str) -> None:
        sys.stderr.write(text)
        sys.stderr.flush()

    def _print_header(self) -> None:
        separator = "=" * self._HEADER_WIDTH
        self._write(f"\n{separator}\nStem Matching\n{separator}\n\n")

    def run(self) -> ThesaurusMatchResult:

        self.with_thesaurus_file("concepts.the.txt")
        self.with_source_field(CorpusField.KEY_AND_NP_AND_WORDS)

        thesaurus_df = load_thesaurus_as_dataframe(params=self.params)

        self._print_header()
        self._write(f"{self._STEP_PREFIX}Applying Stemming rule\n")

        apply_stemming_rule(
            thesaurus_df=thesaurus_df,
            params=self.params,
        )

        return ThesaurusMatchResult(
            colored_output=self.params.colored_output,
            output_file=None,
            thesaurus_file=self.params.thesaurus_file,
            msg="Stem matching completed.",
            success=True,
            field=self.params.source_field.value,
        )
