from pprint import pprint  # type: ignore

from colorama import Fore
from colorama import init
from techminer2.database.tools import Query  # type: ignore


def execute_doctypes_command():

    document_types = (
        Query()
        #
        .with_query_expression("SELECT DISTINCT document_type FROM database;")
        #
        .where_root_directory_is("./")
        .where_database_is("main")
        .where_record_years_range_is(None, None)
        .where_record_citations_range_is(None, None)
        #
        .run()
    )["document_type"].to_list()

    print()
    pprint(sorted(document_types))
    print()
