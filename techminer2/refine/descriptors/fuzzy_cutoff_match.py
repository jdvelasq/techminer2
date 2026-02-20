"""
FuzzyCutoffMatch
===============================================================================

Smoke test:
    >>> from techminer2 import CorpusField

    >>> from techminer2.refine.descriptors import CreateThesaurus

    >>> (
    ...     CreateThesaurus()
    ...     .using_colored_output(False)
    ...     .where_root_directory("examples/tests/")
    ...     .run()
    ... )
    INFO: Thesaurus initialized successfully.
      Success      : True
      File         : examples/tests/refine/thesaurus/descriptors.the.txt
      Source field : DESCRIPTOR_TOK
      Status       : 2441 items added to the thesaurus.
    <BLANKLINE>


    >>> from techminer2.refine.descriptors.pre_processing_merger import PreProcessingMerger
    >>> (
    ...     PreProcessingMerger()
    ...     .using_colored_output(False)
    ...     .where_root_directory("examples/tests/")
    ...     .run()
    ... )
    INFO: Fuzzy cutoff matching completed.
      Success        : True
      Field          : _UNSPECIFIED_
      Thesaurus      : descriptors.the.txt
    <BLANKLINE>


    >>> from techminer2.refine.descriptors.fuzzy_cutoff_match import FuzzyCutoffMatch
    >>> (
    ...     FuzzyCutoffMatch()
    ...     .using_colored_output(False)
    ...     .using_similarity_cutoff(85)
    ...     .using_fuzzy_threshold(95)
    ...     .where_root_directory("examples/tests/")
    ...     .run()
    ... )
    INFO: Fuzzy cutoff matching completed.
      Success        : True
      Field          : _UNSPECIFIED_
      Thesaurus      : descriptors.the.txt
    <BLANKLINE>


"""

from techminer2 import CorpusField
from techminer2._internals import ParamsMixin
from techminer2.refine._internals.objs.thesaurus_match_result import (
    ThesaurusMatchResult,
)
from techminer2.refine._internals.rules import apply_fuzzy_cutoff_match_rule

from .._internals.data_access import load_thesaurus_as_dataframe


class FuzzyCutoffMatch(
    ParamsMixin,
):
    """:meta private:"""

    def run(self) -> ThesaurusMatchResult:

        self.with_thesaurus_file("descriptors.the.txt")
        self.with_source_field(CorpusField.DESCRIPTOR_TOK)

        thesaurus_df = load_thesaurus_as_dataframe(params=self.params)

        apply_fuzzy_cutoff_match_rule(
            thesaurus_df=thesaurus_df,
            params=self.params,
        )

        return ThesaurusMatchResult(
            colored_output=self.params.colored_output,
            output_file=None,
            thesaurus_file=self.params.thesaurus_file,
            msg="Fuzzy cutoff matching completed.",
            success=True,
            field=self.params.field.value,
        )
