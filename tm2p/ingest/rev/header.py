"""
ExtractSectionHeaders
===============================================================================

Smoke test:
    >>> from tm2p.ingest.rev import ExtractSectionHeaders
    >>> text = (
    ...     ExtractSectionHeaders()
    ...     .where_root_directory("tests/tinyml-scopus/")
    ...     .run()
    ... )
    >>> assert isinstance(text, list)
    >>> assert all(isinstance(t, str) for t in text)
    >>> for t in text[:5]: print(t)  # doctest: +SKIP
                                                        FIGURE 1  :  CALM_PPG_SIGNAL ( a ) , stressed PPG_SIGNAL ( b ) 2025 CO…
                                                        FIGURE 1  :  EXPERIMENTAL_TEST_SETUP implemented in the LABORATORY
                                                         GROUP 1  :  the SUGGESTED_TRADITIONAL_RAIL_MONITORING_SYSTEM ( RULE_B…
                                                         GROUP 2  :  relates to RAILWAY_TRANSIT for_the_purpose_of TRACKING an…
          we_evaluate two CLASSES of PRUNING_IMPORTANCE_CRITERIA  :  STRUCTURAL_METRICS , represented by BATCH_NORMALIZATION_S…

"""

from tm2p._intern import ParamsMixin
from tm2p.enum import Field
from tm2p.explor.concord import KWICConcordance

__reviewed__ = "2026-01-28"


class ExtractSectionHeaders(
    ParamsMixin,
):
    """:meta private:"""

    def run(self) -> list[str]:

        return (
            KWICConcordance()
            .update(**self.params.__dict__)
            .with_source_field(Field.ABSTR_UPPER)
            .having_text_matching(" : ")
            .where_record_years_range(None, None)
            .where_record_global_citations_range(None, None)
            .where_records_match(None)
            .run()
        )


if __name__ == "__main__":

    (
        KWICConcordance()
        .where_root_directory("./")
        .with_source_field(Field.ABSTR_UPPER)
        .having_text_matching(" : ")
        .where_record_years_range(None, None)
        .where_record_global_citations_range(None, None)
        .where_records_match(None)
        .run()
    )
