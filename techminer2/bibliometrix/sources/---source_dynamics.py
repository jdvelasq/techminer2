"""
Source Dynamics
===============================================================================


>>> directory = "data/regtech/"
>>> file_name = "sphinx/_static/bibliometrix__source_dynamics.html"

>>> from techminer2 import bibliometrix
>>> r = bibliometrix.sources.source_dynamics(
...     topics_length=10, 
...     directory=directory,
... )
>>> r.plot_.write_html(file_name)

.. raw:: html

    <iframe src="../../_static/bibliometrix__source_dynamics.html" height="600px" width="100%" frameBorder="0"></iframe>

>>> print(r.table_.head().to_markdown())
|    |   year | source_abbr   |   cum_OCC |
|---:|-------:|:--------------|----------:|
|  0 |   2016 | J BANK REGUL  |         0 |
|  1 |   2017 | J BANK REGUL  |         0 |
|  2 |   2018 | J BANK REGUL  |         0 |
|  3 |   2019 | J BANK REGUL  |         0 |
|  4 |   2020 | J BANK REGUL  |         1 |


>>> print(r.dynamics_.to_markdown())
| source_abbr                              |   2016 |   2017 |   2018 |   2019 |   2020 |   2021 |   2022 |   2023 |
|:-----------------------------------------|-------:|-------:|-------:|-------:|-------:|-------:|-------:|-------:|
| DUKE LAW J                               |      1 |      1 |      1 |      1 |      1 |      1 |      1 |      1 |
| FOSTER INNOV AND COMPET WITH FINTECH,... |      0 |      0 |      0 |      0 |      2 |      2 |      2 |      2 |
| INT CONF INF TECHNOL SYST INNOV,...      |      0 |      0 |      0 |      0 |      0 |      0 |      2 |      2 |
| J BANK REGUL                             |      0 |      0 |      0 |      0 |      1 |      2 |      2 |      2 |
| J ECON BUS                               |      0 |      0 |      1 |      1 |      1 |      1 |      1 |      1 |
| J FINANC CRIME                           |      0 |      0 |      0 |      0 |      1 |      1 |      2 |      2 |
| NORTHWEST J INTL LAW BUS                 |      0 |      1 |      1 |      1 |      1 |      1 |      1 |      1 |
| PALGRAVE STUD DIGIT BUS ENABLING TECHNOL |      0 |      0 |      0 |      1 |      1 |      1 |      1 |      1 |
| ROUTLEDGE HANDB OF FINANCIAL...          |      0 |      0 |      0 |      0 |      0 |      2 |      2 |      2 |
| STUD COMPUT INTELL                       |      0 |      0 |      0 |      0 |      0 |      2 |      2 |      2 |


>>> print(r.prompt_)
<BLANKLINE>
Imagine that you are a researcher analyzing a bibliographic dataset. The table below provides data on cumulative document production by year per document source for the top 10 most productive sources in the dataset. Use the information in the table to draw conclusions about the cumulative productivity per year of the sources. In your analysis, be sure to describe in a clear and concise way, any findings or any patterns you observe, and identify any outliers or anomalies in the data. Limit your description to one paragraph with no more than 250 words.
<BLANKLINE>
| source_abbr                              |   2016 |   2017 |   2018 |   2019 |   2020 |   2021 |   2022 |   2023 |
|:-----------------------------------------|-------:|-------:|-------:|-------:|-------:|-------:|-------:|-------:|
| DUKE LAW J                               |      1 |      1 |      1 |      1 |      1 |      1 |      1 |      1 |
| FOSTER INNOV AND COMPET WITH FINTECH,... |      0 |      0 |      0 |      0 |      2 |      2 |      2 |      2 |
| INT CONF INF TECHNOL SYST INNOV,...      |      0 |      0 |      0 |      0 |      0 |      0 |      2 |      2 |
| J BANK REGUL                             |      0 |      0 |      0 |      0 |      1 |      2 |      2 |      2 |
| J ECON BUS                               |      0 |      0 |      1 |      1 |      1 |      1 |      1 |      1 |
| J FINANC CRIME                           |      0 |      0 |      0 |      0 |      1 |      1 |      2 |      2 |
| NORTHWEST J INTL LAW BUS                 |      0 |      1 |      1 |      1 |      1 |      1 |      1 |      1 |
| PALGRAVE STUD DIGIT BUS ENABLING TECHNOL |      0 |      0 |      0 |      1 |      1 |      1 |      1 |      1 |
| ROUTLEDGE HANDB OF FINANCIAL...          |      0 |      0 |      0 |      0 |      0 |      2 |      2 |      2 |
| STUD COMPUT INTELL                       |      0 |      0 |      0 |      0 |      0 |      2 |      2 |      2 |
<BLANKLINE>
<BLANKLINE>
<BLANKLINE>    

"""


from .._dynamics import _dynamics


def source_dynamics(
    topics_length=10,
    topic_min_occ=None,
    topic_min_citations=None,
    directory="./",
    title="Source Dynamics",
    plot=True,
    database="documents",
    start_year=None,
    end_year=None,
    **filters,
):
    """Makes a dynamics chat for top sources."""

    results = _dynamics(
        criterion="source_abbr",
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
    table = table[["source_abbr", "year", "cum_OCC"]]
    table = table.pivot(index="source_abbr", columns="year", values="cum_OCC")
    table = table.fillna(0)
    results.dynamics_ = table
    results.prompt_ = _create_prompt(table)

    return results


def _create_prompt(table):
    return f"""
Imagine that you are a researcher analyzing a bibliographic dataset. The table \
below provides data on cumulative document production by year per document \
source for the top {table.shape[0]} most productive sources in the dataset. \
Use the information in the table to draw conclusions about the cumulative \
productivity per year of the sources. \
In your analysis, be sure to describe in a clear and concise way, any findings \
or any patterns you observe, and identify any outliers or anomalies in the \
data. Limit your description to one paragraph with no more than 250 words.

{table.to_markdown()}


"""
