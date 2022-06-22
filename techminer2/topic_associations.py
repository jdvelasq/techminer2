"""
Topic Associations
===============================================================================


>>> from techminer2 import *
>>> directory = "data/"
>>> file_name = "sphinx/images/topic_associations_table.png"

>>> Topic_associations(
...     'fintech', 
...     'author_keywords', 
...     directory=directory,
... ).table_.write_html(file_name)

# ... ).table_.write_image(file_name)

.. raw:: html
   :file: sphinx/_static/topic_associations_table.html

---

.. image:: images/topic_associations_table.png
    :width: 700px
    :align: center


>>> Topic_associations(
...     'fintech', 
...     'author_keywords', 
...     directory=directory,
... ).head()
author_keywords
financial inclusion       15
financial technologies    14
blockchain                13
innovation                10
regulation                10
Name: fintech, dtype: int64

"""
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

from .co_occurrence_matrix import co_occurrence_matrix


class Topic_associations:
    def __init__(
        self, item, column, directory, top_n=10, min_occ=1, normalization=None
    ):
        self.directory = directory
        self.item = item
        self.column = column
        self.top_n = top_n
        self.min_occ = min_occ
        self.normalization = normalization
        self._compute_associations()

    def _compute_associations(self):
        coc_matrix = co_occurrence_matrix(
            self.column,
            min_occ=self.min_occ,
            normalization=self.normalization,
            directory=self.directory,
        )

        coc_matrix.columns = coc_matrix.columns.get_level_values(0)
        coc_matrix.index = coc_matrix.index.get_level_values(0)

        series = coc_matrix[self.item]
        series = series.map(lambda x: pd.NA if x == 0 else x)
        series = series.dropna()
        series = series[series.index != self.item]
        series = series.astype(int)
        series = series.to_frame()
        series = series.reset_index()
        series = series.sort_values(
            by=[self.item, self.column], ascending=[False, True]
        )
        series = series.set_index(self.column)
        series = series[self.item]
        if self.top_n is not None:
            series = series.head(self.top_n)

        self.associations_ = series

    @property
    def graph_(self):
        fig = px.scatter(
            x=self.associations_.values,
            y=self.associations_.index,
            text=self.associations_.astype(str),
            labels={
                "x": "OCC",
                "y": self.column.replace("_", " ").title(),
            },
        )
        fig.update_traces(marker=dict(size=10, color="black"))
        fig.update_traces(textposition="middle right")
        fig.update_traces(line=dict(color="black"))
        fig.update_layout(paper_bgcolor="white", plot_bgcolor="white")
        fig.update_yaxes(
            linecolor="gray",
            linewidth=2,
            gridcolor="lightgray",
            autorange="reversed",
            griddash="dot",
        )
        fig.update_xaxes(showticklabels=False)

        return fig

    @property
    def table_(self):
        fig = go.Figure(
            data=[
                go.Table(
                    header=dict(values=[self.column, "OCC"]),
                    cells=dict(
                        values=[
                            self.associations_.index,
                            self.associations_.values,
                        ]
                    ),
                )
            ]
        )
        return fig


# def topic_associations(
#     item,
#     column,
#     top_n=10,
#     min_occ=1,
#     normalization=None,
#     directory="./",
#     plot=True,
#     color="k",
#     figsize=(8, 6),
# ):

#     coc_matrix = co_occurrence_matrix(
#         column,
#         min_occ=min_occ,
#         normalization=normalization,
#         directory=directory,
#     )

#     coc_matrix.columns = coc_matrix.columns.get_level_values(0)
#     coc_matrix.index = coc_matrix.index.get_level_values(0)

#     # -----------------------------------------------------------------------------------
#     series = coc_matrix[item]
#     series = series.map(lambda x: np.nan if x == 0 else x)
#     series = series.dropna()
#     series = series[series.index != item]
#     series = series.astype(int)
#     series = series.to_frame()
#     series = series.reset_index()
#     series = series.sort_values(by=[item, column], ascending=[False, True])
#     series = series.set_index(column)
#     series = series[item]
#     # -----------------------------------------------------------------------------------

#     if plot is False:
#         return series

#     series = series.head(top_n)

#     if normalization is None:
#         xlabel = "Occurrences"
#     else:
#         xlabel = normalization.capitalize()

#     return _cleveland_chart(
#         series,
#         figsize=figsize,
#         color=color,
#         title="'" + item + "' associations",
#         xlabel=xlabel,
#         ylabel="Words",
#     )
