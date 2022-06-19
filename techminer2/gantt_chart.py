"""
Gantt Chart (*)
===============================================================================

>>> from techminer2 import *
>>> directory = "data/"
>>> file_name = "sphinx/images/gantt_chart.png"
>>> gantt_chart(
...     column='author_keywords',
...     top_n=20, 
...     directory=directory,
... ).write_image(file_name)

.. image:: images/gantt_chart.png
    :width: 700px
    :align: center


"""
import plotly.express as px
from pyparsing import col

from ._read_records import read_filtered_records


def gantt_chart(
    column="author_keywords",
    directory="./",
    top_n=10,
):

    records = read_filtered_records(directory)
    records = records[["pub_year", column]]
    records = records.dropna(subset=[column])
    records[column] = records[column].str.split(";")
    records = records.explode(column)
    records[column] = records[column].str.strip()
    records = records.groupby(column).agg({"pub_year": [min, max]})
    records.columns = records.columns.droplevel()
    records = records.rename(columns={"min": "start", "max": "finish"})
    records["data"] = records.index

    records["start"] = records["start"].astype(str) + "-01-01"
    records["finish"] = records["finish"].astype(str) + "-12-31"

    index = read_filtered_records(directory)
    index = index[column]
    index = index.dropna()
    index = index.str.split(";")
    index = index.explode()
    index = index.str.strip()
    index = index.value_counts()
    index = index.sort_values(ascending=False)
    index = index.head(top_n)

    records = records.loc[index.index, :]

    fig = px.timeline(
        records,
        x_start="start",
        x_end="finish",
        y="data",
    )
    fig.update_yaxes(autorange="reversed")
    fig.update_layout(paper_bgcolor="white", plot_bgcolor="white")
    fig.update_traces(marker_color="lightgray")
    fig.update_xaxes(
        linecolor="gray",
        linewidth=2,
        gridcolor="lightgray",
        griddash="dot",
    )

    fig.update_yaxes(
        linecolor="gray",
        linewidth=2,
    )
    fig.update_xaxes(tickangle=270)

    return fig


# def ____gantt_chart(
#     column,
#     metric="num_documents",
#     top_n=None,
#     min_occ=1,
#     max_occ=None,
#     sort_values=None,
#     sort_index=None,
#     directory="./",
#     #
#     color="tab:blue",
#     figsize=(6, 6),
#     plot=True,
# ):
#     indicators = topic_view(
#         column=column,
#         metric=metric,
#         top_n=top_n,
#         min_occ=min_occ,
#         max_occ=max_occ,
#         sort_values=sort_values,
#         sort_index=sort_index,
#         directory=directory,
#     )

#     topics = indicators.index

#     production = annual_occurrence_matrix(
#         column=column,
#         min_occ=1,
#         directory=directory,
#     )

#     production = production.loc[topics]

#     if plot is False:
#         return production

#     return _gantt_chart(production, figsize=figsize, color=color)
