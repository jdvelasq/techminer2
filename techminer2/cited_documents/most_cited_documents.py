# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
# pylint: disable=too-many-statements
"""
Most Cited Documents
===============================================================================



>>> from techminer2.science_mapping.citation import most_cited_documents
>>> documents = most_cited_documents(
...     #
...     # FUNCTION PARAMS:
...     metric="global_citations",
...     top_n=20,
...     #
...     # CHART PARAMS:
...     title=None,
...     field_label=None,
...     metric_label=None,
...     textfont_size=10,
...     marker_size=7,
...     line_width=1.5,
...     yshift=4,
...     #
...     # DATABASE PARAMS:
...     root_dir="example/", 
...     database="main",
...     year_filter=(None, None),
...     cited_by_filter=(None, None),
... )
--INFO-- The file 'example/reports/most_global_cited_documents__abstracts.txt' was created.
--INFO-- The file 'example/reports/most_global_cited_documents__prompt.txt' was created.

>>> documents.fig_.write_html("sphinx/_static/analyze/citation/most_global_cited_documents.html")

.. raw:: html

    <iframe src="../../../../_static/analyze/citation/most_global_cited_documents.html" 
    height="600px" width="100%" frameBorder="0"></iframe>

    
>>> print(documents.df_.head().to_markdown()) 
| article                                       |   year |   rank_gcs |   global_citations |   rank_lcs |   local_citations |   global_citations_per_year |   local_citations_per_year | doi                           |
|:----------------------------------------------|-------:|-----------:|-------------------:|-----------:|------------------:|----------------------------:|---------------------------:|:------------------------------|
| Gomber P., 2018, J MANAGE INF SYST, V35, P220 |   2018 |          1 |                576 |          3 |                 3 |                     288     |                      1.5   | 10.1080/07421222.2018.1440766 |
| Lee I., 2018, BUS HORIZ, V61, P35             |   2018 |          2 |                557 |          6 |                 2 |                     278.5   |                      1     | 10.1016/J.BUSHOR.2017.09.003  |
| Gomber P., 2017, J BUS ECON, V87, P537        |   2017 |          3 |                489 |          1 |                 4 |                     163     |                      1.333 | 10.1007/S11573-017-0852-X     |
| Buchak G., 2018, J FINANC ECON, V130, P453    |   2018 |          4 |                390 |         23 |                 0 |                     195     |                      0     | 10.1016/J.JFINECO.2018.03.011 |
| Gabor D., 2017, NEW POLIT ECON, V22, P423     |   2017 |          5 |                314 |          7 |                 2 |                     104.667 |                      0.667 | 10.1080/13563467.2017.1259298 |



"""

import os
from dataclasses import dataclass

import plotly.express as px

from ..core.read_filtered_database import read_filtered_database
from ..helpers.helper_format_prompt_for_records import helper_format_prompt_for_records
from ..helpers.helper_format_report_for_records import helper_format_report_for_records

MARKER_COLOR = "#7793a5"
MARKER_LINE_COLOR = "#465c6b"


