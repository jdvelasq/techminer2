# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
"""
Trend Metrics Frame
===============================================================================


>>> from techminer2.analyze.metrics import trend_metrics_frame
>>> trend_metrics_frame(
...     #
...     # TABLE PARAMS:
...     selected_columns=[
...         "OCC",
...         "global_citations",
...         "mean_global_citations",
...         "mean_global_citations_per_year",
...     ],
...     ).set_database_params(
...         root_dir="example/", 
...         database="main",
...         year_filter=(None, None),
...         cited_by_filter=(None, None),
...     #
...     ).build()
... )
      OCC  ...  mean_global_citations_per_year
year       ...                                
2015    1  ...                           15.20
2016    7  ...                           31.07
2017   10  ...                           60.50
2018   17  ...                           99.00
2019   15  ...                          133.87
<BLANKLINE>
[5 rows x 4 columns]


"""
from .internals._compute_trend_metrics import compute_trend_metrics

MARKER_COLOR = "#7793a5"
MARKER_LINE_COLOR = "#465c6b"


def trend_metrics_frame(
    #
    # TABLE PARAMS:
    selected_columns=None,
    #
    # DATABASE PARAMS:
    root_dir: str = "./",
    database: str = "main",
    year_filter: tuple = (None, None),
    cited_by_filter: tuple = (None, None),
    **filters,
):
    """:meta private:"""

    #
    # Compute metrics per year
    data_frame = compute_trend_metrics(
        #
        # DATABASE PARAMS
        root_dir=root_dir,
        database=database,
        year_filter=year_filter,
        cited_by_filter=cited_by_filter,
        **filters,
    )

    #
    # Select only columns existent in the data frame
    if selected_columns is None:
        selected_columns = data_frame.columns.copy()
    else:
        selected_columns = [
            col for col in selected_columns if col in data_frame.columns
        ]
    data_frame = data_frame[selected_columns]

    return data_frame
