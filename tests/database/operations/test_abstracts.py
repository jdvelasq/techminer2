# flake8: noqa
# pylint: disable=import-outside-toplevel
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-few-public-methods
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
# pylint: disable=too-many-statements
#
# Check abstrats highlight
"""
Example:
    >>> import shutil
    >>> shutil.copy("examples/fintech/database.csv.zip", "examples/fintech/data/processed/database.csv.zip")
    'examples/fintech/data/processed/database.csv.zip'

    >>> import textwrap
    >>> import pandas as pd
    >>> from techminer2.database.operators import TokenizeOperator
    >>> from techminer2.database.operators import DeleteOperator
    >>> from techminer2.database.operators import HighlightOperator
    >>> from techminer2.database.tools import Query

    >>> (
    ...     TokenizeOperator()
    ...     .with_field("raw_abstract")
    ...     .with_other_field("raw_abstract_copy")
    ...     .where_root_directory_is("examples/fintech/")
    ...     .run()
    ... )

    >>> (
    ...     HighlightOperator()
    ...     .with_field("raw_abstract_copy")
    ...     .with_other_field("raw_abstract_copy")
    ...     .where_root_directory_is("examples/fintech/")
    ...     .run()
    ... )


    >>> df = (
    ...     Query()
    ...     .with_query_expression("SELECT raw_abstract_copy FROM database LIMIT 50;")
    ...     .where_root_directory_is("examples/fintech/")
    ...     .where_database_is("main")
    ...     .where_record_years_range_is(None, None)
    ...     .where_record_citations_range_is(None, None)
    ...     .run()
    ... )

    >>> print(textwrap.fill(df.values[35][0], width=80))
    background : this study aims to_clarify THE_ROLE of
    FINTECH_DIGITAL_BANKING_START_UPS in THE_FINANCIAL_INDUSTRY . we examine
    THE_IMPACT of THE_FUNDING of SUCH_START_UPS on THE_STOCK_RETURNS of 47 incumbent
    us RETAIL_BANKS for 2010 to 2016 . methods : to capture THE_IMPORTANCE of
    FINTECH_START_UPS , we use DATA on BOTH_THE_DOLLAR_VOLUME of FUNDING and NUMBER
    of DEALS . we relate these to THE_STOCK_RETURNS with
    PANEL_DATA_REGRESSION_METHODS . results : OUR_RESULTS indicate a
    POSITIVE_RELATIONSHIP_EXISTS between THE_GROWTH in FINTECH_FUNDING or DEALS and
    THE_CONTEMPORANEOUS_STOCK_RETURNS of INCUMBENT_RETAIL_BANKS . conclusions :
    although THESE_RESULTS suggest COMPLEMENTARITY between FINTECH and
    TRADITIONAL_BANKING , we note that OUR_RESULTS at THE_BANKING_INDUSTRY_LEVEL are
    not statistically significant , and that THE_COEFFICIENT signs for
    ABOUT_ONE_THIRD of THE_BANKS are negative , but not statistically significant .
    since THE_FINTECH_INDUSTRY is young and our SAMPLE_PERIOD short , we can not
    rule out that OUR_FINDINGS are spurious . 2017 , the author ( s ) .


    >>> (
    ...     DeleteOperator()
    ...     .with_field("raw_abstract_copy")
    ...     .where_root_directory_is("examples/fintech/")
    ...     .run()
    ... )


"""
