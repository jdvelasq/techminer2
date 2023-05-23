"""
Most Global Cited Organizations
===============================================================================


>>> directory = "data/regtech/"
>>> file_name = "sphinx/_static/bibliometrix__most_global_cited_organizations.html"

>>> from techminer2 import bibliometrix
>>> r = bibliometrix.organizations.most_global_cited_organizations(
...     directory,
...     topics_length=20,
... )
>>> r.plot_.write_html(file_name)

.. raw:: html

    <iframe src="../../../_static/bibliometrix__most_global_cited_organizations.html" height="600px" width="100%" frameBorder="0"></iframe>

>>> r.table_.head()
organizations
University of Hong Kong        185
---FinTech HK                  161
---Kingston Business School    153
---Centre for Law              150
University College Cork         41
Name: global_citations, dtype: int64

>>> print(r.prompt_)
Analyze the table below, which provides bibliographic indicators for a collection of research articles. Identify any notable patterns, trends, or outliers in the data, and discuss their implications for the research field. Be sure to provide a concise summary of your findings in no more than 150 words.
<BLANKLINE>
| organizations                                                   |   global_citations |
|:----------------------------------------------------------------|-------------------:|
| University of Hong Kong                                         |                185 |
| ---FinTech HK                                                   |                161 |
| ---Kingston Business School                                     |                153 |
| ---Centre for Law                                               |                150 |
| University College Cork                                         |                 41 |
| Duke University School of Law                                   |                 30 |
| Heinrich Heine University                                       |                 24 |
| University of Zurich                                            |                 24 |
| University of Luxembourg                                        |                 24 |
| ---UNSW Sydney                                                  |                 24 |
| Harvard University Weatherhead Center for International Affairs |                 21 |
| ---School of Engineering                                        |                 21 |
| ---Panepistemio Aigaiou                                         |                 21 |
| ---KS Strategic                                                 |                 21 |
| European Central Bank                                           |                 21 |
| Ahlia University                                                |                 19 |
| University of Westminster                                       |                 17 |
| Coventry University                                             |                 17 |
| Dublin City University                                          |                 14 |
| Shanghai University                                             |                 13 |
<BLANKLINE>
<BLANKLINE>




"""
from ... import vantagepoint


def most_global_cited_organizations(
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
    """Most global cited organizations."""

    obj = vantagepoint.analyze.extract_topics(
        criterion="organizations",
        directory=directory,
        database=database,
        metric="global_citations",
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
        title="Most Global Cited Organizations",
        x_label="Global Citations",
        y_label="ORGANIZATIONS",
    )

    return chart
