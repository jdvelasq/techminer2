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

>>> from techminer2.analyze.citation import most_cited_documents
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
...     root_dir="data/regtech/",
...     database="main",
...     year_filter=(None, None),
...     cited_by_filter=(None, None),
... )
--INFO-- The file 'data/regtech/reports/most_global_cited_documents__abstracts.txt' was created.
--INFO-- The file 'data/regtech/reports/most_global_cited_documents__prompt.txt' was created.

>>> documents.fig_.write_html("sphinx/_static/analyze/citation/publications/most_global_cited_documents.html")

.. raw:: html

    <iframe src="../../../../../_static/analyze/citation/publications/most_global_cited_documents.html" 
    height="600px" width="100%" frameBorder="0"></iframe>

    
>>> print(documents.df_.to_markdown())
| article                                                       |   year |   rank_gcs |   global_citations |   rank_lcs |   local_citations |   global_citations_per_year |   local_citations_per_year | doi                                |
|:--------------------------------------------------------------|-------:|-----------:|-------------------:|-----------:|------------------:|----------------------------:|---------------------------:|:-----------------------------------|
| Anagnostopoulos I, 2018, J ECON BUS, V100, P7                 |   2018 |          1 |                153 |          1 |                17 |                      25.5   |                      2.833 | 10.1016/J.JECONBUS.2018.07.003     |
| Arner DW, 2017, NORTHWEST J INTL LAW BUS, V37, P373           |   2017 |          2 |                150 |          2 |                16 |                      21.429 |                      2.286 | nan                                |
| Butler T, 2019, PALGRAVE STUD DIGIT BUS ENABL, P85            |   2019 |          3 |                 33 |          3 |                14 |                       6.6   |                      2.8   | 10.1007/978-3-030-02330-0_6        |
| Baxter LG, 2016, DUKE LAW J, V66, P567                        |   2016 |          4 |                 30 |          4 |                 8 |                       3.75  |                      1     | nan                                |
| Buckley RP, 2020, J BANK REGUL, V21, P26                      |   2020 |          5 |                 24 |          6 |                 5 |                       6     |                      1.25  | 10.1057/S41261-019-00104-1         |
| Kavassalis P, 2018, J RISK FINANC, V19, P39                   |   2018 |          6 |                 21 |          5 |                 8 |                       3.5   |                      1.333 | 10.1108/JRF-07-2017-0111           |
| Singh C, 2020, J MONEY LAUND CONTROL, V24, P464               |   2020 |          7 |                 14 |          9 |                 3 |                       3.5   |                      0.75  | 10.1108/JMLC-09-2020-0100          |
| Muganyi T, 2022, FINANCIAL INNOV, V8                          |   2022 |          8 |                 13 |         19 |                 1 |                       6.5   |                      0.5   | 10.1186/S40854-021-00313-6         |
| Ryan P, 2020, ICEIS - PROC INT CONF ENTERP , V2, P787         |   2020 |          9 |                 12 |         10 |                 3 |                       3     |                      0.75  | nan                                |
| von Solms J, 2021, J BANK REGUL, V22, P152                    |   2021 |         10 |                 11 |          8 |                 4 |                       3.667 |                      1.333 | 10.1057/S41261-020-00134-0         |
| Arner DW, 2017, HANDBBLOCKCHAIN, DIGIT FINANC, P359           |   2017 |         11 |                 11 |         11 |                 3 |                       1.571 |                      0.429 | 10.1016/B978-0-12-810441-5.00016-6 |
| Turki M, 2020, HELIYON, V6                                    |   2020 |         12 |                 11 |         16 |                 2 |                       2.75  |                      0.5   | 10.1016/J.HELIYON.2020.E04949      |
| Kurum E, 2020, J FINANC CRIME                                 |   2020 |         13 |                 10 |         12 |                 3 |                       2.5   |                      0.75  | 10.1108/JFC-04-2020-0051           |
| Butler T, 2018, J RISK MANG FINANCIAL INST, V11, P19          |   2018 |         14 |                  8 |          7 |                 5 |                       1.333 |                      0.833 | nan                                |
| Turki M, 2021, ADV INTELL SYS COMPUT, V1141, P349             |   2021 |         15 |                  7 |         20 |                 1 |                       2.333 |                      0.333 | 10.1007/978-981-15-3383-9_32       |
| Becker M, 2020, INTELL SYST ACCOUNT FINANCE M, V27, P161      |   2020 |         17 |                  5 |         22 |                 1 |                       1.25  |                      0.25  | 10.1002/ISAF.1479                  |
| Das SR, 2019, J FINANCIAL DATA SCI, V1, P8                    |   2019 |         16 |                  5 |         21 |                 1 |                       1     |                      0.2   | 10.3905/JFDS.2019.1.2.008          |
| Waye V, 2020, ADELAIDE LAW REV, V40, P363                     |   2020 |         18 |                  5 |         23 |                 1 |                       1.25  |                      0.25  | nan                                |
| Pantielieieva N, 2020, LECTURE NOTES DATA ENG COMMUN, V42, P1 |   2020 |         20 |                  4 |         28 |                 0 |                       1     |                      0     | 10.1007/978-3-030-35649-1_1        |
| Brand V, 2020, UNIV NEW SOUTH WALES LAW J, V43, P801          |   2020 |         19 |                  4 |         13 |                 3 |                       1     |                      0.75  | nan                                |




"""