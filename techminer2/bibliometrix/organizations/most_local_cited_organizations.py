"""
Most Local Cited Institutions
===============================================================================




>>> directory = "data/regtech/"
>>> file_name = "sphinx/_static/bibliometrix__most_local_cited_organizations.html"

>>> from techminer2 import bibliometrix
>>> r = bibliometrix.organizations.most_local_cited_organizations(
...     topics_length=20,
...     directory=directory,
... )
>>> r.plot_.write_html(file_name)

.. raw:: html

    <iframe src="../../../_static/bibliometrix__most_local_cited_organizations.html" height="600px" width="100%" frameBorder="0"></iframe>

    
>>> r.table_.head()
organizations
University College Cork                                            19
---Kingston Business School                                        17
University of Hong Kong                                             8
Harvard University Weatherhead Center for International Affairs     8
---School of Engineering                                            8
Name: local_citations, dtype: int64

>>> print(r.prompt_)
<BLANKLINE>
Act as a researcher realizing a bibliometric analysis. Analyze the following 
table, which provides data corresponding to the top 20
organizations with more local_citations in a given bibliographic dataset. 
<BLANKLINE>
- 'OCC' is the number of documents published.  
<BLANKLINE>
- 'local_citations' are the local citations in the dataset.
<BLANKLINE>
- 'global_citations' are the citations received 
<BLANKLINE>
| organizations                                                   |   local_citations |
|:----------------------------------------------------------------|------------------:|
| University College Cork                                         |                19 |
| ---Kingston Business School                                     |                17 |
| University of Hong Kong                                         |                 8 |
| Harvard University Weatherhead Center for International Affairs |                 8 |
| ---School of Engineering                                        |                 8 |
| ---Panepistemio Aigaiou                                         |                 8 |
| ---KS Strategic                                                 |                 8 |
| European Central Bank                                           |                 8 |
| Heinrich Heine University                                       |                 5 |
| University of Zurich                                            |                 5 |
| University of Luxembourg                                        |                 5 |
| ---UNSW Sydney                                                  |                 5 |
| Ahlia University                                                |                 5 |
| ---Deloitte LLP                                                 |                 5 |
| University of Westminster                                       |                 4 |
| Coventry University                                             |                 4 |
| University of Johannesburg                                      |                 4 |
| Finance and Banking                                             |                 4 |
| Department of Finance and Banking                               |                 4 |
| Zayed University                                                |                 4 |
<BLANKLINE>
Write a clear and concise paragraph describing the main findings and any 
important trends or patterns you notice. 
<BLANKLINE>
Limit your description to a paragraph with no more than 250 words.        
<BLANKLINE>
<BLANKLINE>

    
"""
from ...vantagepoint.report.chart import chart


def most_local_cited_organizations(
    directory="./",
    topics_length=20,
    topic_min_occ=None,
    topic_min_citations=None,
    plot="cleveland",
    database="documents",
    start_year=None,
    end_year=None,
    **filters,
):
    """Most Local Cited Organizations (from Reference Lists)."""

    return chart(
        criterion="organizations",
        directory=directory,
        database=database,
        metric="local_citations",
        start_year=start_year,
        end_year=end_year,
        topics_length=topics_length,
        topic_min_occ=topic_min_occ,
        topic_min_citations=topic_min_citations,
        custom_topics=None,
        title="Most Local Cited Organizations (from Reference Lists)",
        plot=plot,
        **filters,
    )
