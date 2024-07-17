# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
"""
Item Associations
===============================================================================


>>> from techminer2.analyze.associations import item_associations
>>> associations = item_associations(
...     #
...     # FUNCTION PARAMS:
...     item='FINTECH',
...     #
...     # CO-OCC PARAMS:
...     columns='author_keywords',
...     rows=None,
...     #
...     # COLUMN PARAMS:
...     col_top_n=20,
...     col_occ_range=(None, None),
...     col_gc_range=(None, None),
...     col_custom_items=None,
...     #
...     # ROW PARAMS:
...     row_top_n=None,
...     row_occ_range=(None, None),
...     row_gc_range=(None, None),
...     row_custom_items=None,
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
>>> associations.df_.head()
                             FINTECH 31:5168
author_keywords                             
INNOVATION 07:0911                         5
FINANCIAL_SERVICES 04:0667                 3
BUSINESS 03:0896                           3
SHADOW_BANKING 03:0643                     3
FINANCIAL_INCLUSION 03:0590                3


>>> associations.fig_.write_html("sphinx/_static/analyze/associations/item_associations_chart.html")

.. raw:: html

    <iframe src="../../../../_static/analyze/associations/item_associations_chart.html" 
    height="600px" width="100%" frameBorder="0"></iframe>

    
>>> print(associations.prompt_) # doctest: +ELLIPSIS
Your task is ...


"""
from dataclasses import dataclass

import plotly.express as px

from ...co_occurrence_matrix.compute_co_occurrence_matrix import compute_co_occurrence_matrix
from ...helpers.helper_format_prompt_for_dataframes import helper_format_prompt_for_dataframes

MARKER_COLOR = "#7793a5"
MARKER_LINE_COLOR = "#465c6b"


