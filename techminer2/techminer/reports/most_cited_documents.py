"""
Most Global Cited Documents 
===============================================================================

Generates a report with the most global cited documents that meet the specified
filters.

Example
-------------------------------------------------------------------------------

>>> root_dir = "data/regtech/"

>>> from techminer2 import techminer
>>> techminer.reports.most_cited_documents(
...     root_dir=root_dir,
... )
--INFO-- The file 'data/regtech/reports/most_cited_documents.txt' was created

"""
from .abstracts_report import abstracts_report


def most_cited_documents(
    root_dir="./",
    file_name="most_cited_documents.txt",
    start_year=None,
    end_year=None,
    **filters,
):
    """
    Generates a report with records ordered by global and local citations.

    Args:
        root_dir (str): root directory.
        criterion=None,
        custom_topics=None,
        file_name="abstracts_report.txt",
        start_year=None,
        end_year=None,
        **filters: filters.

    Returns:
        None.

    """
    return abstracts_report(
        criterion=None,
        custom_topics=None,
        file_name=file_name,
        use_textwrap=True,
        root_dir=root_dir,
        database="documents",
        start_year=start_year,
        end_year=end_year,
        **filters,
    )
