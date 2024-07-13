# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
# pylint: disable=import-outside-toplevel
"""
Most Global Cited Documents
===============================================================================

>>> from techminer2.science_mapping.citation import most_cited_documents
>>> documents = most_cited_documents(
...     #
...     # FUNCTION PARAMS:
...     metric="global_citations",
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
--INFO-- The file 'example/reports/most_global_cited_documents__abstracts.txt' was created.
--INFO-- The file 'example/reports/most_global_cited_documents__prompt.txt' was created.

>>> documents.fig_.write_html("sphinx/_static/analyze/citation/publications/most_global_cited_documents.html")

.. raw:: html

    <iframe src="../../../../../_static/analyze/citation/publications/most_global_cited_documents.html" 
    height="600px" width="100%" frameBorder="0"></iframe>

    
>>> print(documents.df_.head().to_markdown())
| article                                       |   year |   rank_gcs |   global_citations |   rank_lcs |   local_citations |   global_citations_per_year |   local_citations_per_year | doi                           |
|:----------------------------------------------|-------:|-----------:|-------------------:|-----------:|------------------:|----------------------------:|---------------------------:|:------------------------------|
| Gomber P., 2018, J MANAGE INF SYST, V35, P220 |   2018 |          1 |                576 |          3 |                 3 |                     288     |                      1.5   | 10.1080/07421222.2018.1440766 |
| Lee I., 2018, BUS HORIZ, V61, P35             |   2018 |          2 |                557 |          6 |                 2 |                     278.5   |                      1     | 10.1016/J.BUSHOR.2017.09.003  |
| Gomber P., 2017, J BUS ECON, V87, P537        |   2017 |          3 |                489 |          1 |                 4 |                     163     |                      1.333 | 10.1007/S11573-017-0852-X     |
| Buchak G., 2018, J FINANC ECON, V130, P453    |   2018 |          4 |                390 |         23 |                 0 |                     195     |                      0     | 10.1016/J.JFINECO.2018.03.011 |
| Gabor D., 2017, NEW POLIT ECON, V22, P423     |   2017 |          5 |                314 |          7 |                 2 |                     104.667 |                      0.667 | 10.1080/13563467.2017.1259298 |




"""
