# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
# pylint: disable=import-outside-toplevel
"""
.. _tm2.citation.documentsmost_local_cited_documents:

Most Local Cited Documents
===============================================================================

>>> from techminer2.analyze.citation import most_cited_documents
>>> documents = most_cited_documents(
...     #
...     # FUNCTION PARAMS:
...     metric="local_citations",
...     top_n=20,
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
--INFO-- The file 'example/reports/most_local_cited_documents__abstracts.txt' was created.
--INFO-- The file 'example/reports/most_local_cited_documents__prompt.txt' was created.

>>> documents.fig_.write_html("sphinx/_static/analyze/citation/publications/most_local_cited_documents.html")

.. raw:: html

    <iframe src="../../../../../_static/analyze/citation/publications/most_local_cited_documents.html" 
    height="600px" width="100%" frameBorder="0"></iframe>


    
>>> print(documents.df_.head().to_markdown())
| article                                          |   year |   rank_gcs |   global_citations |   rank_lcs |   local_citations |   global_citations_per_year |   local_citations_per_year | doi                           |
|:-------------------------------------------------|-------:|-----------:|-------------------:|-----------:|------------------:|----------------------------:|---------------------------:|:------------------------------|
| Gomber P., 2017, J BUS ECON, V87, P537           |   2017 |          3 |                489 |          1 |                 4 |                       163   |                      1.333 | 10.1007/S11573-017-0852-X     |
| Mackenzie A., 2015, LONDON BUS SCH REV, V26, P50 |   2015 |         42 |                 76 |          2 |                 4 |                        15.2 |                      0.8   | 10.1111/2057-1615.12059       |
| Gomber P., 2018, J MANAGE INF SYST, V35, P220    |   2018 |          1 |                576 |          3 |                 3 |                       288   |                      1.5   | 10.1080/07421222.2018.1440766 |
| Shim Y., 2016, TELECOMMUN POLICY, V40, P168      |   2016 |         21 |                146 |          4 |                 3 |                        36.5 |                      0.75  | 10.1016/J.TELPOL.2015.11.005  |
| Zavolokina L., 2016, FINANCIAL INNOV, V2         |   2016 |         27 |                106 |          5 |                 3 |                        26.5 |                      0.75  | 10.1186/S40854-016-0036-7     |



"""
