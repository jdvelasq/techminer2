# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
"""
Concordance Documents
=========================================================================================

>>> from techminer2.search import concordance_documents
>>> docs = concordance_documents( 
...     #
...     # FUNCTION PARAMS:
...     search_for='FINTECH',
...     #
...     # DATABASE PARAMS:
...     root_dir="example/",
...     database="main",
...     year_filter=(None, None),
...     cited_by_filter=(None, None),
...     sort_by="date_newest", # date_newest, date_oldest, global_cited_by_highest, 
...                            # global_cited_by_lowest, local_cited_by_highest, 
...                            # local_cited_by_lowest, first_author_a_to_z, 
...                            # first_author_z_to_a, source_title_a_to_z, 
...                            # source_title_z_to_a
... )
>>> print(len(docs))
50
>>> print(docs[0])
Record-No: 6
AR Haddad C., 2019, SMALL BUS ECON, V53, P81
TI The emergence of the global fintech market: economic and technological
   determinants
AU Haddad C.; Hornuf L.
TC 258
SO Small Business Economics
PY 2019
AB we investigate the economic and TECHNOLOGICAL_DETERMINANTS inducing
   ENTREPRENEURS to establish ventures with the purpose of reinventing
   FINANCIAL_TECHNOLOGY ( FINTECH ) . we find that countries witness more
   FINTECH_STARTUP_FORMATIONS when the economy is well_developed and
   VENTURE_CAPITAL is readily available . furthermore , the number of secure
   INTERNET_SERVERS , MOBILE_TELEPHONE_SUBSCRIPTIONS , and the
   AVAILABLE_LABOR_FORCE has a POSITIVE_IMPACT on the DEVELOPMENT of this
   NEW_MARKET_SEGMENT . finally , the more difficult IT is for companies to
   ACCESS_LOANS , the higher is the number of FINTECH_STARTUPS in a country .
   overall , the EVIDENCE_SUGGESTS that FINTECH_STARTUP_FORMATION_NEED not be
   left to chance , but ACTIVE_POLICIES can INFLUENCE the emergence of this
   NEW_SECTOR . 2018 , the author ( s ) .
DE ENTREPRENEURSHIP; FINANCIAL_INSTITUTIONS; FINTECH; STARTUPS
** ACCESS_LOANS; ACTIVE_POLICIES; AVAILABLE_LABOR_FORCE; EVIDENCE_SUGGESTS;
   FINANCIAL_TECHNOLOGY; FINTECH_STARTUPS; FINTECH_STARTUP_FORMATIONS;
   FINTECH_STARTUP_FORMATION_NEED; GLOBAL_FINTECH_MARKET; INTERNET_SERVERS;
   MOBILE_TELEPHONE_SUBSCRIPTIONS; NEW_MARKET_SEGMENT; NEW_SECTOR;
   POSITIVE_IMPACT; TECHNOLOGICAL_DETERMINANTS; VENTURE_CAPITAL
<BLANKLINE>
>>> print(docs[1])
Record-No: 42
AR Chen M.A., 2019, REV FINANC STUD, V32, P2062
TI How Valuable Is FinTech Innovation?
AU Chen M.A.; Wu Q.; Yang B.
TC 235
SO Review of Financial Studies
PY 2019
AB we provide large_scale EVIDENCE on the occurrence and VALUE of
   FINTECH_INNOVATION . using DATA on PATENT_FILINGS from 2003 to 2017 , we
   apply MACHINE_LEARNING to identify and CLASSIFY_INNOVATIONS by their
   underlying technologies . we find that most FINTECH_INNOVATIONS_YIELD
   SUBSTANTIAL_VALUE to innovators , with BLOCKCHAIN being particularly
   valuable . for the overall FINANCIAL_SECTOR , INTERNET_OF_THINGS ( IOT ) ,
   robo_advising , and BLOCKCHAIN are the most VALUABLE_INNOVATION_TYPES .
   INNOVATIONS affect FINANCIAL_INDUSTRIES more negatively when they involve
   DISRUPTIVE_TECHNOLOGIES from NONFINANCIAL_STARTUPS , but MARKET_LEADERS that
   invest heavily in their OWN_INNOVATION can avoid much of the
   NEGATIVE_VALUE_EFFECT . ( JEL_G14 , G20 , G29 , g39 ) . the author ( s )
   2019 .
** CLASSIFY_INNOVATIONS; DISRUPTIVE_TECHNOLOGIES; FINANCIAL_INDUSTRIES;
   FINANCIAL_SECTOR; FINTECH_INNOVATION; FINTECH_INNOVATIONS_YIELD; JEL_G14;
   LARGESCALE_EVIDENCE; MACHINE_LEARNING; MARKET_LEADERS;
   NEGATIVE_VALUE_EFFECT; NONFINANCIAL_STARTUPS; OWN_INNOVATION;
   PATENT_FILINGS; SUBSTANTIAL_VALUE; VALUABLE_INNOVATION_TYPES
<BLANKLINE>

    
"""
from .._core.read_filtered_database import read_filtered_database
from ..documents.select_documents import select_documents
from ._core.filter_records_by_concordance import _filter_records_by_concordance


def concordance_documents(
    #
    # FUNCTION PARAMS:
    search_for: str,
    #
    # DATABASE PARAMS:
    root_dir: str = "./",
    database: str = "main",
    year_filter: tuple = (None, None),
    cited_by_filter: tuple = (None, None),
    sort_by: str = "date_newest",
    **filters,
):
    """:meta private:"""

    records = read_filtered_database(
        root_dir=root_dir,
        database=database,
        year_filter=year_filter,
        cited_by_filter=cited_by_filter,
        sort_by=sort_by,
        **filters,
    )

    records = _filter_records_by_concordance(
        search_for=search_for,
        records=records,
    )

    documents = select_documents(
        #
        # DATABASE PARAMS
        root_dir=root_dir,
        database=database,
        year_filter=year_filter,
        cited_by_filter=cited_by_filter,
        sort_by=sort_by,
        **filters,
    )

    return documents
