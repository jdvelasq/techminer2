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
--INFO-- The file 'data/regtech/reports/most_local_cited_documents__abstracts.txt' was created.
--INFO-- The file 'data/regtech/reports/most_local_cited_documents__prompt.txt' was created.

>>> documents.fig_.write_html("sphinx/_static/analyze/citation/publications/most_local_cited_documents.html")

.. raw:: html

    <iframe src="../../../../../_static/analyze/citation/publications/most_local_cited_documents.html" 
    height="600px" width="100%" frameBorder="0"></iframe>


    
>>> print(documents.df_.to_markdown())
| article                                               |   year |   rank_gcs |   global_citations |   rank_lcs |   local_citations |   global_citations_per_year |   local_citations_per_year | doi                                |
|:------------------------------------------------------|-------:|-----------:|-------------------:|-----------:|------------------:|----------------------------:|---------------------------:|:-----------------------------------|
| Anagnostopoulos I, 2018, J ECON BUS, V100, P7         |   2018 |          1 |                153 |          1 |                17 |                      25.5   |                      2.833 | 10.1016/J.JECONBUS.2018.07.003     |
| Arner DW, 2017, NORTHWEST J INTL LAW BUS, V37, P373   |   2017 |          2 |                150 |          2 |                16 |                      21.429 |                      2.286 | nan                                |
| Butler T, 2019, PALGRAVE STUD DIGIT BUS ENABL, P85    |   2019 |          3 |                 33 |          3 |                14 |                       6.6   |                      2.8   | 10.1007/978-3-030-02330-0_6        |
| Baxter LG, 2016, DUKE LAW J, V66, P567                |   2016 |          4 |                 30 |          4 |                 8 |                       3.75  |                      1     | nan                                |
| Kavassalis P, 2018, J RISK FINANC, V19, P39           |   2018 |          6 |                 21 |          5 |                 8 |                       3.5   |                      1.333 | 10.1108/JRF-07-2017-0111           |
| Buckley RP, 2020, J BANK REGUL, V21, P26              |   2020 |          5 |                 24 |          6 |                 5 |                       6     |                      1.25  | 10.1057/S41261-019-00104-1         |
| Butler T, 2018, J RISK MANG FINANCIAL INST, V11, P19  |   2018 |         14 |                  8 |          7 |                 5 |                       1.333 |                      0.833 | nan                                |
| von Solms J, 2021, J BANK REGUL, V22, P152            |   2021 |         10 |                 11 |          8 |                 4 |                       3.667 |                      1.333 | 10.1057/S41261-020-00134-0         |
| Brand V, 2020, UNIV NEW SOUTH WALES LAW J, V43, P801  |   2020 |         19 |                  4 |         13 |                 3 |                       1     |                      0.75  | nan                                |
| Muzammil M, 2020, CEUR WORKSHOP PROC, V2815, P382     |   2020 |         27 |                  2 |         15 |                 3 |                       0.5   |                      0.75  | nan                                |
| Nicholls R, 2021, J ANTITRUST ENFORC, V9, P135        |   2021 |         21 |                  3 |         14 |                 3 |                       1     |                      1     | 10.1093/JAENFO/JNAA011             |
| Kurum E, 2020, J FINANC CRIME                         |   2020 |         13 |                 10 |         12 |                 3 |                       2.5   |                      0.75  | 10.1108/JFC-04-2020-0051           |
| Arner DW, 2017, HANDBBLOCKCHAIN, DIGIT FINANC, P359   |   2017 |         11 |                 11 |         11 |                 3 |                       1.571 |                      0.429 | 10.1016/B978-0-12-810441-5.00016-6 |
| Ryan P, 2020, ICEIS - PROC INT CONF ENTERP , V2, P787 |   2020 |          9 |                 12 |         10 |                 3 |                       3     |                      0.75  | nan                                |
| Singh C, 2020, J MONEY LAUND CONTROL, V24, P464       |   2020 |          7 |                 14 |          9 |                 3 |                       3.5   |                      0.75  | 10.1108/JMLC-09-2020-0100          |
| Turki M, 2020, HELIYON, V6                            |   2020 |         12 |                 11 |         16 |                 2 |                       2.75  |                      0.5   | 10.1016/J.HELIYON.2020.E04949      |
| Gasparri G, 2019, FRONTIER ARTIF INTELL, V2           |   2019 |         22 |                  3 |         17 |                 2 |                       0.6   |                      0.4   | 10.3389/FRAI.2019.00014            |
| Goul M, 2019, PROC - IEEE WORLD CONGR SERV,, P219     |   2019 |         23 |                  3 |         18 |                 2 |                       0.6   |                      0.4   | 10.1109/SERVICES.2019.00061        |
| Waye V, 2020, ADELAIDE LAW REV, V40, P363             |   2020 |         18 |                  5 |         23 |                 1 |                       1.25  |                      0.25  | nan                                |
| Siering M, 2022, DECIS SUPPORT SYST, V158             |   2022 |         31 |                  1 |         26 |                 1 |                       0.5   |                      0.5   | 10.1016/J.DSS.2022.113782          |




"""
