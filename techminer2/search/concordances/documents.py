# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
"""
Documents (MIGRATED)
=========================================================================================

## >>> from techminer2.search.concordances import Documents
## >>> docs = (
## ...     Documents()
## ...     .set_database_params(
## ...         root_dir="example/",
## ...         database="main",
## ...         year_filter=(None, None),
## ...         cited_by_filter=(None, None),
## ...         sort_by="date_newest", # date_newest, date_oldest, global_cited_by_highest, 
## ...                                # global_cited_by_lowest, local_cited_by_highest, 
## ...                                # local_cited_by_lowest, first_author_a_to_z, 
## ...                                # first_author_z_to_a, source_title_a_to_z, 
## ...                                # source_title_z_to_a
## ...     ).build(search_for='FINTECH')
## ... )
## >>> print(len(docs))
## 38
## >>> print(docs[0])
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
   FINANCIAL_TECHNOLOGY ( FINTECH )
DE ENTREPRENEURSHIP; FINANCIAL_INSTITUTIONS; FINTECH; STARTUPS
** ACCESS_LOANS; ACTIVE_POLICIES; AVAILABLE_LABOR_FORCE; EVIDENCE_SUGGESTS;
   FINANCIAL_TECHNOLOGY; FINTECH_STARTUPS; FINTECH_STARTUP_FORMATIONS;
   FINTECH_STARTUP_FORMATION_NEED; GLOBAL_FINTECH_MARKET; INTERNET_SERVERS;
   MOBILE_TELEPHONE_SUBSCRIPTIONS; NEW_MARKET_SEGMENT; NEW_SECTOR;
   POSITIVE_IMPACT; TECHNOLOGICAL_DETERMINANTS; VENTURE_CAPITAL
<BLANKLINE>

    
"""
import re

from textblob import TextBlob  # type: ignore

from ...database.load.load__filtered_database import load__filtered_database
from ...internals.params.database_params import DatabaseParams, DatabaseParamsMixin
from ...internals.utils.utils_records_for_reporting import _utils_records_for_reporting
from .._core.filter_records_by_concordance import _filter_records_by_concordance


class Documents(
    DatabaseParamsMixin,
):
    """:meta private:"""

    def __init__(self):
        self.database_params = DatabaseParams()

    def build(self, search_for: str):
        return concordance_documents(search_for, **self.database_params.__dict__)


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

    records = load__filtered_database(
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

    #
    # extract phrases.
    records["abstract"] = records["abstract"].map(lambda x: TextBlob(x).sentences)
    records["abstract"] = records["abstract"].map(lambda x: [str(y) for y in x])
    records["abstract"] = records["abstract"].map(
        lambda x: [y[:-2] if y[-2:] == " ." else y for y in x]
    )
    #
    regex = r"\b" + search_for + r"\b"
    #
    records["abstract"] = records["abstract"].map(
        lambda x: [y for y in x if re.search(regex, y)]
    )
    records["abstract"] = records["abstract"].map(" . ".join)
    # records["abstract"] = records["abstract"] + records["raw_abstract"]

    formated_records = _utils_records_for_reporting(
        records=records,
    )

    return formated_records
