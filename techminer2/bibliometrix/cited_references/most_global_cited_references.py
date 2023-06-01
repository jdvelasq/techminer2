# flake8: noqa
"""
Most Global Cited References
===============================================================================


Example
-------------------------------------------------------------------------------


>>> root_dir = "data/regtech/"
>>> file_name = "sphinx/_static/bibliometrix__most_global_cited_references.html"

>>> from techminer2 import bibliometrix
>>> r = bibliometrix.cited_references.most_global_cited_references(
...     top_n=20,
...     root_dir=root_dir,
... )
--INFO-- The file 'data/regtech/reports/most_global_cited_references.txt' was created

>>> r.plot_.write_html(file_name)

.. raw:: html

    <iframe src="../../../_static/bibliometrix__most_global_cited_references.html" height="600px" width="100%" frameBorder="0"></iframe>

    

>>> print(r.table_.head(5).to_markdown())
| article                                             |   global_citations |   local_citations |   global_citations_per_year |   local_citations_per_year | doi                                |
|:----------------------------------------------------|-------------------:|------------------:|----------------------------:|---------------------------:|:-----------------------------------|
| Jensen MC, 1976, J FINANC ECON, V3, P305            |              29405 |                 1 |                     625.638 |                      0.021 | 10.1016/0304-405X(76)90026-X       |
| Blei DM, 2003, J MACH LEARN RES, V3, P993           |              25474 |                 1 |                    1273.7   |                      0.05  | nan                                |
| Pritchard JK, 2000, GENETICS, V155, P945            |              25177 |                 1 |                    1094.65  |                      0.043 | 10.1093/GENETICS/155.2.945         |
| Coase RH, 1937, ECONOMICA, V4, P386                 |              12819 |                 1 |                     149.058 |                      0.012 | 10.1111/J.1468-0335.1937.TB00002.X |
| Pan SJ, 2010, IEEE TRANS KNOWL DATA ENG, V22, P1345 |              12506 |                 1 |                     962     |                      0.077 | 10.1109/TKDE.2009.191              |


# pylint: disable=line-too-long
"""
from ..cited_documents import bibiometrix_cited_documents


def most_global_cited_references(
    root_dir="./",
    top_n=20,
    title="Most Global Cited References",
    year_filter=None,
    cited_by_filter=None,
    **filters,
):
    """Plots the most global cited references."""

    return bibiometrix_cited_documents(
        metric="global_citations",
        root_dir=root_dir,
        database="references",
        top_n=top_n,
        title=title,
        year_filter=year_filter,
        cited_by_filter=cited_by_filter,
        file_name="most_global_cited_references.txt",
        **filters,
    )
