# flake8: noqa
# pylint: disable=too-many-arguments
# pylint: disable=missing-docstring
# pylint: disable=line-too-long
"""
Filter
==============================================================================

Filters the records

>>> import techminer2plus as tm2p




>>> root_dir = "data/regtech/"

>>> tm2p.records(root_dir=root_dir)
Records(root_dir='data/regtech/', database='main', year_filter=(None, None),
    cited_by_filter=(None, None), filters={})

    
>>> tm2p.records(root_dir=root_dir, filters={
...     "countries": ['Australia', 'United Kingdom', 'United States']
... })
Records(root_dir='data/regtech/', database='main', year_filter=(None, None),
    cited_by_filter=(None, None), filters={'countries': ['Australia', 'United
    Kingdom', 'United States']})


"""
from dataclasses import dataclass
from dataclasses import field as datafield

import pandas as pd

from .._read_records import read_records
from .._stopwords_lib import load_stopwords

# from ..list_items import list_items
from .indicators_by_year import records_per_year_chart


@dataclass
class Filter:
    """Represents the filtered dababase"""

    root_dir: str  # path to main folder of database
    database: str = "main"
    year_filter: tuple = (None, None)
    cited_by_filter: tuple = (None, None)
    filters: dict = datafield(default_factory=dict)
    records: pd.DataFrame = pd.DataFrame()
    stopwords: list = datafield(default_factory=list)

    def __post_init__(self):
        #
        # FILTERS:
        #
        if self.filters is None:
            self.filters = {}

        #
        # READ RECORDS:
        #
        self.records = read_records(
            root_dir=self.root_dir,
            database=self.database,
            year_filter=self.year_filter,
            cited_by_filter=self.cited_by_filter,
            **self.filters,
        )

        self.stopwords = load_stopwords(self.root_dir)

    #
    # COMPUTATIONS:
    #
    def records_per_year_chart(self, title="Records per Year"):
        """Returns a plotly chart with the number of records per year.

        >>> import techminer2plus as tm2p
        >>> root_dir = "data/regtech/"
        >>> chart = (
        ...     tm2p.Database(root_dir)
        ...     .filter()
        ...     .records_per_year_chart()
        ... )

        >>> chart.fig_.write_html("sphinx/_static/filter/records_per_year_chart.html")

        .. raw:: html

            <iframe src="../../../../_static/filter/records_per_year_chart.html"  height="600px" width="100%" frameBorder="0"></iframe>

        >>> print(chart.df_.to_markdown())
        |   year |   OCC |   cum_OCC |   local_citations |   global_citations |   citable_years |   mean_global_citations |   cum_global_citations |   mean_global_citations_per_year |   mean_local_citations |   cum_local_citations |   mean_local_citations_per_year |
        |-------:|------:|----------:|------------------:|-------------------:|----------------:|------------------------:|-----------------------:|---------------------------------:|-----------------------:|----------------------:|--------------------------------:|
        |   2016 |     1 |         1 |                 0 |                 30 |               8 |                30       |                     30 |                             3.75 |                0       |                     0 |                            0    |
        |   2017 |     4 |         5 |                 3 |                162 |               7 |                40.5     |                    192 |                             5.79 |                0.75    |                     3 |                            0.11 |
        |   2018 |     3 |         8 |                30 |                182 |               6 |                60.6667  |                    374 |                            10.11 |               10       |                    33 |                            1.67 |
        |   2019 |     6 |        14 |                19 |                 47 |               5 |                 7.83333 |                    421 |                             1.57 |                3.16667 |                    52 |                            0.63 |
        |   2020 |    14 |        28 |                29 |                 93 |               4 |                 6.64286 |                    514 |                             1.66 |                2.07143 |                    81 |                            0.52 |
        |   2021 |    10 |        38 |                 9 |                 27 |               3 |                 2.7     |                    541 |                             0.9  |                0.9     |                    90 |                            0.3  |
        |   2022 |    12 |        50 |                 3 |                 22 |               2 |                 1.83333 |                    563 |                             0.92 |                0.25    |                    93 |                            0.12 |
        |   2023 |     2 |        52 |                 0 |                  0 |               1 |                 0       |                    563 |                             0    |                0       |                    93 |                            0    |

        >>> print(chart.prompt_)
        The table below, delimited by triple backticks, provides data on the annual \\
        scientific production in a bibliographic database. Use the table to draw \\
        conclusions about annual research productivity and the cumulative \\
        productivity. The column 'OCC' is the number of documents published in a \\
        given year. The column 'cum_OCC' is the cumulative number of documents \\
        published up to a given year. The information in the table is used to \\
        create a line plot of number of publications per year. In your analysis, be \\
        sure to describe in a clear and concise way, any trends or patterns you \\
        observe, and identify any outliers or anomalies in the data. Limit your \\
        description to one paragraph with no more than 250 words.
        <BLANKLINE>
        Table:
        ```
        |   year |   OCC |   cum_OCC |
        |-------:|------:|----------:|
        |   2016 |     1 |         1 |
        |   2017 |     4 |         5 |
        |   2018 |     3 |         8 |
        |   2019 |     6 |        14 |
        |   2020 |    14 |        28 |
        |   2021 |    10 |        38 |
        |   2022 |    12 |        50 |
        |   2023 |     2 |        52 |
        ```
        <BLANKLINE>

        """
        return records_per_year_chart(self.records, title=title)

    def list_items(
        self,
        field,
        metric="OCC",
        top_n=None,
        occ_range=(None, None),
        gc_range=(None, None),
        custom_items=None,
    ):
        """Returns bibliometric indicators for a list of items.

        >>> import techminer2plus as tm2p
        >>> root_dir = "data/regtech/"
        >>> items = (
        ...     tm2p.Database(root_dir)
        ...     .filter()
        ...     .list_items(
        ...         field='author_keywords',
        ...         top_n=10,
        ...     )
        ... ) 
        >>> items.df_.head()
                            rank_occ  rank_gc  OCC  ...  h_index  g_index  m_index
        author_keywords                                ...                           
        REGTECH                       1        1   28  ...      9.0      4.0     1.29
        FINTECH                       2        2   12  ...      5.0      3.0     0.83
        REGULATORY_TECHNOLOGY         3        8    7  ...      4.0      2.0     1.00
        COMPLIANCE                    4       12    7  ...      3.0      2.0     0.60
        REGULATION                    5        4    5  ...      2.0      2.0     0.33
        <BLANKLINE>
        [5 rows x 18 columns]

        >>> print(items.prompt_)
        Your task is to generate an analysis about the bibliometric indicators of \\
        the 'author_keywords' field in a scientific bibliography database. \\
        Summarize the table below, sorted by the 'OCC' metric, and delimited by \\
        triple backticks, identify any notable patterns, trends, or outliers in the \\
        data, and discuss their implications for the research field. Be sure to \\
        provide a concise summary of your findings in no more than 150 words.
        <BLANKLINE>
        Table:
        ```
        | author_keywords         |   rank_occ |   rank_gc |   OCC |   Before 2022 |   Between 2022-2023 |   global_citations |   local_citations |   global_citations_per_document |   local_citations_per_document |   average_growth_rate |   average_docs_per_year |   percentage_docs_last_year |   first_publication_year |   age |   global_citations_per_year |   h_index |   g_index |   m_index |
        |:------------------------|-----------:|----------:|------:|--------------:|--------------------:|-------------------:|------------------:|--------------------------------:|-------------------------------:|----------------------:|------------------------:|----------------------------:|-------------------------:|------:|----------------------------:|----------:|----------:|----------:|
        | REGTECH                 |          1 |         1 |    28 |            20 |                   8 |                329 |                74 |                           11.75 |                           2.64 |                  -0.5 |                     4   |                   0.142857  |                     2017 |     7 |                       47    |         9 |         4 |      1.29 |
        | FINTECH                 |          2 |         2 |    12 |            10 |                   2 |                249 |                49 |                           20.75 |                           4.08 |                  -0.5 |                     1   |                   0.0833333 |                     2018 |     6 |                       41.5  |         5 |         3 |      0.83 |
        | REGULATORY_TECHNOLOGY   |          3 |         8 |     7 |             5 |                   2 |                 37 |                14 |                            5.29 |                           2    |                  -1.5 |                     1   |                   0.142857  |                     2020 |     4 |                        9.25 |         4 |         2 |      1    |
        | COMPLIANCE              |          4 |        12 |     7 |             5 |                   2 |                 30 |                 9 |                            4.29 |                           1.29 |                   0   |                     1   |                   0.142857  |                     2019 |     5 |                        6    |         3 |         2 |      0.6  |
        | REGULATION              |          5 |         4 |     5 |             4 |                   1 |                164 |                22 |                           32.8  |                           4.4  |                  -0.5 |                     0.5 |                   0.1       |                     2018 |     6 |                       27.33 |         2 |         2 |      0.33 |
        | ANTI_MONEY_LAUNDERING   |          6 |        10 |     5 |             5 |                   0 |                 34 |                 8 |                            6.8  |                           1.6  |                  -1.5 |                     0   |                   0         |                     2020 |     4 |                        8.5  |         3 |         2 |      0.75 |
        | FINANCIAL_SERVICES      |          7 |         3 |     4 |             3 |                   1 |                168 |                20 |                           42    |                           5    |                   0   |                     0.5 |                   0.125     |                     2017 |     7 |                       24    |         3 |         2 |      0.43 |
        | FINANCIAL_REGULATION    |          8 |         9 |     4 |             2 |                   2 |                 35 |                 8 |                            8.75 |                           2    |                   0   |                     1   |                   0.25      |                     2017 |     7 |                        5    |         2 |         2 |      0.29 |
        | ARTIFICIAL_INTELLIGENCE |          9 |        19 |     4 |             3 |                   1 |                 23 |                 6 |                            5.75 |                           1.5  |                   0   |                     0.5 |                   0.125     |                     2019 |     5 |                        4.6  |         3 |         2 |      0.6  |
        | RISK_MANAGEMENT         |         10 |        25 |     3 |             2 |                   1 |                 14 |                 8 |                            4.67 |                           2.67 |                   0   |                     0.5 |                   0.166667  |                     2018 |     6 |                        2.33 |         2 |         2 |      0.33 |
        ```
        <BLANKLINE>



        """
        return list_items(
            records=self.records,
            stopwods=self.stopwords,
            field=field,
            metric=metric,
            top_n=top_n,
            occ_range=occ_range,
            gc_range=gc_range,
            custom_items=custom_items,
        )
