"""
Annual Scientific Production
===============================================================================


>>> directory = "data/regtech/"
>>> file_name = "sphinx/_static/bibliometrix__annual_scientific_production.html"

>>> from techminer2 import bibliometrix
>>> r = bibliometrix.overview.annual_scientific_production(directory)
>>> r.plot_.write_html(file_name)

.. raw:: html

    <iframe src="../../_static/bibliometrix__annual_scientific_production.html" height="600px" width="100%" frameBorder="0"></iframe>

    
>>> r.table_.head()
      OCC  cum_OCC
year              
2016    1        1
2017    4        5
2018    3        8
2019    6       14
2020   14       28


>>> print(r.prompt_)
<BLANKLINE>
Imagine that you are a researcher analyzing a bibliographic dataset. The table below provides data on the annual scientific production. Use the table to draw conclusions about annual research productivity and the cumulative productivity. The column 'OCC' is the number of documents published in a given year. The column 'cum_OCC' is the cumulative number of documents published up to a given year. The information in the table is used to create a line plot of number of publications per year. In your analysis, be sure to describe in a clear and concise way, any trends or patterns you observe, and identify any outliers or anomalies in the data. Limit your description to one paragraph with no more than 250 words.
<BLANKLINE>
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
    prompt_ = None


def annual_scientific_production(
    directory="./",
    database="documents",
    start_year=None,
    end_year=None,
    **filters,
):
    """Computes annual scientific production (number of documents per year)."""

    indicators = indicators_by_year(
        directory=directory,
        database=database,
        start_year=start_year,
        end_year=end_year,
        **filters,
    )

    results = _Results()
    results.table_ = indicators[["OCC", "cum_OCC"]]
    results.plot_ = time_plot(
        indicators,
        metric="OCC",
        title="Annual Scientific Production",
    )
    results.prompt_ = _annual_scientific_production_prompt(results.table_)

    return results


def _annual_scientific_production_prompt(table):
    """Generates the prompt for annual_scientific_production."""

    prompt = f"""
Imagine that you are a researcher analyzing a bibliographic dataset. The table \
below provides data on the annual scientific production. Use the table to draw \
conclusions about annual research productivity and the cumulative productivity. \
The column 'OCC' is the number of documents published in a given year. The \
column 'cum_OCC' is the cumulative number of documents published up to a given \
year. The information in the table is used to create a line plot of number of \
publications per year. In your analysis, be sure to describe in a clear and \
concise way, any trends or patterns you observe, and identify any outliers or \
anomalies in the data. Limit your description to one paragraph with no more than \
250 words.

{table.to_markdown()}

"""

    return prompt
