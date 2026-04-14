"""
Main Path Documents
===============================================================================

Smoke tests:
    >>> from tm2p import RecordOrderBy
    >>> from tm2p.synthesize.main_path import MainPathDocuments
    >>> df = (
    ...     MainPathDocuments()
    ...     #
    ...     # ANALYSIS UNIT:
    ...     .having_items_in_top(None)
    ...     .having_minimum_citation_count(0)
    ...     #
    ...     # DATABASE:
    ...     .where_root_directory("tests/wos/")
    ...     .where_record_years_range(None, None)
    ...     .where_record_citations_range(None, None)
    ...     .where_records_match(None)
    ...     .where_records_ordered_by(RecordOrderBy.YEAR_NEWEST)
    ...     #
    ...     .run()
    ... )
    >>> len(df)
    8
    >>> print(df[0])
    UT 105
    AR Li YW, 2025, MANAG DECIS ECON, V46, P3683, DOI 10.1002/mde.4552
    TI Can Bank Regulatory Technology (RegTech) Boost Corporate Investment
       Efficiency?  Evidence From Matched Bank-Firm Loan Data
    AU Li YW; Xia YF; Shi HY; Li N; Shi ZX
    TC 1
    SO MANAG DECIS ECON
    PY 2025
    AB Banks are dedicated to serving the real economy.  In recent years,
       regulatory technology (RegTech) has served as a prime focus in the banking
       sector and may further spillover to external parties.  This paper aims to
       investigate whether bank RegTech enhances corporate investment efficiency
       (CIE) through its influence on lending activities.  Using novel matched
       bank-firm loan data from 2013 to 2023, we empirically demonstrate that bank
       RegTech improves CIE. A 1% rise in the standard deviation of bank RegTech
       corresponds to a maximum of approximately 18.13% improvement in average CIE.
       Specifically, bank RegTech enhances CIE by mitigating financing constraints,
       strengthening governance capabilities, and reducing operational risks.  The
       beneficial effects of bank RegTech on CIE are further amplified by
       information transparency and media coverage, while industry competition
       weakens this effect.  The impact of bank RegTech on CIE exhibits
       heterogeneous characteristics, varying with different dimensions of bank
       RegTech and firm-level characteristics.  Our results still hold after
       alleviating endogeneity concerns and performing robustness checks.
       Furthermore, we find that improvements in CIE enhance firm performance,
       stimulate innovation, and promote job creation.
    DE financing constraints; governance capacity; investment effi-ciency;
       operational risk; regulatory technology
    ID product market competition; managerial overconfidence; social-
       responsibility; information asymmetry; earnings ma-nagement; governance;
       per-formance; quality; impact; constraints
    <BLANKLINE>





"""

from tm2p._intern import ParamsMixin
from tm2p.enum import Field
from tm2p.ingest.records import RecordViewer
from tm2p.portfolio.intellectual_structure.main_path._intern.compute_main_path import (
    compute_main_path,
)


class MainPathDocuments(
    ParamsMixin,
):
    """:meta private:"""

    def run(self):
        """:meta private:"""

        #
        # Creates a table with citing and cited articles
        articles_in_main_path, _ = compute_main_path(params=self.params)

        #
        # remove counters
        articles_in_main_path = [
            " ".join(article.split(" ")[:-1]) for article in articles_in_main_path
        ]

        #
        # build the filter
        records_match = {Field.REC_ID: articles_in_main_path}

        documents = (
            RecordViewer()
            .update(**self.params.__dict__)
            .with_source_field(Field.ABSTR_RAW)
            .where_records_match(records_match)
            .run()
        )

        return documents
