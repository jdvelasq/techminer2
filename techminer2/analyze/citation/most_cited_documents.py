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



>>> from techminer2.analyze.citation import most_cited_documents
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
--INFO-- The file 'data/regtech/reports/most_global_cited_documents__abstracts.txt' was created.
--INFO-- The file 'data/regtech/reports/most_global_cited_documents__prompt.txt' was created.

>>> documents.fig_.write_html("sphinx/_static/analyze/citation/most_global_cited_documents.html")

.. raw:: html

    <iframe src="../../../../_static/analyze/citation/most_global_cited_documents.html" 
    height="600px" width="100%" frameBorder="0"></iframe>

    
>>> print(documents.df_.to_markdown())
| article                                                       |   year |   rank_gcs |   global_citations |   rank_lcs |   local_citations |   global_citations_per_year |   local_citations_per_year | doi                                |
|:--------------------------------------------------------------|-------:|-----------:|-------------------:|-----------:|------------------:|----------------------------:|---------------------------:|:-----------------------------------|
| Anagnostopoulos I, 2018, J ECON BUS, V100, P7                 |   2018 |          1 |                153 |          1 |                17 |                      25.5   |                      2.833 | 10.1016/J.JECONBUS.2018.07.003     |
| Arner DW, 2017, NORTHWEST J INTL LAW BUS, V37, P373           |   2017 |          2 |                150 |          2 |                16 |                      21.429 |                      2.286 | nan                                |
| Butler T, 2019, PALGRAVE STUD DIGIT BUS ENABL, P85            |   2019 |          3 |                 33 |          3 |                14 |                       6.6   |                      2.8   | 10.1007/978-3-030-02330-0_6        |
| Baxter LG, 2016, DUKE LAW J, V66, P567                        |   2016 |          4 |                 30 |          4 |                 8 |                       3.75  |                      1     | nan                                |
| Buckley RP, 2020, J BANK REGUL, V21, P26                      |   2020 |          5 |                 24 |          6 |                 5 |                       6     |                      1.25  | 10.1057/S41261-019-00104-1         |
| Kavassalis P, 2018, J RISK FINANC, V19, P39                   |   2018 |          6 |                 21 |          5 |                 8 |                       3.5   |                      1.333 | 10.1108/JRF-07-2017-0111           |
| Singh C, 2020, J MONEY LAUND CONTROL, V24, P464               |   2020 |          7 |                 14 |          9 |                 3 |                       3.5   |                      0.75  | 10.1108/JMLC-09-2020-0100          |
| Muganyi T, 2022, FINANCIAL INNOV, V8                          |   2022 |          8 |                 13 |         19 |                 1 |                       6.5   |                      0.5   | 10.1186/S40854-021-00313-6         |
| Ryan P, 2020, ICEIS - PROC INT CONF ENTERP , V2, P787         |   2020 |          9 |                 12 |         10 |                 3 |                       3     |                      0.75  | nan                                |
| von Solms J, 2021, J BANK REGUL, V22, P152                    |   2021 |         10 |                 11 |          8 |                 4 |                       3.667 |                      1.333 | 10.1057/S41261-020-00134-0         |
| Arner DW, 2017, HANDBBLOCKCHAIN, DIGIT FINANC, P359           |   2017 |         11 |                 11 |         11 |                 3 |                       1.571 |                      0.429 | 10.1016/B978-0-12-810441-5.00016-6 |
| Turki M, 2020, HELIYON, V6                                    |   2020 |         12 |                 11 |         16 |                 2 |                       2.75  |                      0.5   | 10.1016/J.HELIYON.2020.E04949      |
| Kurum E, 2020, J FINANC CRIME                                 |   2020 |         13 |                 10 |         12 |                 3 |                       2.5   |                      0.75  | 10.1108/JFC-04-2020-0051           |
| Butler T, 2018, J RISK MANG FINANCIAL INST, V11, P19          |   2018 |         14 |                  8 |          7 |                 5 |                       1.333 |                      0.833 | nan                                |
| Turki M, 2021, ADV INTELL SYS COMPUT, V1141, P349             |   2021 |         15 |                  7 |         20 |                 1 |                       2.333 |                      0.333 | 10.1007/978-981-15-3383-9_32       |
| Becker M, 2020, INTELL SYST ACCOUNT FINANCE M, V27, P161      |   2020 |         17 |                  5 |         22 |                 1 |                       1.25  |                      0.25  | 10.1002/ISAF.1479                  |
| Das SR, 2019, J FINANCIAL DATA SCI, V1, P8                    |   2019 |         16 |                  5 |         21 |                 1 |                       1     |                      0.2   | 10.3905/JFDS.2019.1.2.008          |
| Waye V, 2020, ADELAIDE LAW REV, V40, P363                     |   2020 |         18 |                  5 |         23 |                 1 |                       1.25  |                      0.25  | nan                                |
| Pantielieieva N, 2020, LECTURE NOTES DATA ENG COMMUN, V42, P1 |   2020 |         20 |                  4 |         28 |                 0 |                       1     |                      0     | 10.1007/978-3-030-35649-1_1        |
| Brand V, 2020, UNIV NEW SOUTH WALES LAW J, V43, P801          |   2020 |         19 |                  4 |         13 |                 3 |                       1     |                      0.75  | nan                                |



"""

import os
from dataclasses import dataclass

import plotly.express as px

from ..._read_records import read_records
from ...format_prompt_for_records import format_prompt_for_records
from ...format_report_for_records import format_report_for_records

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
        data_frame = read_records(
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
            global_citations_per_year=data_frame.global_citations.astype(float)
            / (max_year - data_frame.year + 1)
        )
        data_frame = data_frame.assign(
            global_citations_per_year=data_frame.global_citations_per_year.round(3)
        )

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
            local_citations_per_year=data_frame.local_citations.astype(float)
            / (max_year - data_frame.year + 1)
        )
        data_frame = data_frame.assign(
            local_citations_per_year=data_frame.local_citations_per_year.round(3)
        )

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

        field_label = (
            metric.replace("_", " ").upper() + " RANKING" if field_label is None else field_label
        )

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

        format_report_for_records(
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
        text = format_prompt_for_records(
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
