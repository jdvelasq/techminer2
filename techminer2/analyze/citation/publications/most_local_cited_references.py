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
--INFO-- The file 'data/regtech/reports/most_local_cited_references__abstracts.txt' was created.
--INFO-- The file 'data/regtech/reports/most_local_cited_references__prompt.txt' was created.


>>> documents.fig_.write_html("sphinx/_static/analyze/citation/publications/most_local_cited_references.html")

.. raw:: html

    <iframe src="../../../../../_static/analyze/citation/publications/most_local_cited_references.html" 
    height="600px" width="100%" frameBorder="0"></iframe>


>>> print(documents.df_.head(5).to_markdown())
| article                                             |   year |   rank_gcs |   global_citations |   rank_lcs |   local_citations |   global_citations_per_year |   local_citations_per_year | doi                            |
|:----------------------------------------------------|-------:|-----------:|-------------------:|-----------:|------------------:|----------------------------:|---------------------------:|:-------------------------------|
| Anagnostopoulos I, 2018, J ECON BUS, V100, P7       |   2018 |        222 |                153 |          1 |                17 |                      30.6   |                      3.4   | 10.1016/J.JECONBUS.2018.07.003 |
| Arner DW, 2017, NORTHWEST J INTL LAW BUS, V37, P373 |   2017 |        227 |                150 |          2 |                16 |                      25     |                      2.667 | nan                            |
| Butler T, 2019, PALGRAVE STUD DIGIT BUS ENABL, P85  |   2019 |        484 |                 33 |          3 |                14 |                       8.25  |                      3.5   | 10.1007/978-3-030-02330-0_6    |
| Kavassalis P, 2018, J RISK FINANC, V19, P39         |   2018 |        569 |                 21 |          5 |                 8 |                       4.2   |                      1.6   | 10.1108/JRF-07-2017-0111       |
| Baxter LG, 2016, DUKE LAW J, V66, P567              |   2016 |        509 |                 30 |          4 |                 8 |                       4.286 |                      1.143 | nan                            |



"""
