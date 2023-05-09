"""
Average Citations per Year
===============================================================================


>>> directory = "data/regtech/"
>>> file_name = "sphinx/_static/bibliometrix__average_citations_per_year.html"

>>> from techminer2 import bibliometrix
>>> r = bibliometrix.overview.average_citations_per_year(directory)
>>> r.plot_.write_html(file_name)

.. raw:: html

    <iframe src="../../_static/bibliometrix__average_citations_per_year.html" height="600px" width="100%" frameBorder="0"></iframe>

>>> print(r.table_.head().to_markdown())
|   year |   OCC |   cum_OCC |   local_citations |   global_citations |   citable_years |   mean_global_citations |   cum_global_citations |   mean_global_citations_per_year |   mean_local_citations |   cum_local_citations |   mean_local_citations_per_year |
|-------:|------:|----------:|------------------:|-------------------:|----------------:|------------------------:|-----------------------:|---------------------------------:|-----------------------:|----------------------:|--------------------------------:|
|   2016 |     1 |         1 |                 0 |                 30 |               8 |                30       |                     30 |                             3.75 |                0       |                     0 |                            0    |
|   2017 |     4 |         5 |                 3 |                162 |               7 |                40.5     |                    192 |                             5.79 |                0.75    |                     3 |                            0.11 |
|   2018 |     3 |         8 |                30 |                182 |               6 |                60.6667  |                    374 |                            10.11 |               10       |                    33 |                            1.67 |
|   2019 |     6 |        14 |                19 |                 47 |               5 |                 7.83333 |                    421 |                             1.57 |                3.16667 |                    52 |                            0.63 |
|   2020 |    14 |        28 |                29 |                 93 |               4 |                 6.64286 |                    514 |                             1.66 |                2.07143 |                    81 |                            0.52 |


>>> print(r.plot_prompt_)
<BLANKLINE>
Imagine that you are a researcher analyzing a bibliographic dataset. The table below provides data on the average citations per year of the dataset. Use the the information in the table to draw conclusions about the impact per year. In your analysis, be sure to describe in a clear and concise way, any trends or patterns you observe, and identify any outliers or anomalies in the data. Limit your description to one paragraph with no more than 250 words.
<BLANKLINE>
|   year |   mean_global_citations |
|-------:|------------------------:|
|   2016 |                30       |
|   2017 |                40.5     |
|   2018 |                60.6667  |
|   2019 |                 7.83333 |
|   2020 |                 6.64286 |
|   2021 |                 2.7     |
|   2022 |                 1.83333 |
|   2023 |                 0       |
<BLANKLINE>
<BLANKLINE>



"""
from dataclasses import dataclass
from ..._lib._time_plot import time_plot
from ...techminer.indicators.indicators_by_year import indicators_by_year


@dataclass(init=False)
class _Results:
    table_ = None
    plot_ = None
    plot_prompt_ = None


def average_citations_per_year(
    directory="./",
    database="documents",
    start_year=None,
    end_year=None,
    **filters,
):
    """Average citations per year."""

    indicators = indicators_by_year(
        directory=directory,
        database=database,
        start_year=start_year,
        end_year=end_year,
        **filters,
    )

    results = _Results()

    results.table_ = indicators.copy()
    results.plot_ = time_plot(
        indicators,
        metric="mean_global_citations",
        title="Average Citations per Year",
    )

    results.plot_prompt_ = f"""
Imagine that you are a researcher analyzing a bibliographic dataset. The table \
below provides data on the average citations per year of the dataset. Use the \
the information in the table to draw conclusions about the impact per year. \
In your analysis, be sure to describe in a clear and concise way, any trends \
or patterns you observe, and identify any outliers or anomalies in the data. \
Limit your description to one paragraph with no more than 250 words.

{results.table_[["mean_global_citations"]].to_markdown()}

"""

    return results
