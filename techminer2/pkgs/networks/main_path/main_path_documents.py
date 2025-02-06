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

## >>> from techminer2.pkgs.main_path_analysis import MainPathDocuments
## >>> documents = (
## ...     MainPathDocuments()
## ...     .set_analysis_params(
## ...         top_n=None,
## ...         citations_threshold=0,
## ...     #
## ...     ).set_database_params(
## ...     #
## ...     # DATABASE:
## ...     .where_directory_is("example/")
## ...     .where_database_is("main")
## ...     .where_record_years_between(None, None)
## ...     .where_record_citations_between(None, None)
## ...     .where_records_match(None)
## ...     #
## ...     .build()
## ...         sort_by="date_oldest", # date_newest, date_oldest, global_cited_by_highest, 
## ...                                # global_cited_by_lowest, local_cited_by_highest, 
## ...                                # local_cited_by_lowest, first_author_a_to_z, 
## ...                                # first_author_z_to_a, source_title_a_to_z, 
## ...                                # source_title_z_to_a
## ...     #
## ...     ).build()
## ... )
--INFO-- Paths computed.
--INFO-- Points per link computed.
--INFO-- Points per path computed.
## >>> len(documents)
5
## >>> print(documents[0])
Record-No: 12
AR Gomber P., 2017, J BUS ECON, V87, P537
TI Digital Finance and FinTech: current research and future research directions
AU Gomber P.; Koch J.-A.; Siering M.
TC 489
SO Journal of Business Economics
PY 2017
AB since decades , the FINANCIAL_INDUSTRY has experienced a
   CONTINUOUS_EVOLUTION in SERVICE_DELIVERY due to DIGITALIZATION . this
   EVOLUTION is characterized by expanded connectivity and enhanced SPEED of
   INFORMATION_PROCESSING both at the CUSTOMER_INTERFACE and in back_office
   PROCESSES . recently , there has been a shift in the focus of DIGITALIZATION
   from improving the DELIVERY of TRADITIONAL_TASKS to introducing
   fundamentally NEW_BUSINESS_OPPORTUNITIES and MODELS for
   FINANCIAL_SERVICE_COMPANIES . DIGITAL_FINANCE_ENCOMPASSES a magnitude of
   NEW_FINANCIAL_PRODUCTS , FINANCIAL_BUSINESSES , finance_related SOFTWARE ,
   and NOVEL_FORMS of CUSTOMER_COMMUNICATION and interactiondelivered by
   FINTECH_COMPANIES and innovative FINANCIAL_SERVICE_PROVIDERS . against this
   backdrop , the RESEARCH on FINANCE and INFORMATION_SYSTEMS has started to
   analyze these changes and the impact of DIGITAL_PROGRESS on the
   FINANCIAL_SECTOR . therefore , this ARTICLE_REVIEWS the CURRENT_STATE of
   RESEARCH in DIGITAL_FINANCE that deals with these novel and
   INNOVATIVE_BUSINESS_FUNCTIONS . moreover , IT gives an outlook on potential
   FUTURE_RESEARCH_DIRECTIONS . as a CONCEPTUAL_BASIS for reviewing this field
   , the DIGITAL_FINANCE_CUBE , which embraces three KEY_DIMENSIONS of
   DIGITAL_FINANCE and FINTECH , i.e., the RESPECTIVE_BUSINESS_FUNCTIONS , the
   technologies and TECHNOLOGICAL_CONCEPTS applied as well as the INSTITUTIONS
   concerned , is introduced . this CONCEPTUALIZATION_SUPPORTS_RESEARCHERS and
   practitioners when orientating in the field of DIGITAL_FINANCE , allows for
   the arrangement of ACADEMIC_RESEARCH relatively to each other , and enables
   for the revelation of the gaps in RESEARCH . 2017 , springer_verlag berlin
   heidelberg .
DE DIGITAL_FINANCE; E_FINANCE; FINTECH; FUTURE_RESEARCH_OPPORTUNITIES;
   LITERATURE_REVIEW; STATE_OF_THE_ART
** ACADEMIC_RESEARCH; ARTICLE_REVIEWS; BACKOFFICE_PROCESSES;
   CONCEPTUALIZATION_SUPPORTS_RESEARCHERS; CONCEPTUAL_BASIS;
   CONTINUOUS_EVOLUTION; CURRENT_RESEARCH; CURRENT_STATE;
   CUSTOMER_COMMUNICATION; CUSTOMER_INTERFACE; DIGITAL_FINANCE;
   DIGITAL_FINANCE_CUBE; DIGITAL_FINANCE_ENCOMPASSES; DIGITAL_PROGRESS;
   FINANCIAL_BUSINESSES; FINANCIAL_INDUSTRY; FINANCIAL_SECTOR;
   FINANCIAL_SERVICE_COMPANIES; FINANCIAL_SERVICE_PROVIDERS; FINTECH_COMPANIES;
   FUTURE_RESEARCH_DIRECTIONS; INFORMATION_PROCESSING; INFORMATION_SYSTEMS;
   INNOVATIVE_BUSINESS_FUNCTIONS; KEY_DIMENSIONS; NEW_BUSINESS_OPPORTUNITIES;
   NEW_FINANCIAL_PRODUCTS; NOVEL_FORMS; RESPECTIVE_BUSINESS_FUNCTIONS;
   SERVICE_DELIVERY; SPRINGERVERLAG_BERLIN_HEIDELBERG; TECHNOLOGICAL_CONCEPTS;
   TRADITIONAL_TASKS
<BLANKLINE>



"""
# from ....database.tools.record_viewer import select_documents
from .internals.compute_main_path import _compute_main_path


def main_path_documents(
    #
    # COLUMN PARAMS:
    top_n=None,
    citations_threshold=0,
    #
    # DATABASE PARAMS:
    root_dir="./",
    database="main",
    year_filter=(None, None),
    cited_by_filter=(None, None),
    sort_by=None,
    **filters,
):
    """:meta private:"""

    #
    # Creates a table with citing and cited articles
    articles_in_main_path, _ = _compute_main_path(
        #
        # NETWORK PARAMS:
        top_n=top_n,
        citations_threshold=citations_threshold,
        #
        # DATABASE PARAMS:
        root_dir=root_dir,
        database=database,
        year_filter=year_filter,
        cited_by_filter=cited_by_filter,
        **filters,
    )

    #
    # remove counters
    #
    articles_in_main_path = [
        " ".join(article.split(" ")[:-1]) for article in articles_in_main_path
    ]

    documents = select_documents(
        #
        # FILTERS:
        article=list(articles_in_main_path),
        #
        # DATABASE PARAMS:
        root_dir=root_dir,
        database=database,
        year_filter=(None, None),
        cited_by_filter=(None, None),
        sort_by=sort_by,
        **filters,
    )

    return documents
