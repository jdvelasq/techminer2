"""
Compararison between word pairs
===============================================================================



>>> root_dir = "data/regtech/"

>>> from techminer2 import tlab
>>> cwp = tlab.comparison_between_word_pairs(
...     criterion="author_keywords",
...     topic_a="artificial intelligence",
...     topic_b="regtech",
...     root_dir=root_dir,
... )

>>> file_name = "sphinx/_static/tlab__co_occurrence_analysis__comparison_between_word_pairs_bar_chart-1.html"
>>> cwp.plot_.write_html(file_name)

.. raw:: html

    <iframe src="../../_static/tlab__co_occurrence_analysis__comparison_between_word_pairs_bar_chart-1.html" height="600px" width="100%" frameBorder="0"></iframe>


>>> cwp.table_.head(10)
                                 row                     column  OCC
0            artificial intelligence             fintech 12:249    0
1  artificial intelligence & regtech             fintech 12:249    1
2                            regtech             fintech 12:249   11
3            artificial intelligence          compliance 07:030    0
4                            regtech          compliance 07:030    6
5  artificial intelligence & regtech          compliance 07:030    1
6            artificial intelligence          regulation 05:164    0
7                            regtech          regulation 05:164    4
8  artificial intelligence & regtech          regulation 05:164    0
9                            regtech  financial services 04:168    3


>>> from techminer2 import tlab
>>> cwp = tlab.comparison_between_word_pairs(
...     criterion="author_keywords",
...     topic_a="artificial intelligence",
...     topic_b="regtech",
...     custom_topics=[
...         "fintech",
...         "blockchain",
...         "machine learning",
...     ],
...     root_dir=root_dir,
... )

>>> file_name = "sphinx/_static/tlab__co_occurrence_analysis__comparison_between_word_pairs_bar_chart-2.html"
>>> cwp.plot_.write_html(file_name)

.. raw:: html

    <iframe src="../../_static/tlab__co_occurrence_analysis__comparison_between_word_pairs_bar_chart-2.html" height="600px" width="100%" frameBorder="0"></iframe>


>>> cwp.table_.head(10)
                                 row                   column  OCC
0            artificial intelligence           fintech 12:249    0
1  artificial intelligence & regtech           fintech 12:249    1
2                            regtech           fintech 12:249   11
3            artificial intelligence        blockchain 03:005    0
4  artificial intelligence & regtech        blockchain 03:005    1
5                            regtech        blockchain 03:005    1
6            artificial intelligence  machine learning 01:003    0
7  artificial intelligence & regtech  machine learning 01:003    0
8                            regtech  machine learning 01:003    1


"""


import plotly.express as px

from ..classes import WordComparison
from ..counters import add_counters_to_column_values
from ..item_utils import generate_custom_items
from ..sort_utils import sort_indicators_by_metric
from ..techminer.indicators.indicators_by_topic import indicators_by_topic
from ..utils.load_utils import load_stopwords
from ..utils.records import read_records


