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
...     field='countries',
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
>>> metrics.fig_.write_html("sphinx/_static/performance/contributors/countries/collaboration_metrics.html")

.. raw:: html

    <iframe src="../../../../_static/performance/contributors/countries/collaboration_metrics.html" 
    height="600px" width="100%" frameBorder="0"></iframe>


>>> print(metrics.df_.head().to_markdown())
| countries      |   OCC |   global_citations |   local_citations |   single_publication |   multiple_publication |   mp_ratio |
|:---------------|------:|-------------------:|------------------:|---------------------:|-----------------------:|-----------:|
| United Kingdom |     7 |                199 |                35 |                    4 |                      3 |       0.43 |
| Australia      |     7 |                199 |                30 |                    4 |                      3 |       0.43 |
| United States  |     6 |                 59 |                19 |                    4 |                      2 |       0.33 |
| Ireland        |     5 |                 55 |                22 |                    4 |                      1 |       0.2  |
| China          |     5 |                 27 |                 5 |                    2 |                      3 |       0.6  |


>>> print(metrics.prompt_)
Your task is to generate an analysis about the collaboration between \\
countries according to the data in a scientific bibliography database. \\
Summarize the table below, delimited by triple backticks, where the column \\
'single publication' is the number of documents in which all the authors \\
belongs to the same countries, and the  column 'multiple publication' is \\
the number of documents in which the authors are from different countries. \\
The column 'mcp ratio' is the ratio between the columns 'multiple \\
publication' and 'OCC'. The higher the ratio, the higher the collaboration \\
between countries. Use the information in the table to draw conclusions \\
about the level of collaboration between countries in the dataset. In your \\
analysis, be sure to describe in a clear and concise way, any findings or \\
any patterns you observe, and identify any outliers or anomalies in the \\
data. Limit your description to one paragraph with no more than 250 words.
<BLANKLINE>
Table:
```
| countries            |   OCC |   global_citations |   local_citations |   single_publication |   multiple_publication |   mp_ratio |
|:---------------------|------:|-------------------:|------------------:|---------------------:|-----------------------:|-----------:|
| United Kingdom       |     7 |                199 |                35 |                    4 |                      3 |       0.43 |
| Australia            |     7 |                199 |                30 |                    4 |                      3 |       0.43 |
| United States        |     6 |                 59 |                19 |                    4 |                      2 |       0.33 |
| Ireland              |     5 |                 55 |                22 |                    4 |                      1 |       0.2  |
| China                |     5 |                 27 |                 5 |                    2 |                      3 |       0.6  |
| Italy                |     5 |                  5 |                 2 |                    4 |                      1 |       0.2  |
| Germany              |     4 |                 51 |                14 |                    2 |                      2 |       0.5  |
| Switzerland          |     4 |                 45 |                12 |                    1 |                      3 |       0.75 |
| Bahrain              |     4 |                 19 |                 3 |                    2 |                      2 |       0.5  |
| Hong Kong            |     3 |                185 |                23 |                    0 |                      3 |       1    |
| Luxembourg           |     2 |                 34 |                 7 |                    1 |                      1 |       0.5  |
| United Arab Emirates |     2 |                 13 |                 5 |                    1 |                      1 |       0.5  |
| Spain                |     2 |                  4 |                 0 |                    2 |                      0 |       0    |
| Indonesia            |     2 |                  0 |                 0 |                    2 |                      0 |       0    |
| Greece               |     1 |                 21 |                 8 |                    0 |                      1 |       1    |
| Japan                |     1 |                 13 |                 1 |                    0 |                      1 |       1    |
| South Africa         |     1 |                 11 |                 4 |                    1 |                      0 |       0    |
| Jordan               |     1 |                 11 |                 2 |                    0 |                      1 |       1    |
| Ukraine              |     1 |                  4 |                 0 |                    1 |                      0 |       0    |
| Malaysia             |     1 |                  3 |                 0 |                    1 |                      0 |       0    |
```
<BLANKLINE>


"""
