"""
Most Local Cited References
===============================================================================


>>> directory = "data/regtech/"
>>> file_name = "sphinx/_static/bibliometrix__most_local_cited_references.html"

>>> from techminer2 import bibliometrix
>>> r = bibliometrix.cited_references.most_local_cited_references(
...     topics_length=20,
...     directory=directory,
... )
>>> r.plot_.write_html(file_name)

.. raw:: html

    <iframe src="../../../_static/bibliometrix__most_local_cited_references.html" height="600px" width="100%" frameBorder="0"></iframe>

    
>>> print(r.table_.head(5).to_markdown())
| article                                                                                  |   global_citations |   local_citations |   global_citations_per_year |   local_citations_per_year | doi                              |
|:-----------------------------------------------------------------------------------------|-------------------:|------------------:|----------------------------:|---------------------------:|:---------------------------------|
| AKCAY S, 2020, APPL ECON LETT, V27, P1206                                                |                 13 |                 1 |                       4.333 |                      0.333 | 10.1080/13504851.2019.1676376    |
| Acedo FJ, 2006, J MANAGE STUD, V43, P957                                                 |                427 |                 1 |                      25.118 |                      0.059 | 10.1111/J.1467-6486.2006.00625.X |
| Acharya VV, 2016, REV CORP FINANC STUD, V5, P36                                          |                 53 |                 1 |                       7.571 |                      0.143 | 10.1093/RCFS/CFV006              |
| Adhami S, 2018, J ECON BUS, V100, P64                                                    |                237 |                 1 |                      47.4   |                      0.2   | 10.1016/J.JECONBUS.2018.04.001   |
| Admati A, 2014, THE BANK NEW CLOTHES: WHAT'S WRONG WITH BANK AND WHAT TO DO ABOUT IT, P1 |                103 |                 0 |                      11.444 |                      0     | nan                              |



"""
from ..cited_documents import bibiometrix_cited_documents


def most_local_cited_references(
    directory="./",
    topics_length=20,
    title="Most Local Cited References",
    start_year=None,
    end_year=None,
    **filters,
):
    """Plots the most local cited references."""

    return bibiometrix_cited_documents(
        metric="local_citations",
        directory=directory,
        database="references",
        top_n=topics_length,
        title=title,
        start_year=start_year,
        end_year=end_year,
        **filters,
    )
