"""
Find records
===============================================================================

Smoke tests:
    >>> from tm2p.enum import Field, RecordOrderBy
    >>> from tm2p.ingest.rec import FindRecords
    >>> docs = (
    ...     FindRecords()
    ...     #
    ...     # FIELD:
    ...     .with_source_field(Field.AUTHKW_NORM)
    ...     #
    ...     # SEARCH:
    ...     .having_text_matching('tinyml')
    ...     .having_regex_search(False)
    ...     .having_case_sensitive(False)
    ...     .having_regex_flags(0)
    ...     #
    ...     .where_root_directory("tests/tinyml-scopus/")
    ...     .where_record_years_range(None, None)
    ...     .where_record_global_citations_range(None, None)
    ...     .where_records_match(None)
    ...     .where_records_ordered_by(RecordOrderBy.YEAR_NEWEST)
    ...      #
    ...      .run()
    ... )
    >>> assert len(docs) > 0
    >>> assert isinstance(docs[0], str)
    >>> print(docs[0])  # doctest: +SKIP
    UT 292
    AR Heydari S, 2025, SENSORS, V25, DOI 10.3390/s25103191
    TI Tiny Machine Learning and On-Device Inference: A Survey of Applications,
       Challenges, and Future Directions
    AU Heydari S; Mahmoud QH
    TC 45
    SO SENSORS
    PY 2025
    AB the growth in ARTIFICIAL_INTELLIGENCE and_its applications has LED to
       INCREASED_DATA_PROCESSING_AND_INFERENCE_REQUIREMENTS .
       TRADITIONAL_CLOUD_BASED_INFERENCE_SOLUTIONS are often used but may prove
       inadequate for applications requiring NEAR_INSTANTANEOUS_RESPONSE_TIMES .
       this_review_examines TINY_MACHINE_LEARNING , also known as TINYML , as an
       alternative to CLOUD_BASED_INFERENCE . the REVIEW_FOCUSES on applications
       where TRANSMISSION_DELAYS make traditional
       INTERNET_OF_THINGS_APPROACHES_IMPRACTICAL , thus necessitating a solution
       that USES_TINYML_AND_ON_DEVICE_INFERENCE . this_study , which follows the
       PRISMA_GUIDELINES , covers TINYML s USE_CASES for REAL_WORLD_APPLICATIONS by
       analyzing EXPERIMENTAL_STUDIES and synthesizing current research_on
       the_characteristics_of TINYML_EXPERIMENTS , such as
       MACHINE_LEARNING_TECHNIQUES and the HARDWARE used for EXPERIMENTS .
       this_review_identifies existing gaps in research as_well_as the means to
       address these gaps . the REVIEW_FINDINGS suggest that TINYML has a
       STRONG_RECORD of REAL_WORLD_USABILITY and offers advantages over
       CLOUD_BASED_INFERENCE , particularly in environments with
       BANDWIDTH_CONSTRAINTS and USE_CASES that require RAPID_RESPONSE_TIMES .
       this_review discusses the implications of TINYML s EXPERIMENTAL_PERFORMANCE
       for future research_on TINYML_APPLICATIONS . 2025 by the_authors .
    DE edge ai; edge computing; embedded ml; embedded systems; iot; resource-
       constrained devices; sensors; tinyml
    ID data integration; data streams; sorting; cloud-based; edge ai; edge
       computing; embedded ml; embedded-system; its applications; machine learning;
       real-world; resource-constrained devices; tinyml; artificial intelligence;
       bandwidth; cloud computing; data processing; experimental study; human;
       internet of things; machine learning; nonhuman; preferred reporting items
       for systematic reviews and meta-analyses; reaction time; review; sensor;
       data reduction
    <BLANKLINE>




"""

from tm2p._intern import ParamsMixin
from tm2p._intern.data_access.load_filtered_main_csv_zip import (
    load_filtered_main_csv_zip,
)
from tm2p._intern.rec_build import dicts_to_strings, records_to_dicts
from tm2p.enum import Field


class FindRecords(ParamsMixin):
    """:meta private:"""

    # -------------------------------------------------------------------------
    def _filter_records(self, records):

        records = records.copy()
        records = records.dropna(subset=[self.params.source_field.value])
        records["_order_"] = range(len(records))

        if isinstance(self.params.pattern, str):
            patterns = (self.params.pattern,)
        else:
            patterns = self.params.pattern

        selected = set()
        for pattern in patterns:

            contains = records[self.params.source_field.value].str.contains(
                pat=pattern,
                case=self.params.case_sensitive,
                flags=self.params.regex_flags,
                regex=self.params.regex_search,
            )
            selected.update(records[contains]["_order_"].tolist())

        records = records[records["_order_"].isin(selected)].drop(columns="_order_")

        return records

    # -------------------------------------------------------------------------
    def run(self):

        records = load_filtered_main_csv_zip(params=self.params)
        records = self._filter_records(records)
        mapping = records_to_dicts(records, field=Field.ABSTR_UPPER)
        documents = dicts_to_strings(mapping)

        return documents
