# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
# pylint: disable=too-many-statements
"""
Record Viewer
=======================================================================================

>>> # order_records_by:
>>> #   date_newest, date_oldest, global_cited_by_highest, global_cited_by_lowest
>>> #   local_cited_by_highest, local_cited_by_lowest, first_author_a_to_z
>>> #   first_author_z_to_a, source_title_a_to_z, source_title_z_to_a
>>> # 
>>> # For most global cited documents use: 
>>> #    .where_database_is("main")
>>> #    .where_records_ordered_by("global_cited_by_highest")
>>> #
>>> # For most local cited documents use: 
>>> #    .where_database_is("main")
>>> #    .where_records_ordered_by("local_cited_by_highest")
>>> #
>>> # For most global cited references use:
>>> #    .where_database_is("references")
>>> #    .where_records_ordered_by("global_cited_by_highest")
>>> #
>>> # For most local cited references use: 
>>> #    .where_database_is("references")
>>> #    .where_records_ordered_by("local_cited_by_highest")
>>> #
>>> from techminer2.database.tools import RecordViewer
>>> documents = (
...     RecordViewer()
...     #
...     .where_directory_is("example/")
...     .where_database_is("main")
...     .where_record_years_between(None, None)
...     .where_record_citations_between(None, None)
...     .where_records_match(None)
...     .where_records_ordered_by("global_cited_by_highest")  
...     #
...     .build()
... )
>>> len(documents)
50
>>> print(documents[0])
UT 1260
AR Gomber P., 2018, J MANAGE INF SYST, V35, P220
TI On the Fintech Revolution: Interpreting the Forces of Innovation,
   Disruption, and Transformation in Financial Services
AU Gomber P.; Kauffman R.J.; Parker C.; Weber B.W.
TC 576
SO Journal of Management Information Systems
PY 2018
AB THE_FINANCIAL_SERVICES_INDUSTRY has been experiencing THE_RECENT_EMERGENCE
   of NEW_TECHNOLOGY_INNOVATIONS and PROCESS_DISRUPTIONS . THE_INDUSTRY overall
   , and MANY_FINTECH_START_UPS are looking for NEW_PATHWAYS to
   SUCCESSFUL_BUSINESS_MODELS , THE_CREATION of ENHANCED_CUSTOMER_EXPERIENCE ,
   and APPROACHES that result in SERVICES_TRANSFORMATION . INDUSTRY and
   ACADEMIC_OBSERVERS believe this to be more of A_REVOLUTION than A_SET of
   LESS_INFLUENTIAL_CHANGES , with FINANCIAL_SERVICES as A_WHOLE due for
   MAJOR_IMPROVEMENTS in EFFICIENCY , CUSTOMER_CENTRICITY , and INFORMEDNESS .
   THE_LONG_STANDING_DOMINANCE of LEADING_FIRMS that are not able to figure out
   how to effectively hook up with THE_FINTECH_REVOLUTION is at STAKE . we
   present A_NEW_FINTECH_INNOVATION_MAPPING_APPROACH that enables
   THE_ASSESSMENT of THE_EXTENT to which there are CHANGES and TRANSFORMATIONS
   in FOUR_AREAS of FINANCIAL_SERVICES . we discuss : OPERATIONS_MANAGEMENT in
   FINANCIAL_SERVICES and THE_CHANGES occurring . TECHNOLOGY_INNOVATIONS that
   have begun to leverage THE_EXECUTION and STAKEHOLDER_VALUE associated with
   PAYMENTS , CRYPTOCURRENCIES , BLOCKCHAIN , and CROSS_BORDER_PAYMENTS .
   MULTIPLE_INNOVATIONS that have affected LENDING_AND_DEPOSIT_SERVICES ,
   PEER_TO_PEER ( P2P ) LENDING , and SOCIAL_MEDIA_USE . ISSUES with_respect_to
   INVESTMENTS , FINANCIAL_MARKETS , TRADING , RISK_MANAGEMENT , ROBO_ADVISORY
   and SERVICES influenced by BLOCKCHAIN_AND_FINTECH_INNOVATIONS .
   COPYRIGHT_TAYLOR and FRANCIS_GROUP , llc .
ID BLOCKCHAIN; COMMERCE; RISK_MANAGEMENT; BUSINESS_MODELS; CUSTOMER_EXPERIENCE;
   FINANCIAL_SERVICE; FINANCIAL_SERVICES_INDUSTRIES; NEW_TECHNOLOGIES;
   OPERATIONS_MANAGEMENT; STAKEHOLDER_VALUES; TECHNOLOGY_INNOVATION; FINANCE
<BLANKLINE>


"""

from ...internals.mixins import ParamsMixin, RecordMappingMixin, RecordViewerMixin
from ..internals.io.load_filtered_database import internal__load_filtered_database


class RecordViewer(
    ParamsMixin,
    RecordMappingMixin,
    RecordViewerMixin,
):
    """:meta private:"""

    def build(self):

        records = (
            internal__load_filtered_database()
            .update_params(**self.params.__dict__)
            .build()
        )
        mapping = self.build_record_mapping(records)
        documents = self.build_record_viewer(mapping)
        return documents
