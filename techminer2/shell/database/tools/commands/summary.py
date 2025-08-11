from techminer2.database.tools import SummarySheet
from techminer2.shell.colorized_input import colorized_input


def execute_summary_command():

    result = (
        SummarySheet()
        #
        .where_root_directory_is("./")
        .where_database_is("main")
        .where_record_years_range_is(None, None)
        .where_record_citations_range_is(None, None)
        #
        .run()
    )

    print()
    print(result.to_string())
    print()
