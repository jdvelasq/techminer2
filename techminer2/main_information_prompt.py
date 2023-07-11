# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
"""
.. _main_information_prompt:

Main Information Prompt
===============================================================================

>>> import techminer2plus as tm2p
>>> root_dir = "data/regtech/"
>>> prompt = tm2p.main_information_prompt(
...     root_dir=root_dir,
... )
>>> print(prompt)
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

"""

from .format_prompt_for_dataframes import format_prompt_for_dataframes
from .main_information_table import main_information_table


def main_information_prompt(
    root_dir: str = "./",
    database: str = "main",
    year_filter: tuple = (None, None),
    cited_by_filter: tuple = (None, None),
    **filters,
):
    df = main_information_table(
        #
        # DATABASE PARAMS
        root_dir=root_dir,
        database=database,
        year_filter=year_filter,
        cited_by_filter=cited_by_filter,
        **filters,
    )

    main_text = (
        "Your task is to generate a short summary for a research paper of a "
        "table with record and field statistics for a dataset of scientific "
        "publications. The table below, delimited by triple backticks, "
        "provides data on the main characteristics of the records and fields "
        "of the bibliographic dataset. Use the the information in the table "
        "to draw conclusions. Limit your description to one paragraph in at "
        "most 100 words. "
    )

    table_text = df.to_markdown()

    return format_prompt_for_dataframes(main_text, table_text)
