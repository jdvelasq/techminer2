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
Analyze the table below, which provides bibliographic indicators for a collection of research articles. Identify any notable patterns, trends, or outliers in the data, and discuss their implications for the research field. Be sure to provide a concise summary of your findings in no more than 150 words.
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
<BLANKLINE>



"""
from ..bibliometric_indicators_by_topic import bibliometric_indicators_by_topic


def most_local_cited_organizations(
    plot="cleveland_chart",
    x_label=None,
    y_label=None,
    directory="./",
    topics_length=20,
    topic_min_occ=None,
    topic_max_occ=None,
    topic_min_citations=None,
    topic_max_citations=None,
    custom_topics=None,
    database="documents",
    start_year=None,
    end_year=None,
    **filters,
):
    """Most local cited organizations."""

    return bibliometric_indicators_by_topic(
        criterion="organizations",
        metric="local_citations",
        plot=plot,
        x_label=x_label,
        y_label=y_label,
        title="Most Local Cited Organizations",
        directory=directory,
        topics_length=topics_length,
        topic_min_occ=topic_min_occ,
        topic_max_occ=topic_max_occ,
        topic_min_citations=topic_min_citations,
        topic_max_citations=topic_max_citations,
        custom_topics=custom_topics,
        database=database,
        start_year=start_year,
        end_year=end_year,
        **filters,
    )
