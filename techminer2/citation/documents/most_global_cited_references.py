# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
# pylint: disable=import-outside-toplevel
"""
.. _tm2.citation.documentsmost_global_cited_references:

Most Global Cited References
===============================================================================


>>> from techminer2.citation.documents import most_cited_documents
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
...     database="references",
...     year_filter=(None, None),
...     cited_by_filter=(None, None),
... )
--INFO-- The file 'data/regtech/reports/most_global_cited_references__abstracts.txt' was created.
--INFO-- The file 'data/regtech/reports/most_global_cited_references__prompt.txt' was created.


>>> documents.fig_.write_html("sphinx/_static/citation/documents/most_global_cited_references.html")

.. raw:: html

    <iframe src="../../../../_static/citation/documents/most_global_cited_references.html" 
    height="600px" width="100%" frameBorder="0"></iframe>


>>> print(documents.df_.head(5).to_markdown())
| article                                             |   year |   global_citations |   local_citations |   global_citations_per_year |   local_citations_per_year | doi                                |
|:----------------------------------------------------|-------:|-------------------:|------------------:|----------------------------:|---------------------------:|:-----------------------------------|
| Jensen MC, 1976, J FINANC ECON, V3, P305            |   1976 |              29405 |                 0 |                     625.638 |                          0 | 10.1016/0304-405X(76)90026-X       |
| Blei DM, 2003, J MACH LEARN RES, V3, P993           |   2003 |              25474 |                 0 |                    1273.7   |                          0 | nan                                |
| Pritchard JK, 2000, GENETICS, V155, P945            |   2000 |              25177 |                 0 |                    1094.65  |                          0 | 10.1093/GENETICS/155.2.945         |
| Coase RH, 1937, ECONOMICA, V4, P386                 |   1937 |              12819 |                 0 |                     149.058 |                          0 | 10.1111/J.1468-0335.1937.TB00002.X |
| Pan SJ, 2010, IEEE TRANS KNOWL DATA ENG, V22, P1345 |   2010 |              12506 |                 0 |                     962     |                          0 | 10.1109/TKDE.2009.191              |


"""
