"""
Word Dynamics
===============================================================================


>>> directory = "data/regtech/"
>>> file_name = "sphinx/_static/bibliometrix__word_dynamics.html"

>>> from techminer2 import bibliometrix
>>> r = bibliometrix.words.word_dynamics(
...     criterion="author_keywords",
...     topics_length=5,
...     directory=directory,
... )
>>> r.plot_.write_html(file_name)

.. raw:: html

    <iframe src="../../../_static/bibliometrix__word_dynamics.html" height="600px" width="100%" frameBorder="0"></iframe>

    
>>> print(r.table_.head().to_markdown())
|    |   year | author_keywords   |   cum_OCC |
|---:|-------:|:------------------|----------:|
|  0 |   2017 | regtech           |         2 |
|  1 |   2018 | regtech           |         5 |
|  2 |   2019 | regtech           |         9 |
|  3 |   2020 | regtech           |        17 |
|  4 |   2021 | regtech           |        20 |


>>> print(r.dynamics_.to_markdown())
| author_keywords       |   2017 |   2018 |   2019 |   2020 |   2021 |   2022 |   2023 |
|:----------------------|-------:|-------:|-------:|-------:|-------:|-------:|-------:|
| compliance            |      0 |      0 |      1 |      4 |      5 |      6 |      7 |
| fintech               |      0 |      2 |      6 |      9 |     10 |     12 |     12 |
| regtech               |      2 |      5 |      9 |     17 |     20 |     26 |     28 |
| regulation            |      0 |      2 |      2 |      3 |      4 |      5 |      5 |
| regulatory technology |      0 |      0 |      0 |      2 |      5 |      7 |      7 |


>>> print(r.prompt_)
<BLANKLINE>
Imagine that you are a researcher analyzing a bibliographic dataset. The table below provides data on cumulative occurrences of author keywords for the top 5 most frequent author keywords in the dataset. Use the information in the table to draw conclusions about the cumulative occurrence per year of the author keywords. In your analysis, be sure to describe in a clear and concise way, any findings or any patterns you observe, and identify any outliers or anomalies in the data. Limit your description to one paragraph with no more than 250 words.
<BLANKLINE>
| author_keywords       |   2017 |   2018 |   2019 |   2020 |   2021 |   2022 |   2023 |
|:----------------------|-------:|-------:|-------:|-------:|-------:|-------:|-------:|
| compliance            |      0 |      0 |      1 |      4 |      5 |      6 |      7 |
| fintech               |      0 |      2 |      6 |      9 |     10 |     12 |     12 |
| regtech               |      2 |      5 |      9 |     17 |     20 |     26 |     28 |
| regulation            |      0 |      2 |      2 |      3 |      4 |      5 |      5 |
| regulatory technology |      0 |      0 |      0 |      2 |      5 |      7 |      7 |
<BLANKLINE>
<BLANKLINE>
<BLANKLINE>


"""
from .._dynamics import _dynamics


def word_dynamics(
    criterion="author_keywords",
    topics_length=5,
    topic_min_occ=None,
    topic_min_citations=None,
    directory="./",
    title="Word Dynamics",
    plot=True,
    database="documents",
    start_year=None,
    end_year=None,
    **filters,
):
    """Makes a dynamics chat for top sources."""

    results = _dynamics(
        criterion=criterion,
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
    table = table[[criterion, "year", "cum_OCC"]]
    table = table.pivot(index=criterion, columns="year", values="cum_OCC")
    table = table.fillna(0)
    results.dynamics_ = table
    results.prompt_ = _create_prompt(table, criterion)

    return results


def _create_prompt(table, criterion):
    return f"""
Imagine that you are a researcher analyzing a bibliographic dataset. The table \
below provides data on cumulative occurrences of {criterion.replace("_", " ")} \
for the top {table.shape[0]} most frequent {criterion.replace("_", " ")} in the dataset. \
Use the information in the table to draw conclusions about the cumulative \
occurrence per year of the {criterion.replace("_", " ")}. \
In your analysis, be sure to describe in a clear and concise way, any findings \
or any patterns you observe, and identify any outliers or anomalies in the \
data. Limit your description to one paragraph with no more than 250 words.

{table.to_markdown()}


"""
