# flake8: noqa
# pylint: disable=line-too-long
"""
.. _item_associations:

Item Associations
===============================================================================

Computes the associations of a item in a co-occurrence matrix.

* Preparation

>>> import techminer2plus as tm2p
>>> root_dir = "data/regtech/"

* Object oriented interface

>>> associations = (
...     tm2p.records(root_dir=root_dir)
...     .co_occurrence_matrix(
...         columns='author_keywords',
...         col_top_n=20,
...     )
...     .item_associations("REGTECH")
... )
>>> associations
ItemAssociations(item='REGTECH',
    cooc_matrix='CoocMatrix(columns='author_keywords',
    rows='author_keywords', dims=(20,  20))')

* Functional interface

>>> cooc_matrix = tm2p.co_occurrence_matrix(
...    columns='author_keywords',
...    col_top_n=20,
...    root_dir=root_dir,
... )
>>> associations = tm2p.item_associations("REGTECH", cooc_matrix)
>>> associations
ItemAssociations(item='REGTECH',
    cooc_matrix='CoocMatrix(columns='author_keywords',
    rows='author_keywords', dims=(20,  20))')

* Results

>>> associations.df_
                                REGTECH 28:329
author_keywords                               
FINTECH 12:249                              12
COMPLIANCE 07:030                            7
REGULATION 05:164                            4
FINANCIAL_SERVICES 04:168                    3
SUPTECH 03:004                               3
REGULATORY_TECHNOLOGY 07:037                 2
FINANCIAL_REGULATION 04:035                  2
ARTIFICIAL_INTELLIGENCE 04:023               2
RISK_MANAGEMENT 03:014                       2
BLOCKCHAIN 03:005                            2
SEMANTIC_TECHNOLOGIES 02:041                 2
DATA_PROTECTION 02:027                       2
SMART_CONTRACTS 02:022                       2
CHARITYTECH 02:017                           2
ENGLISH_LAW 02:017                           2
ACCOUNTABILITY 02:014                        2
DATA_PROTECTION_OFFICER 02:014               2
ANTI_MONEY_LAUNDERING 05:034                 1
INNOVATION 03:012                            1


>>> print(associations.prompt_)
Your task is to generate a short analysis of a table for a research paper. \\
Summarize the table below, delimited by triple backticks, in one unique \\
paragraph with at most 30 words. The table contains the values of co- \\
occurrence (OCC) of the 'author_keywords' with the 'REGTECH' field in a \\
bibliographic dataset. Identify any notable patterns, trends, or outliers \\
in the data, and discuss their implications for the research field. Be sure \\
to provide a concise summary of your findings.
<BLANKLINE>
Table:
```
| author_keywords                |   REGTECH 28:329 |
|:-------------------------------|-----------------:|
| FINTECH 12:249                 |               12 |
| COMPLIANCE 07:030              |                7 |
| REGULATION 05:164              |                4 |
| FINANCIAL_SERVICES 04:168      |                3 |
| SUPTECH 03:004                 |                3 |
| REGULATORY_TECHNOLOGY 07:037   |                2 |
| FINANCIAL_REGULATION 04:035    |                2 |
| ARTIFICIAL_INTELLIGENCE 04:023 |                2 |
| RISK_MANAGEMENT 03:014         |                2 |
| BLOCKCHAIN 03:005              |                2 |
| SEMANTIC_TECHNOLOGIES 02:041   |                2 |
| DATA_PROTECTION 02:027         |                2 |
| SMART_CONTRACTS 02:022         |                2 |
| CHARITYTECH 02:017             |                2 |
| ENGLISH_LAW 02:017             |                2 |
| ACCOUNTABILITY 02:014          |                2 |
| DATA_PROTECTION_OFFICER 02:014 |                2 |
| ANTI_MONEY_LAUNDERING 05:034   |                1 |
| INNOVATION 03:012              |                1 |
```
<BLANKLINE>


"""
import textwrap
from dataclasses import dataclass

import pandas as pd

from ._chatbot import format_chatbot_prompt_for_df
from .associations_plot import associations_plot
from .radial_diagram import radial_diagram


@dataclass
class ItemAssociations:
    """Item associations."""

    #
    # PARAMS:
    item: str
    cooc_matrix: pd.DataFrame
    #
    # RESULTS:
    df_: pd.DataFrame
    prompt_: str
    item_name_: str
    #
    # COMPATIBILITY:
    field: str = ""
    metric: str = "OCC"  # compatibility for plotting

    def __repr__(self):
        text = "ItemAssociations("
        text += f"item='{self.item}'"
        text += f", cooc_matrix='{self.cooc_matrix.__repr__().replace('    ', '   ').replace('   ', '  ').replace('  ', ' ')}'"
        text += ")"
        text = textwrap.fill(text, width=75, subsequent_indent="    ")
        return text

    # pylint: disable=too-many-arguments
    def radial_diagram(
        self,
        #
        # Figure params:
        n_labels=None,
        nx_k=None,
        nx_iterations=30,
        nx_random_state=0,
        node_size_min=30,
        node_size_max=70,
        textfont_size_min=10,
        textfont_size_max=20,
        xaxes_range=None,
        yaxes_range=None,
        show_axes=False,
    ):
        """Radial diagram of the item associations."""
        return radial_diagram(
            item_associations=self,
            #
            # Figure params:
            n_labels=n_labels,
            nx_k=nx_k,
            nx_iterations=nx_iterations,
            nx_random_state=nx_random_state,
            node_size_min=node_size_min,
            node_size_max=node_size_max,
            textfont_size_min=textfont_size_min,
            textfont_size_max=textfont_size_max,
            xaxes_range=xaxes_range,
            yaxes_range=yaxes_range,
            show_axes=show_axes,
        )

    def associations_plot(
        self,
        title=None,
        field_label=None,
        metric_label=None,
    ):
        """Associations plot"""

        return associations_plot(
            item_associations=self,
            title=title,
            field_label=field_label,
            metric_label=metric_label,
        )


# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
def item_associations(
    item,
    cooc_matrix,
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
        series = series[series > 0]
        series.index.name = obj.rows
        return series

    def create_prompt(field, item, table):
        main_text = (
            "Your task is to generate a short analysis of a table for a "
            "research paper. Summarize the table below, delimited by triple "
            "backticks, in one unique paragraph with at most 30 words. The "
            "table contains the values of co-occurrence (OCC) of the "
            f"'{item}' with the '{field}' field in a bibliographic dataset. "
            "Identify any notable patterns, trends, or outliers in the data, "
            "and discuss their implications for the research field. Be sure "
            "to provide a concise summary of your findings."
        )
        table_text = table.to_markdown()
        return format_chatbot_prompt_for_df(main_text, table_text)

    #
    # Main code:
    #
    pos, name = extract_item_position_and_name(cooc_matrix.df_.columns, item)
    series = extract_item_column_from_coc_matrix(cooc_matrix, pos, name)
    frame = series.to_frame()
    frame["OCC"] = [text.split(" ")[-1].split(":")[0] for text in frame.index]
    frame["GC"] = [text.split(" ")[-1].split(":")[-1] for text in frame.index]
    frame["NAME"] = [" ".join(text.split(" ")[:-1]) for text in frame.index]
    frame = frame.sort_values(
        by=[name, "OCC", "GC", "NAME"], ascending=[False, False, False, True]
    )
    series = frame[[name]]
    prompt = create_prompt(item, cooc_matrix.rows, series)

    return ItemAssociations(
        item=item,
        cooc_matrix=cooc_matrix,
        df_=series,
        prompt_=prompt,
        item_name_=name,
        field=cooc_matrix.df_.index.name,
    )
