# flake8: noqa
"""
Compararison between word pairs
===============================================================================



>>> root_dir = "data/regtech/"
>>> from techminer2 import tlab
>>> cwp = tlab.comparison_between_word_pairs(
...     field="author_keywords",
...     item_a="ARTIFICIAL_INTELLIGENCE",
...     item_b="REGTECH",
...     root_dir=root_dir,
... )
>>> file_name = "sphinx/_static/tlab__co_occurrence_analysis__comparison_between_word_pairs_bar_chart-1.html"
>>> cwp.plot_.write_html(file_name)

.. raw:: html

    <iframe src="../../_static/tlab__co_occurrence_analysis__comparison_between_word_pairs_bar_chart-1.html" height="600px" width="100%" frameBorder="0"></iframe>


>>> cwp.table_.head(10)
                                 row             column  OCC
0            ARTIFICIAL_INTELLIGENCE     FINTECH 12:249    0
1  ARTIFICIAL_INTELLIGENCE & REGTECH     FINTECH 12:249    1
2                            REGTECH     FINTECH 12:249   11
3                            REGTECH  COMPLIANCE 07:030    6
4  ARTIFICIAL_INTELLIGENCE & REGTECH  COMPLIANCE 07:030    1
5            ARTIFICIAL_INTELLIGENCE  COMPLIANCE 07:030    0
6                            REGTECH  REGULATION 05:164    4
7            ARTIFICIAL_INTELLIGENCE  REGULATION 05:164    0
8  ARTIFICIAL_INTELLIGENCE & REGTECH  REGULATION 05:164    0
9                            REGTECH     SUPTECH 03:004    3


>>> from techminer2 import tlab
>>> cwp = tlab.comparison_between_word_pairs(
...     field="author_keywords",
...     item_a="ARTIFICIAL_INTELLIGENCE",
...     item_b="REGTECH",
...     custom_items=[
...         "FINTECH",
...         "BLOCKCHAIN",
...         "MACHINE_LEARNING",
...     ],
...     root_dir=root_dir,
... )

>>> file_name = "sphinx/_static/tlab__co_occurrence_analysis__comparison_between_word_pairs_bar_chart-2.html"
>>> cwp.plot_.write_html(file_name)

.. raw:: html

    <iframe src="../../_static/tlab__co_occurrence_analysis__comparison_between_word_pairs_bar_chart-2.html" height="600px" width="100%" frameBorder="0"></iframe>


>>> cwp.table_.head(10)
                                 row                   column  OCC
0            ARTIFICIAL_INTELLIGENCE           FINTECH 12:249    0
1  ARTIFICIAL_INTELLIGENCE & REGTECH           FINTECH 12:249    1
2                            REGTECH           FINTECH 12:249   11
3            ARTIFICIAL_INTELLIGENCE        BLOCKCHAIN 03:005    0
4  ARTIFICIAL_INTELLIGENCE & REGTECH        BLOCKCHAIN 03:005    1
5                            REGTECH        BLOCKCHAIN 03:005    1
6            ARTIFICIAL_INTELLIGENCE  MACHINE_LEARNING 01:003    0
7  ARTIFICIAL_INTELLIGENCE & REGTECH  MACHINE_LEARNING 01:003    0
8                            REGTECH  MACHINE_LEARNING 01:003    1




# pylint: disable=line-too-long
"""


import plotly.express as px

from ..classes import WordComparison
from ..counters import add_counters_to_column_values
from ..item_utils import generate_custom_items
from ..load_utils import load_stopwords
from ..record_utils import read_records
from ..sort_utils import sort_indicators_by_metric
from ..techminer.indicators.indicators_by_field import indicators_by_field


def comparison_between_word_pairs(
    field,
    item_a,
    item_b,
    # Item filters:
    top_n=None,
    occ_range=None,
    gc_range=None,
    custom_items=None,
    # Database params:
    root_dir="./",
    database="documents",
    year_filter=None,
    cited_by_filter=None,
    **filters,
):
    """Comparison between topics."""

    matrix_list = _create_comparison_matrix_list(
        item_a=item_a,
        item_b=item_b,
        field=field,
        root_dir=root_dir,
        database=database,
        year_filter=year_filter,
        cited_by_filter=cited_by_filter,
        **filters,
    )

    matrix_list = _remove_stopwords(
        root_dir,
        matrix_list,
    )

    matrix_list = _select_topics(
        matrix_list=matrix_list,
        occ_range=occ_range,
        gc_range=gc_range,
        top_n=top_n,
        custom_items=custom_items,
        field=field,
        root_dir=root_dir,
        database=database,
        year_filter=year_filter,
        cited_by_filter=cited_by_filter,
        **filters,
    )

    matrix_list = add_counters_to_column_values(
        criterion=field,
        name="column",
        root_dir=root_dir,
        database=database,
        table=matrix_list,
        start_year=year_filter,
        end_year=cited_by_filter,
        **filters,
    )

    matrix_list = _sort_matrix_list(matrix_list)
    matrix_list = matrix_list.reset_index(drop=True)

    wordcomparison = WordComparison()
    wordcomparison.table_ = matrix_list
    wordcomparison.plot_ = _create_bart_chart(matrix_list, item_a, item_b)

    return wordcomparison


