# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
# pylint: disable=import-outside-toplevel
"""
Most Local Cited Documents (Example)
===============================================================================

>>> from techminer2.documents import select_documents
>>> documents = select_documents(
...     #
...     # DATABASE PARAMS:
...     root_dir="example/", 
...     database="main",
...     year_filter=(None, None),
...     cited_by_filter=(None, None),
...     sort_by="local_cited_by_highest",
... )
>>> print(documents[0])
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
