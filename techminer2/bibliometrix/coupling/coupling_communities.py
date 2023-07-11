# flake8: noqa
"""
Coupling Communities
===============================================================================

>>> ROOT_DIR = "data/regtech/"
>>> import techminer2plus
>>> coupling_matrix = techminer2plus.analyze.coupling.coupling_matrix(
...     field="author_keywords",
...     top_n=20,
...     root_dir=ROOT_DIR,
... )

>>> graph = techminer2plus.analyze.coupling.coupling_network(
...    coupling_matrix,
...    algorithm_or_estimator="louvain",
... )
>>> print(techminer2plus.analyze.coupling.coupling_communities(graph).to_markdown())
|    | CL_00                                                                      | CL_01                                                           | CL_02                                                    |
|---:|:---------------------------------------------------------------------------|:----------------------------------------------------------------|:---------------------------------------------------------|
|  0 | Butler T, 2018, J RISK MANG FINANCIAL INST, V11, P19 1:8                   | Turki M, 2021, ADV INTELL SYS COMPUT, V1141, P349 1:7           | Buckley RP, 2020, J BANK REGUL, V21, P26 1:24            |
|  1 | Pantielieieva N, 2020, LECTURE NOTES DATA ENG COMMUN, V42, P1 1:4          | Becker M, 2020, INTELL SYST ACCOUNT FINANCE M, V27, P161 1:5    | Arner DW, 2017, HANDBBLOCKCHAIN, DIGIT FINANC, P359 1:11 |
|  2 | Butler T, 2019, PALGRAVE STUD DIGIT BUS ENABL, P85 1:33                    | Rouhollahi Z, 2021, ACM INT CONF PROC SER, P538 1:2             | Campbell-Verduyn M, 2022, NEW POLIT ECON 1:0             |
|  3 | Cruz Rambaud S, 2022, EUR J RISK REGUL, V13, P333 1:3                      | Singh C, 2020, J MONEY LAUND CONTROL, V24, P464 1:14            | McCarthy J, 2022, J FINANC REGUL COMPLIANCE 1:0          |
|  4 | Gasparri G, 2019, FRONTIER ARTIF INTELL, V2 1:3                            | Turki M, 2020, HELIYON, V6 1:11                                 |                                                          |
|  5 | Goul M, 2019, PROC - IEEE WORLD CONGR SERV,, P219 1:3                      | von Solms J, 2021, J BANK REGUL, V22, P152 1:11                 |                                                          |
|  6 | Nasir F, 2019, J ADV RES DYN CONTROL SYST, V11, P912 1:3                   | Ghanem S, 2021, STUD COMPUT INTELL, V954, P139 1:1              |                                                          |
|  7 | Nicholls R, 2021, J ANTITRUST ENFORC, V9, P135 1:3                         | Grassi L, 2022, J IND BUS ECON, V49, P441 1:1                   |                                                          |
|  8 | Singh C, 2022, J FINANC CRIME, V29, P45 1:3                                | Rabbani MR, 2022, LECT NOTES NETWORKS SYST, V423 LNNS, P381 1:1 |                                                          |
|  9 | Kavassalis P, 2018, J RISK FINANC, V19, P39 1:21                           | Siering M, 2022, DECIS SUPPORT SYST, V158 1:1                   |                                                          |
| 10 | Muzammil M, 2020, CEUR WORKSHOP PROC, V2815, P382 1:2                      | Mohamed H, 2021, STUD COMPUT INTELL, V935, P153 1:0             |                                                          |
| 11 | Ryan P, 2021, LECT NOTES BUS INF PROCESS, V417, P905 1:2                   |                                                                 |                                                          |
| 12 | Anagnostopoulos I, 2018, J ECON BUS, V100, P7 1:153                        |                                                                 |                                                          |
| 13 | Muganyi T, 2022, FINANCIAL INNOV, V8 1:13                                  |                                                                 |                                                          |
| 14 | Ryan P, 2020, ICEIS - PROC INT CONF ENTERP , V2, P787 1:12                 |                                                                 |                                                          |
| 15 | Kurum E, 2020, J FINANC CRIME 1:10                                         |                                                                 |                                                          |
| 16 | Battanta L, 2020, PROC EUR CONF INNOV ENTREPREN, V2020-September, P112 1:1 |                                                                 |                                                          |
| 17 | Huang GKJ, 2017, PROC INT CONF ELECTRON BUS (I, V2017-December, P308 1:1   |                                                                 |                                                          |
| 18 | Kera DR, 2021, EAI/SPRINGER INNO COMM COMP, P67 1:1                        |                                                                 |                                                          |
| 19 | Firmansyah B, 2022, INT CONF INF TECHNOL SYST INN, P310 1:0                |                                                                 |                                                          |
| 20 | Kristanto AD, 2022, INT CONF INF TECHNOL SYST INN, P300 1:0                |                                                                 |                                                          |
| 21 | Lan G, 2023, RES INT BUS FINANC, V64 1:0                                   |                                                                 |                                                          |
| 22 | Miglionico A, 2020, EUR BUS LAW REV, V31, P641 1:0                         |                                                                 |                                                          |
| 23 | Teichmann F, 2023, TECHNOL SOC, V72 1:0                                    |                                                                 |                                                          |


# pylint: disable=line-too-long
"""
# from ..network import network_communities


def coupling_communities(graph):
    """Gets communities from a networkx graph as a dataframe."""

    return network_communities(graph)
