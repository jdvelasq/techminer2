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

Example:
    >>> from techminer2.thesaurus.countries import (
    ...     InitializeThesaurus as CreateCountryThesaurus,
    ...     ApplyThesaurus as ApplyCountryThesaurus,
    ... )
    >>> from techminer2.thesaurus.organizations import (
    ...     InitializeThesaurus as CreateOrganizationsThesaurus,
    ...     ApplyThesaurus as ApplyOrganizationsThesaurus,
    ... )
    >>> from techminer2.thesaurus.descriptors import (
    ...     InitializeThesaurus as CreateDescriptorsThesaurus,
    ...     ApplyThesaurus as ApplyDescriptorsThesaurus,
    ... )
    >>> from techminer2.tools import RecordMapping
    >>> from pprint import pprint

    >>> # Countries:
    >>> CreateCountryThesaurus(root_directory="examples/fintech/", quiet=True).run()
    >>> ApplyCountryThesaurus(root_directory="examples/fintech/", quiet=True).run()

    >>> # Organizations:
    >>> CreateOrganizationsThesaurus(root_directory="examples/fintech/", quiet=True).run()
    >>> ApplyOrganizationsThesaurus(root_directory="examples/fintech/", quiet=True).run()

    >>> # Descriptors:
    >>> CreateDescriptorsThesaurus(root_directory="examples/fintech/", quiet=True).run()
    >>> ApplyDescriptorsThesaurus(root_directory="examples/fintech/", quiet=True).run()



    >>> # Create, configure, and run the mapper
    >>> # order_records_by:
    >>> #   date_newest, date_oldest, global_cited_by_highest, global_cited_by_lowest
    >>> #   local_cited_by_highest, local_cited_by_lowest, first_author_a_to_z
    >>> #   first_author_z_to_a, source_title_a_to_z, source_title_z_to_a
    >>> #
    >>> mapper = (
    ...     RecordMapping()
    ...     #
    ...     .where_root_directory_is("examples/fintech/")
    ...     .where_database_is("main")
    ...     .where_record_years_range_is(None, None)
    ...     .where_record_citations_range_is(None, None)
    ...     .where_records_match(None)
    ...     .where_records_ordered_by("global_cited_by_highest")
    ... )
    >>> mapping = mapper.run()

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
           'SERVICES influenced by BLOCKCHAIN_AND_FINTECH_INNOVATIONS . copyright '
           'taylor and francis group , llc .',
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
     'UT': 30}


"""

from techminer2._internals.mixins import (
    ParamsMixin,
    RecordMappingMixin,
    RecordViewerMixin,
)
from techminer2.database._internals.io.load_filtered_records_from_database import (
    internal__load_filtered_records_from_database,
)


class RecordMapping(
    ParamsMixin,
    RecordMappingMixin,
    RecordViewerMixin,
):
    """:meta private:"""

    def run(self):

        records = internal__load_filtered_records_from_database(params=self.params)
        mapping = self.build_record_mapping(records)
        return mapping
