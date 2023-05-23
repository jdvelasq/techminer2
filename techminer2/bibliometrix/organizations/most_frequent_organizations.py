"""
Most Frequent Organizations
===============================================================================


>>> directory = "data/regtech/"
>>> file_name = "sphinx/_static/bibliometrix__most_frequent_organizations.html"

>>> from techminer2 import bibliometrix
>>> r = bibliometrix.organizations.most_frequent_organizations(
...     directory=directory,
...     topics_length=20,
...     database="documents",
... )
>>> r.plot_.write_html(file_name)

.. raw:: html

    <iframe src="../../../_static/bibliometrix__most_relevant_organizations.html" height="600px" width="100%" frameBorder="0"></iframe>

    
>>> r.table_.head()
organizations
University of Hong Kong      3
University College Cork      3
Ahlia University             3
---FinTech HK                2
University of Westminster    2
Name: OCC, dtype: int64

>>> print(r.prompt_)
Analyze the table below, which provides bibliographic indicators for a collection of research articles. Identify any notable patterns, trends, or outliers in the data, and discuss their implications for the research field. Be sure to provide a concise summary of your findings in no more than 150 words.
<BLANKLINE>
| organizations                                                   |   OCC |
|:----------------------------------------------------------------|------:|
| University of Hong Kong                                         |     3 |
| University College Cork                                         |     3 |
| Ahlia University                                                |     3 |
| ---FinTech HK                                                   |     2 |
| University of Westminster                                       |     2 |
| Coventry University                                             |     2 |
| Dublin City University                                          |     2 |
| Politecnico di Milano                                           |     2 |
| ---School of Electrical Engineering and Informatics             |     2 |
| ---Kingston Business School                                     |     1 |
| ---Centre for Law                                               |     1 |
| Duke University School of Law                                   |     1 |
| Heinrich Heine University                                       |     1 |
| University of Zurich                                            |     1 |
| University of Luxembourg                                        |     1 |
| ---UNSW Sydney                                                  |     1 |
| Harvard University Weatherhead Center for International Affairs |     1 |
| ---School of Engineering                                        |     1 |
| ---Panepistemio Aigaiou                                         |     1 |
| ---KS Strategic                                                 |     1 |
<BLANKLINE>
<BLANKLINE>


"""
from ... import vantagepoint


def most_frequent_organizations(
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
    """Plots the number of documents by organizations using the specified plot."""

    obj = vantagepoint.analyze.extract_topics(
        criterion="organizations",
        directory=directory,
        database=database,
        metric="OCC",
        start_year=start_year,
        end_year=end_year,
        topics_length=topics_length,
        topic_min_occ=topic_min_occ,
        topic_max_occ=topic_max_occ,
        topic_min_citations=topic_min_citations,
        topic_max_citations=topic_max_citations,
        custom_topics=custom_topics,
        **filters,
    )

    chart = vantagepoint.report.cleveland_chart(
        obj,
        title="Most Frequent Organizations",
        x_label="OCC",
        y_label="ORGANIZATIONS",
    )

    return chart
