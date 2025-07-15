from techminer2.database.tools import SummarySheet

from ....colorized_input import colorized_input


def execute_summary_command():

    # PARAMETERS:

    # database:
    # database = colorized_input(". Enter databases (main) >").strip()
    # if not database:
    #     database = "main"

    # # initial year range:
    # initial_year = colorized_input(". Enter the initial year [default: None] >").strip()
    # if initial_year == "":
    #     initial_year = None
    # else:
    #     initial_year = int(initial_year)

    # # final year range:
    # final_year = colorized_input(". Enter the final year (None) >").strip()
    # if final_year == "":
    #     final_year = None
    # else:
    #     final_year = int(final_year)

    # # initial citations range:
    # initial_citations = colorized_input(
    #     ". Enter the lower limit of citations [default: None] >"
    # ).strip()
    # if initial_citations == "":
    #     initial_citations = None
    # else:
    #     initial_citations = int(initial_citations)

    # # final citations range:
    # final_citations = colorized_input(
    #     ". Enter the upper limit of citations (None) >"
    # ).strip()
    # if final_citations == "":
    #     final_citations = None
    # else:
    #     final_citations = int(final_citations)

    # RUN:

    result = (
        SummarySheet()
        #
        .where_root_directory_is("./")
        .where_database_is(None)
        .where_record_years_range_is(None, None)
        .where_record_citations_range_is(None, None)
        #
        .run()
    )

    print()
    print(result.to_string())
