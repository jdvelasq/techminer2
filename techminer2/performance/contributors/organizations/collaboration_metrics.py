# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
# pylint: disable=import-outside-toplevel
"""
Collaboration Metrics
===============================================================================


>>> from techminer2.performance import collaboration_metrics
>>> metrics = collaboration_metrics(
...     #
...     # PARAMS:
...     field="organizations",
...     #
...     # ITEM FILTERS:
...     top_n=20,
...     occ_range=(None, None),
...     gc_range=(None, None),
...     custom_items=None,
...     #
...     # DATABASE PARAMS:
...     root_dir="data/regtech/",
...     database="main",
...     year_filter=(None, None),
...     cited_by_filter=(None, None),
... )
>>> metrics.fig_.write_html("sphinx/_static/performance/contributors/organizations/collaboration_metrics.html")

.. raw:: html

    <iframe src="../../../../_static/performance/contributors/organizations/collaboration_metrics.html" 
    height="600px" width="100%" frameBorder="0"></iframe>


>>> print(metrics.df_.head().to_markdown())
| organizations             |   OCC |   global_citations |   local_citations |   single_publication |   multiple_publication |   mp_ratio |
|:--------------------------|------:|-------------------:|------------------:|---------------------:|-----------------------:|-----------:|
| Univ of Hong Kong (HKG)   |     3 |                185 |                23 |                    0 |                      3 |       1    |
| Univ Coll Cork (IRL)      |     3 |                 41 |                19 |                    2 |                      1 |       0.33 |
| Ahlia Univ (BHR)          |     3 |                 19 |                 3 |                    0 |                      3 |       1    |
| Coventry Univ (GBR)       |     2 |                 17 |                 4 |                    0 |                      2 |       1    |
| Univ of Westminster (GBR) |     2 |                 17 |                 4 |                    0 |                      2 |       1    |


>>> print(metrics.prompt_)
Your task is to generate an analysis about the collaboration between \\
organizations according to the data in a scientific bibliography database. \\
Summarize the table below, delimited by triple backticks, where the column \\
'single publication' is the number of documents in which all the authors \\
belongs to the same organizations, and the  column 'multiple publication' \\
is the number of documents in which the authors are from different \\
organizations. The column 'mcp ratio' is the ratio between the columns \\
'multiple publication' and 'OCC'. The higher the ratio, the higher the \\
collaboration between organizations. Use the information in the table to \\
draw conclusions about the level of collaboration between organizations in \\
the dataset. In your analysis, be sure to describe in a clear and concise \\
way, any findings or any patterns you observe, and identify any outliers or \\
anomalies in the data. Limit your description to one paragraph with no more \\
than 250 words.
<BLANKLINE>
Table:
```
| organizations                                                      |   OCC |   global_citations |   local_citations |   single_publication |   multiple_publication |   mp_ratio |
|:-------------------------------------------------------------------|------:|-------------------:|------------------:|---------------------:|-----------------------:|-----------:|
| Univ of Hong Kong (HKG)                                            |     3 |                185 |                23 |                    0 |                      3 |       1    |
| Univ Coll Cork (IRL)                                               |     3 |                 41 |                19 |                    2 |                      1 |       0.33 |
| Ahlia Univ (BHR)                                                   |     3 |                 19 |                 3 |                    0 |                      3 |       1    |
| Coventry Univ (GBR)                                                |     2 |                 17 |                 4 |                    0 |                      2 |       1    |
| Univ of Westminster (GBR)                                          |     2 |                 17 |                 4 |                    0 |                      2 |       1    |
| Dublin City Univ (IRL)                                             |     2 |                 14 |                 3 |                    1 |                      1 |       0.5  |
| Politec di Milano (ITA)                                            |     2 |                  2 |                 0 |                    2 |                      0 |       0    |
| Kingston Bus Sch (GBR)                                             |     1 |                153 |                17 |                    1 |                      0 |       0    |
| FinTech HK, Hong Kong (HKG)                                        |     1 |                150 |                16 |                    0 |                      1 |       1    |
| ctr for Law, Markets & Regulation, UNSW Australia, Australia (AUS) |     1 |                150 |                16 |                    0 |                      1 |       1    |
| Duke Univ Sch of Law (USA)                                         |     1 |                 30 |                 8 |                    1 |                      0 |       0    |
| Heinrich-Heine-Univ (DEU)                                          |     1 |                 24 |                 4 |                    0 |                      1 |       1    |
| UNSW Sydney, Kensington, Australia (AUS)                           |     1 |                 24 |                 4 |                    0 |                      1 |       1    |
| Univ of Luxembourg (LUX)                                           |     1 |                 24 |                 4 |                    0 |                      1 |       1    |
| Univ of Zurich (CHE)                                               |     1 |                 24 |                 4 |                    0 |                      1 |       1    |
| European Central B (DEU)                                           |     1 |                 21 |                 8 |                    0 |                      1 |       1    |
| Harvard Univ Weatherhead ctr for International Affairs (USA)       |     1 |                 21 |                 8 |                    0 |                      1 |       1    |
| KS Strategic, London, United Kingdom (GBR)                         |     1 |                 21 |                 8 |                    0 |                      1 |       1    |
| Panepistemio Aigaiou, Chios, Greece (GRC)                          |     1 |                 21 |                 8 |                    0 |                      1 |       1    |
| Sch of Eng (CHE)                                                   |     1 |                 21 |                 8 |                    0 |                      1 |       1    |
```
<BLANKLINE>


"""
