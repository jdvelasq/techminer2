# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
# pylint: disable=import-outside-toplevel
"""
Most Global Cited References
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
...     root_dir="example/", 
...     database="references",
...     year_filter=(None, None),
...     cited_by_filter=(None, None),
... )
--INFO-- The file 'example/reports/most_global_cited_references__abstracts.txt' was created.
--INFO-- The file 'example/reports/most_global_cited_references__prompt.txt' was created.


>>> documents.fig_.write_html("sphinx/_static/analyze/citation/publications/most_global_cited_references.html")

.. raw:: html

    <iframe src="../../../../../_static/analyze/citation/publications/most_global_cited_references.html" 
    height="600px" width="100%" frameBorder="0"></iframe>


>>> print(documents.df_.head(5).to_markdown())
| article                                                    |   year |   rank_gcs |   global_citations |   rank_lcs |   local_citations |   global_citations_per_year |   local_citations_per_year | doi                          |
|:-----------------------------------------------------------|-------:|-----------:|-------------------:|-----------:|------------------:|----------------------------:|---------------------------:|:-----------------------------|
| Landis J.R., 1977, BIOMETRICS, V33, P159                   |   1977 |          1 |              54055 |         23 |                 0 |                    1228.52  |                          0 | 10.2307/2529310              |
| Ajzen I., 1991, ORGAN BEHAV HUM DECIS PROCESSES, V50, P179 |   1991 |          2 |              50106 |         24 |                 0 |                    1670.2   |                          0 | 10.1016/0749-5978(91)90020-T |
| Podsakoff P.M., 2003, J APPL PSYCHOL, V88, P879            |   2003 |          3 |              46470 |         25 |                 0 |                    2581.67  |                          0 | 10.1037/0021-9010.88.5.879   |
| Davis F.D., 1989, MIS QUART MANAGE INF SYST, V13, P319     |   1989 |          4 |              32939 |         26 |                 0 |                    1029.34  |                          0 | 10.2307/249008               |
| Anderson J.C., 1988, PSYCHOL BULL, V103, P411              |   1988 |          5 |              28119 |         27 |                 0 |                     852.091 |                          0 | 10.1037/0033-2909.103.3.411  |

"""
