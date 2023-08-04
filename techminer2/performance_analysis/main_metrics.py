# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
"""
.. _performance_analysis.main_metrics:

Main Metrics
===============================================================================

>>> from techminer2.performance_analysis import main_metrics
>>> info = main_metrics(
...     #
...     # DATABASE PARAMS:
...     root_dir="data/regtech/",
...     database="main",
...     year_filter=(None, None),
...     cited_by_filter=(None, None),
... )
>>> info.df_
                                                            Value
Category       Item                                              
GENERAL        Timespan                                 2016:2023
               Documents                                       52
               Annual growth rate %                         63.87
               Document average age                          2.77
               References                                     932
               Average citations per document               10.83
               Average citations per document per year       1.35
               Average references per document              20.71
               Sources                                         46
               Average documents per source                  1.13
DOCUMENT TYPES article                                         31
               book                                             1
               book_chapter                                     9
               conference_paper                                11
AUTHORS        Authors                                        102
               Authors of single-authored documents            19
               Single-authored documents                       19
               Multi-authored documents                        33
               Authors per document                          2.29
               Co-authors per document                       3.03
               International co-authorship %                23.08
               Author appearances                             119
               Documents per author                          0.44
               Collaboration index                            1.0
               Organizations                                   81
               Organizations (1st author)                       0
               Countries                                       29
               Countries (1st author)                           0
KEYWORDS       Raw author keywords                            148
               Cleaned author keywords                        143
               Raw index keywords                             155
               Cleaned index keywords                         149
               Raw keywords                                   273
               Cleaned keywords                               252
NLP PHRASES    Raw title NLP phrases                           40
               Cleaned title NLP phrases                       40
               Raw abstract NLP phrases                       157
               Cleaned abstract NLP phrases                   149
               Raw NLP phrases                                167
               Cleaned NLP phrases                            158
DESCRIPTORS    Raw descriptors                                373
               Cleaned descriptors                            338

               
>>> info.fig_.write_html("sphinx/_static/performance_analysis/main_metrics_dashboard.html")

.. raw:: html

    <iframe src="../../../../_static/performance_analysis/main_metrics_dashboard.html"
    height="800px" width="100%" frameBorder="0"></iframe>

>>> print(info.prompt_)
Your task is to generate a short summary for a research paper of a table \\
with record and field statistics for a dataset of scientific publications. \\
The table below, delimited by triple backticks, provides data on the main \\
characteristics of the records and fields of the bibliographic dataset. Use \\
the the information in the table to draw conclusions. Limit your \\
description to one paragraph in at most 100 words.
<BLANKLINE>
Table:
```
|                                                        | Value     |
|:-------------------------------------------------------|:----------|
| ('GENERAL', 'Timespan')                                | 2016:2023 |
| ('GENERAL', 'Documents')                               | 52        |
| ('GENERAL', 'Annual growth rate %')                    | 63.87     |
| ('GENERAL', 'Document average age')                    | 2.77      |
| ('GENERAL', 'References')                              | 932       |
| ('GENERAL', 'Average citations per document')          | 10.83     |
| ('GENERAL', 'Average citations per document per year') | 1.35      |
| ('GENERAL', 'Average references per document')         | 20.71     |
| ('GENERAL', 'Sources')                                 | 46        |
| ('GENERAL', 'Average documents per source')            | 1.13      |
| ('DOCUMENT TYPES', 'article')                          | 31        |
| ('DOCUMENT TYPES', 'book')                             | 1         |
| ('DOCUMENT TYPES', 'book_chapter')                     | 9         |
| ('DOCUMENT TYPES', 'conference_paper')                 | 11        |
| ('AUTHORS', 'Authors')                                 | 102       |
| ('AUTHORS', 'Authors of single-authored documents')    | 19        |
| ('AUTHORS', 'Single-authored documents')               | 19        |
| ('AUTHORS', 'Multi-authored documents')                | 33        |
| ('AUTHORS', 'Authors per document')                    | 2.29      |
| ('AUTHORS', 'Co-authors per document')                 | 3.03      |
| ('AUTHORS', 'International co-authorship %')           | 23.08     |
| ('AUTHORS', 'Author appearances')                      | 119       |
| ('AUTHORS', 'Documents per author')                    | 0.44      |
| ('AUTHORS', 'Collaboration index')                     | 1.0       |
| ('AUTHORS', 'Organizations')                           | 81        |
| ('AUTHORS', 'Organizations (1st author)')              | 0         |
| ('AUTHORS', 'Countries')                               | 29        |
| ('AUTHORS', 'Countries (1st author)')                  | 0         |
| ('KEYWORDS', 'Raw author keywords')                    | 148       |
| ('KEYWORDS', 'Cleaned author keywords')                | 143       |
| ('KEYWORDS', 'Raw index keywords')                     | 155       |
| ('KEYWORDS', 'Cleaned index keywords')                 | 149       |
| ('KEYWORDS', 'Raw keywords')                           | 273       |
| ('KEYWORDS', 'Cleaned keywords')                       | 252       |
| ('NLP PHRASES', 'Raw title NLP phrases')               | 40        |
| ('NLP PHRASES', 'Cleaned title NLP phrases')           | 40        |
| ('NLP PHRASES', 'Raw abstract NLP phrases')            | 157       |
| ('NLP PHRASES', 'Cleaned abstract NLP phrases')        | 149       |
| ('NLP PHRASES', 'Raw NLP phrases')                     | 167       |
| ('NLP PHRASES', 'Cleaned NLP phrases')                 | 158       |
| ('DESCRIPTORS', 'Raw descriptors')                     | 373       |
| ('DESCRIPTORS', 'Cleaned descriptors')                 | 338       |
```
<BLANKLINE>

    


"""
from dataclasses import dataclass

import pandas as pd
import plotly.graph_objects as go

from ._main_metrics_dashboard import main_metrics_dashboard
from ._main_metrics_prompt import main_metrics_prompt
from ._main_metrics_table import main_metrics_table


def main_metrics(
    #
    # DATABASE PARAMS:
    root_dir: str = "./",
    database: str = "main",
    year_filter: tuple = (None, None),
    cited_by_filter: tuple = (None, None),
    **filters,
):
    """Main information

    :meta private:
    """

    @dataclass
    class Result:
        df_: pd.DataFrame
        fig_: go.Figure
        prompt_: str

    data_frame = main_metrics_table(
        #
        # DATABASE PARAMS:
        root_dir=root_dir,
        database=database,
        year_filter=year_filter,
        cited_by_filter=cited_by_filter,
        **filters,
    )

    prompt = main_metrics_prompt(data_frame)
    fig = main_metrics_dashboard(data_frame)

    return Result(
        df_=data_frame,
        prompt_=prompt,
        fig_=fig,
    )
