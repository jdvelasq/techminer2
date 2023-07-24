# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
# pylint: disable=too-many-statements
"""
Co-citation Network
===============================================================================

See VOSviewer / :ref:`vosviewer_co_citation_network`


>>> root_dir = "data/regtech/"

>>> import techminer2plus
>>> nnet = techminer2plus.publish.intellectual_structure.co_citation_network(
...     top_n=50,
...     root_dir=root_dir,
...     algorithm_or_estimator="louvain",
...     network_viewer_dict={'nx_k': 0.2, 'nx_iterations': 10},
... )


>>> file_name = "sphinx/_static/examples/co_citation_network_plot.html"
>>> nnet.plot_.write_html(file_name)

.. raw:: html

    <iframe src="../../_static/examples/co_citation_network_plot.html" height="600px" width="100%" frameBorder="0"></iframe>

    
>>> print(nnet.communities_.to_markdown())
|    | CL_00                                                           | CL_01                                                            | CL_02                                                           |
|---:|:----------------------------------------------------------------|:-----------------------------------------------------------------|:----------------------------------------------------------------|
|  0 | Yang D, 2018, EMERG MARK FINANC TRADE, V54, P3256 08:020        | Barrell R, 2011, NATL INST ECON REV, V216, PF4 68:713            | Singh C, 2020, J MONEY LAUND CONTROL, V24, P464 03:004          |
|  1 | Kavassalis P, 2018, J RISK FINANC, V19, P39 08:010              | Anagnostopoulos I, 2018, J ECON BUS, V100, P7 17:061             | Bellamy RKE, 2019, IBM J RES DEV, V63 02:017                    |
|  2 | Butler T, 2018, J RISK MANG FINANCIAL INST, V11, P19 05:007     | Butler T, 2019, PALGRAVE STUD DIGIT BUS ENABL, P85 14:026        | Kingston KG, 2020, AFRICAN J INT COMP LAW, V28, P106 02:017     |
|  3 | Williams JW, 2013, ACCOUNT ORGAN SOC, V38, P544 05:007          | Kroll JA, 2017, UNIV PA LAW REV, V165, P633 05:005               | Lee Kuo Chuen D, 2017, HANDBBLOCKCHAIN, DIGIT FINANC, P1 02:017 |
|  4 | Buckley RP, 2020, J BANK REGUL, V21, P26 05:003                 | Romanova I, 2016, CONTEMP STUD ECON FINANC ANAL, V98, P21 03:153 | Raymond Choo KK, 2008, J MONEY LAUND CONTROL, V11, P371 02:017  |
|  5 | Micheler E, 2020, EUR BUS ORG LAW REV, V21, P349 05:001         | Dutta A, 2016, WIPDA - IEEE WORKSHOP WIDE BA, P11 03:099         | Simser J, 2008, J MONEY LAUND CONTROL, V11, P15 02:017          |
|  6 | Arner DW, 2019, EUR BUS ORG LAW REV, V20, P55 04:025            | Bamberger KA, 2010, TEX LAW REV, V88, P669 03:008                | Smith KT, 2010, J STRATEG MARK, V18, P201 02:017                |
|  7 | Sheridan I, 2017, CAP MARK LAW J, V12, P417 04:006              | Hildebrandt M, 2018, PHILOS TRANS R SOC A MATH PHY, V376 03:001  | Walker D, 2006, POLICE J, V79, P169 02:017                      |
|  8 | Turki M, 2020, HELIYON, V6 04:001                               | Brummer C, 2015, FORDHAM LAW REV, V84, P977 02:303               |                                                                 |
|  9 | von Solms J, 2021, J BANK REGUL, V22, P152 04:001               | Philippon T, 2015, AM ECON REV, V105, P1408 02:174               |                                                                 |
| 10 | Currie WL, 2018, J INF TECHNOL, V33, P304 03:005                | Gomber P, 2017, J BUS ECON, V87, P537 02:161                     |                                                                 |
| 11 | Arner DW, 2017, HANDBBLOCKCHAIN, DIGIT FINANC, P359 03:004      | Zavolokina L, 2016, FINANCIAL INNOV, V2 02:154                   |                                                                 |
| 12 | Gomber P, 2018, J MANAGE INF SYST, V35, P220 03:002             | Rhodes-Kropf M, 2004, J FINANC, V59, P2685 02:153                |                                                                 |
| 13 | Ryan P, 2020, ICEIS - PROC INT CONF ENTERP , V2, P787 03:002    | Scott SV, 2017, RES POLICY, V46, P984 02:153                     |                                                                 |
| 14 | Becker M, 2020, INTELL SYST ACCOUNT FINANCE M, V27, P161 03:001 | Van Alstyne MW, 2016, HARV BUS REV, V2016 02:153                 |                                                                 |
| 15 | Brand V, 2020, UNIV NEW SOUTH WALES LAW J, V43, P801 03:001     | Haldane AG, 2011, NATURE, V469, P351 02:030                      |                                                                 |
| 16 | Kurum E, 2020, J FINANC CRIME 03:001                            | Lane J, 2013, PRIV, BIG DATA,THE PUBLIC GOO, P1 02:021           |                                                                 |
| 17 | Lee J, 2020, EUR BUS ORG LAW REV, V21, P731 03:001              | Buttarelli G, 2016, INT DATA PRIVACY LAW, V6, P77 02:014         |                                                                 |
| 18 | Loiacono G, 2022, J BANK REGUL, V23, P227 03:001                | Drewer D, 2018, COMPUT LAW SECUR REV, V34, P806 02:014           |                                                                 |
| 19 | Muzammil M, 2020, CEUR WORKSHOP PROC, V2815, P382 03:001        |                                                                  |                                                                 |
| 20 | Gozman DP, 2020, MIS Q EXEC, V19, P19 03:000                    |                                                                  |                                                                 |
| 21 | Nicholls R, 2021, J ANTITRUST ENFORC, V9, P135 03:000           |                                                                  |                                                                 |
| 22 | Parra Moyano J, 2017, BUSIN INFO SYS ENG, V59, P411 03:000      |                                                                  |                                                                 |


>>> print(nnet.network_metrics__table_.head().to_markdown())
|                                                           |   Degree |   Betweenness |   Closeness |   PageRank |   Centrality |   Density |
|:----------------------------------------------------------|---------:|--------------:|------------:|-----------:|-------------:|----------:|
| Barrell R, 2011, NATL INST ECON REV, V216, PF4 68:713     |       42 |     0.16566   |    0.875    |  0.042847  |           68 |       413 |
| Butler T, 2019, PALGRAVE STUD DIGIT BUS ENABL, P85 14:026 |       35 |     0.0537176 |    0.777778 |  0.0334499 |           14 |       100 |
| Anagnostopoulos I, 2018, J ECON BUS, V100, P7 17:061      |       34 |     0.0313247 |    0.765625 |  0.0313116 |           17 |       140 |
| Kavassalis P, 2018, J RISK FINANC, V19, P39 08:010        |       34 |     0.0313247 |    0.765625 |  0.0313116 |            8 |        94 |
| Yang D, 2018, EMERG MARK FINANC TRADE, V54, P3256 08:020  |       30 |     0.0117544 |    0.720588 |  0.027168  |            8 |        97 |



>>> print(nnet.network_metrics__prompt_)
Your task is to generate a short analysis of the indicators of a network \\
for a research paper. Summarize the text below, delimited by triple \\
backticks, in at most 30 words, identifiying any notable patterns, trends, \\
or outliers in the data.
<BLANKLINE>
Table:
```
|                                                                  |   Degree |   Betweenness |   Closeness |   PageRank |   Centrality |   Density |
|:-----------------------------------------------------------------|---------:|--------------:|------------:|-----------:|-------------:|----------:|
| Barrell R, 2011, NATL INST ECON REV, V216, PF4 68:713            |       42 |   0.16566     |    0.875    | 0.042847   |           68 |       413 |
| Butler T, 2019, PALGRAVE STUD DIGIT BUS ENABL, P85 14:026        |       35 |   0.0537176   |    0.777778 | 0.0334499  |           14 |       100 |
| Anagnostopoulos I, 2018, J ECON BUS, V100, P7 17:061             |       34 |   0.0313247   |    0.765625 | 0.0313116  |           17 |       140 |
| Kavassalis P, 2018, J RISK FINANC, V19, P39 08:010               |       34 |   0.0313247   |    0.765625 | 0.0313116  |            8 |        94 |
| Yang D, 2018, EMERG MARK FINANC TRADE, V54, P3256 08:020         |       30 |   0.0117544   |    0.720588 | 0.027168   |            8 |        97 |
| Buckley RP, 2020, J BANK REGUL, V21, P26 05:003                  |       30 |   0.0174442   |    0.720588 | 0.0276161  |            5 |        83 |
| Singh C, 2020, J MONEY LAUND CONTROL, V24, P464 03:004           |       30 |   0.252663    |    0.720588 | 0.0337094  |            3 |        39 |
| Arner DW, 2019, EUR BUS ORG LAW REV, V20, P55 04:025             |       29 |   0.0123028   |    0.710145 | 0.0264417  |            4 |        60 |
| Williams JW, 2013, ACCOUNT ORGAN SOC, V38, P544 05:007           |       28 |   0.0120729   |    0.7      | 0.025848   |            5 |        62 |
| Micheler E, 2020, EUR BUS ORG LAW REV, V21, P349 05:001          |       28 |   0.00786372  |    0.7      | 0.025466   |            5 |        95 |
| Sheridan I, 2017, CAP MARK LAW J, V12, P417 04:006               |       28 |   0.00786372  |    0.7      | 0.025466   |            4 |        60 |
| von Solms J, 2021, J BANK REGUL, V22, P152 04:001                |       28 |   0.00620151  |    0.7      | 0.0254008  |            4 |        76 |
| Butler T, 2018, J RISK MANG FINANCIAL INST, V11, P19 05:007      |       27 |   0.0114543   |    0.690141 | 0.0251149  |            5 |        50 |
| Becker M, 2020, INTELL SYST ACCOUNT FINANCE M, V27, P161 03:001  |       27 |   0.00271917  |    0.690141 | 0.0243189  |            3 |        69 |
| Brand V, 2020, UNIV NEW SOUTH WALES LAW J, V43, P801 03:001      |       27 |   0.00271917  |    0.690141 | 0.0243189  |            3 |        69 |
| Kurum E, 2020, J FINANC CRIME 03:001                             |       27 |   0.00271917  |    0.690141 | 0.0243189  |            3 |        69 |
| Lee J, 2020, EUR BUS ORG LAW REV, V21, P731 03:001               |       27 |   0.00271917  |    0.690141 | 0.0243189  |            3 |        69 |
| Loiacono G, 2022, J BANK REGUL, V23, P227 03:001                 |       27 |   0.00271917  |    0.690141 | 0.0243189  |            3 |        69 |
| Muzammil M, 2020, CEUR WORKSHOP PROC, V2815, P382 03:001         |       27 |   0.00271917  |    0.690141 | 0.0243189  |            3 |        69 |
| Zavolokina L, 2016, FINANCIAL INNOV, V2 02:154                   |       27 |   0.0447218   |    0.690141 | 0.0261582  |            2 |        34 |
| Turki M, 2020, HELIYON, V6 04:001                                |       26 |   0.00511092  |    0.680556 | 0.0237726  |            4 |        51 |
| Arner DW, 2017, HANDBBLOCKCHAIN, DIGIT FINANC, P359 03:004       |       26 |   0.00216523  |    0.680556 | 0.0235321  |            3 |        51 |
| Parra Moyano J, 2017, BUSIN INFO SYS ENG, V59, P411 03:000       |       26 |   0.00625814  |    0.620253 | 0.023852   |            3 |        54 |
| Gomber P, 2018, J MANAGE INF SYST, V35, P220 03:002              |       25 |   0.00528088  |    0.6125   | 0.0230329  |            3 |        38 |
| Ryan P, 2020, ICEIS - PROC INT CONF ENTERP , V2, P787 03:002     |       25 |   0.00517766  |    0.6125   | 0.0230909  |            3 |        52 |
| Nicholls R, 2021, J ANTITRUST ENFORC, V9, P135 03:000            |       24 |   0.00597131  |    0.604938 | 0.0220455  |            3 |        46 |
| Gozman DP, 2020, MIS Q EXEC, V19, P19 03:000                     |       23 |   7.56231e-05 |    0.597561 | 0.0209426  |            3 |        64 |
| Currie WL, 2018, J INF TECHNOL, V33, P304 03:005                 |       20 |   0           |    0.628205 | 0.0187937  |            3 |        30 |
| Romanova I, 2016, CONTEMP STUD ECON FINANC ANAL, V98, P21 03:153 |       18 |   0.0102752   |    0.563218 | 0.0194416  |            3 |        31 |
| Scott SV, 2017, RES POLICY, V46, P984 02:153                     |       15 |   0.00649618  |    0.544444 | 0.0168291  |            2 |        21 |
| Van Alstyne MW, 2016, HARV BUS REV, V2016 02:153                 |       14 |   0.00489222  |    0.538462 | 0.0160596  |            2 |        19 |
| Kroll JA, 2017, UNIV PA LAW REV, V165, P633 05:005               |       10 |   0.000931325 |    0.515789 | 0.0115475  |            5 |        24 |
| Philippon T, 2015, AM ECON REV, V105, P1408 02:174               |        9 |   0.000880709 |    0.510417 | 0.0119714  |            2 |        12 |
| Gomber P, 2017, J BUS ECON, V87, P537 02:161                     |        9 |   0.00229592  |    0.510417 | 0.0120924  |            2 |        10 |
| Rhodes-Kropf M, 2004, J FINANC, V59, P2685 02:153                |        9 |   0.00166019  |    0.510417 | 0.0117508  |            2 |        11 |
| Lane J, 2013, PRIV, BIG DATA,THE PUBLIC GOO, P1 02:021           |        9 |   0.000836168 |    0.510417 | 0.0108234  |            2 |        13 |
| Brummer C, 2015, FORDHAM LAW REV, V84, P977 02:303               |        8 |   0           |    0.505155 | 0.0109197  |            2 |         9 |
| Hildebrandt M, 2018, PHILOS TRANS R SOC A MATH PHY, V376 03:001  |        7 |   0.0011844   |    0.538462 | 0.00895501 |            3 |        12 |
| Bellamy RKE, 2019, IBM J RES DEV, V63 02:017                     |        7 |   0           |    0.445455 | 0.0145797  |            2 |        13 |
| Kingston KG, 2020, AFRICAN J INT COMP LAW, V28, P106 02:017      |        7 |   0           |    0.445455 | 0.0145797  |            2 |        13 |
| Lee Kuo Chuen D, 2017, HANDBBLOCKCHAIN, DIGIT FINANC, P1 02:017  |        7 |   0           |    0.445455 | 0.0145797  |            2 |        13 |
| Raymond Choo KK, 2008, J MONEY LAUND CONTROL, V11, P371 02:017   |        7 |   0           |    0.445455 | 0.0145797  |            2 |        13 |
| Simser J, 2008, J MONEY LAUND CONTROL, V11, P15 02:017           |        7 |   0           |    0.445455 | 0.0145797  |            2 |        13 |
| Smith KT, 2010, J STRATEG MARK, V18, P201 02:017                 |        7 |   0           |    0.445455 | 0.0145797  |            2 |        13 |
| Walker D, 2006, POLICE J, V79, P169 02:017                       |        7 |   0           |    0.445455 | 0.0145797  |            2 |        13 |
| Buttarelli G, 2016, INT DATA PRIVACY LAW, V6, P77 02:014         |        7 |   0           |    0.5      | 0.00889223 |            2 |        11 |
| Drewer D, 2018, COMPUT LAW SECUR REV, V34, P806 02:014           |        7 |   0           |    0.5      | 0.00889223 |            2 |        11 |
| Bamberger KA, 2010, TEX LAW REV, V88, P669 03:008                |        6 |   0.00102041  |    0.494949 | 0.00815002 |            3 |         9 |
| Haldane AG, 2011, NATURE, V469, P351 02:030                      |        3 |   0           |    0.480392 | 0.0054641  |            2 |        10 |
| Dutta A, 2016, WIPDA - IEEE WORKSHOP WIDE BA, P11 03:099         |        1 |   0           |    0.471154 | 0.00386712 |            3 |         3 |
```
<BLANKLINE>


>>> file_name = "sphinx/_static/examples/co_citation_network_degree_plot.html"
>>> nnet.degree_plot__plot_.write_html(file_name)

.. raw:: html

    <iframe src="../../_static/examples/co_citation_network_degree_plot.html" height="600px" width="100%" frameBorder="0"></iframe>


    
>>> print(nnet.degree_plot__table_.head())
   Node                                               Name  Degree
0     0  Barrell R, 2011, NATL INST ECON REV, V216, PF4...      42
1     1  Butler T, 2019, PALGRAVE STUD DIGIT BUS ENABL,...      35
2     2  Anagnostopoulos I, 2018, J ECON BUS, V100, P7 ...      34
3     3  Kavassalis P, 2018, J RISK FINANC, V19, P39 08...      34
4     4  Yang D, 2018, EMERG MARK FINANC TRADE, V54, P3...      30

>>> print(nnet.degree_plot__prompt_)
Your task is to generate an analysis about the degree of the nodes in a \\
networkx graph of a co-ocurrence matrix. Analyze the table below, delimited \\
by triple backticks, identifying any notable patterns, trends, or outliers \\
in the data, and discuss their implications in the network.
<BLANKLINE>
Table:
```
|    |   Node | Name                                                             |   Degree |
|---:|-------:|:-----------------------------------------------------------------|---------:|
|  0 |      0 | Barrell R, 2011, NATL INST ECON REV, V216, PF4 68:713            |       42 |
|  1 |      1 | Butler T, 2019, PALGRAVE STUD DIGIT BUS ENABL, P85 14:026        |       35 |
|  2 |      2 | Anagnostopoulos I, 2018, J ECON BUS, V100, P7 17:061             |       34 |
|  3 |      3 | Kavassalis P, 2018, J RISK FINANC, V19, P39 08:010               |       34 |
|  4 |      4 | Yang D, 2018, EMERG MARK FINANC TRADE, V54, P3256 08:020         |       30 |
|  5 |      5 | Buckley RP, 2020, J BANK REGUL, V21, P26 05:003                  |       30 |
|  6 |      6 | Singh C, 2020, J MONEY LAUND CONTROL, V24, P464 03:004           |       30 |
|  7 |      7 | Arner DW, 2019, EUR BUS ORG LAW REV, V20, P55 04:025             |       29 |
|  8 |      8 | Williams JW, 2013, ACCOUNT ORGAN SOC, V38, P544 05:007           |       28 |
|  9 |      9 | Micheler E, 2020, EUR BUS ORG LAW REV, V21, P349 05:001          |       28 |
| 10 |     10 | Sheridan I, 2017, CAP MARK LAW J, V12, P417 04:006               |       28 |
| 11 |     11 | von Solms J, 2021, J BANK REGUL, V22, P152 04:001                |       28 |
| 12 |     12 | Butler T, 2018, J RISK MANG FINANCIAL INST, V11, P19 05:007      |       27 |
| 13 |     13 | Becker M, 2020, INTELL SYST ACCOUNT FINANCE M, V27, P161 03:001  |       27 |
| 14 |     14 | Brand V, 2020, UNIV NEW SOUTH WALES LAW J, V43, P801 03:001      |       27 |
| 15 |     15 | Kurum E, 2020, J FINANC CRIME 03:001                             |       27 |
| 16 |     16 | Lee J, 2020, EUR BUS ORG LAW REV, V21, P731 03:001               |       27 |
| 17 |     17 | Loiacono G, 2022, J BANK REGUL, V23, P227 03:001                 |       27 |
| 18 |     18 | Muzammil M, 2020, CEUR WORKSHOP PROC, V2815, P382 03:001         |       27 |
| 19 |     19 | Zavolokina L, 2016, FINANCIAL INNOV, V2 02:154                   |       27 |
| 20 |     20 | Turki M, 2020, HELIYON, V6 04:001                                |       26 |
| 21 |     21 | Arner DW, 2017, HANDBBLOCKCHAIN, DIGIT FINANC, P359 03:004       |       26 |
| 22 |     22 | Parra Moyano J, 2017, BUSIN INFO SYS ENG, V59, P411 03:000       |       26 |
| 23 |     23 | Gomber P, 2018, J MANAGE INF SYST, V35, P220 03:002              |       25 |
| 24 |     24 | Ryan P, 2020, ICEIS - PROC INT CONF ENTERP , V2, P787 03:002     |       25 |
| 25 |     25 | Nicholls R, 2021, J ANTITRUST ENFORC, V9, P135 03:000            |       24 |
| 26 |     26 | Gozman DP, 2020, MIS Q EXEC, V19, P19 03:000                     |       23 |
| 27 |     27 | Currie WL, 2018, J INF TECHNOL, V33, P304 03:005                 |       20 |
| 28 |     28 | Romanova I, 2016, CONTEMP STUD ECON FINANC ANAL, V98, P21 03:153 |       18 |
| 29 |     29 | Scott SV, 2017, RES POLICY, V46, P984 02:153                     |       15 |
| 30 |     30 | Van Alstyne MW, 2016, HARV BUS REV, V2016 02:153                 |       14 |
| 31 |     31 | Kroll JA, 2017, UNIV PA LAW REV, V165, P633 05:005               |       10 |
| 32 |     32 | Philippon T, 2015, AM ECON REV, V105, P1408 02:174               |        9 |
| 33 |     33 | Gomber P, 2017, J BUS ECON, V87, P537 02:161                     |        9 |
| 34 |     34 | Rhodes-Kropf M, 2004, J FINANC, V59, P2685 02:153                |        9 |
| 35 |     35 | Lane J, 2013, PRIV, BIG DATA,THE PUBLIC GOO, P1 02:021           |        9 |
| 36 |     36 | Brummer C, 2015, FORDHAM LAW REV, V84, P977 02:303               |        8 |
| 37 |     37 | Hildebrandt M, 2018, PHILOS TRANS R SOC A MATH PHY, V376 03:001  |        7 |
| 38 |     38 | Buttarelli G, 2016, INT DATA PRIVACY LAW, V6, P77 02:014         |        7 |
| 39 |     39 | Drewer D, 2018, COMPUT LAW SECUR REV, V34, P806 02:014           |        7 |
| 40 |     40 | Bellamy RKE, 2019, IBM J RES DEV, V63 02:017                     |        7 |
| 41 |     41 | Kingston KG, 2020, AFRICAN J INT COMP LAW, V28, P106 02:017      |        7 |
| 42 |     42 | Lee Kuo Chuen D, 2017, HANDBBLOCKCHAIN, DIGIT FINANC, P1 02:017  |        7 |
| 43 |     43 | Raymond Choo KK, 2008, J MONEY LAUND CONTROL, V11, P371 02:017   |        7 |
| 44 |     44 | Simser J, 2008, J MONEY LAUND CONTROL, V11, P15 02:017           |        7 |
| 45 |     45 | Smith KT, 2010, J STRATEG MARK, V18, P201 02:017                 |        7 |
| 46 |     46 | Walker D, 2006, POLICE J, V79, P169 02:017                       |        7 |
| 47 |     47 | Bamberger KA, 2010, TEX LAW REV, V88, P669 03:008                |        6 |
| 48 |     48 | Haldane AG, 2011, NATURE, V469, P351 02:030                      |        3 |
| 49 |     49 | Dutta A, 2016, WIPDA - IEEE WORKSHOP WIDE BA, P11 03:099         |        1 |
```
<BLANKLINE>


"""
# from ...analyze.matrix import co_occurrence_matrix
# from ...analyze.network import (
#     cluster_network,
#     network_communities,
#     network_degree_plot,
#     network_metrics,
#     network_viewer,
# )
# from ...classes import CocitationNetwork

