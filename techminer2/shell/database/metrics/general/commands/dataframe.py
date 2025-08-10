from techminer2.database.metrics.general import DataFrame


def execute_dataframe_command():

    df = (
        DataFrame()
        #
        # DATABASE:
        .where_root_directory_is("./")
        .where_database_is("main")
        .where_record_years_range_is(None, None)
        .where_record_citations_range_is(None, None)
        .where_records_match(None)
        .run()
    )
    print()
    print(df.to_string())
    print()