def _create_bart_chart(matrix_list, topic_a, topic_b):
    matrix_list = matrix_list.copy()

    fig = px.bar(
        matrix_list,
        x="OCC",
        y="column",
        color="row",
        title="Co-occurrences between topics",
        hover_data=["OCC"],
        orientation="h",
        color_discrete_map={
            topic_a: "#CCD3D9",
            topic_b: "#99A8B3",
            " & ".join(sorted([topic_a, topic_b])): "#556f81",
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

    fig.update_layout(
        yaxis_title=None,
    )

    return fig


def _select_topics(
    matrix_list,
    occ_range,
    gc_range,
    top_n,
    custom_items,
    field,
    root_dir,
    database,
    year_filter,
    cited_by_filter,
    **filters,
):
    indicators = indicators_by_field(
        field=field,
        root_dir=root_dir,
        database=database,
        year_filter=year_filter,
        cited_by_filter=cited_by_filter,
        **filters,
    )

    indicators = sort_indicators_by_metric(indicators, metric="OCC")

    if custom_items is None:
        custom_items = generate_custom_items(
            indicators=indicators,
            top_n=top_n,
            occ_range=occ_range,
            gc_range=gc_range,
        )

    matrix_list = matrix_list.loc[matrix_list.column.isin(custom_items), :]

    return matrix_list


def _remove_stopwords(directory, matrix_list):
    stopwords = load_stopwords(directory)
    matrix_list = matrix_list[~matrix_list["column"].isin(stopwords)]
    return matrix_list


def _create_comparison_matrix_list(
    item_a,
    item_b,
    field,
    root_dir,
    database,
    year_filter,
    cited_by_filter,
    **filters,
):
    records = read_records(
        root_dir=root_dir,
        database=database,
        year_filter=year_filter,
        cited_by_filter=cited_by_filter,
        **filters,
    )

    matrix_list = records[[field]].copy()
    matrix_list = matrix_list.dropna()
    matrix_list = matrix_list.rename(columns={field: "column"})
    matrix_list = matrix_list.assign(row=records[[field]])

    # Explode 'row' for topic_a and topic_b
    matrix_list["row"] = matrix_list["row"].str.split(";")
    matrix_list["row"] = matrix_list["row"].map(
        lambda x: [y.strip() for y in x]
    )
    matrix_list = matrix_list[
        matrix_list["row"].map(
            lambda x: any([y in [item_a, item_b] for y in x])
        )
    ]

    matrix_list["row"] = matrix_list["row"].map(
        lambda x: sorted([y for y in x if y in [item_a, item_b]])
    )
    matrix_list["row"] = matrix_list["row"].str.join(" & ")
    matrix_list = matrix_list.explode("row")
    matrix_list["row"] = matrix_list["row"].str.strip()

    # Explode 'column' for all topics
    matrix_list["column"] = matrix_list["column"].str.split(";")
    matrix_list = matrix_list.explode("column")
    matrix_list["column"] = matrix_list["column"].str.strip()
    matrix_list = matrix_list[
        matrix_list["column"].map(lambda x: x not in [item_a, item_b])
    ]

    # count
    matrix_list["OCC"] = 1
    matrix_list = matrix_list.groupby(
        ["row", "column"], as_index=False
    ).aggregate("sum")

    matrix = matrix_list.pivot(index="row", columns="column", values="OCC")
    matrix = matrix.fillna(0)
    if " & ".join([item_a, item_b]) not in matrix.index.to_list():
        matrix.loc[" & ".join(sorted([item_a, item_b]))] = 0

    matrix_list = matrix.melt(
        value_name="OCC", var_name="column", ignore_index=False
    )

    matrix_list = matrix_list.reset_index()
    matrix_list["OCC"] = matrix_list["OCC"].astype(int)

    return matrix_list


def _sort_matrix_list(matrix_list):
    indicators = matrix_list.copy()
    indicators = indicators[["column", "OCC"]]
    indicators = indicators.groupby("column", as_index=False).aggregate("sum")
    indicators = indicators.sort_values(by=["OCC"], ascending=False)
    sorted_topics = indicators["column"]
    topics2rank = {topic: i for i, topic in enumerate(sorted_topics)}

    matrix_list["rank"] = matrix_list["column"].map(topics2rank)
    matrix_list = matrix_list.sort_values(by=["rank"], ascending=True)
    matrix_list = matrix_list.drop(columns=["rank"])

    return matrix_list
