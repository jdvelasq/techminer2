from techminer2.analyze._metrics.general import DataFrame


def execute_dataframe_command():

    df = (
        DataFrame()
        #
        # DATABASE:
        .where_root_directory("./")
        .where_database("main")
        .where_record_years_range(None, None)
        .where_record_citations_range(None, None)
        .where_records_match(None)
        .run()
    )
    print()
    print(df.to_string())
    print()
