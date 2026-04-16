"""
RecordViewer
=======================================================================================

Smoke tests:
    >>> from tm2p.enum import Field, RecordOrderBy
    >>> from tm2p.ingest.records import RecordViewer
    >>> docs = (
    ...     RecordViewer()
    ...     #
    ...     .with_source_field(Field.ABSTR_RAW)
    ...     .where_root_directory("tests/scopus/")
    ...     .where_record_years_range(None, None)
    ...     .where_record_global_citations_range(None, None)
    ...     .where_records_match(None)
    ...     .where_records_ordered_by(RecordOrderBy.YEAR_NEWEST)
    ...     .run()
    ... )
    >>> len(docs)
    180
    >>> print(docs[0])
    UT 54
    AR Al-Sartawi A, 2024, J FINANC REP ACC, DOI 10.1108/JFRA-01-2024-0010
    TI The diffusion of financial technology-enabled innovation in GCC-listed banks
       and its relationship with profitability and market value
    AU Al-Sartawi A
    TC 125
    SO J FINANC REP ACC
    PY 2024
    AB Purpose: This study aims to examine the relationship between the diffusion
       of technology-enabled innovation in financial services (i.e.  financial
       technology [FinTech]) and the financial performance, i.e.  profitability and
       market value of the banks listed in the Gulf Cooperation Council (GCC)
       countries.  Design/methodology/approach: An extensive review of the
       literature was carried out, and a diffusion index of 73 items including was
       adopted to measure the level of FinTech usage or diffusion for the banks
       that are listed on the GCC stock exchanges.  The study used return on assets
       (ROA) and Tobin’s Q (TQ) as proxies to measure profitability and market
       value, respectively.  Findings: The findings of the empirical results
       indicate that there is a positive relationship between FinTech
       implementation and market performance (TQ) in the GCC banks.  The results
       also showed that the highest level of FinTech implementation was 79.7% by
       United Arab Emirates banks followed by Bahraini banks at 76.7% based on the
       index developed for this study.  Practical implications: This study, hence,
       recommends that policymakers and governments implement supportive policies
       and initiatives, allowing consumers to embrace technology as part of their
       way of life.  This encourages banks and other organizations to formulate
       strategies that integrate technology into operations.  Originality/value:
       This paper offers new contributions to the GCC literature regarding
       financial technology and provides recommendations to the GCC financial
       institutions, financial markets, policymakers and governments.  © 2024,
       Emerald Publishing Limited.
    DE digital transformation; financial sector; fintech; fintech governance;
       fintech strategies; firm market value; gcc countries; profitability
    <BLANKLINE>



"""

from tm2p._intern import ParamsMixin
from tm2p._intern.rec_build import dicts_to_strings
from tm2p.ingest.records import RecordMapping


class RecordViewer(ParamsMixin):
    """:meta private:"""

    def run(self):

        mapping = RecordMapping().update(**self.params.__dict__).run()
        string_list = dicts_to_strings(mapping)
        return string_list
