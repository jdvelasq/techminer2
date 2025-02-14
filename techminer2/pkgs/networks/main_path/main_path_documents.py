# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
# pylint: disable=too-many-statements
"""
Main Path Documents
===============================================================================


>>> # where_records_ordered_by:
>>> #     date_newest, date_oldest, global_cited_by_highest, 
>>> #     global_cited_by_lowest, local_cited_by_highest, 
>>> #     local_cited_by_lowest, first_author_a_to_z, 
>>> #     first_author_z_to_a, source_title_a_to_z, 
>>> #     source_title_z_to_a
>>> from techminer2.pkgs.networks.main_path import MainPathDocuments
>>> documents = (
...     MainPathDocuments()
...     #
...     # UNIT OF ANALYSIS:
...     .having_terms_in_top(None)
...     .having_citation_threshold(0)
...     #
...     # DATABASE:
...     .where_directory_is("example/")
...     .where_database_is("main")
...     .where_record_years_between(None, None)
...     .where_record_citations_between(None, None)
...     .where_records_match(None)
...     .where_records_ordered_by("data_newest") 
...     #
...     .build()
... )
--INFO-- Paths computed.
--INFO-- Points per link computed.
--INFO-- Points per path computed.

>>> len(documents)
5
>>> print(documents[0])
UT 1178
AR Gomber P., 2017, J BUS ECON, V87, P537
TI Digital Finance and FinTech: current research and future research directions
AU Gomber P.; Koch J.-A.; Siering M.
TC 489
SO Journal of Business Economics
PY 2017
AB since DECADES , THE_FINANCIAL_INDUSTRY has experienced
   A_CONTINUOUS_EVOLUTION in SERVICE_DELIVERY due_to DIGITALIZATION .
   THIS_EVOLUTION is characterized by EXPANDED_CONNECTIVITY and ENHANCED_SPEED
   of INFORMATION_PROCESSING both at THE_CUSTOMER_INTERFACE and in
   BACK_OFFICE_PROCESSES . recently , there has been A_SHIFT in THE_FOCUS of
   DIGITALIZATION from improving THE_DELIVERY of TRADITIONAL_TASKS to
   introducing FUNDAMENTALLY_NEW_BUSINESS_OPPORTUNITIES and MODELS for
   FINANCIAL_SERVICE_COMPANIES . DIGITAL_FINANCE_ENCOMPASSES A_MAGNITUDE of
   NEW_FINANCIAL_PRODUCTS , FINANCIAL_BUSINESSES , FINANCE RELATED_SOFTWARE ,
   and NOVEL_FORMS of CUSTOMER_COMMUNICATION and INTERACTION delivered by
   FINTECH_COMPANIES and INNOVATIVE_FINANCIAL_SERVICE_PROVIDERS . against
   THIS_BACKDROP , THE_RESEARCH on FINANCE and INFORMATION_SYSTEMS has started
   to analyze THESE_CHANGES and THE_IMPACT of DIGITAL_PROGRESS on
   THE_FINANCIAL_SECTOR . therefore , THIS_ARTICLE REVIEWS THE_CURRENT_STATE of
   RESEARCH in DIGITAL_FINANCE that deals with
   THESE_NOVEL_AND_INNOVATIVE_BUSINESS_FUNCTIONS . moreover , it gives
   AN_OUTLOOK on POTENTIAL_FUTURE_RESEARCH_DIRECTIONS . as A_CONCEPTUAL_BASIS
   for reviewing THIS_FIELD , the DIGITAL_FINANCE_CUBE , which embraces
   THREE_KEY_DIMENSIONS of DIGITAL_FINANCE and FINTECH , i . e . ,
   THE_RESPECTIVE_BUSINESS_FUNCTIONS , THE_TECHNOLOGIES and
   TECHNOLOGICAL_CONCEPTS applied as_well_as THE_INSTITUTIONS concerned , is
   introduced . THIS_CONCEPTUALIZATION supports RESEARCHERS and PRACTITIONERS
   when orientating in THE_FIELD of DIGITAL_FINANCE , allows for
   THE_ARRANGEMENT of ACADEMIC_RESEARCH relatively to each other , and enables
   for THE_REVELATION of THE_GAPS in RESEARCH . 2017 ,
   SPRINGER_VERLAG_BERLIN_HEIDELBERG .
DE DIGITAL_FINANCE; E_FINANCE; FINTECH; FUTURE_RESEARCH_OPPORTUNITIES;
   LITERATURE_REVIEW; STATE_OF_THE_ART
<BLANKLINE>



"""
from ....database.tools import RecordViewer
from ....internals.mixins import ParamsMixin
from .internals.compute_main_path import internal__compute_main_path


class MainPathDocuments(
    ParamsMixin,
):
    """:meta private:"""

    def build(self):
        """:meta private:"""

        #
        # Creates a table with citing and cited articles
        articles_in_main_path, _ = internal__compute_main_path(params=self.params)

        #
        # remove counters
        articles_in_main_path = [
            " ".join(article.split(" ")[:-1]) for article in articles_in_main_path
        ]

        #
        # build the filter
        records_match = {"record_id": articles_in_main_path}

        documents = (
            RecordViewer()
            .update_params(**self.params.__dict__)
            .where_records_match(records_match)
            .build()
        )

        return documents
