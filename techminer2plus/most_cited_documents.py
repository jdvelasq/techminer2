# flake8: noqa
# pylint: disable=line-too-long
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

# from ..bibliometrix.abstract.abstracts_report import abstracts_report


# def most_cited_documents(
#     file_name="most_cited_documents.txt",
#     root_dir="./",
#     # Database filters:
#     year_filter=None,
#     cited_by_filter=None,
#     **filters,
# ):
#     """Generates a report with records ordered by global and local citations.

#     Args:
#         root_dir (str): root directory.
#         file_name (str): output file name.
#         start_year (int): start year.
#         end_year (int): end year.
#         **filters: filters.


#     Returns:
#         None.

#     """
#     return abstracts_report(
#         field=None,
#         custom_items=None,
#         file_name=file_name,
#         use_textwrap=True,
#         root_dir=root_dir,
#         database="main",
#         year_filter=year_filter,
#         cited_by_filter=cited_by_filter,
#         **filters,
#     )
