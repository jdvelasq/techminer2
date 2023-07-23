# flake8: noqa
# pylint: disable=line-too-long
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
# pylint: disable=missing-docstring
"""Main Information Dashboard."""

import plotly.graph_objects as go
from plotly.subplots import make_subplots


def main_metrics_dashboard(
    data_frame,
):
    def add_text_trace(fig, category, caption, row, col):
        text = (
            f'<span style="font-size: 8px;">{caption}</span><br>'
            f'<br><span style="font-size: 20px;">'
            f"{data_frame.loc[(category, caption)].values[0]}</span>"
        )

        fig.add_trace(
            go.Scatter(
                x=[0.5],
                y=[0.5],
                text=[text],
                mode="text",
            ),
            row=row,
            col=col,
        )
        fig.update_xaxes(visible=False, row=row, col=col)
        fig.update_yaxes(visible=False, row=row, col=col)

    fig = make_subplots(rows=7, cols=3)

    add_text_trace(fig, "GENERAL", "Timespan", 1, 1)
    add_text_trace(fig, "GENERAL", "Sources", 1, 2)
    add_text_trace(fig, "GENERAL", "Documents", 1, 3)

    add_text_trace(fig, "GENERAL", "Annual growth rate %", 2, 1)
    add_text_trace(fig, "AUTHORS", "Authors", 2, 2)
    add_text_trace(fig, "AUTHORS", "Authors of single-authored documents", 2, 3)

    add_text_trace(fig, "AUTHORS", "International co-authorship %", 3, 1)
    add_text_trace(fig, "AUTHORS", "Co-authors per document", 3, 2)
    add_text_trace(fig, "GENERAL", "References", 3, 3)

    add_text_trace(fig, "KEYWORDS", "Raw author keywords", 4, 1)
    add_text_trace(fig, "KEYWORDS", "Cleaned author keywords", 4, 2)
    add_text_trace(fig, "KEYWORDS", "Raw index keywords", 4, 3)

    add_text_trace(fig, "KEYWORDS", "Raw keywords", 5, 1)
    add_text_trace(fig, "KEYWORDS", "Cleaned keywords", 5, 2)
    add_text_trace(fig, "NLP PHRASES", "Raw NLP phrases", 5, 3)

    add_text_trace(
        fig,
        "NLP PHRASES",
        "Cleaned NLP phrases",
        6,
        1,
    )

    add_text_trace(
        fig,
        "DESCRIPTORS",
        "Raw descriptors",
        6,
        2,
    )

    add_text_trace(
        fig,
        "DESCRIPTORS",
        "Cleaned descriptors",
        6,
        3,
    )

    add_text_trace(fig, "GENERAL", "Document average age", 7, 1)
    add_text_trace(fig, "GENERAL", "Average citations per document", 7, 2)

    fig.update_layout(showlegend=False)
    fig.update_layout(title="Main Information")
    fig.update_layout(height=800)

    return fig
