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
    >>> import textwrap
    >>> import pandas as pd
    >>> from techminer2.database.field_operators import CleanTextOperator
    >>> from techminer2.database.field_operators import DeleteFieldOperator
    >>> from techminer2.database.field_operators import HighlightNounAndPhrasesOperator
    >>> from techminer2.tools import Query

    >>> (
    ...     CleanTextOperator()
    ...     .with_field("raw_abstract")
    ...     .with_other_field("raw_abstract_copy")
    ...     .where_root_directory_is("examples/fintech/")
    ...     .run()
    ... )

    >>> (
    ...     HighlightNounAndPhrasesOperator()
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
    not statistically significant , and THAT_THE_COEFFICIENT_SIGNS for about one
    third of THE_BANKS are negative , but not statistically significant . since
    THE_FINTECH_INDUSTRY is young and our SAMPLE_PERIOD short , we can not rule out
    that OUR_FINDINGS are spurious . 2017 , the author ( s ) .


    >>> (
    ...     DeleteFieldOperator()
    ...     .with_field("raw_abstract_copy")
    ...     .where_root_directory_is("examples/fintech/")
    ...     .run()
    ... )


"""
