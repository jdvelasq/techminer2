# flake8: noqa
"""
Annual Scientific Production
===============================================================================


>>> directory = "data/regtech/"
>>> file_name = "sphinx/_static/bibliometrix__annual_scientific_production.html"

>>> from techminer2 import bibliometrix
>>> r = bibliometrix.overview.annual_scientific_production(directory)
>>> r.plot_.write_html(file_name)

.. raw:: html

    <iframe src="../../_static/bibliometrix__annual_scientific_production.html" 
    height="600px" width="100%" frameBorder="0"></iframe>


>>> r.table_.head()
      OCC  cum_OCC  ...  cum_local_citations  mean_local_citations_per_year
year                ...                                                    
2016    1        1  ...                  0.0                           0.00
2017    4        5  ...                  3.0                           0.11
2018    3        8  ...                 33.0                           1.67
2019    6       14  ...                 52.0                           0.63
2020   14       28  ...                 81.0                           0.52
<BLANKLINE>
[5 rows x 11 columns]


>>> print(r.prompt_)
The table below provides data on the annual scientific production. Use the table to draw conclusions about annual research productivity and the cumulative productivity. The column 'OCC' is the number of documents published in a given year. The column 'cum_OCC' is the cumulative number of documents published up to a given year. The information in the table is used to create a line plot of number of publications per year. In your analysis, be sure to describe in a clear and concise way, any trends or patterns you observe, and identify any outliers or anomalies in the data. Limit your description to one paragraph with no more than 250 words.
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

# pylint: disable=line-too-long
"""
# from ...classes import IndicatorByYearChart
# from ...techminer.indicators import indicators_by_year, indicators_by_year_plot


def annual_scientific_production(
    root_dir="./",
    database="main",
    year_filter=None,
    cited_by_filter=None,
    **filters,
):
    """Computes annual scientific production (number of documents per year).

    Args:
        root_dir (str, optional): Root directory. Defaults to "./".
        database (str, optional): Database name. Defaults to "documents".
        year_filter (tuple, optional): Year filter. Defaults to None.
        cited_by_filter (tuple, optional): Cited by filter. Defaults to None.
        **filters (dict, optional): Filters to be applied to the database. Defaults to {}.

    Returns:
        :class:`IndicatorByYearChart`: A :class:`IndicatorByYearChart` instance.


    """

    def generate_chatgpt_prompt(table):
        """Generates the prompt for annual_scientific_production."""

        return (
            "The table below provides data on the annual scientific "
            "production. Use the table to draw conclusions about annual "
            "research productivity and the cumulative productivity. The "
            "column 'OCC' is the number of documents published in a given "
            "year. The column 'cum_OCC' is the cumulative number of "
            "documents published up to a given year. The information in the "
            "table is used to create a line plot of number of publications "
            "per year. In your analysis, be sure to describe in a clear and "
            "concise way, any trends or patterns you observe, and identify "
            "any outliers or anomalies in the data. Limit your description "
            "to one paragraph with no more than 250 words."
            f"\n\n{table.to_markdown()}\n\n"
        )

    #
    # Main code
    #

    indicators = indicators_by_year(
        root_dir=root_dir,
        database=database,
        year_filter=year_filter,
        cited_by_filter=cited_by_filter,
        **filters,
    )

    results = IndicatorByYearChart()
    results.table_ = indicators
    results.plot_ = indicators_by_year_plot(
        indicators,
        metric="OCC",
        title="Annual Scientific Production",
    )
    results.prompt_ = generate_chatgpt_prompt(indicators[["OCC", "cum_OCC"]])

    return results