"""
RecordMapping
===============================================================================

Smoke Test:
    >>> from pprint import pprint
    >>> from tm2p.enum import Field, RecordOrderBy
    >>> from tm2p.ingest.rec import RecordMapping
    >>> mapping = (
    ...     RecordMapping()
    ...     #
    ...     .with_source_field(Field.ABSTR_RAW)
    ...     .where_root_directory("tests/tinyml-scopus/")
    ...     .where_record_years_range(None, None)
    ...     .where_record_global_citations_range(None, None)
    ...     .where_records_match(None)
    ...     .where_records_ordered_by(RecordOrderBy.GCS_HIGHEST)
    ...     .run()
    ... )
    >>> assert len(mapping) > 0
    >>> pprint(mapping[0])  # doctest: +SKIP
    {'AB': 'Machine learning has become an indispensable part of the existing '
           'technological domain. Edge computing and Internet of Things (IoT) '
           'together presents a new opportunity to imply machine learning '
           'techniques at the resource constrained embedded devices at the edge of '
           'the network. Conventional machine learning requires enormous amount of '
           'power to predict a scenario. Embedded machine learning – TinyML '
           'paradigm aims to shift such plethora from traditional high-end systems '
           'to low-end clients. Several challenges are paved while doing such '
           'transition such as, maintaining the accuracy of learning models, '
           'provide train-to-deploy facility in resource frugal tiny edge devices, '
           'optimizing processing capacity, and improving reliability. In this '
           'paper, we present an intuitive review about such possibilities for '
           'TinyML. We firstly, present background of TinyML. Secondly, we list '
           'the tool sets for supporting TinyML. Thirdly, we present key enablers '
           'for improvement of TinyML systems. Fourthly, we present '
           'state-of-the-art about frameworks for TinyML. Finally, we identify key '
           'challenges and prescribe a future roadmap for mitigating several '
           'research issues of TinyML. © 2021 The Authors',
     'AR': 'Ray PP, 2022, J KING SAUD UNIV - COMPUT INF SCI, V34, P1595, DOI '
           '10.1016/j.jksuci.2021.11.019',
     'AU': 'Ray PP',
     'DE': 'edge intelligence; embedded ai; energy efficient ai; iot; '
           'resource-constrained intelligence; tinyml',
     'ID': nan,
     'PY': 2022,
     'SO': 'J KING SAUD UNIV - COMPUT INF SCI',
     'TC': 352,
     'TI': 'A review on TinyML: State-of-the-art and prospects',
     'UT': 1135}



"""

from tm2p._intern import ParamsMixin
from tm2p._intern.data_access.load_filtered_main_csv_zip import (
    load_filtered_main_csv_zip,
)
from tm2p._intern.rec_build import records_to_dicts


class RecordMapping(
    ParamsMixin,
):
    """:meta private:"""

    def run(self):

        records = load_filtered_main_csv_zip(params=self.params)
        mapping = records_to_dicts(records, field=self.params.source_field)
        return mapping
