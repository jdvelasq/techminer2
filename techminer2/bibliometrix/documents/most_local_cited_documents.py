"""
Most Local Cited Documents
===============================================================================


>>> directory = "data/regtech/"
>>> file_name = "sphinx/_static/bibliometrix__most_local_cited_documents.html"

>>> from techminer2 import bibliometrix
>>> r = bibliometrix.documents.most_local_cited_documents(
...     topics_length=20,
...     directory=directory,
... )
>>> r.plot_.write_html(file_name)

.. raw:: html

    <iframe src="../../../_static/bibliometrix__most_local_cited_documents.html" height="600px" width="100%" frameBorder="0"></iframe>

    
>>> r.table_.head(5)
                                                    global_citations  ...                                 doi
article                                                               ...                                    
Anagnostopoulos I, 2018, J ECON BUS, V100, P7                    153  ...      10.1016/J.JECONBUS.2018.07.003
Arner DW, 2017, HANDB OF BLOCKCHAIN, DIGIT FINA...                11  ...  10.1016/B978-0-12-810441-5.00016-6
Arner DW, 2017, NORTHWEST J INTL LAW BUS, V37, ...               150  ...                                 NaN
Battanta L, 2020, PROC EUR CONF INNOV ENTREPREN...                 1  ...                 10.34190/EIE.20.143
Baxter LG, 2016, DUKE LAW J, V66, P567                            30  ...                                 NaN
<BLANKLINE>
[5 rows x 5 columns]


"""
from ..cited_documents import bibiometrix_cited_documents


def most_local_cited_documents(
    directory="./",
    topics_length=20,
    title="Most Local Cited Documents",
    start_year=None,
    end_year=None,
    **filters,
):
    """Most local cited documents."""

    return bibiometrix_cited_documents(
        metric="local_citations",
        directory=directory,
        database="documents",
        top_n=topics_length,
        title=title,
        start_year=start_year,
        end_year=end_year,
        **filters,
    )