def most_cited_documents(
    #
    # PARAMS:
    metric,
    top_n,
    #
    # CHART PARAMS:
    title=None,
    field_label=None,
    metric_label=None,
    textfont_size=10,
    marker_size=7,
    line_width=1.5,
    yshift=4,
    #
    # DATABASE PARAMS:
    root_dir: str = "./",
    database: str = "main",
    year_filter: tuple = (None, None),
    cited_by_filter: tuple = (None, None),
    **filters,
):
    """
    :meta private:
    """

    # -----------------------------------------------------------------------------------
    #
    def compute_metrics(
        #
        # PARAMS:
        metric,
        top_n,
        #
        # DATABASE PARAMS:
        root_dir,
        database,
        year_filter,
        cited_by_filter,
        **filters,
    ):
        data_frame = read_filtered_database(
            root_dir=root_dir,
            database=database,
            year_filter=year_filter,
            cited_by_filter=cited_by_filter,
            **filters,
        )

        max_year = data_frame.year.dropna().max()

        #
        # Global citations per year
        data_frame["global_citations"] = data_frame.global_citations.astype(int)
        data_frame = data_frame.assign(
            global_citations_per_year=data_frame.global_citations.astype(float) / (max_year - data_frame.year + 1)
        )
        data_frame = data_frame.assign(global_citations_per_year=data_frame.global_citations_per_year.round(3))

        #
        # Global citation score rank
        data_frame = data_frame.sort_values(
            ["global_citations", "local_citations", "year", "authors"],
            ascending=[False, False, True, True],
        )
        data_frame["rank_gcs"] = range(1, len(data_frame) + 1)

        #
        # Local citation score rank
        data_frame = data_frame.sort_values(
            ["local_citations", "global_citations", "year", "authors"],
            ascending=[False, False, True, True],
        )
        data_frame["rank_lcs"] = range(1, len(data_frame) + 1)

        #
        # Local citations per year
        data_frame["local_citations"] = data_frame.local_citations.astype(int)
        data_frame = data_frame.assign(
            local_citations_per_year=data_frame.local_citations.astype(float) / (max_year - data_frame.year + 1)
        )
        data_frame = data_frame.assign(local_citations_per_year=data_frame.local_citations_per_year.round(3))

        #
        # Set the index to the article identifier
        data_frame = data_frame.set_index("article")

        #
        # Selects the top-n documents
        data_frame = data_frame.sort_values([metric], ascending=False).head(top_n)

        return data_frame

    # -----------------------------------------------------------------------------------
    # Create the figure
    #
    def create_fig(
        data_frame,
        metric,
        #
        # CHART PARAMS:
        title,
        field_label,
        metric_label,
        textfont_size,
        marker_size,
        line_width,
        yshift,
    ):
        data_frame = data_frame.copy()

        metric_label = metric.replace("_", " ").upper() if metric_label is None else metric_label

        field_label = metric.replace("_", " ").upper() + " RANKING" if field_label is None else field_label

        data_frame["Rank"] = list(range(1, len(data_frame) + 1))

        fig = px.line(
            data_frame,
            x="Rank",
            y=metric,
            hover_data=data_frame.columns.to_list(),
            markers=True,
        )

        fig.update_traces(
            marker={
                "size": marker_size,
                "line": {"color": MARKER_LINE_COLOR, "width": 1},
            },
            marker_color=MARKER_COLOR,
            line={"color": MARKER_LINE_COLOR, "width": line_width},
        )
        fig.update_layout(
            paper_bgcolor="white",
            plot_bgcolor="white",
            title_text=title if title is not None else "",
        )
        fig.update_yaxes(
            linecolor="gray",
            linewidth=1,
            gridcolor="lightgray",
            griddash="dot",
            title=metric_label,
        )
        fig.update_xaxes(
            linecolor="gray",
            linewidth=1,
            gridcolor="lightgray",
            griddash="dot",
            title=field_label,
        )

        for name, row in data_frame.iterrows():
            fig.add_annotation(
                x=row["Rank"],
                y=row[metric],
                text=name,
                showarrow=False,
                textangle=-90,
                yanchor="bottom",
                font={"size": textfont_size},
                yshift=yshift,
            )

        return fig

    # -----------------------------------------------------------------------------------
    #
    def create_report(
        data_frame,
        metric,
    ):
        report_filename = "most_"
        if metric == "local_citations":
            report_filename += "local_cited_"
        if metric == "global_citations":
            report_filename += "global_cited_"
        if database == "main":
            report_filename += "documents__abstracts.txt"
        if database == "references":
            report_filename += "references__abstracts.txt"

        helper_format_report_for_records(
            root_dir=root_dir,
            target_dir="",
            records=data_frame,
            report_filename=report_filename,
        )

    # -----------------------------------------------------------------------------------
    #
    def create_prompt(
        data_frame,
        metric,
    ):
        prompt_filename = "most_"
        if metric == "local_citations":
            prompt_filename += "local_cited_"
        if metric == "global_citations":
            prompt_filename += "global_cited_"
        if database == "main":
            prompt_filename += "documents__prompt.txt"
        if database == "references":
            prompt_filename += "references__prompt.txt"

        main_text = (
            "You are researcher writing a scientific paper. "
            "Your task is to write a short summary for each of the following "
            "paragraphs. Summarize each one the paragraphs below, delimited by "
            "triple backticks, in at most 30 words, focusing on the main "
            "contribution described in the paragraph. "
        )

        data_frame = data_frame.copy()
        data_frame["article"] = data_frame.index
        text = helper_format_prompt_for_records(
            main_text,
            main_text,
            data_frame,
            weight=None,
        )

        file_name = os.path.join(root_dir, "reports", prompt_filename)
        with open(file_name, "w", encoding="utf-8") as file:
            print(text, file=file)

        print(f"--INFO-- The file '{file_name}' was created.")

    #
    #
    # MAIN CODE:
    #
    #
    data_frame = compute_metrics(
        #
        # PARAMS:
        metric=metric,
        top_n=top_n,
        #
        # DATABASE PARAMS:
        root_dir=root_dir,
        database=database,
        year_filter=year_filter,
        cited_by_filter=cited_by_filter,
        **filters,
    )

    #
    # Abstracts Report:
    create_report(
        data_frame=data_frame,
        metric=metric,
    )

    #
    # Creates ChatGPT Prompt
    create_prompt(
        data_frame=data_frame,
        metric=metric,
    )

    #
    # Selects the columns
    data_frame = data_frame[
        [
            "year",
            "rank_gcs",
            "global_citations",
            "rank_lcs",
            "local_citations",
            "global_citations_per_year",
            "local_citations_per_year",
            "doi",
        ]
    ]

    fig = create_fig(
        data_frame=data_frame,
        metric=metric,
        #
        # CHART PARAMS:
        title=title,
        field_label=field_label,
        metric_label=metric_label,
        textfont_size=textfont_size,
        marker_size=marker_size,
        line_width=line_width,
        yshift=yshift,
    )

    @dataclass
    class Results:
        df_ = data_frame
        fig_ = fig

    return Results()
