"""
UppercaseColumn
===============================================================================

Smoke test:
    >>> from tm2p.enum import Field
    >>> from tm2p.ingest.oper import UppercaseColumn
    >>> (
    ...     UppercaseColumn()
    ...     #
    ...     # FIELDS:
    ...     .with_source_field(Field.ABSTR_TOK)
    ...     .with_target_field(Field.USR0)
    ...     #
    ...     # DATABASE:
    ...     .where_root_directory("tests/regtech-scopus/")
    ...     #
    ...     .run()
    ... )

    >>> from tm2p.ingest.oper import Query
    >>> df = (
    ...     Query()
    ...     .with_query_expression("SELECT USR0 FROM database LIMIT 10;")
    ...     .where_root_directory("tests/regtech-scopus/")
    ...     .where_record_years_range(None, None)
    ...     .where_record_global_citations_range(None, None)
    ...     .where_records_match(None)
    ...     .run()
    ... )
    >>> import textwrap
    >>> print(textwrap.fill(df.values[1][0], width=90))  # doctest: +SKIP
    CORPORATE_CORRUPTION remains_a_significant_challenge to GOVERNANCE and ECONOMIC_STABILITY
    . this_study_investigates the efficacy of TECHNOLOGICAL_SOLUTIONS by examining how
    FINANCIAL_REGULATORY_TECHNOLOGY ( FINTECH ) , within the BROADER_CONTEXT of
    CORPORATE_DIGITAL_TRANSFORMATION , inhibits INTERNAL_CORRUPTION . using a PANEL_DATASET of
    CHINESE_PUBLICLY_LISTED_FIRMS from 2013 to 2023 , this_study find ROBUST_EVIDENCE that the
    ADOPTION_OF_FINTECH significantly CURTAILS_CORRUPTION . crucially , this DETERRENT_EFFECT
    is amplified by the firm s DIGITAL_TRANSFORMATION , indicating a POWERFUL_SYNERGY between
    SPECIFIC_REGULATORY_TOOLS and SYSTEMIC_ORGANIZATIONAL_CHANGE . the benefits , however ,
    are not uniform . HETEROGENEITY_ANALYSIS_REVEALS that LARGER_FIRMS , with
    GREATER_RESOURCES and more COMPLEX_STRUCTURES , derive more significant
    ANTI_CORRUPTION_BENEFITS from FINTECH . furthermore , the MODERATING_EFFECT of
    DIGITAL_TRANSFORMATION is most pronounced in firms with high INVESTMENT_LEVELS , which
    enables a more PROFOUND_TECHNOLOGICAL_INTEGRATION . these_findings_highlight that
    ISOLATED_TECHNOLOGICAL_SOLUTIONS are insufficient . rather , a HOLISTIC_DIGITAL_STRATEGY
    is KEY to enhancing CORPORATE_INTEGRITY . 2026 published by elsevier inc .



"""

from tm2p._intern import ParamsMixin
from tm2p.ingest.datasrc._intern.oper.upperc_keyterm import uppercase_keyterms
from tm2p.ingest.extr._helpers._protected_fields import PROTECTED_FIELDS


class UppercaseColumn(
    ParamsMixin,
):
    """:meta private:"""

    def run(self) -> None:

        if self.params.target_field in PROTECTED_FIELDS:
            raise ValueError(f"Field `{self.params.target_field}` is protected")

        uppercase_keyterms(
            source=self.params.source_field,
            target=self.params.target_field,
            root_directory=self.params.root_directory,
        )


#
