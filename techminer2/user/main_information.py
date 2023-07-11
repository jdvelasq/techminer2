# flake8: noqa
"""
.. _main_information:

Main Information
===============================================================================

TODO: check organizations_1st_author, countries_1st_author

>>> import techminer2plus as tm2p
>>> root_dir = "data/regtech/"
>>> main_info = tm2p.Records(root_dir=root_dir).main_information()
>>> main_info
MainInformation(root_dir='data/regtech/', database='main', year_filter=(None,
    None), cited_by_filter=(None, None), filters={})

>>> main_info.frame_
                                                            Value
Category       Item                                              
GENERAL        Timespan                                 2016:2023
               Documents                                       52
               Annual growth rate %                         63.87
               Document average age                          2.77
               References                                    2968
               Average citations per document               10.83
               Average citations per document per year       1.35
               Average references per document              59.36
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
                                                            

               
>>> file_name = "sphinx/_static/main_info.html"               
>>> main_info.fig_.write_html(file_name)

.. raw:: html

    <iframe src="../_static/main_info.html" height="800px" width="100%" frameBorder="0"></iframe>


    
>>> print(main_info.prompt_)
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
| ('GENERAL', 'References')                              | 2968      |
| ('GENERAL', 'Average citations per document')          | 10.83     |
| ('GENERAL', 'Average citations per document per year') | 1.35      |
| ('GENERAL', 'Average references per document')         | 59.36     |
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

    
* **COMPUTATIONAL API:**

>>> frame_, prompt_, fig_ = main_information(
...     root_dir=root_dir,
... )
>>> frame_
                                                            Value
Category       Item                                              
GENERAL        Timespan                                 2016:2023
               Documents                                       52
               Annual growth rate %                         63.87
               Document average age                          2.77
               References                                    2968
               Average citations per document               10.83
               Average citations per document per year       1.35
               Average references per document              59.36
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



# pylint: disable=line-too-long
"""
import textwrap
from dataclasses import dataclass
from dataclasses import field as datafield

import pandas as pd
import plotly.graph_objects as go

# from ..api.records.main_information import main_information

# =============================================================================
#
#
#  USER COMPUTATIONAL INTERFACE:
#
#
# =============================================================================


# pylint: disable=too-many-instance-attributes
@dataclass
class MainInformation:
    """Main Information."""

    #
    # DATABASE PARAMS:
    #
    root_dir: str = "./"
    database: str = "main"
    year_filter: tuple = (None, None)
    cited_by_filter: tuple = (None, None)
    filters: dict = datafield(default_factory=dict)

    #
    # RESULTS:
    #
    frame_: pd.DataFrame = pd.DataFrame()
    prompt_: str = ""
    fig: go.Figure = go.Figure()

    def __post_init__(self):
        #
        # COMPUTATIONS:
        #
        if self.filters is None:
            self.filters = {}

        self.frame_, self.fig_, self.prompt_ = main_information(
            root_dir=self.root_dir,
            database=self.database,
            year_filter=self.year_filter,
            cited_by_filter=self.cited_by_filter,
            **self.filters,
        )

    def __repr__(self):
        """String representation."""
        text = (
            "MainInformation("
            f"root_dir='{self.root_dir}'"
            f", database='{self.database}'"
            f", year_filter={self.year_filter}"
            f", cited_by_filter={self.cited_by_filter}"
            f", filters={self.filters}"
            ")"
        )

        return textwrap.fill(text, width=80, subsequent_indent="    ")
