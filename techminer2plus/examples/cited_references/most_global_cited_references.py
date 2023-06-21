# flake8: noqa
"""
Most Global Cited References
===============================================================================



>>> root_dir = "data/regtech/"
>>> file_name = "sphinx/_static/examples/cited_references/most_global_cited_references.html"

>>> import techminer2plus
>>> r = techminer2plus.examples.cited_references.most_global_cited_references(
...     top_n=20,
...     root_dir=root_dir,
... )


>>> r.plot_.write_html(file_name)

.. raw:: html

    <iframe src="../../../_static/examples/cited_references/most_global_cited_references.html" height="600px" width="100%" frameBorder="0"></iframe>

    

>>> print(r.table_.head(5).to_markdown())
| article                                             |   year |   global_citations |   local_citations |   global_citations_per_year |   local_citations_per_year | doi                                |
|:----------------------------------------------------|-------:|-------------------:|------------------:|----------------------------:|---------------------------:|:-----------------------------------|
| Jensen MC, 1976, J FINANC ECON, V3, P305            |   1976 |              29405 |                 1 |                     625.638 |                      0.021 | 10.1016/0304-405X(76)90026-X       |
| Blei DM, 2003, J MACH LEARN RES, V3, P993           |   2003 |              25474 |                 1 |                    1273.7   |                      0.05  | nan                                |
| Pritchard JK, 2000, GENETICS, V155, P945            |   2000 |              25177 |                 1 |                    1094.65  |                      0.043 | 10.1093/GENETICS/155.2.945         |
| Coase RH, 1937, ECONOMICA, V4, P386                 |   1937 |              12819 |                 1 |                     149.058 |                      0.012 | 10.1111/J.1468-0335.1937.TB00002.X |
| Pan SJ, 2010, IEEE TRANS KNOWL DATA ENG, V22, P1345 |   2010 |              12506 |                 1 |                     962     |                      0.077 | 10.1109/TKDE.2009.191              |


# pylint: disable=line-too-long
"""
from ..most_cited_documents import most_cited_documents


def most_global_cited_references(
    top_n=None,
    # Figure params:
    title="Most Global Cited References",
    field_label=None,
    metric_label=None,
    textfont_size=10,
    marker_size=7,
    line_color="black",
    line_width=1.5,
    yshift=4,
    # Database filters:
    root_dir="./",
    database="references",
    year_filter=None,
    cited_by_filter=None,
    **filters,
):
    """Plots the most local cited documents in the main collection."""

    return most_cited_documents(
        metric="global_citations",
        top_n=top_n,
        # Figure params:
        title=title,
        field_label=field_label,
        metric_label=metric_label,
        textfont_size=textfont_size,
        marker_size=marker_size,
        line_color=line_color,
        line_width=line_width,
        yshift=yshift,
        # Database filters:
        root_dir=root_dir,
        database=database,
        year_filter=year_filter,
        cited_by_filter=cited_by_filter,
        **filters,
    )
