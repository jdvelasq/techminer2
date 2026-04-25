"""
RecordViewer
=======================================================================================

Smoke tests:
    >>> from tm2p.enum import Field, RecordOrderBy
    >>> from tm2p.ingest.rec import RecordViewer
    >>> docs = (
    ...     RecordViewer()
    ...     #
    ...     .with_source_field(Field.ABSTR_RAW)
    ...     .where_root_directory("tests/tinyml-scopus/")
    ...     .where_record_years_range(None, None)
    ...     .where_record_global_citations_range(None, None)
    ...     .where_records_match(None)
    ...     .where_records_ordered_by(RecordOrderBy.YEAR_NEWEST)
    ...     .run()
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
    AB The growth in artificial intelligence and its applications has led to
       increased data processing and inference requirements.  Traditional cloud-
       based inference solutions are often used but may prove inadequate for
       applications requiring near-instantaneous response times.  This review
       examines Tiny Machine Learning, also known as TinyML, as an alternative to
       cloud-based inference.  The review focuses on applications where
       transmission delays make traditional Internet of Things (IoT) approaches
       impractical, thus necessitating a solution that uses TinyML and on-device
       inference.  This study, which follows the PRISMA guidelines, covers TinyML’s
       use cases for real-world applications by analyzing experimental studies and
       synthesizing current research on the characteristics of TinyML experiments,
       such as machine learning techniques and the hardware used for experiments.
       This review identifies existing gaps in research as well as the means to
       address these gaps.  The review findings suggest that TinyML has a strong
       record of real-world usability and offers advantages over cloud-based
       inference, particularly in environments with bandwidth constraints and use
       cases that require rapid response times.  This review discusses the
       implications of TinyML’s experimental performance for future research on
       TinyML applications.  © 2025 by the authors.
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
from tm2p._intern.rec_build import dicts_to_strings
from tm2p.ingest.rec import RecordMapping


class RecordViewer(ParamsMixin):
    """:meta private:"""

    def run(self):

        mapping = RecordMapping().update(**self.params.__dict__).run()
        string_list = dicts_to_strings(mapping)
        return string_list
