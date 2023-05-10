"""
Country Dynamics
===============================================================================




>>> directory = "data/regtech/"
>>> file_name = "sphinx/_static/bibliometrix__country_dynamics.html"

>>> from techminer2 import bibliometrix
>>> r = bibliometrix.countries.country_dynamics(
...     topics_length=5, 
...     directory=directory,
... )
>>> r.plot_.write_html(file_name)

.. raw:: html

    <iframe src="../../../_static/bibliometrix__country_dynamics.html" height="600px" width="100%" frameBorder="0"></iframe>


>>> print(r.table_.head().to_markdown())
|    |   year | countries      |   cum_OCC |
|---:|-------:|:---------------|----------:|
|  0 |   2016 | United Kingdom |         0 |
|  1 |   2017 | United Kingdom |         0 |
|  2 |   2018 | United Kingdom |         3 |
|  3 |   2019 | United Kingdom |         4 |
|  4 |   2020 | United Kingdom |         6 |

>>> print(r.prompt_)
<BLANKLINE>
Imagine that you are a researcher analyzing a bibliographic dataset. The table below provides data on cumulative document production by year per country for the top 5 most productive countries in the dataset. Use the information in the table to draw conclusions about the cumulative productivity per year of the countries. In your analysis, be sure to describe in a clear and concise way, any findings or any patterns you observe, and identify any outliers or anomalies in the data. Limit your description to one paragraph with no more than 250 words.
<BLANKLINE>
| countries      |   2016 |   2017 |   2018 |   2019 |   2020 |   2021 |   2022 |   2023 |
|:---------------|-------:|-------:|-------:|-------:|-------:|-------:|-------:|-------:|
| Australia      |      0 |      2 |      2 |      2 |      5 |      7 |      7 |      7 |
| China          |      0 |      1 |      1 |      1 |      1 |      1 |      4 |      5 |
| Ireland        |      0 |      0 |      1 |      2 |      3 |      4 |      5 |      5 |
| United Kingdom |      0 |      0 |      3 |      4 |      6 |      6 |      7 |      7 |
| United States  |      1 |      1 |      2 |      4 |      4 |      4 |      5 |      6 |
<BLANKLINE>
<BLANKLINE>
<BLANKLINE>


"""

from .._dynamics import _dynamics


def country_dynamics(
    topics_length=5,
    topic_min_occ=None,
    topic_min_citations=None,
    directory="./",
    title="Country Dynamics",
    plot=True,
    database="documents",
    start_year=None,
    end_year=None,
    **filters,
):
    """Makes a dynamics chat for top sources."""

    results = _dynamics(
        criterion="countries",
        topics_length=topics_length,
        topic_min_occ=topic_min_occ,
        topic_min_citations=topic_min_citations,
        directory=directory,
        plot=plot,
        title=title,
        database=database,
        start_year=start_year,
        end_year=end_year,
        **filters,
    )

    table = results.table_.copy()
    table = table[["countries", "year", "cum_OCC"]]
    table = table.pivot(index="countries", columns="year", values="cum_OCC")
    table = table.fillna(0)
    results.prompt_ = _create_prompt(table)

    return results


def _create_prompt(table):
    return f"""
Imagine that you are a researcher analyzing a bibliographic dataset. The table \
below provides data on cumulative document production by year per \
country for the top {table.shape[0]} most productive countries in the dataset. \
Use the information in the table to draw conclusions about the cumulative \
productivity per year of the countries. \
In your analysis, be sure to describe in a clear and concise way, any findings \
or any patterns you observe, and identify any outliers or anomalies in the \
data. Limit your description to one paragraph with no more than 250 words.

{table.to_markdown()}


"""
