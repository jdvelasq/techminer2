# flake8: noqa
"""
Main information
===============================================================================


>>> directory = "data/regtech/"

>>> from techminer2 import bibliometrix
>>> r = bibliometrix.overview.main_information(directory)
>>> r.table_
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
               Organizations                                   80
               Organizations (1st author)                      44
               Countries                                       29
               Countries (1st author)                          25
KEYWORDS       Raw author keywords                            149
               Cleaned author keywords                        144
               Raw index keywords                             155
               Cleaned index keywords                         150





>>> file_name = "sphinx/_static/bibliometrix__main_info_plot.html"               
>>> r.plot_.write_html(file_name)

.. raw:: html

    <iframe src="../../_static/bibliometrix__main_info_plot.html" 
    height="600px" width="100%" frameBorder="0"></iframe>



>>> print(r.prompt_)
The table below provides data on the main characteristics of the dataset. Use the the information in the table to draw conclusions. Limit your description to one paragraph with no more than 250 words.
<BLANKLINE>
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
| ('AUTHORS', 'Organizations')                           | 80        |
| ('AUTHORS', 'Organizations (1st author)')              | 44        |
| ('AUTHORS', 'Countries')                               | 29        |
| ('AUTHORS', 'Countries (1st author)')                  | 25        |
| ('KEYWORDS', 'Raw author keywords')                    | 149       |
| ('KEYWORDS', 'Cleaned author keywords')                | 144       |
| ('KEYWORDS', 'Raw index keywords')                     | 155       |
| ('KEYWORDS', 'Cleaned index keywords')                 | 150       |
<BLANKLINE>
<BLANKLINE>


# pylint: disable=line-too-long
"""

from ...vantagepoint.analyze import statistics


def main_information(
    root_dir="./",
    database="documents",
    year_filter=None,
    cited_by_filter=None,
    **filters,
):
    """Returns main statistics of the dataset.

    Args:
        root_dir (str, optional): root directory. Defaults to "./".
        database (str, optional): database name. Defaults to "documents".
        year_filter (tuple, optional): Year filter. Defaults to None.
        cited_by_filter (tuple, optional): Cited by filter. Defaults to None.
        **filters (dict, optional): Filters to be applied to the database. Defaults to {}.

    Returns:
        RecordStatistics: RecordStatistics object.

    """

    return statistics(
        root_dir=root_dir,
        database=database,
        year_filter=year_filter,
        cited_by_filter=cited_by_filter,
        **filters,
    )
