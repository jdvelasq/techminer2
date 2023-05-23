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
--INFO-- The file 'data/regtech/reports/most_local_cited_references.txt' was created

>>> r.plot_.write_html(file_name)

.. raw:: html

    <iframe src="../../../_static/bibliometrix__most_local_cited_references.html" height="600px" width="100%" frameBorder="0"></iframe>

    
>>> print(r.table_.head(5).to_markdown())
| article                                                         |   global_citations |   local_citations |   global_citations_per_year |   local_citations_per_year | doi                            |
|:----------------------------------------------------------------|-------------------:|------------------:|----------------------------:|---------------------------:|:-------------------------------|
| Barrell R, 2011, NATL INST ECON REV, V216, PF4                  |                  2 |                68 |                       0.167 |                      5.667 | 10.1177/0027950111411368       |
| Anagnostopoulos I, 2018, J ECON BUS, V100, P7                   |                153 |                17 |                      30.6   |                      3.4   | 10.1016/J.JECONBUS.2018.07.003 |
| Butler T/1, 2019, PALGRAVE STUD DIGIT BUS ENABLING TECHNOL, P85 |                 33 |                14 |                       8.25  |                      3.5   | 10.1007/978-3-030-02330-0_6    |
| Yang D, 2018, EMERG MARK FINANC TRADE, V54, P3256               |                 32 |                 8 |                       6.4   |                      1.6   | 10.1080/1540496X.2018.1496422  |
| Kavassalis P, 2018, J RISK FINANC, V19, P39                     |                 21 |                 8 |                       4.2   |                      1.6   | 10.1108/JRF-07-2017-0111       |



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
        file_name="most_local_cited_references.txt",
        **filters,
    )
