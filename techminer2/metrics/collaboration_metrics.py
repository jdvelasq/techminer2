# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
# pylint: disable=too-many-statements
"""
Collaboration Metrics
===============================================================================

>>> from techminer2.metrics.collaboration_metrics import collaboration_metrics
>>> metrics = collaboration_metrics(
...     #
...     # PARAMS:
...     field="countries",
...     #
...     # ITEM FILTERS:
...     top_n=20,
...     occ_range=(None, None),
...     gc_range=(None, None),
...     custom_terms=None,
...     #
...     # DATABASE PARAMS:
...     root_dir="example/", 
...     database="main",
...     year_filter=(None, None),
...     cited_by_filter=(None, None),
... )
>>> metrics.fig_.write_html("sphinx/_static/metrics/collaboration_metrics.html")

.. raw:: html

    <iframe src="../_static/metrics/collaboration_metrics.html" 
    height="600px" width="100%" frameBorder="0"></iframe>


>>> print(metrics.df_.head().to_markdown())
| countries     |   OCC |   global_citations |   local_citations |   single_publication |   multiple_publication |   mp_ratio |
|:--------------|------:|-------------------:|------------------:|---------------------:|-----------------------:|-----------:|
| United States |    16 |               3189 |                 8 |                    8 |                      8 |       0.5  |
| China         |     8 |               1085 |                 4 |                    3 |                      5 |       0.62 |
| Germany       |     7 |               1814 |                11 |                    4 |                      3 |       0.43 |
| South Korea   |     6 |               1192 |                 8 |                    4 |                      2 |       0.33 |
| Australia     |     5 |                783 |                 3 |                    1 |                      4 |       0.8  |

"""
from dataclasses import dataclass

import numpy as np
import plotly.express as px

from .._core.metrics.extract_top_n_terms_by_metric import extract_top_n_terms_by_metric
from .._core.read_filtered_database import read_filtered_database
from ..helpers.helper_format_prompt_for_dataframes import helper_format_prompt_for_dataframes


def collaboration_metrics(
    #
    # PARAMS:
    field,
    #
    # ITEM FILTERS:
    top_n,
    occ_range,
    gc_range,
    custom_terms,
    #
    # DATABASE PARAMS:
    root_dir,
    database,
    year_filter,
    cited_by_filter,
    **filters,
):
    """
    :meta private:
    """

    #
    # Computes the number of single and multiple publications
    # and the ratio between them.
    #
    def compute_collaboration_metrics(
        #
        # PARAMS:
        field,
        custom_terms,
        #
        # DATABASE PARAMS:
        root_dir,
        database,
        year_filter,
        cited_by_filter,
        **filters,
    ):
        #
        # Read documents from the database
        records = read_filtered_database(
            #
            # DATABASE PARAMS:
            root_dir=root_dir,
            database=database,
            year_filter=year_filter,
            cited_by_filter=cited_by_filter,
            sort_by=None,
            **filters,
        )

        #
        # Add a column to represent the number of occurrences of a document
        records = records.assign(OCC=1)

        #
        # Add columns to represent single and multiple publications for a document
        records["single_publication"] = records[field].map(lambda x: 1 if isinstance(x, str) and len(x.split(";")) == 1 else 0)
        records["multiple_publication"] = records[field].map(lambda x: 1 if isinstance(x, str) and len(x.split(";")) > 1 else 0)

        #
        # Split multi-topic documents into individual documents with one topic each
        exploded = records[
            [
                field,
                "OCC",
                "global_citations",
                "local_citations",
                "single_publication",
                "multiple_publication",
                "article",
            ]
        ].copy()
        exploded[field] = exploded[field].str.split(";")
        exploded = exploded.explode(field)
        exploded[field] = exploded[field].str.strip()

        #
        # Compute collaboration indicators for each topic
        metrics = exploded.groupby(field, as_index=False).agg(
            {
                "OCC": np.sum,
                "global_citations": np.sum,
                "local_citations": np.sum,
                "single_publication": np.sum,
                "multiple_publication": np.sum,
            }
        )

        #
        # Compute the multiple publication ratio for each topic
        metrics["mp_ratio"] = metrics["multiple_publication"] / metrics["OCC"]
        metrics["mp_ratio"] = metrics["mp_ratio"].round(2)

        #
        # Sort the topics by number of occurrences, global citations, and local
        # citations
        metrics = metrics.sort_values(
            by=["OCC", "global_citations", "local_citations"],
            ascending=[False, False, False],
        )

        #
        # Set the index to the criterion column
        metrics = metrics.set_index(field)

        #
        #  Filter the metrics
        if custom_terms is None:
            custom_terms = extract_top_n_terms_by_metric(
                indicators=metrics,
                metric="OCC",
                top_n=top_n,
                occ_range=occ_range,
                gc_range=gc_range,
            )

        metrics = metrics[metrics.index.isin(custom_terms)]

        return metrics

    #
    # Chat GPT prompt
    #
    def create_prompt(
        field,
        metrics,
    ):
        main_text = (
            f"Your task is to generate an analysis about the collaboration between {field} "
            "according to the data in a scientific bibliography database. Summarize the table "
            "below, delimited by triple backticks, where the column 'single publication' is the "
            f"number of documents in which all the authors belongs to the same {field}, and the  "
            "column 'multiple publication' is the number of documents in which the authors are "
            f"from different {field}. The column 'mcp ratio' is the ratio between the columns "
            "'multiple publication' and 'OCC'. The higher the ratio, the higher "
            f"the collaboration between {field}. Use the information in the table to draw "
            f"conclusions about the level of collaboration between {field} in the dataset. In "
            "your analysis, be sure to describe in a clear and concise way, any findings or any "
            "patterns you observe, and identify any outliers or anomalies in the data. Limit your "
            "description to one paragraph with no more than 250 words."
        )
        return helper_format_prompt_for_dataframes(main_text, metrics.to_markdown())

    #
    # Figure
    #
    def create_fig(field, metrics):
        #
        metrics = metrics.copy()
        metrics = metrics.reset_index()

        metrics = metrics.melt(
            id_vars=field,
            value_vars=["single_publication", "multiple_publication"],
        )
        metrics = metrics.rename(columns={"variable": "publication", "value": "Num Documents"})
        metrics.publication = metrics.publication.map(lambda x: x.replace("_", " ").title())
        metrics[field] = metrics[field].map(lambda x: x.title())

        fig = px.bar(
            metrics,
            x="Num Documents",
            y=field,
            color="publication",
            title="Corresponding Author's " + field.title(),
            hover_data=["Num Documents"],
            orientation="h",
            color_discrete_map={
                "Single Publication": "#7793a5",
                "Multiple Publication": "#465c6b",
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

    #
    # MAIN CODE:
    #
    metrics = compute_collaboration_metrics(
        #
        # PARAMS:
        field=field,
        custom_terms=custom_terms,
        #
        # DATABASE PARAMS:
        root_dir=root_dir,
        database=database,
        year_filter=year_filter,
        cited_by_filter=cited_by_filter,
        **filters,
    )
    prompt = create_prompt(
        field=field,
        metrics=metrics,
    )
    fig = create_fig(field, metrics)

    @dataclass
    class Results:
        df_ = metrics
        prompt_ = prompt
        fig_ = fig

    return Results()
