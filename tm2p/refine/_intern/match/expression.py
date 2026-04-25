"""
BaseExpressionMatch
===============================================================================

Smoke tests:
    >>> from tm2p.enum import ThFile, AnalysisUnit
    >>> from tm2p.refine._intern.match import BaseExpressionMatch
    >>> (
    ...     BaseExpressionMatch()
    ...     #
    ...     .having_text_matching("firm")
    ...     #
    ...     # FIELD:
    ...     .with_thesaurus_file(ThFile.CONCEPT)
    ...     .with_analysis_unit(AnalysisUnit.DESCRIPTOR)
    ...     .where_root_directory("tests/regtech-scopus/")
    ...     .run()
    ... )

"""

import sys

from tm2p._intern import ParamsMixin
from tm2p.enum import ThField, UnitOrderBy

from ._intern import (
    add_padding,
    load_thesaurus,
    remove_thesaurus_stopwords,
    report_matches,
)

PREFERRED = ThField.PREFERRED.value
SIGNATURE = ThField.SIGNATURE.value


class BaseExpressionMatch(
    ParamsMixin,
):
    """:meta private:"""

    def run(self) -> None:

        from tm2p.portf.perf_metric.unit import Metrics

        if isinstance(self.params.pattern, str):
            self.params.pattern = (self.params.pattern,)

        thesaurus_df = load_thesaurus(params=self.params)
        thesaurus_df = add_padding(thesaurus_df=thesaurus_df)  # type: ignore
        thesaurus_df = remove_thesaurus_stopwords(thesaurus_df=thesaurus_df)

        thesaurus_df = thesaurus_df.loc[
            thesaurus_df[PREFERRED].apply(
                lambda x: any(p in x for p in self.params.pattern)
            ),
            :,
        ]

        metrics = (
            Metrics()
            .update(**self.params.__dict__)
            #
            .having_top_n_units(None)
            .having_units_ordered_by(UnitOrderBy.OCC)
            .having_unit_occurrence_between(None, None)
            .having_unit_global_citation_between(None, None)
            .having_units_in(None)
            #
            .where_record_years_range(None, None)
            .where_record_global_citations_range(None, None)
            .where_records_match(None)
            .run()
        )
        counters = dict(zip(metrics.index, metrics.COUNTERS))

        terms = thesaurus_df[PREFERRED].tolist()
        matches: dict[str, list[str]] = {}

        for pat in self.params.pattern:

            pat_with_counters = counters.get(pat, pat + " 0:0")
            for term in terms:
                if pat == term:
                    pat_with_counters = counters.get(term, term + " 0:0")
                    break

            for term in terms:
                if pat in term:

                    if pat == term:
                        continue
                    term_with_counters = counters.get(term, term + " 0:0")
                    matches.setdefault(pat_with_counters, []).append(term_with_counters)

        report_matches(
            params=self.params,
            mapping=matches,
        )

        sys.stderr.write(f"\n{len(thesaurus_df)} records found\n")
        sys.stderr.flush()