def comparison_between_word_pairs(
    criterion,
    topic_a,
    topic_b,
    topics_length=20,
    topic_occ_min=None,
    topic_occ_max=None,
    topic_citations_min=None,
    topic_citations_max=None,
    custom_topics=None,
    root_dir="./",
    database="documents",
    start_year=None,
    end_year=None,
    **filters,
):
    """Comparison between topics."""

    matrix_list = _create_comparison_matrix_list(
        topic_a=topic_a,
        topic_b=topic_b,
        criterion=criterion,
        root_dir=root_dir,
        database=database,
        start_year=start_year,
        end_year=end_year,
        **filters,
    )

    matrix_list = _remove_stopwords(
        root_dir,
        matrix_list,
    )

    matrix_list = _select_topics(
        matrix_list=matrix_list,
        topic_occ_min=topic_occ_min,
        topic_occ_max=topic_occ_max,
        topic_citations_min=topic_citations_min,
        topic_citations_max=topic_citations_max,
        topics_length=topics_length,
        custom_topics=custom_topics,
        criterion=criterion,
        directory=root_dir,
        database=database,
        start_year=start_year,
        end_year=end_year,
        **filters,
    )

    matrix_list = add_counters_to_column_values(
        criterion=criterion,
        name="column",
        root_dir=root_dir,
        database=database,
        table=matrix_list,
        start_year=start_year,
        end_year=end_year,
        **filters,
    )

    matrix_list = _sort_matrix_list(matrix_list)
    matrix_list = matrix_list.reset_index(drop=True)

    wordcomparison = WordComparison()
    wordcomparison.table_ = matrix_list
    wordcomparison.plot_ = _create_bart_chart(matrix_list, topic_a, topic_b)

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
    topic_occ_min,
    topic_occ_max,
    topic_citations_min,
    topic_citations_max,
    topics_length,
    custom_topics,
    criterion,
    directory,
    database,
    start_year,
    end_year,
    **filters,
):
    indicators = indicators_by_topic(
        field=criterion,
        root_dir=directory,
        database=database,
        year_filter=start_year,
        cited_by_filter=end_year,
        **filters,
    )

    indicators = sort_indicators_by_metric(indicators, metric="OCC")

    if custom_topics is None:
        custom_topics = generate_custom_items(
            indicators=indicators,
            top_n=topics_length,
            occ_range=topic_occ_min,
            topic_occ_max=topic_occ_max,
            gc_range=topic_citations_min,
            topic_citations_max=topic_citations_max,
        )

    matrix_list = matrix_list.loc[matrix_list.column.isin(custom_topics), :]

    return matrix_list


def _remove_stopwords(directory, matrix_list):
    stopwords = load_stopwords(directory)
    matrix_list = matrix_list[~matrix_list["column"].isin(stopwords)]
    return matrix_list


def _create_comparison_matrix_list(
    topic_a,
    topic_b,
    criterion,
    root_dir,
    database,
    start_year,
    end_year,
    **filters,
):
    records = read_records(
        root_dir=root_dir,
        database=database,
        start_year=start_year,
        end_year=end_year,
        **filters,
    )

    matrix_list = records[[criterion]].copy()
    matrix_list = matrix_list.dropna()
    matrix_list = matrix_list.rename(columns={criterion: "column"})
    matrix_list = matrix_list.assign(row=records[[criterion]])

    # Explode 'row' for topic_a and topic_b
    matrix_list["row"] = matrix_list["row"].str.split(";")
    matrix_list["row"] = matrix_list["row"].map(
        lambda x: [y.strip() for y in x]
    )
    matrix_list = matrix_list[
        matrix_list["row"].map(
            lambda x: any([y in [topic_a, topic_b] for y in x])
        )
    ]

    matrix_list["row"] = matrix_list["row"].map(
        lambda x: sorted([y for y in x if y in [topic_a, topic_b]])
    )
    matrix_list["row"] = matrix_list["row"].str.join(" & ")
    matrix_list = matrix_list.explode("row")
    matrix_list["row"] = matrix_list["row"].str.strip()

    # Explode 'column' for all topics
    matrix_list["column"] = matrix_list["column"].str.split(";")
    matrix_list = matrix_list.explode("column")
    matrix_list["column"] = matrix_list["column"].str.strip()
    matrix_list = matrix_list[
        matrix_list["column"].map(lambda x: x not in [topic_a, topic_b])
    ]

    # count
    matrix_list["OCC"] = 1
    matrix_list = matrix_list.groupby(
        ["row", "column"], as_index=False
    ).aggregate("sum")

    matrix = matrix_list.pivot(index="row", columns="column", values="OCC")
    matrix = matrix.fillna(0)
    if " & ".join([topic_a, topic_b]) not in matrix.index.to_list():
        matrix.loc[" & ".join(sorted([topic_a, topic_b]))] = 0

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