FIELD = "local_references"


# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
def co_citation_network(
    algorithm_or_estimator="louvain",
    network_viewer_dict=None,
    network_degree_plot_dict=None,
    # Items params:
    top_n=None,
    occ_range=None,
    gc_range=None,
    custom_items=None,
    # Database params:
    root_dir="./",
    database="main",
    year_filter=None,
    cited_by_filter=None,
    **filters,
):
    """Co-authorship network"""

    if network_degree_plot_dict is None:
        network_degree_plot_dict = {}

    if network_viewer_dict is None:
        network_viewer_dict = {}

    coc_matrix = co_occurrence_matrix(
        columns=FIELD,
        col_top_n=top_n,
        col_occ_range=occ_range,
        col_gc_range=gc_range,
        col_custom_items=custom_items,
        # Database params:
        root_dir=root_dir,
        database=database,
        year_filter=year_filter,
        cited_by_filter=cited_by_filter,
        **filters,
    )

    graph = cluster_network(coc_matrix, algorithm_or_estimator=algorithm_or_estimator)

    degree_plot = network_degree_plot(graph=graph, **network_degree_plot_dict)

    metrics = network_metrics(graph=graph)

    network = CocitationNetwork()
    network.plot_ = network_viewer(graph=graph, is_article=True, **network_viewer_dict)
    network.graph_ = graph
    network.communities_ = network_communities(graph=graph)

    network.network_metrics__table_ = metrics.table_
    network.network_metrics__prompt_ = metrics.prompt_

    network.degree_plot__plot_ = degree_plot.plot_
    network.degree_plot__table_ = degree_plot.table_
    network.degree_plot__prompt_ = degree_plot.prompt_

    return network
