"""
Apply Thesaurus
===============================================================================

Smoke tests:
    >>> from tm2p.refine.concept.apply import Apply
    >>> (
    ...     Apply()
    ...     .where_root_directory("tests/scopus/")
    ...     .run()
    ... )
    180




"""

import sys

from tm2p._intern import ParamsMixin
from tm2p.enum import Field, ThFile
from tm2p.refine._intern.apply import BaseApply


class Apply(
    ParamsMixin,
):
    def run(self) -> int:
        """:meta private:"""

        results = []

        for source, target in (
            #
            (Field.AUTHKW_TOK, Field.AUTHKW_NORM),
            (Field.IDXKW_TOK, Field.IDXKW_NORM),
            #
            (Field.KW_TOK, Field.KW_NORM),
            #
            (Field.CONCEPT_RAW, Field.CONCEPT_NORM),
            (Field.WORD_RAW, Field.WORD_NORM),
            #
            (Field.DESCRIPTOR_RAW, Field.DESCRIPTOR_NORM),
        ):

            results.append(
                BaseApply()
                .with_thesaurus_file(ThFile.CONCEPT)
                .with_source_field(source)
                .with_target_field(target)
                .where_root_directory(self.params.root_directory)
                .run()
            )

        sys.stderr.write("\n")
        sys.stderr.flush()
        return results[0]
