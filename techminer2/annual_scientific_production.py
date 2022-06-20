"""
Annual Scientific Production (*)
===============================================================================


>>> from techminer2 import *
>>> directory = "data/"
>>> file_name = "sphinx/images/annual_scientific_production.png"
>>> Annual_scientific_production(directory).plot_.write_image(file_name)

.. image:: images/annual_scientific_production.png
    :width: 700px
    :align: center


>>> Annual_scientific_production(directory).table_
pub_year
2016     5
2017    10
2018    34
2019    38
2020    62
2021    99
Name: num_documents, dtype: int64

"""
import plotly.express as px

from .annual_indicators import annual_indicators


class Annual_scientific_production:
    def __init__(self, directory="./"):
        self.directory = directory
        self.make_table()
        self.make_plot()

    def make_table(self):
        self.table_ = annual_indicators(self.directory).num_documents

    def make_plot(self):
        indicators = annual_indicators(self.directory)
        fig = px.line(
            x=indicators.index,
            y=indicators.num_documents,
            title="Annual Scientific Production",
            markers=True,
            text=indicators.num_documents,
            labels={"x": "Year", "y": "Number of publications"},
        )
        fig.update_traces(marker=dict(size=12))
        fig.update_traces(textposition="bottom right")
        fig.update_traces(line=dict(color="black"))
        fig.update_xaxes(tickangle=270)
        fig.update_layout(paper_bgcolor="white", plot_bgcolor="white")
        fig.update_xaxes(linecolor="gray", gridcolor="lightgray")
        fig.update_yaxes(linecolor="gray", gridcolor="lightgray")
        fig.update_yaxes(showticklabels=False)
        self.plot_ = fig
