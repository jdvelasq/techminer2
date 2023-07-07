# flake8: noqa
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
