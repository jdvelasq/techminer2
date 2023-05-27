"""
Corresponding Author's Country
===============================================================================



>>> directory = "data/regtech/"
>>> file_name = "sphinx/_static/bibliometrix__corresponding_authors_country.html"

>>> from techminer2 import bibliometrix
>>> r = bibliometrix.countries.corresponding_authors_country(
...     topics_length=20,
...     directory=directory,
... )
>>> r.plot_.write_html(file_name)

.. raw:: html

    <iframe src="../../../_static/bibliometrix__corresponding_authors_country.html"height="600px" width="100%" frameBorder="0"></iframe>


>>> r.table_.head()


>>> print(r.prompt_)


"""
from dataclasses import dataclass

import numpy as np
import plotly.express as px

from ...techminer.indicators.collaboration_indicators_by_topic import (
    collaboration_indicators_by_topic,
)


@dataclass(init=False)
class _Results:
    plot_: None
    table_: None
    prompt_: None


def corresponding_authors_country(
    topics_length=20,
    topic_min_occ=None,
    topic_min_citations=None,
    directory="./",
    database="documents",
    start_year=None,
    end_year=None,
    **filters,
):
    """Corresponding Author's Country"""

    table = collaboration_indicators_by_topic(
        "countries",
        root_dir=directory,
        database=database,
        start_year=start_year,
        end_year=end_year,
        **filters,
    )

    if topic_min_occ is not None:
        table = table[table.OCC >= topic_min_occ]
    if topic_min_citations is not None:
        table = table[table.global_citations >= topic_min_citations]
    table = table.head(topics_length)

    results = _Results()
    results.table_ = table
    table = table.reset_index()
    results.plot_ = _make_plot(table)
    results.prompt_ = _create_prompt(table)
    return results


def _create_prompt(table):
    return f"""
Imagine that you are a researcher analyzing a bibliographic dataset. The table \
below provides data on top {table.shape[0]} most frequent countries in the \
dataset. 'single publication' is the number of documents in which all the \
authors are from the same country. 'multiple publication' is the number \
of documents in which the authors are from different countries. \
'mcp ratio' is the ratio between 'multiple publication' and 'single publication'. \
The higher the ratio, the higher the collaboration between countries. \
Use the information in the table to draw conclusions about the level of \
collaboration between countries in the dataset. In your analysis, be sure to \
describe in a clear and concise way, any findings or any patterns you \
observe, and identify any outliers or anomalies in the data. \
Limit your description to one paragraph with no more than 250 words.

{table.to_markdown()}


"""


def _make_table(
    directory,
    database,
    start_year,
    end_year,
    **filters,
):
    indicators = indicators.sort_values(by="OCC", ascending=False)
    indicators = indicators[["single_publication", "multiple_publication"]]
    indicators = indicators.assign(
        mcp_ratio=indicators["multiple_publication"]
        / indicators["single_publication"]
    )
    indicators = indicators.replace(np.inf, "-")
    return indicators


def _make_plot(indicators):
    indicators = indicators.melt(
        id_vars="countries",
        value_vars=["single_publication", "multiple_publication"],
    )
    indicators = indicators.rename(
        columns={"variable": "publication", "value": "Num Documents"}
    )
    indicators.publication = indicators.publication.map(
        lambda x: x.replace("_", " ").title()
    )
    indicators.countries = indicators.countries.map(lambda x: x.title())

    fig = px.bar(
        indicators,
        x="Num Documents",
        y="countries",
        color="publication",
        title="Corresponding Author's Country",
        hover_data=["Num Documents"],
        orientation="h",
        color_discrete_map={
            "Single Publication": "#8da4b4",
            "Multiple Publication": "#556f81",
        },
    )
    fig.update_layout(paper_bgcolor="white", plot_bgcolor="white")
    fig.update_yaxes(
        linecolor="gray",
        linewidth=2,
        autorange="reversed",
    )
    fig.update_xaxes(
        linecolor="gray",
        linewidth=2,
        gridcolor="gray",
        griddash="dot",
    )

    return fig
