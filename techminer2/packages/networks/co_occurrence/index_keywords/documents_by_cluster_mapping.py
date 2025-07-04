# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
# pylint: disable=too-many-statements
"""
Terms to Cluster Mapping
===============================================================================


Example:
    >>> # where_records_ordered_by: date_newest, date_oldest, global_cited_by_highest,
    >>> #                           global_cited_by_lowest, local_cited_by_highest,
    >>> #                           local_cited_by_lowest, first_author_a_to_z,
    >>> #                           first_author_z_to_a, source_title_a_to_z,
    >>> #                           source_title_z_to_a
    >>> from techminer2.packages.networks.co_occurrence.index_keywords import DocumentsByClusterMapping
    >>> documents_by_cluster = (
    ...     DocumentsByClusterMapping()
    ...     #
    ...     # FIELD:
    ...     .having_terms_in_top(20)
    ...     .having_terms_ordered_by("OCC")
    ...     .having_term_occurrences_between(None, None)
    ...     .having_term_citations_between(None, None)
    ...     .having_terms_in(None)
    ...     #
    ...     # NETWORK:
    ...     .using_clustering_algorithm_or_dict("louvain")
    ...     .using_association_index("association")
    ...     #
    ...     # DATABASE:
    ...     .where_root_directory_is("example/")
    ...     .where_database_is("main")
    ...     .where_record_years_range_is(None, None)
    ...     .where_record_citations_range_is(None, None)
    ...     .where_records_match(None)
    ...     .where_records_ordered_by("date_newest")
    ...     #
    ...     .run()
    ... )
    >>> print(len(documents_by_cluster))
    4
    >>> print(documents_by_cluster[0][0])
    UT 1346
    AR Gracia D.B., 2019, IND MANAGE DATA SYS, V119, P1411
    TI Artificial Intelligence in FinTech: understanding robo-advisors adoption
       among customers
    AU Gracia D.B.; Casaló-Ariño L.V.; Flavián C.
    TC 225
    SO Industrial Management and Data Systems
    PY 2019
    AB purpose : considering THE_INCREASING_IMPACT of ARTIFICIAL_INTELLIGENCE ( AI
       ) on FINANCIAL_TECHNOLOGY ( FINTECH ) , the purpose of this paper is to
       propose A_RESEARCH_FRAMEWORK to better understand ROBO_ADVISOR_ADOPTION by
       A_WIDE_RANGE of POTENTIAL_CUSTOMERS . it also predicts that
       PERSONAL_AND_SOCIODEMOGRAPHIC_VARIABLES ( FAMILIARITY with ROBOTS , AGE ,
       GENDER and COUNTRY ) moderate THE_MAIN_RELATIONSHIPS .
       DESIGN/METHODOLOGY/approach : DATA from A_WEB_SURVEY of 765 north american ,
       british and PORTUGUESE_POTENTIAL_USERS of ROBO_ADVISOR_SERVICES confirm
       THE_VALIDITY of THE_MEASUREMENT_SCALES and provide THE_INPUT for
       STRUCTURAL_EQUATION_MODELING and MULTISAMPLE_ANALYSES of THE_HYPOTHESES .
       findings : CONSUMERS ' attitudes toward ROBO_ADVISORS , together_with
       MASS_MEDIA and INTERPERSONAL_SUBJECTIVE_NORMS , are found to be
       THE_KEY_DETERMINANTS of ADOPTION . THE_INFLUENCES of PERCEIVED_USEFULNESS
       and ATTITUDE are slightly higher for USERS with A_HIGHER_LEVEL of
       FAMILIARITY with ROBOTS . in_turn , SUBJECTIVE_NORMS are significantly more
       relevant for USERS with A_LOWER_FAMILIARITY and for CUSTOMERS from
       ANGLO_SAXON_COUNTRIES . practical implications : BANKS and OTHER_FIRMS in
       THE_FINANCE_INDUSTRY should DESIGN_ROBO_ADVISORS to be used by
       A_WIDE_SPECTRUM of CONSUMERS . MARKETING_TACTICS applied should consider
       THE_CUSTOMER_LEVEL of FAMILIARITY with ROBOTS . originality/VALUE : this
       research identifies THE_KEY_DRIVERS of ROBO_ADVISOR_ADOPTION and
       THE_MODERATING_EFFECT of PERSONAL_AND_SOCIODEMOGRAPHIC_VARIABLES . it
       contributes to UNDERSTANDING_CONSUMERS ' perceptions regarding
       THE_INTRODUCTION of AI_IN_FINTECH . 2019 , emerald publishing limited .
    DE ARTIFICIAL_INTELLIGENCE; FINANCE; ROBO_ADVISORS; ROBOTS; TECHNOLOGY_ADOPTION
    ID FINANCE; FINTECH; INTELLIGENT_ROBOTS; ROBOTS; SALES;
       DESIGN_METHODOLOGY_APPROACH; PERCEIVED_USEFULNESS; POTENTIAL_CUSTOMERS;
       RESEARCH_FRAMEWORKS; ROBO_ADVISORS; SOCIO_DEMOGRAPHIC_VARIABLES;
       STRUCTURAL_EQUATION_MODELING; TECHNOLOGY_ADOPTION; ARTIFICIAL_INTELLIGENCE
    <BLANKLINE>






"""
from ....._internals.mixins import ParamsMixin
from ..user.documents_by_cluster_mapping import (
    DocumentsByClusterMapping as UserDocumentsByClusterMapping,
)


class DocumentsByClusterMapping(
    ParamsMixin,
):
    """:meta private:"""

    def run(self):
        """:meta private:"""

        return (
            UserDocumentsByClusterMapping()
            .update(**self.params.__dict__)
            .with_field("index_keywords")
            .run()
        )
