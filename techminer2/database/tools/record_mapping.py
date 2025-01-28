# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
# pylint: disable=too-many-statements
"""
Record Mapping
===============================================================================

>>> # order_records_by:
>>> #   date_newest, date_oldest, global_cited_by_highest, global_cited_by_lowest
>>> #   local_cited_by_highest, local_cited_by_lowest, first_author_a_to_z
>>> #   first_author_z_to_a, source_title_a_to_z, source_title_z_to_a
>>> # 
>>> from techminer2.database.tools import RecordMapping
>>> mapping = (
...     RecordMapping()
...     #
...     .where_directory_is("example/")
...     .where_database_is("main")
...     .where_record_years_between(None, None)
...     .where_record_citations_between(None, None)
...     .where_records_match(None)
...     .order_records_by("global_cited_by_highest")  
...     #
...     .build()
... )
>>> from pprint import pprint
>>> pprint(mapping[0])
{'AB': 'THE_FINANCIAL_SERVICES_INDUSTRY has been experiencing '
       'THE_RECENT_EMERGENCE of NEW_TECHNOLOGY_INNOVATIONS and '
       'PROCESS_DISRUPTIONS . THE_INDUSTRY overall , and '
       'MANY_FINTECH_START_UPS are looking for NEW_PATHWAYS to '
       'SUCCESSFUL_BUSINESS_MODELS , THE_CREATION of '
       'ENHANCED_CUSTOMER_EXPERIENCE , and APPROACHES that result in '
       'SERVICES_TRANSFORMATION . INDUSTRY and ACADEMIC_OBSERVERS believe this '
       'to be more of A_REVOLUTION than A_SET of LESS_INFLUENTIAL_CHANGES , '
       'with FINANCIAL_SERVICES as A_WHOLE due for MAJOR_IMPROVEMENTS in '
       'EFFICIENCY , CUSTOMER_CENTRICITY , and INFORMEDNESS . '
       'THE_LONG_STANDING_DOMINANCE of LEADING_FIRMS that are not able to '
       'figure out how to effectively hook up with THE_FINTECH_REVOLUTION is '
       'at STAKE . we present A_NEW_FINTECH_INNOVATION_MAPPING_APPROACH that '
       'enables THE_ASSESSMENT of THE_EXTENT to which there are CHANGES and '
       'TRANSFORMATIONS in FOUR_AREAS of FINANCIAL_SERVICES . we discuss : '
       'OPERATIONS_MANAGEMENT in FINANCIAL_SERVICES and THE_CHANGES occurring '
       '. TECHNOLOGY_INNOVATIONS that have begun to leverage THE_EXECUTION and '
       'STAKEHOLDER_VALUE associated with PAYMENTS , CRYPTOCURRENCIES , '
       'BLOCKCHAIN , and CROSS_BORDER_PAYMENTS . MULTIPLE_INNOVATIONS that '
       'have affected LENDING_AND_DEPOSIT_SERVICES , PEER_TO_PEER ( P2P ) '
       'LENDING , and SOCIAL_MEDIA_USE . ISSUES with_respect_to INVESTMENTS , '
       'FINANCIAL_MARKETS , TRADING , RISK_MANAGEMENT , ROBO_ADVISORY and '
       'SERVICES influenced by BLOCKCHAIN_AND_FINTECH_INNOVATIONS . '
       'COPYRIGHT_TAYLOR and FRANCIS_GROUP , llc .',
 'AR': 'Gomber P., 2018, J MANAGE INF SYST, V35, P220',
 'AU': 'Gomber P.; Kauffman R.J.; Parker C.; Weber B.W.',
 'DE': nan,
 'ID': 'BLOCKCHAIN; COMMERCE; RISK_MANAGEMENT; BUSINESS_MODELS; '
       'CUSTOMER_EXPERIENCE; FINANCIAL_SERVICE; FINANCIAL_SERVICES_INDUSTRIES; '
       'NEW_TECHNOLOGIES; OPERATIONS_MANAGEMENT; STAKEHOLDER_VALUES; '
       'TECHNOLOGY_INNOVATION; FINANCE',
 'PY': 2018,
 'SO': 'Journal of Management Information Systems',
 'TC': 576,
 'TI': 'On the Fintech Revolution: Interpreting the Forces of Innovation, '
       'Disruption, and Transformation in Financial Services',
 'UT': 1260}

"""

from ...internals.mixins import InputFunctionsMixin
from ..load.load__database import DatabaseLoader


class RecordMapping(
    InputFunctionsMixin,
):
    """:meta private:"""

    def _step_01_load_filtered_records(self):
        return DatabaseLoader().update_params(**self.params.__dict__).build()

    def _step_02_list_columns_to_report(self, records, candiate_columns):
        columns_to_report = []
        for criterion in candiate_columns:
            if criterion in records.columns:
                columns_to_report.append(criterion)
        return columns_to_report

    def _step_03_filter_record_columns(self, records, selected_columns):
        records = records[selected_columns]
        return records

    def _step_04_rename_columns(self, records, names_mapping):
        records = records.rename(columns=names_mapping)
        return records

    def _step_05_build_record_mapping(self, records):
        return records.to_dict(orient="records")

    def build(self):

        names_mapping = {
            "record_no": "UT",
            "record_id": "AR",
            "raw_document_title": "TI",
            "authors": "AU",
            "global_citations": "TC",
            "source_title": "SO",
            "year": "PY",
            "abstract": "AB",
            "raw_author_keywords": "DE",
            "raw_index_keywords": "ID",
        }

        candiate_columns = names_mapping.keys()

        filtered_records = self._step_01_load_filtered_records()

        columns_to_report = self._step_02_list_columns_to_report(
            filtered_records,
            candiate_columns,
        )

        filtered_records = self._step_03_filter_record_columns(
            filtered_records,
            columns_to_report,
        )

        filtered_records = self._step_04_rename_columns(
            filtered_records,
            names_mapping,
        )

        mapping = self._step_05_build_record_mapping(
            filtered_records,
        )

        return mapping
