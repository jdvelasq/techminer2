# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
# pylint: disable=import-outside-toplevel
"""
Most Local Cited References
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
...     database="references",
...     year_filter=(None, None),
...     cited_by_filter=(None, None),
... )
--INFO-- The file 'example/reports/most_local_cited_references__abstracts.txt' was created.
--INFO-- The file 'example/reports/most_local_cited_references__prompt.txt' was created.


>>> documents.fig_.write_html("sphinx/_static/analyze/citation/publications/most_local_cited_references.html")

.. raw:: html

    <iframe src="../../../../../_static/analyze/citation/publications/most_local_cited_references.html" 
    height="600px" width="100%" frameBorder="0"></iframe>


>>> print(documents.df_.head(5).to_markdown())
| article                                          |   year |   rank_gcs |   global_citations |   rank_lcs |   local_citations |   global_citations_per_year |   local_citations_per_year | doi                           |
|:-------------------------------------------------|-------:|-----------:|-------------------:|-----------:|------------------:|----------------------------:|---------------------------:|:------------------------------|
| Gomber P., 2017, J BUS ECON, V87, P537           |   2017 |        282 |                489 |          1 |                 4 |                     122.25  |                      1     | 10.1007/S11573-017-0852-X     |
| Mackenzie A., 2015, LONDON BUS SCH REV, V26, P50 |   2015 |        822 |                 76 |          2 |                 4 |                      12.667 |                      0.667 | 10.1111/2057-1615.12059       |
| Gomber P., 2018, J MANAGE INF SYST, V35, P220    |   2018 |        239 |                576 |          3 |                 3 |                     192     |                      1     | 10.1080/07421222.2018.1440766 |
| Zavolokina L., 2016, FINANCIAL INNOV, V2         |   2016 |        699 |                106 |          5 |                 3 |                      21.2   |                      0.6   | 10.1186/S40854-016-0036-7     |
| Shim Y., 2016, TELECOMMUN POLICY, V40, P168      |   2016 |        589 |                146 |          4 |                 3 |                      29.2   |                      0.6   | 10.1016/J.TELPOL.2015.11.005  |



"""
