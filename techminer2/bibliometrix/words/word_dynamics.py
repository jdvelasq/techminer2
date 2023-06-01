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
| author_keywords              |   2017 |   2018 |   2019 |   2020 |   2021 |   2022 |   2023 |
|:-----------------------------|-------:|-------:|-------:|-------:|-------:|-------:|-------:|
| regtech 28:329               |      2 |      3 |      4 |      8 |      3 |      6 |      2 |
| fintech 12:249               |      0 |      2 |      4 |      3 |      1 |      2 |      0 |
| regulatory technology 07:037 |      0 |      0 |      0 |      2 |      3 |      2 |      0 |
| compliance 07:030            |      0 |      0 |      1 |      3 |      1 |      1 |      1 |
| regulation 05:164            |      0 |      2 |      0 |      1 |      1 |      1 |      0 |

>>> print(r.prompt_)
Analyze the table below which contains the  occurrences by year for the author_keywords. Identify any notable patterns, trends, or outliers in the data, and discuss their implications for the research field. Be sure to provide a concise summary of your findings in no more than 150 words.
<BLANKLINE>
| author_keywords              |   2017 |   2018 |   2019 |   2020 |   2021 |   2022 |   2023 |
|:-----------------------------|-------:|-------:|-------:|-------:|-------:|-------:|-------:|
| regtech 28:329               |      2 |      3 |      4 |      8 |      3 |      6 |      2 |
| fintech 12:249               |      0 |      2 |      4 |      3 |      1 |      2 |      0 |
| regulatory technology 07:037 |      0 |      0 |      0 |      2 |      3 |      2 |      0 |
| compliance 07:030            |      0 |      0 |      1 |      3 |      1 |      1 |      1 |
| regulation 05:164            |      0 |      2 |      0 |      1 |      1 |      1 |      0 |
<BLANKLINE>
<BLANKLINE>

"""
from ... import vantagepoint
from ...techminer.indicators.indicators_by_item_per_year import (
    indicators_by_item_per_year,
)
from ..documents_per_criterion import documents_per_criterion


def word_dynamics(
    criterion="author_keywords",
    topics_length=50,
    topic_min_occ=None,
    topic_max_occ=None,
    topic_min_citations=None,
    topic_max_citations=None,
    custom_topics=None,
    cumulative=False,
    directory="./",
    title="Word Dynamics",
    plot=True,
    database="documents",
    start_year=None,
    end_year=None,
    **filters,
):
    """Makes a dynamics chat for top words."""

    terms_by_year = vantagepoint.analyze.terms_by_year(
        field=criterion,
        top_n=topics_length,
        occ_range=topic_min_occ,
        topic_occ_max=topic_max_occ,
        gc_range=topic_min_citations,
        topic_citations_max=topic_max_citations,
        custom_items=custom_topics,
        root_dir=directory,
        database=database,
        year_filter=start_year,
        cited_by_filter=end_year,
        cumulative=cumulative,
        **filters,
    )

    chart = vantagepoint.report.gantt_chart(
        terms_by_year,
        title=criterion.replace("_", " ").title() + " Dynamics",
    )

    chart.documents_per_keyword_ = documents_per_criterion(
        field=criterion,
        root_dir=directory,
        database=database,
        year_filter=start_year,
        cited_by_filter=end_year,
        **filters,
    )

    chart.production_per_year_ = indicators_by_item_per_year(
        field=criterion,
        root_dir=directory,
        database=database,
        year_filter=start_year,
        cited_by_filter=end_year,
        **filters,
    )

    chart.table_ = terms_by_year.table_.copy()

    return chart

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
