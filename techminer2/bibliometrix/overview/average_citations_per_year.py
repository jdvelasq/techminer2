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

>>> r.table_.head()    
      local_citations  ...  mean_local_citations_per_year
year                   ...                               
2016              0.0  ...                           0.00
2017              3.0  ...                           0.11
2018             30.0  ...                           1.67
2019             19.0  ...                           0.63
2020             29.0  ...                           0.52
<BLANKLINE>
[5 rows x 9 columns]

>>> print(r.prompt_)
Act as a researcher. Analyze the following table, 
which provides data corresponding to the average citations per year of a 
bibliographic dataset. 
<BLANKLINE>
Column 'OCC' is the number of documents published in 
a given year. Column 'cum_OCC' is the cumulative number of documents 
published up to a given year. The information in the table is used to create 
a line plot.
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
Write a clear and concise paragraph describing the main findings and any 
important trends or patterns you notice. 
<BLANKLINE>
Limit your description to a paragraph with no more than 250 words.    
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

    results.table_ = indicators.drop(columns=["OCC", "cum_OCC"])
    results.plot_ = time_plot(
        indicators,
        metric="mean_global_citations",
        title="Average Citations per Year",
    )

    results.prompt_ = f"""Act as a researcher. Analyze the following table, 
which provides data corresponding to the average citations per year of a 
bibliographic dataset. 

Column 'OCC' is the number of documents published in 
a given year. Column 'cum_OCC' is the cumulative number of documents 
published up to a given year. The information in the table is used to create 
a line plot.

{results.table_[["mean_global_citations"]].to_markdown()}

Write a clear and concise paragraph describing the main findings and any 
important trends or patterns you notice. 

Limit your description to a paragraph with no more than 250 words.    
"""

    return results
