# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
# pylint: disable=import-outside-toplevel
"""
.. _citation_analysis.most_local_cited_documents:

Most Local Cited Documents
===============================================================================

>>> from techminer2.citation_analysis import most_local_cited_documents
>>> documents = most_local_cited_documents(
...     #
...     # FUNCTION PARAMS:
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
--INFO-- The file 'data/regtech/reports/most_local_cited_documents__abstracts.txt' was created.
--INFO-- The file 'data/regtech/reports/most_local_cited_documents__prompt.txt' was created.

>>> documents.fig_.write_html("sphinx/_static/citation_analysis/most_local_cited_documents.html")

.. raw:: html

    <iframe src="../../../../_static/citation_analysis/most_local_cited_documents.html" 
    height="600px" width="100%" frameBorder="0"></iframe>


    
>>> print(documents.df_.to_markdown())
| article                                                  |   year |   global_citations |   local_citations |   global_citations_per_year |   local_citations_per_year | doi                                |
|:---------------------------------------------------------|-------:|-------------------:|------------------:|----------------------------:|---------------------------:|:-----------------------------------|
| Anagnostopoulos I, 2018, J ECON BUS, V100, P7            |   2018 |                153 |                17 |                      25.5   |                      2.833 | 10.1016/J.JECONBUS.2018.07.003     |
| Arner DW, 2017, NORTHWEST J INTL LAW BUS, V37, P373      |   2017 |                150 |                16 |                      21.429 |                      2.286 | nan                                |
| Butler T, 2019, PALGRAVE STUD DIGIT BUS ENABL, P85       |   2019 |                 33 |                14 |                       6.6   |                      2.8   | 10.1007/978-3-030-02330-0_6        |
| Kavassalis P, 2018, J RISK FINANC, V19, P39              |   2018 |                 21 |                 8 |                       3.5   |                      1.333 | 10.1108/JRF-07-2017-0111           |
| Baxter LG, 2016, DUKE LAW J, V66, P567                   |   2016 |                 30 |                 8 |                       3.75  |                      1     | nan                                |
| Butler T, 2018, J RISK MANG FINANCIAL INST, V11, P19     |   2018 |                  8 |                 5 |                       1.333 |                      0.833 | nan                                |
| Buckley RP, 2020, J BANK REGUL, V21, P26                 |   2020 |                 24 |                 4 |                       6     |                      1     | 10.1057/S41261-019-00104-1         |
| von Solms J, 2021, J BANK REGUL, V22, P152               |   2021 |                 11 |                 4 |                       3.667 |                      1.333 | 10.1057/S41261-020-00134-0         |
| Brand V, 2020, UNIV NEW SOUTH WALES LAW J, V43, P801     |   2020 |                  4 |                 3 |                       1     |                      0.75  | nan                                |
| Singh C, 2020, J MONEY LAUND CONTROL, V24, P464          |   2020 |                 14 |                 3 |                       3.5   |                      0.75  | 10.1108/JMLC-09-2020-0100          |
| Nicholls R, 2021, J ANTITRUST ENFORC, V9, P135           |   2021 |                  3 |                 3 |                       1     |                      1     | 10.1093/JAENFO/JNAA011             |
| Kurum E, 2020, J FINANC CRIME                            |   2020 |                 10 |                 3 |                       2.5   |                      0.75  | 10.1108/JFC-04-2020-0051           |
| Arner DW, 2017, HANDBBLOCKCHAIN, DIGIT FINANC, P359      |   2017 |                 11 |                 3 |                       1.571 |                      0.429 | 10.1016/B978-0-12-810441-5.00016-6 |
| Ryan P, 2020, ICEIS - PROC INT CONF ENTERP , V2, P787    |   2020 |                 12 |                 3 |                       3     |                      0.75  | nan                                |
| Muzammil M, 2020, CEUR WORKSHOP PROC, V2815, P382        |   2020 |                  2 |                 3 |                       0.5   |                      0.75  | nan                                |
| Turki M, 2020, HELIYON, V6                               |   2020 |                 11 |                 2 |                       2.75  |                      0.5   | 10.1016/J.HELIYON.2020.E04949      |
| Gasparri G, 2019, FRONTIER ARTIF INTELL, V2              |   2019 |                  3 |                 2 |                       0.6   |                      0.4   | 10.3389/FRAI.2019.00014            |
| Goul M, 2019, PROC - IEEE WORLD CONGR SERV,, P219        |   2019 |                  3 |                 2 |                       0.6   |                      0.4   | 10.1109/SERVICES.2019.00061        |
| Singh C, 2022, J FINANC CRIME, V29, P45                  |   2022 |                  3 |                 1 |                       1.5   |                      0.5   | 10.1108/JFC-06-2021-0131           |
| Becker M, 2020, INTELL SYST ACCOUNT FINANCE M, V27, P161 |   2020 |                  5 |                 1 |                       1.25  |                      0.25  | 10.1002/ISAF.1479                  |




"""


def most_local_cited_documents(
    #
    # FUNCTION PARAMS:
    top_n=10,
    #
    # CHART PARAMS:
    title=None,
    field_label=None,
    metric_label=None,
    textfont_size=10,
    marker_size=7,
    line_width=1.5,
    yshift=4,
    #
    # DATABASE PARAMS:
    root_dir="./",
    database="main",
    year_filter=(None, None),
    cited_by_filter=(None, None),
    **filters,
):
    """Plots the most global cited documents in the main collection.

    :meta private:
    """

    from .most_cited_documents import most_cited_documents

    return most_cited_documents(
        #
        # FUNCTION PARAMS:
        metric="local_citations",
        top_n=top_n,
        #
        # CHART PARAMS:
        title=title,
        field_label=field_label,
        metric_label=metric_label,
        textfont_size=textfont_size,
        marker_size=marker_size,
        line_width=line_width,
        yshift=yshift,
        #
        # DATABASE PARAMS:
        root_dir=root_dir,
        database=database,
        year_filter=year_filter,
        cited_by_filter=cited_by_filter,
        **filters,
    )
