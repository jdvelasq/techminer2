# flake8: noqa
"""
Most Local Cited References
===============================================================================




>>> root_dir = "data/regtech/"
>>> file_name = "sphinx/_static/examples/cited_references/most_local_cited_references.html"

>>> import techminer2plus
>>> r = techminer2plus.publish.cited_references.most_local_cited_references(
...     top_n=20,
...     root_dir=root_dir,
... )

>>> r.plot_.write_html(file_name)

.. raw:: html

    <iframe src="../../../_static/examples/cited_references/most_local_cited_references.html" height="600px" width="100%" frameBorder="0"></iframe>

    
>>> print(r.table_.head(5).to_markdown())
| article                                            |   year |   global_citations |   local_citations |   global_citations_per_year |   local_citations_per_year | doi                            |
|:---------------------------------------------------|-------:|-------------------:|------------------:|----------------------------:|---------------------------:|:-------------------------------|
| Barrell R, 2011, NATL INST ECON REV, V216, PF4     |   2011 |                  2 |                68 |                       0.167 |                      5.667 | 10.1177/0027950111411368       |
| Anagnostopoulos I, 2018, J ECON BUS, V100, P7      |   2018 |                153 |                17 |                      30.6   |                      3.4   | 10.1016/J.JECONBUS.2018.07.003 |
| Butler T, 2019, PALGRAVE STUD DIGIT BUS ENABL, P85 |   2019 |                 33 |                14 |                       8.25  |                      3.5   | 10.1007/978-3-030-02330-0_6    |
| Yang D, 2018, EMERG MARK FINANC TRADE, V54, P3256  |   2018 |                 32 |                 8 |                       6.4   |                      1.6   | 10.1080/1540496X.2018.1496422  |
| Kavassalis P, 2018, J RISK FINANC, V19, P39        |   2018 |                 21 |                 8 |                       4.2   |                      1.6   | 10.1108/JRF-07-2017-0111       |





# pylint: disable=line-too-long
"""
from ..most_cited_documents import most_cited_documents


def most_local_cited_references(
    top_n=None,
    # Figure params:
    title="Most Local Cited References",
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
        metric="local_citations",
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