def item_associations(
    #
    # FUNCTION PARAMS:
    item,
    #
    # CO-OCC PARAMS:
    columns,
    rows=None,
    #
    # COLUMN PARAMS:
    col_top_n=None,
    col_occ_range=(None, None),
    col_gc_range=(None, None),
    col_custom_items=None,
    #
    # ROW PARAMS:
    row_top_n=None,
    row_occ_range=(None, None),
    row_gc_range=(None, None),
    row_custom_items=None,
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
    root_dir="./",
    database="main",
    year_filter=(None, None),
    cited_by_filter=(None, None),
    **filters,
):
    """association plot

    :meta private:
    """
    data_frame = __table(
        #
        # FUNCTION PARAMS:
        item=item,
        #
        # CO-OCC PARAMS:
        columns=columns,
        rows=rows,
        #
        # COLUMN PARAMS:
        col_top_n=col_top_n,
        col_occ_range=col_occ_range,
        col_gc_range=col_gc_range,
        col_custom_items=col_custom_items,
        #
        # ROW PARAMS:
        row_top_n=row_top_n,
        row_occ_range=row_occ_range,
        row_gc_range=row_gc_range,
        row_custom_items=row_custom_items,
        #
        # DATABASE PARAMS:
        root_dir=root_dir,
        database=database,
        year_filter=year_filter,
        cited_by_filter=cited_by_filter,
        **filters,
    )

    prompt = __prompt(data_frame, columns, item)

    chart = __chart(
        data_frame,
        #
        # CO-OCC PARAMS:
        columns=columns,
        rows=rows,
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
        prompt_ = prompt
        fig_ = chart

    return Results()


def __prompt(data_frame, columns, item):
    main_text = (
        "Your task is to generate a short analysis of a table for a "
        "research paper. Summarize the table below, delimited by triple "
        "backticks, in one unique paragraph with at most 30 words. The "
        "table contains the values of co-occurrence (OCC) of the "
        f"'{item}' with the '{columns}' field in a bibliographic dataset. "
        "Identify any notable patterns, trends, or outliers in the data, "
        "and discuss their implications for the research field. Be sure "
        "to provide a concise summary of your findings."
    )
    table_text = data_frame.to_markdown()
    return helper_format_prompt_for_dataframes(main_text, table_text)


def __table(
    #
    # FUNCTION PARAMS:
    item,
    #
    # CO-OCC PARAMS:
    columns,
    rows,
    #
    # COLUMN PARAMS:
    col_top_n,
    col_occ_range,
    col_gc_range,
    col_custom_items,
    #
    # ROW PARAMS:
    row_top_n,
    row_occ_range,
    row_gc_range,
    row_custom_items,
    #
    # DATABASE PARAMS:
    root_dir,
    database,
    year_filter,
    cited_by_filter,
    **filters,
):
    """Computes the associations of a item in a co-occurrence matrix."""

    def extract_item_position_and_name(candidate_items, item):
        """Obtains the positions of topics in a list."""

        org_candidate_items = candidate_items[:]
        candidate_items = [col.split(" ")[:-1] for col in candidate_items]
        candidate_items = [" ".join(col) for col in candidate_items]
        pos = candidate_items.index(item)
        name = org_candidate_items[pos]
        return pos, name

    def extract_item_column_from_coc_matrix(obj, pos, name):
        matrix = obj.df_.copy()
        series = matrix.iloc[:, pos]
        series = series.drop(labels=[name], axis=0, errors="ignore")
        # series = series[series > 0]
        series.index.name = obj.df_.index.name
        return series

    #
    #
    # MAIN CODE:
    #
    #
    cooc_matrix = compute_co_occurrence_matrix(
        #
        # FUNCTION PARAMS:
        columns=columns,
        rows=rows,
        #
        # COLUMN PARAMS:
        col_top_n=col_top_n,
        col_occ_range=col_occ_range,
        col_gc_range=col_gc_range,
        col_custom_items=col_custom_items,
        #
        # ROW PARAMS:
        row_top_n=row_top_n,
        row_occ_range=row_occ_range,
        row_gc_range=row_gc_range,
        row_custom_items=row_custom_items,
        #
        # DATABASE PARAMS:
        root_dir=root_dir,
        database=database,
        year_filter=year_filter,
        cited_by_filter=cited_by_filter,
        **filters,
    )

    pos, name = extract_item_position_and_name(cooc_matrix.df_.columns, item)
    series = extract_item_column_from_coc_matrix(cooc_matrix, pos, name)
    frame = series.to_frame()
    frame["OCC"] = [text.split(" ")[-1].split(":")[0] for text in frame.index]
    frame["GC"] = [text.split(" ")[-1].split(":")[-1] for text in frame.index]
    frame["NAME"] = [" ".join(text.split(" ")[:-1]) for text in frame.index]
    frame = frame.sort_values(by=[name, "OCC", "GC", "NAME"], ascending=[False, False, False, True])
    series = frame[[name]]

    return series


def __chart(
    data_frame,
    #
    # CO-OCC PARAMS:
    columns,
    rows=None,
    #
    # CHART PARAMS:
    title=None,
    field_label=None,
    metric_label=None,
    textfont_size=10,
    marker_size=7,
    line_width=1.5,
    yshift=4,
):
    """association plot"""

    if title is None:
        item_name = data_frame.iloc[:, 0].name
        item_name = " ".join(item_name.split(" ")[:-1])
        series_name = data_frame.iloc[:, 0].index.name
        title = f"Co-occurrence with of '{item_name}' with '{series_name}'"

    data_frame = data_frame.copy()
    data_frame.columns = ["OCC"]

    if rows is None:
        rows = columns

    metric_label = "OCC" if metric_label is None else metric_label

    field_label = rows.replace("_", " ").upper() + " RANKING" if field_label is None else field_label

    table = data_frame.copy()
    table["Rank"] = list(range(1, len(table) + 1))

    fig = px.line(
        table,
        x="Rank",
        y="OCC",
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

    for name, row in table.iterrows():
        fig.add_annotation(
            x=row["Rank"],
            y=row["OCC"],
            text=name,
            showarrow=False,
            textangle=-90,
            yanchor="bottom",
            font={"size": textfont_size},
            yshift=yshift,
        )

    return fig
