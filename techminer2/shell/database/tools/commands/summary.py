from techminer2.explore import SummarySheet
from techminer2.shell.colorized_input import colorized_input


def execute_summary_command():

    result = (
        SummarySheet()
        #
        .where_root_directory("./")
        .where_database("main")
        .where_record_years_range(None, None)
        .where_record_citations_range(None, None)
        #
        .run()
    )

    print()
    print(result.to_string())
    print()
